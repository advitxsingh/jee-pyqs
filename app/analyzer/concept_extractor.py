"""
Concept & Formula Extractor for JEE Main PYQs.
Maps every question to core syllabus concepts, identifies formulas,
computes difficulty, notes common exam traps, and links concepts to PYQs.
"""

import re
from typing import List, Dict, Any, Tuple
from app.db.models import QuestionModel, ConceptModel, ConceptPYQLinkModel


# Curated Concept Taxonomy for Pilot Chapters (with fallback heuristic for all others)
CURATED_TAXONOMY = {
    "electrochemistry": [
        {
            "name": "Nernst Equation & Cell Potential",
            "category": "Core Formula",
            "primary": ["nernst", "cell potential", "emf of the cell", "concentration cell", "e_cell", "standard cell potential", "0.0591", "0.059", "log q", "log k", "equilibrium constant k"],
            "formula_cues": [r"e^\circ", r"e_{\text{cell}}", r"e_{cell}", r"\log q", r"\log k", r"0.059"],
            "secondary": ["cell", "emf", "potential", "half cell", "danielle", "daniell"],
            "keywords": ["nernst", "cell potential", "emf", "concentration cell", "e_cell", r"e^\circ", "log q", "standard electrode"],
            "summary": "Calculation of non-standard cell potential E_cell = E° - (0.0591/n)*log10(Q) at 298 K, equilibrium constant K_eq, and concentration cells where E° = 0.",
            "standard_formulas": r"E_{\text{cell}} = E^{\circ}_{\text{cell}} - \frac{0.0591}{n} \log_{10} Q, \quad \Delta G^{\circ} = -n F E^{\circ}_{\text{cell}} = -2.303 RT \log_{10} K",
            "common_traps": "1. Forgetting to square/cube concentrations corresponding to stoichiometric coefficients in Q. 2. Confusing reduction and oxidation potential signs. 3. For concentration cells, misidentifying anode (dilute) vs cathode (concentrated).",
            "tips_and_tricks": "At 298 K, E° = (0.0591/n)*log10(K). If reaction is spontaneous, E_cell > 0 and Delta G < 0."
        },
        {
            "name": "Electrode Potential & Delta G Relation",
            "category": "Thermodynamics",
            "primary": ["gibbs", "delta g", r"\delta g", r"\deltag", "spontaneity", "nfe", "standard reduction potential", "standard electrode potential", "reducing agent", "oxidizing agent", "half-cell potential", "tendency to act as reducing"],
            "formula_cues": [r"\delta g", r"\deltag", r"-nfe", r"e^{\circ}", r"fe^{3+}/fe^{2+}"],
            "secondary": ["reduction potential", "spontaneous", "redox", "oxidation potential"],
            "keywords": ["gibbs", r"\delta g", "delta g", "spontaneity", "nfe", "electrode potential", "standard reduction"],
            "summary": "Relationship between standard reduction potentials and Gibbs free energy Delta G° = -nFE°. When combining non-standard half-reactions, add Delta G values, never add E° potentials directly!",
            "standard_formulas": r"\Delta G = -nFE, \quad \Delta G^{\circ}_3 = \Delta G^{\circ}_1 + \Delta G^{\circ}_2 \implies n_3 E^{\circ}_3 = n_1 E^{\circ}_1 + n_2 E^{\circ}_2",
            "common_traps": "Directly adding E° potentials of two half-cells to get the E° of a composite couple (e.g. Fe3+ -> Fe from Fe3+ -> Fe2+ and Fe2+ -> Fe). You MUST weight by electron count n: n3*E3 = n1*E1 + n2*E2!",
            "tips_and_tricks": "Always write Delta G = -nFE before combining equations. Higher standard reduction potential means stronger oxidizing agent (more readily reduced)."
        },
        {
            "name": "Electrolytic Conductance & Cell Constant",
            "category": "Conductance",
            "primary": ["conductivity", "conductance", "cell constant", "resistivity", "resistance of conductivity cell", "s cm^-1", "s cm^{-1}", "s m^-1", "molar conductivity", "molar conductance", "debye-huckel"],
            "formula_cues": [r"\kappa", r"\lambda_m", r"\wedge_m", r"g^*", r"1000\kappa", r"1000 \cdot \kappa"],
            "secondary": ["resistance", "solution", "siemens", "ohm"],
            "keywords": ["conductivity", "conductance", "cell constant", "resistivity", "resistance", r"\kappa", "kappa", "s cm^-1", "s m^-1"],
            "summary": "Conductivity kappa = (1/R) * (l/A) = G * G*. Molar conductivity Lambda_m = 1000 * kappa / M (in S cm^2 mol^-1) or kappa / (1000 * M) (in S m^2 mol^-1).",
            "standard_formulas": r"\kappa = \frac{1}{R} \left(\frac{l}{A}\right) = G \cdot G^*, \quad \Lambda_m = \frac{1000 \cdot \kappa}{M} \quad (\kappa \text{ in S cm}^{-1})",
            "common_traps": "Unit confusion between cm and m. If kappa is given in S m^-1, Lambda_m = kappa / (1000 * M) or kappa / c (with c in mol m^-3). If in S cm^-1, use 1000*kappa / M.",
            "tips_and_tricks": "Cell constant G* = l/A is constant for a given conductivity cell and does not change with electrolyte solution."
        },
        {
            "name": "Kohlrausch's Law & Weak Electrolyte Dissociation",
            "category": "Electrolyte Behavior",
            "primary": ["kohlrausch", "limiting molar", "infinite dilution", "degree of dissociation", "dissociation constant", "weak electrolyte", "acetic acid", "sparingly soluble", "solubility product", "baso4", "agcl"],
            "formula_cues": [r"\lambda^\circ", r"\lambda^{\circ}", r"\alpha =", r"k_a =", r"k_{sp}"],
            "secondary": ["dissociation", "electrolyte", "weak acid"],
            "keywords": ["kohlrausch", "limiting molar conductivity", "degree of dissociation", "alpha", "dissociation constant", "ka", "weak electrolyte", "acetic acid"],
            "summary": "Independent migration of ions at infinite dilution: Lambda°_m = nu_+ * lambda°_+ + nu_- * lambda°_-. Degree of dissociation alpha = Lambda_m / Lambda°_m, Ostwald's dilution law Ka = c*alpha^2 / (1 - alpha).",
            "standard_formulas": r"\Lambda_m^{\circ} = \nu_+ \lambda_+^{\circ} + \nu_- \lambda_-^{\circ}, \quad \alpha = \frac{\Lambda_m}{\Lambda_m^{\circ}}, \quad K_a = \frac{c \alpha^2}{1 - \alpha}",
            "common_traps": "1. Forgetting to multiply ionic conductances by the stoichiometric numbers (e.g. for Al2(SO4)3, 2*lambda(Al3+) + 3*lambda(SO4 2-)). 2. For weak acids, if alpha is not << 1, do not approximate 1 - alpha approx 1.",
            "tips_and_tricks": "Lambda°_m for weak electrolytes like CH3COOH can be determined using strong electrolytes: Lambda°(CH3COOH) = Lambda°(CH3COONa) + Lambda°(HCl) - Lambda°(NaCl)."
        },
        {
            "name": "Faraday's Laws of Electrolysis",
            "category": "Quantitative Electrolysis",
            "primary": ["faraday", "electrolysis", "electrolysed", "electrolyzed", "mass deposited", "deposited at cathode", "charge passed", "96500", "current passed", "electroplating", "moles of metal", "liberated at"],
            "formula_cues": [r"96500", r"i \cdot t", r"it/f", r"w = z"],
            "secondary": ["coulomb", "ampere", "current", "cathode", "deposit", "seconds"],
            "keywords": ["faraday", "electrolysis", "mass deposited", "current", "coulomb", "charge", "ampere", "96500", "w = z i t", "it / f"],
            "summary": "First and second laws of electrolysis: Mass deposited w = Z*I*t = (M / (n*F)) * I*t. Charge Q = I*t = n_e * F.",
            "standard_formulas": r"w = \frac{M \cdot I \cdot t}{n \cdot F}, \quad \text{Moles of metal} = \frac{I \cdot t}{n \cdot F}, \quad F \approx 96500\text{ C mol}^{-1}",
            "common_traps": "1. Using incorrect n-factor (electrons transferred per atom/molecule). E.g. for O2 from H2O, 4 electrons are needed for 1 mole of O2 (n=4). For H2, n=2. 2. Time must strictly be in seconds.",
            "tips_and_tricks": "Volume of gas at STP: moles * 22.4 L or 22.7 L. For electroplating problems, volume = Area * thickness, and mass = density * volume."
        },
        {
            "name": "Commercial Batteries, Fuel Cells & Corrosion",
            "category": "Applied Electrochemistry",
            "primary": ["battery", "batteries", "lead storage", "fuel cell", "dry cell", "mercury cell", "corrosion", "rusting", "discharge", "recharging", "sacrificial", "galvanized", "lead-acid"],
            "formula_cues": [r"pb(s)", r"pbo_2", r"2h_2so_4"],
            "secondary": ["anode", "cathode", "cell", "efficiency"],
            "keywords": ["battery", "lead storage", "fuel cell", "dry cell", "corrosion", "rusting", "anode", "cathode", "discharge", "recharge"],
            "summary": "Primary cells (dry cell, mercury cell), secondary cells (lead-acid battery reactions during charge/discharge), H2-O2 fuel cell (efficiency = Delta G / Delta H), and electrochemical rust prevention.",
            "standard_formulas": r"\text{Lead Storage Discharge: } \text{Pb(s)} + \text{PbO}_2\text{(s)} + 2\text{H}_2\text{SO}_4 \rightarrow 2\text{PbSO}_4\text{(s)} + 2\text{H}_2\text{O}, \quad \eta = \frac{\Delta G}{\Delta H}",
            "common_traps": "In lead storage battery, density of H2SO4 decreases on discharging because H2SO4 is consumed and water is formed.",
            "tips_and_tricks": "In galvanic cell: Anode is negative, Cathode is positive (An Ox, Red Cat). In electrolytic cell: Anode is positive, Cathode is negative."
        }
    ],

    "electromagnetic-induction": [
        {
            "name": "Magnetic Flux & Faraday-Lenz Law",
            "category": "Core Principle",
            "primary": ["magnetic flux", "flux through", "faraday", "lenz", "induced emf", "induced current", "dphi/dt", "flux change", "time varying magnetic field", "varying magnetic field", "change in magnetic flux", "flux linkage"],
            "formula_cues": [r"\phi", r"\phi_b", r"b \cdot a", r"\frac{d\phi}{dt}", r"-\frac{d\phi}{dt}", r"\omega ba", r"nba"],
            "secondary": ["loop", "magnetic field", "time", "turns", "emf", "coil"],
            "keywords": ["magnetic flux", "faraday", "lenz", "induced emf", "dphi/dt", "flux change", "b dot a"],
            "summary": "Magnetic flux Phi = B * A * cos(theta). Induced EMF e = -dPhi/dt. Lenz's law dictates that the induced current opposes the change in magnetic flux producing it.",
            "standard_formulas": r"\Phi_B = \vec{B} \cdot \vec{A} = B A \cos\theta, \quad \mathcal{E} = -\frac{d\Phi_B}{dt} = -N \frac{d\Phi_B}{dt}, \quad q = \frac{\Delta \Phi}{R}",
            "common_traps": "1. Charge flown through circuit Delta q = Delta Phi / R is independent of the rate/time of flux change! 2. Angle theta is between B and the normal to the coil area, not the coil plane.",
            "tips_and_tricks": "When a coil of N turns rotates with angular velocity omega: e = NBA*omega*sin(omega*t), e_max = NBA*omega."
        },
        {
            "name": "Motional EMF (Translational & Rotational)",
            "category": "Motional Induction",
            "primary": ["motional emf", "rod moving", "moving rod", "rotating rod", "rotating about", "rod of length", "conducting rod", "rails", "sliding on rails", "metal rod", "bvl", "wire falling under gravity", "aircraft", "axle", "sliding"],
            "formula_cues": [r"bvl", r"b v l", r"\frac{1}{2} b \omega l^2", r"\frac{1}{2}b\omega l^2", r"\omega l^2"],
            "secondary": ["velocity", "speed", "conductor", "moving", "rod"],
            "keywords": ["motional emf", "rod moving", "bvl", "rotating rod", "1/2 b omega l^2", "magnetic force", "rail"],
            "summary": "EMF induced in a conductor of length L moving with velocity v perpendicular to B: e = B*v*L. For a rod rotating about one end: e = (1/2)*B*omega*L^2.",
            "standard_formulas": r"\mathcal{E} = B v L, \quad I = \frac{B v L}{R}, \quad F_{\text{mag}} = \frac{B^2 L^2 v}{R}, \quad \mathcal{E}_{\text{rot}} = \frac{1}{2} B \omega L^2",
            "common_traps": "1. Mechanical power delivered by external agent F*v equals electrical power dissipated I^2*R. 2. For an irregularly shaped wire moving in B, replace it with the straight displacement vector connecting its endpoints.",
            "tips_and_tricks": "Direction of motional EMF: find direction of (v x B). Positive charges accumulate at the end pointed to by (v x B)."
        },
        {
            "name": "Self Inductance & RL Transient Circuits",
            "category": "Inductance & Circuits",
            "primary": ["self inductance", "self-inductance", "inductance of", "solenoid", "solenoid coil", "toroid", "choke coil", "time constant", "rl circuit", "energy stored in inductor", "magnetic energy density", "growth of current", "decay of current", "inductor having inductance"],
            "formula_cues": [r"l \frac{di}{dt}", r"l\frac{di}{dt}", r"\frac{1}{2} l i^2", r"\frac{l}{r}", r"\mu_0 n^2"],
            "secondary": ["inductor", "henry", "switch", "steady state", "resistance"],
            "keywords": ["self inductance", "solenoid", "l di/dt", "time constant", "growth of current", "decay of current", "rl circuit", "energy stored"],
            "summary": "Self-inductance L = Phi / I, induced back EMF e = -L*(dI/dt). Solenoid L = mu_0 * n^2 * A * l. RL circuit current growth: I(t) = I_0*(1 - e^(-t/tau)), tau = L/R.",
            "standard_formulas": r"\mathcal{E} = -L \frac{dI}{dt}, \quad L = \mu_0 n^2 A l, \quad U = \frac{1}{2} L I^2, \quad \tau = \frac{L}{R}, \quad I(t) = \frac{V}{R} (1 - e^{-t/\tau})",
            "common_traps": "At t = 0+ (immediately after switch closing), inductor acts as an open circuit (infinite resistance). At t -> infinity (steady state), inductor acts as an ideal zero-resistance short wire.",
            "tips_and_tricks": "Magnetic energy density in space: u_B = B^2 / (2*mu_0). Inductor resists sudden changes in current, not voltage."
        },
        {
            "name": "Mutual Inductance & Coupled Coils",
            "category": "Coupling",
            "primary": ["mutual inductance", "mutual induction", "coaxial solenoids", "two coils", "two concentric", "coupling coefficient", "coupled coils", "inner loop", "concentric circular loop", "square loop inside", "between circular loop and square"],
            "formula_cues": [r"m \frac{di}{dt}", r"m\frac{di}{dt}", r"k\sqrt{l_1", r"\mu_0 n_1 n_2"],
            "secondary": ["two loops", "secondary", "primary", "coaxial"],
            "keywords": ["mutual inductance", "coaxial solenoids", "coupling", "m di/dt", "two coils"],
            "summary": "Flux in secondary due to current in primary Phi_2 = M*I_1. Induced EMF e_2 = -M*(dI_1/dt). Coaxial solenoids M = mu_0 * n_1 * n_2 * pi * r_1^2 * l.",
            "standard_formulas": r"\mathcal{E}_2 = -M \frac{dI_1}{dt}, \quad M = \mu_0 n_1 n_2 (\pi r_{\text{inner}}^2) l, \quad M = k \sqrt{L_1 L_2} \quad (0 \le k \le 1)",
            "common_traps": "In coaxial solenoids, always use the area of the INNER coil (r_inner), because magnetic field of outer coil only exists over the area of inner coil.",
            "tips_and_tricks": "Reciprocity theorem holds: M_12 = M_21 regardless of differing geometry or number of turns."
        },
        {
            "name": "Induced Electric Field & Eddy Currents",
            "category": "Field Theory",
            "primary": ["induced electric field", "non-conservative", "eddy current", "eddy currents", "cylindrical region", "circular electric field", "line integral of e", "non-electrostatic"],
            "formula_cues": [r"\oint \vec{e}", r"\frac{r}{2} \frac{db}{dt}", r"\frac{r^2}{2r}"],
            "secondary": ["electric field", "cylindrical", "laminated"],
            "keywords": ["induced electric field", "cylindrical", "non-conservative", "eddy current", "line integral"],
            "summary": "Time-varying magnetic field produces non-conservative circular electric field: oint E*dl = -dPhi/dt. E = (r/2)*(dB/dt) for r <= R, E = (R^2 / (2r))*(dB/dt) for r > R.",
            "standard_formulas": r"\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt}, \quad E(r) = \frac{r}{2} \frac{dB}{dt} \; (r \le R), \quad E(r) = \frac{R^2}{2r} \frac{dB}{dt} \; (r > R)",
            "common_traps": "Induced electric field is non-electrostatic: field lines form closed loops and work done along a closed path is non-zero!",
            "tips_and_tricks": "Eddy currents are minimized by laminating metallic cores with insulation (used in transformers and motors)."
        }
    ],

    "alternating-current": [
        {
            "name": "AC Fundamentals: Peak, RMS & Phase",
            "category": "Foundations",
            "primary": ["rms", "r.m.s", "peak value", "root mean square", "average value", "peak current", "rms current", "rms voltage", "phase difference", "instantaneous value", "household electric", "peak to peak"],
            "formula_cues": [r"i_{rms}", r"v_{rms}", r"e_{rms}", r"\frac{i_0}{\sqrt{2}}", r"\frac{v_0}{\sqrt{2}}", r"\sqrt{2}", r"sin(100\pi t)"],
            "secondary": ["alternating current", "ac source", "frequency", "cycle"],
            "keywords": ["rms", "peak value", "root mean square", "average value", "phase difference", r"i_0 / \sqrt{2}", "v_rms"],
            "summary": "Sinusoidal AC quantities: I_rms = I_0 / sqrt(2) approx 0.707*I_0, V_rms = V_0 / sqrt(2). Average current over full cycle is 0, over half cycle is (2/pi)*I_0 approx 0.637*I_0.",
            "standard_formulas": r"I_{\text{rms}} = \frac{I_0}{\sqrt{2}}, \quad V_{\text{rms}} = \frac{V_0}{\sqrt{2}}, \quad I_{\text{avg, half}} = \frac{2 I_0}{\pi}",
            "common_traps": "AC voltmeters and ammeters measure RMS values, not peak values! When JEE specifies '220 V AC', it always denotes V_rms.",
            "tips_and_tricks": "Peak voltage for 220 V AC household line is 220 * sqrt(2) approx 311 V."
        },
        {
            "name": "Reactance: Inductive & Capacitive",
            "category": "Impedance Elements",
            "primary": ["reactance", "inductive reactance", "capacitive reactance", "pure inductor", "pure capacitor", "capacitor in ac", "inductor in ac", "omega l", "1 / omega c", "x_l", "x_c"],
            "formula_cues": [r"x_l", r"x_c", r"\omega l", r"\frac{1}{\omega c}", r"2\pi f l", r"\frac{1}{2\pi f c}"],
            "secondary": ["capacitor", "inductor", "frequency", "microfarad", "millihenry"],
            "keywords": ["reactance", "inductive reactance", "capacitive reactance", "x_l", "x_c", r"\omega l", r"1 / \omega c", "pure inductor", "pure capacitor"],
            "summary": "Pure L: voltage leads current by 90° (pi/2), X_L = omega*L = 2*pi*f*L. Pure C: current leads voltage by 90° (pi/2), X_C = 1 / (omega*C) = 1 / (2*pi*f*C).",
            "standard_formulas": r"X_L = \omega L = 2\pi f L, \quad X_C = \frac{1}{\omega C} = \frac{1}{2\pi f C}",
            "common_traps": "In DC (f = 0), inductor has X_L = 0 (short circuit) and capacitor has X_C = infinity (open circuit/blocks DC).",
            "tips_and_tricks": "Mnemonic 'CIVIL': In Capacitor (C), Current (I) leads Voltage (V); in Inductor (L), Voltage (V) leads Current (I)."
        },
        {
            "name": "Series LCR Circuit & Impedance",
            "category": "Circuits",
            "primary": ["lcr", "series lcr", "l-c-r", "impedance", "phase angle", "tan phi", "voltage across", "phasor", "phasor diagram", "resistor and capacitor in series", "inductor and resistor in series", "rlc"],
            "formula_cues": [r"z = \sqrt", r"\tan\phi", r"\sqrt{r^2 +", r"\sqrt{v_r^2"],
            "secondary": ["resistor", "capacitor", "inductor", "phase", "series"],
            "keywords": ["lcr", "series lcr", "impedance", r"z = \sqrt", "phase angle", "tan phi", "phasor"],
            "summary": "Series LCR impedance Z = sqrt(R^2 + (X_L - X_C)^2). Current I = V / Z. Phase angle tan(phi) = (X_L - X_C) / R. Voltage across elements V = sqrt(V_R^2 + (V_L - V_C)^2).",
            "standard_formulas": r"Z = \sqrt{R^2 + (X_L - X_C)^2}, \quad \tan\phi = \frac{X_L - X_C}{R}, \quad V_{\text{total}} = \sqrt{V_R^2 + (V_L - V_C)^2}",
            "common_traps": "Voltages across series AC components do NOT add algebraically! V_total != V_R + V_L + V_C. Use phasor vector addition: V_total = sqrt(V_R^2 + (V_L - V_C)^2).",
            "tips_and_tricks": "If X_L > X_C, circuit is inductive (voltage leads current). If X_C > X_L, circuit is capacitive (current leads voltage)."
        },
        {
            "name": "Resonance, Q-Factor & Bandwidth",
            "category": "Resonance",
            "primary": ["resonance", "resonant frequency", "quality factor", "q-factor", "q factor", "bandwidth", "sharpness of resonance", "maximum current", "half power frequencies", "at resonance"],
            "formula_cues": [r"\frac{1}{\sqrt{lc}}", r"\frac{1}{\sqrt{l c}}", r"\frac{\omega_0 l}{r}", r"\frac{1}{r}\sqrt{\frac{l}{c}}", r"\omega_0"],
            "secondary": ["sharpness", "current is maximum", "impedance is minimum"],
            "keywords": ["resonance", "resonant frequency", "quality factor", "q factor", "bandwidth", "sharpness", "maximum current"],
            "summary": "At resonance: X_L = X_C, omega_0 = 1 / sqrt(L*C), f_0 = 1 / (2*pi*sqrt(L*C)). Impedance is purely resistive and minimum (Z = R), current is maximum (I = V/R). Q = (1/R)*sqrt(L/C) = omega_0 / Delta_omega.",
            "standard_formulas": r"\omega_0 = \frac{1}{\sqrt{LC}}, \quad Z_{\min} = R, \quad I_{\max} = \frac{V}{R}, \quad Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 C R} = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{\omega_0}{\Delta\omega}",
            "common_traps": "At resonance, V_L and V_C are NOT zero! In fact, V_L = V_C = Q * V_supply, which can be much larger than supply voltage (voltage magnification)!",
            "tips_and_tricks": "Bandwidth Delta_omega = R / L. To increase sharpness of resonance (higher Q), decrease R or increase L/C ratio."
        },
        {
            "name": "Power in AC Circuits & Power Factor",
            "category": "Power & Efficiency",
            "primary": ["power factor", "average power", "power dissipated", "wattless current", "apparent power", "cos phi", "cos𝜙", "true power", "power in an ac circuit", "power in the circuit"],
            "formula_cues": [r"\cos\phi", r"v_{rms} i_{rms} \cos", r"\frac{r}{z}"],
            "secondary": ["watt", "power", "energy dissipation"],
            "keywords": ["power factor", "average power", "cos phi", "wattless current", "p = v_rms i_rms", "apparent power"],
            "summary": "Average power P_avg = V_rms * I_rms * cos(phi). Power factor = cos(phi) = R / Z. In pure L or pure C, phi = 90°, cos(phi) = 0, so average power dissipated is zero (wattless current I_wattless = I_rms * sin(phi)).",
            "standard_formulas": r"P_{\text{avg}} = V_{\text{rms}} I_{\text{rms}} \cos\phi, \quad \cos\phi = \frac{R}{Z} = \frac{R}{\sqrt{R^2 + (X_L - X_C)^2}}, \quad I_{\text{wattless}} = I_{\text{rms}} \sin\phi",
            "common_traps": "Power factor is cos(phi), not tan(phi)! Always compute Z first: cos(phi) = R / Z.",
            "tips_and_tricks": "A choke coil has high inductance L and very low resistance R, allowing it to reduce AC current with negligible power loss (cos phi approx 0)."
        },
        {
            "name": "LC Oscillations & Transformers",
            "category": "Devices & Oscillations",
            "primary": ["transformer", "step up", "step down", "turns ratio", "primary coil", "secondary coil", "efficiency of transformer", "lc oscillation", "lc circuit", "energy transferred to the inductor", "energy in the capacitor is transferred"],
            "formula_cues": [r"\frac{v_s}{v_p}", r"\frac{n_s}{n_p}", r"\frac{i_p}{i_s}", r"q(t) = q_0"],
            "secondary": ["primary", "secondary", "core", "efficiency"],
            "keywords": ["transformer", "turns ratio", "step up", "step down", "lc oscillation", "efficiency", "n_s / n_p"],
            "summary": "Ideal transformer: V_s / V_p = N_s / N_p = I_p / I_s. Efficiency eta = (V_s * I_s) / (V_p * I_p) * 100%. LC oscillation frequency omega = 1 / sqrt(LC) with energy conservation U_total = q^2/(2C) + (1/2)*L*i^2.",
            "standard_formulas": r"\frac{V_s}{V_p} = \frac{N_s}{N_p} = \frac{I_p}{I_s}, \quad \eta = \frac{P_{\text{out}}}{P_{\text{in}}} = \frac{V_s I_s}{V_p I_p}, \quad q(t) = q_0 \cos(\omega_0 t)",
            "common_traps": "Transformers work ONLY with AC, never with steady DC (dPhi/dt = 0 for DC, so secondary voltage is zero).",
            "tips_and_tricks": "In step-up transformer (N_s > N_p), voltage increases but current decreases, keeping total power constant."
        }
    ],

    "vector-algebra": [
        {
            "name": "Dot Product, Projections & Orthogonality",
            "category": "Scalar Product",
            "primary": ["dot product", "scalar product", "projection of", "scalar projection", "orthogonal", "angle between", "unit vector perpendicular to neither", "modulus of", "mutually perpendicular"],
            "formula_cues": [r"\cdot", r"\perp", r"|\vec{a}|", r"|\vec{b}|", r"|\vec{u}|"],
            "secondary": ["perpendicular", "unit vector", "magnitude", "acute angle", "obtuse angle"],
            "keywords": ["dot product", "scalar product", "projection", "perpendicular", "orthogonal", r"\vec{a} \cdot \vec{b}", "angle between"],
            "summary": "Dot product a . b = |a||b|*cos(theta) = a_x*b_x + a_y*b_y + a_z*b_z. Condition for perpendicular vectors: a . b = 0. Scalar projection of a on b is (a . b) / |b|.",
            "standard_formulas": r"\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos\theta, \quad \vec{a} \perp \vec{b} \iff \vec{a} \cdot \vec{b} = 0, \quad \text{Proj}_{\vec{b}} \vec{a} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}",
            "common_traps": "1. Projection vector along b is ((a . b) / |b|^2) * b. 2. Modulus square |a + b|^2 = |a|^2 + |b|^2 + 2(a . b). Do not write 2|a||b| unless vectors are collinear!",
            "tips_and_tricks": "To find unit vector bisecting the angle between a and b: (hat{a} + hat{b}) / |hat{a} + hat{b}|."
        },
        {
            "name": "Cross Product & Geometric Areas",
            "category": "Vector Product",
            "primary": ["cross product", "vector product", "area of triangle", "area of the triangle", "area of parallelogram", "area of the parallelogram", "adjacent sides", "diagonals of"],
            "formula_cues": [r"\times", r"|\vec{a} \times \vec{b}|", r"|\vec{u} \times \vec{v}|"],
            "secondary": ["parallelogram", "triangle", "normal to the plane"],
            "keywords": ["cross product", "vector product", "area of triangle", "area of parallelogram", "perpendicular unit vector", r"\vec{a} \times \vec{b}"],
            "summary": "Cross product a x b = |a||b|*sin(theta)*hat{n}. Condition for collinear/parallel vectors: a x b = 0. Area of parallelogram with sides a, b is |a x b|; with diagonals d1, d2 is (1/2)*|d1 x d2|.",
            "standard_formulas": r"\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix}, \quad \text{Area}_{\triangle} = \frac{1}{2} |\vec{a} \times \vec{b}|, \quad \hat{n} = \pm \frac{\vec{a} \times \vec{b}}{|\vec{a} \times \vec{b}|}",
            "common_traps": "1. Cross product is anti-commutative: a x b = -(b x a). 2. Lagrange's identity: |a x b|^2 = |a|^2*|b|^2 - (a . b)^2.",
            "tips_and_tricks": "Area of parallelogram given diagonals d1 and d2 is (1/2)*|d1 x d2|, NOT |d1 x d2|!"
        },
        {
            "name": "Scalar Triple Product (Box Product) & Coplanarity",
            "category": "Volume & Coplanarity",
            "primary": ["scalar triple product", "box product", "coplanar", "co-planar", "coplanarity", "volume of parallelepiped", "volume of tetrahedron", "parallelepiped", "tetrahedron"],
            "formula_cues": [r"[\vec{a}", r"[\vec{b}", r"[\vec{u}", r"\cdot (\vec{b} \times", r"\cdot (\vec{a} \times", r"\cdot (\vec{c} \times"],
            "secondary": ["same plane", "lie in plane"],
            "keywords": ["scalar triple product", "box product", "coplanar", "[a b c]", "volume of parallelepiped", "tetrahedron"],
            "summary": "Box product [a b c] = a . (b x c) = determinant of components. Three vectors are coplanar if and only if [a b c] = 0. Volume of parallelepiped = |[a b c]|; volume of tetrahedron = (1/6)*|[a b c]|.",
            "standard_formulas": r"[\vec{a}\; \vec{b}\; \vec{c}] = \vec{a} \cdot (\vec{b} \times \vec{c}) = \begin{vmatrix} a_x & a_y & a_z \\ b_x & b_y & b_z \\ c_x & c_y & c_z \end{vmatrix}, \quad [\vec{a}\; \vec{b}\; \vec{c}] = 0 \iff \text{coplanar}",
            "common_traps": "1. Cyclic permutation maintains value: [a b c] = [b c a] = [c a b]. Non-cyclic permutation negates value: [a c b] = -[a b c]. 2. If any two vectors are equal or parallel, [a a b] = 0.",
            "tips_and_tricks": "Four points A, B, C, D are coplanar if [AB AC AD] = 0."
        },
        {
            "name": "Vector Triple Product & Lagrange Identity",
            "category": "Triple Products",
            "primary": ["vector triple product", "lagrange identity", "lagrange's identity", "triple vector product"],
            "formula_cues": [r"\times (\vec{b} \times", r"\times (\vec{c} \times", r"\times (\vec{a} \times", r"(\vec{a} \times \vec{b}) \times", r"(\vec{b} \times \vec{c}) \times"],
            "secondary": ["bac - cab", "bac cab"],
            "keywords": ["vector triple product", "a x (b x c)", "bac - cab", "lagrange"],
            "summary": "Vector triple product expands via the BAC-CAB rule: a x (b x c) = (a . c)*b - (a . b)*c. It lies in the plane of b and c, perpendicular to a.",
            "standard_formulas": r"\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}, \quad (\vec{a} \times \vec{b}) \times \vec{c} = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{b} \cdot \vec{c})\vec{a}",
            "common_traps": "Vector triple product is NOT associative: a x (b x c) != (a x b) x c. Pay rigorous attention to bracket positioning!",
            "tips_and_tricks": "Mnemonic: 'BAC minus CAB'. Dot product of outer vectors multiplied by inner vector, minus dot product of first two multiplied by third."
        },
        {
            "name": "Linear Combination & Vector Equations",
            "category": "Vector Equations",
            "primary": ["linear combination", "vector equation", "find vector", "unknown vector", "vector c be such that", "vector r be such that", "vector v be such that", "vectors c such that", "vector r such that", "linearly dependent", "linearly independent"],
            "formula_cues": [r"\vec{r} \times", r"\vec{r} \cdot", r"\vec{c} = \lambda", r"\lambda\vec{a}+\mu\vec{b}", r"\lambda\overset{⃗}{a}", r"\vec{c} = \alpha", r"2(\vec{a} \times \vec{b})"],
            "secondary": ["plane of vectors", "scalars lambda", "linearly"],
            "keywords": ["linear combination", "coplanar vectors", "vector equation", "find vector r", r"r \times", r"r \cdot"],
            "summary": "Solving vector equations of the form r x a = b and r . c = d. Express r as a linear combination or take cross/dot products on both sides with known vectors.",
            "standard_formulas": r"\vec{r} = x \vec{a} + y \vec{b} + z (\vec{a} \times \vec{b}), \quad \text{or take } \vec{a} \times (\vec{r} \times \vec{b}) \text{ to decouple}",
            "common_traps": "When r x a = b, note that b must be perpendicular to a (b . a = 0). Then r x a = b implies r = lambda*a + (a x b) / |a|^2.",
            "tips_and_tricks": "If r x a = b, taking dot product with c gives [r a c] = b . c. Taking cross product with a helps resolve r."
        },
        {
            "name": "Section Formula, Collinearity & Centroids",
            "category": "Geometry & Position Vectors",
            "primary": ["section formula", "collinear", "collinearity", "centroid", "internal division", "external division", "divides the line segment", "points are collinear", "points a, b, c are collinear"],
            "formula_cues": [r"\frac{m\vec{b}", r"\frac{\vec{a}+\vec{b}+\vec{c}}{3}", r"\vec{OP}=", r"\vec{OR}="],
            "secondary": ["midpoint", "equidistant", "origin"],
            "keywords": ["section formula", "collinear", "centroid", "internal division", "external division", "position vector"],
            "summary": "Section formula r = (m*b + n*a) / (m + n). Three points A, B, C are collinear if AB = lambda * BC or AB x AC = 0. Centroid of triangle G = (a + b + c) / 3.",
            "standard_formulas": r"\vec{r} = \frac{m\vec{b} + n\vec{a}}{m + n}, \quad \vec{G} = \frac{\vec{a} + \vec{b} + \vec{c}}{3}, \quad \vec{a} = \lambda \vec{b} \iff \text{collinear}",
            "common_traps": "Collinear vectors can have opposite directions (negative lambda). External division has a minus sign: (mb - na)/(m - n).",
            "tips_and_tricks": "In a triangle, line joining midpoints is parallel to third side and half its length: MN = (1/2)*BC."
        }
    ]
}


def extract_formulas_from_text(text: str) -> List[str]:
    """Find math formulas enclosed in $...$ or \\begin{aligned}...\\end{aligned}."""
    formulas = []
    # Match inline math
    inline_matches = re.findall(r'\$([^\$]{3,80})\$', text)
    for m in inline_matches:
        m_clean = m.strip()
        if any(sym in m_clean for sym in ['=', r'\times', r'\frac', '^', '_', r'\cdot', r'\vec', r'\omega', r'\kappa', r'\mathcal']):
            formulas.append(m_clean)
    return list(dict.fromkeys(formulas))[:6]


def estimate_difficulty(q: QuestionModel) -> str:
    """
    Estimate question difficulty ('Easy', 'Medium', 'Hard') based on:
    - Text and explanation length
    - Number of formulas and derivation steps
    - Numerical vs MCQ
    """
    score = 0
    full_text = f"{q.question_text} {q.explanation_text}"
    
    # Length & steps
    if len(q.explanation_text or "") > 400:
        score += 2
    elif len(q.explanation_text or "") > 200:
        score += 1

    # Formulas density
    math_count = full_text.count('$')
    if math_count > 10:
        score += 2
    elif math_count > 4:
        score += 1

    # Multi-concept or matrix or calculus
    if any(term in full_text.lower() for term in ['differential', 'integral', 'matrix', 'determinant', 'simultaneous', 'quadratic']):
        score += 1

    # Numerical questions have no options
    if q.question_type == "Numerical":
        score += 1

    if score <= 2:
        return "Easy"
    elif score <= 4:
        return "Medium"
    else:
        return "Hard"


def match_concepts_for_question(
    q: QuestionModel,
    chapter_slug: str
) -> Tuple[List[str], List[Tuple[str, str]]]:
    """
    Match a question to relevant concepts in the chapter taxonomy.
    Returns:
        (matched_concept_names, list of (concept_name, relevance_note))
    """
    matched_names: List[str] = []
    links_info: List[Tuple[str, str]] = []

    content = f"{q.question_text} {q.explanation_text}".lower()

    # Check curated taxonomy
    taxonomy = CURATED_TAXONOMY.get(chapter_slug, [])
    
    for c_def in taxonomy:
        is_match = False
        # 1. Primary high-signal keywords
        if any(p in content for p in c_def.get("primary", [])):
            is_match = True
        # 2. Key formula cues
        elif any(f.lower() in content for f in c_def.get("formula_cues", [])):
            is_match = True
        # 3. Secondary contextual terms (require at least 2)
        elif sum(1 for s in c_def.get("secondary", []) if s in content) >= 2:
            is_match = True
        # 4. Backward compatibility with any legacy keywords
        elif any(k.lower() in content for k in c_def.get("keywords", [])):
            is_match = True

        if is_match:
            c_name = c_def["name"]
            matched_names.append(c_name)
            rel_note = f"Tests {c_name} in {q.year} ({q.shift or 'JEE Main'})"
            links_info.append((c_name, rel_note))

    # If no curated match found, create a sensible fallback topic
    if not matched_names:
        fallback_name = f"{chapter_slug.replace('-', ' ').title()} - Core Application"
        matched_names.append(fallback_name)
        links_info.append((fallback_name, f"Standard problem archetype in {q.year}"))

    return (matched_names, links_info)


def analyze_chapter_questions(
    questions: List[QuestionModel],
    chapter_slug: str
) -> Tuple[List[QuestionModel], List[ConceptModel], List[ConceptPYQLinkModel]]:
    """
    Run comprehensive concept extraction on all questions of a chapter.
    Returns enriched questions, chapter concept models, and link models.
    """
    # Concept frequency counter and PYQ collector
    concept_stats: Dict[str, Dict[str, Any]] = {}

    # Initialize taxonomy concepts
    taxonomy = CURATED_TAXONOMY.get(chapter_slug, [])
    for c_def in taxonomy:
        concept_stats[c_def["name"]] = {
            "def": c_def,
            "pyq_ids": [],
            "years": set(),
            "formulas": set()
        }

    enriched_questions: List[QuestionModel] = []
    all_links: List[ConceptPYQLinkModel] = []

    for q in questions:
        # Extract formulas
        formulas = extract_formulas_from_text(f"{q.question_text} {q.explanation_text}")
        q.key_formulas = formulas
        q.difficulty = estimate_difficulty(q)

        # Match concepts
        matched_concepts, links = match_concepts_for_question(q, chapter_slug)
        q.key_concepts = matched_concepts
        if matched_concepts:
            q.topic_tag = matched_concepts[0]

        enriched_questions.append(q)

        # Aggregate stats
        for c_name, rel_note in links:
            if c_name not in concept_stats:
                concept_stats[c_name] = {
                    "def": {
                        "name": c_name,
                        "category": "General Concept",
                        "summary": f"Key problem pattern in {chapter_slug.replace('-', ' ').title()}.",
                        "standard_formulas": "",
                        "common_traps": "Watch for algebraic and sign errors.",
                        "tips_and_tricks": "Verify dimensions and boundary conditions."
                    },
                    "pyq_ids": [],
                    "years": set(),
                    "formulas": set()
                }
            concept_stats[c_name]["pyq_ids"].append(q.id or q.question_index)
            concept_stats[c_name]["years"].add(q.year)
            for f in formulas[:2]:
                concept_stats[c_name]["formulas"].add(f)

    # Build ConceptModel list
    concept_models: List[ConceptModel] = []
    for c_name, data in concept_stats.items():
        c_def = data["def"]
        freq = len(data["pyq_ids"])
        
        # Tier classification
        if freq >= 15:
            tier = "Very High"
        elif freq >= 8:
            tier = "High"
        elif freq >= 3:
            tier = "Moderate"
        else:
            tier = "Standard"

        # Formulas string
        sample_formulas = c_def.get("standard_formulas", "")
        if not sample_formulas and data["formulas"] and not c_name.endswith("Core Application"):
            # Only pick formulas that look like algebraic / symbolic expressions, not raw arithmetic
            valid_f = [f for f in data["formulas"] if not re.match(r'^[0-9\.\s\+\-\*/=]+$', f)]
            if valid_f:
                sample_formulas = r", \quad ".join(valid_f[:3])

        concept = ConceptModel(
            chapter_slug=chapter_slug,
            name=c_name,
            category=c_def.get("category", "Core Concept"),
            summary=c_def.get("summary", ""),
            standard_formulas=sample_formulas,
            exam_frequency=freq,
            frequency_tier=tier,
            common_traps=c_def.get("common_traps", ""),
            tips_and_tricks=c_def.get("tips_and_tricks", ""),
            pyq_ids=data["pyq_ids"]
        )
        concept_models.append(concept)

    # Sort concepts by frequency descending
    concept_models.sort(key=lambda x: x.exam_frequency, reverse=True)

    return (enriched_questions, concept_models, all_links)
