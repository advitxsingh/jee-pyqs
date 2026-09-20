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
            "summary": "Calculation of non-standard cell potential $E_{\\text{cell}} = E^\\circ_{\\text{cell}} - \\frac{0.0591}{n}\\log_{10} Q$ at $298\\text{ K}$, equilibrium constant $K_{eq}$, and concentration cells where $E^\\circ_{\\text{cell}} = 0$.",
            "standard_formulas": r"E_{\text{cell}} = E^{\circ}_{\text{cell}} - \frac{0.0591}{n} \log_{10} Q, \quad \Delta G^{\circ} = -n F E^{\circ}_{\text{cell}} = -2.303 RT \log_{10} K",
            "common_traps": "1. Forgetting to raise concentrations to their stoichiometric powers in reaction quotient $Q$. 2. Confusing oxidation vs reduction potential signs: $E^\\circ_{\\text{red}} = -E^\\circ_{\\text{ox}}$. 3. In concentration cells, anode is always the dilute compartment ($c_1 < c_2$).",
            "tips_and_tricks": "At $298\\text{ K}$, $E^\\circ = \\frac{0.0591}{n}\\log_{10} K$. For spontaneous cell operation, $E_{\\text{cell}} > 0$ and $\\Delta G < 0$."
        },
        {
            "name": "Electrode Potential & Delta G Relation",
            "category": "Thermodynamics",
            "primary": ["gibbs", "delta g", r"\delta g", r"\deltag", "spontaneity", "nfe", "standard reduction potential", "standard electrode potential", "reducing agent", "oxidizing agent", "half-cell potential", "tendency to act as reducing"],
            "formula_cues": [r"\delta g", r"\deltag", r"-nfe", r"e^{\circ}", r"fe^{3+}/fe^{2+}"],
            "secondary": ["reduction potential", "spontaneous", "redox", "oxidation potential"],
            "keywords": ["gibbs", r"\delta g", "delta g", "spontaneity", "nfe", "electrode potential", "standard reduction"],
            "summary": "Relationship between standard reduction potentials and Gibbs free energy: $\\Delta G^\\circ = -nFE^\\circ$. When combining half-reactions, always add extensive $\\Delta G$ values, never add intensive $E^\\circ$ potentials directly!",
            "standard_formulas": r"\Delta G = -nFE, \quad \Delta G^{\circ}_3 = \Delta G^{\circ}_1 + \Delta G^{\circ}_2 \implies n_3 E^{\circ}_3 = n_1 E^{\circ}_1 + n_2 E^{\circ}_2",
            "common_traps": "Directly adding $E^\\circ$ potentials of two half-cells to obtain $E^\\circ$ of a composite couple (e.g. $\\text{Fe}^{3+} \\to \\text{Fe}$ from $\\text{Fe}^{3+} \\to \\text{Fe}^{2+}$ and $\\text{Fe}^{2+} \\to \\text{Fe}$). You MUST weight by electron transfer count: $n_3 E_3^\\circ = n_1 E_1^\\circ + n_2 E_2^\\circ$!",
            "tips_and_tricks": "Always write $\\Delta G = -nFE$ before combining half-reactions. A more positive standard reduction potential $E^\\circ$ denotes a stronger oxidizing agent (more readily reduced)."
        },
        {
            "name": "Electrolytic Conductance & Cell Constant",
            "category": "Conductance",
            "primary": ["conductivity", "conductance", "cell constant", "resistivity", "resistance of conductivity cell", "s cm^-1", "s cm^{-1}", "s m^-1", "molar conductivity", "molar conductance", "debye-huckel"],
            "formula_cues": [r"\kappa", r"\lambda_m", r"\wedge_m", r"g^*", r"1000\kappa", r"1000 \cdot \kappa"],
            "secondary": ["resistance", "solution", "siemens", "ohm"],
            "keywords": ["conductivity", "conductance", "cell constant", "resistivity", "resistance", r"\kappa", "kappa", "s cm^-1", "s m^-1"],
            "summary": "Specific conductivity $\\kappa = \\frac{1}{R}\\left(\\frac{l}{A}\\right) = G \\cdot G^*$. Molar conductivity $\\Lambda_m = \\frac{1000\\kappa}{M}$ (with $\\kappa$ in $\\text{S cm}^{-1}$) or $\\Lambda_m = \\frac{\\kappa}{1000M}$ (with $\\kappa$ in $\\text{S m}^{-1}$).",
            "standard_formulas": r"\kappa = \frac{1}{R} \left(\frac{l}{A}\right) = G \cdot G^*, \quad \Lambda_m = \frac{1000 \cdot \kappa}{M} \quad (\kappa \text{ in S cm}^{-1})",
            "common_traps": "Unit confusion between $\\text{cm}$ and $\\text{m}$. If $\\kappa$ is in $\\text{S m}^{-1}$, use $\\Lambda_m = \\frac{\\kappa}{c}$ ($c$ in $\\text{mol m}^{-3}$). If in $\\text{S cm}^{-1}$, use $\\Lambda_m = \\frac{1000\\kappa}{M}$ ($M$ in $\\text{mol L}^{-1}$).",
            "tips_and_tricks": "Cell constant $G^* = \\frac{l}{A}$ is an intrinsic geometric property of the conductivity cell and is strictly independent of the electrolyte filled."
        },
        {
            "name": "Kohlrausch's Law & Weak Electrolyte Dissociation",
            "category": "Electrolyte Behavior",
            "primary": ["kohlrausch", "limiting molar", "infinite dilution", "degree of dissociation", "dissociation constant", "weak electrolyte", "acetic acid", "sparingly soluble", "solubility product", "baso4", "agcl"],
            "formula_cues": [r"\lambda^\circ", r"\lambda^{\circ}", r"\alpha =", r"k_a =", r"k_{sp}"],
            "secondary": ["dissociation", "electrolyte", "weak acid"],
            "keywords": ["kohlrausch", "limiting molar conductivity", "degree of dissociation", "alpha", "dissociation constant", "ka", "weak electrolyte", "acetic acid"],
            "summary": "Independent migration of ions at infinite dilution: $\\Lambda_m^\\circ = \\nu_+ \\lambda_+^\\circ + \\nu_- \\lambda_-^\\circ$. Degree of dissociation $\\alpha = \\frac{\\Lambda_m}{\\Lambda_m^\\circ}$, and Ostwald's dilution law $K_a = \\frac{c\\alpha^2}{1 - \\alpha}$.",
            "standard_formulas": r"\Lambda_m^{\circ} = \nu_+ \lambda_+^{\circ} + \nu_- \lambda_-^{\circ}, \quad \alpha = \frac{\Lambda_m}{\Lambda_m^{\circ}}, \quad K_a = \frac{c \alpha^2}{1 - \alpha}",
            "common_traps": "1. Forgetting to multiply ionic conductances by stoichiometric coefficients (e.g., for $\\text{Al}_2(\\text{SO}_4)_3 \\implies 2\\lambda^\\circ(\\text{Al}^{3+}) + 3\\lambda^\\circ(\\text{SO}_4^{2-})$). 2. For weak electrolytes, if $\\alpha \\not\\ll 1$, do not approximate $1 - \\alpha \\approx 1$.",
            "tips_and_tricks": "$\\Lambda_m^\\circ$ for weak electrolytes like $\\text{CH}_3\\text{COOH}$ can be obtained using strong electrolytes: $\\Lambda_m^\\circ(\\text{CH}_3\\text{COOH}) = \\Lambda_m^\\circ(\\text{CH}_3\\text{COONa}) + \\Lambda_m^\\circ(\\text{HCl}) - \\Lambda_m^\\circ(\\text{NaCl})$."
        },
        {
            "name": "Faraday's Laws of Electrolysis",
            "category": "Quantitative Electrolysis",
            "primary": ["faraday", "electrolysis", "electrolysed", "electrolyzed", "mass deposited", "deposited at cathode", "charge passed", "96500", "current passed", "electroplating", "moles of metal", "liberated at"],
            "formula_cues": [r"96500", r"i \cdot t", r"it/f", r"w = z"],
            "secondary": ["coulomb", "ampere", "current", "cathode", "deposit", "seconds"],
            "keywords": ["faraday", "electrolysis", "mass deposited", "current", "coulomb", "charge", "ampere", "96500", "w = z i t", "it / f"],
            "summary": "First and second laws of quantitative electrolysis: Mass deposited $w = Z I t = \\frac{M \\cdot I \\cdot t}{n F}$. Total charge passed $Q = I t = n_e F$.",
            "standard_formulas": r"w = \frac{M \cdot I \cdot t}{n \cdot F}, \quad \text{Moles of metal} = \frac{I \cdot t}{n \cdot F}, \quad F \approx 96500\text{ C mol}^{-1}",
            "common_traps": "1. Using an incorrect $n$-factor (electrons transferred per molecule). E.g. for $\\text{O}_2$ from $\\text{H}_2\\text{O}$, $n = 4$; for $\\text{H}_2$, $n = 2$. 2. Time $t$ must strictly be substituted in seconds ($s$).",
            "tips_and_tricks": "Gas volume at STP: $\\text{Moles} \\times 22.4\\text{ L}$. For electroplating, $\\text{Volume} = \\text{Area} \\times \\text{Thickness}$ and $\\text{Mass} = \\text{Density} \\times \\text{Volume}$."
        },
        {
            "name": "Commercial Batteries, Fuel Cells & Corrosion",
            "category": "Applied Electrochemistry",
            "primary": ["battery", "batteries", "lead storage", "fuel cell", "dry cell", "mercury cell", "corrosion", "rusting", "discharge", "recharging", "sacrificial", "galvanized", "lead-acid"],
            "formula_cues": [r"pb(s)", r"pbo_2", r"2h_2so_4"],
            "secondary": ["anode", "cathode", "cell", "efficiency"],
            "keywords": ["battery", "lead storage", "fuel cell", "dry cell", "corrosion", "rusting", "anode", "cathode", "discharge", "recharge"],
            "summary": "Primary cells (dry cell, mercury cell), secondary lead-acid batteries (charge/discharge cycles), $\\text{H}_2\\text{-O}_2$ fuel cells (thermodynamic efficiency $\\eta = \\frac{\\Delta G}{\\Delta H}$), and electrochemical corrosion prevention.",
            "standard_formulas": r"\text{Lead Storage Discharge: } \text{Pb(s)} + \text{PbO}_2\text{(s)} + 2\text{H}_2\text{SO}_4 \rightarrow 2\text{PbSO}_4\text{(s)} + 2\text{H}_2\text{O}, \quad \eta = \frac{\Delta G}{\Delta H}",
            "common_traps": "In a lead storage battery, the density of $\\text{H}_2\\text{SO}_4$ decreases during discharge because sulfuric acid is consumed and water is produced.",
            "tips_and_tricks": "In galvanic cells: Anode is negative, Cathode is positive (An Ox, Red Cat). In electrolytic cells: Anode is positive, Cathode is negative."
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
            "summary": "Magnetic flux $\\Phi_B = \\vec{B} \\cdot \\vec{A} = B A \\cos\\theta$. Induced EMF $\\mathcal{E} = -\\frac{d\\Phi_B}{dt} = -N \\frac{d\\Phi_B}{dt}$. Lenz's law dictates that induced currents oppose the change in magnetic flux.",
            "standard_formulas": r"\Phi_B = \vec{B} \cdot \vec{A} = B A \cos\theta, \quad \mathcal{E} = -\frac{d\Phi_B}{dt} = -N \frac{d\Phi_B}{dt}, \quad q = \frac{\Delta \Phi}{R}",
            "common_traps": "1. Total induced charge flown $\\Delta q = \\frac{\\Delta\\Phi_B}{R}$ is independent of the rate or time interval of flux change! 2. Angle $\\theta$ is measured from the surface normal $\\vec{A}$, not the coil plane.",
            "tips_and_tricks": "When an $N$-turn coil rotates with angular velocity $\\omega$ in field $B$: $\\mathcal{E}(t) = N B A \\omega \\sin(\\omega t)$, with peak EMF $\\mathcal{E}_0 = N B A \\omega$."
        },
        {
            "name": "Motional EMF (Translational & Rotational)",
            "category": "Motional Induction",
            "primary": ["motional emf", "rod moving", "moving rod", "rotating rod", "rotating about", "rod of length", "conducting rod", "rails", "sliding on rails", "metal rod", "bvl", "wire falling under gravity", "aircraft", "axle", "sliding"],
            "formula_cues": [r"bvl", r"b v l", r"\frac{1}{2} b \omega l^2", r"\frac{1}{2}b\omega l^2", r"\omega l^2"],
            "secondary": ["velocity", "speed", "conductor", "moving", "rod"],
            "keywords": ["motional emf", "rod moving", "bvl", "rotating rod", "1/2 b omega l^2", "magnetic force", "rail"],
            "summary": "Motional EMF in a conductor moving through field $\\vec{B}$: $\\mathcal{E} = B v L$. For a rod rotating about one pivot with angular speed $\\omega$: $\\mathcal{E}_{\\text{rot}} = \\frac{1}{2} B \\omega L^2$.",
            "standard_formulas": r"\mathcal{E} = B v L, \quad I = \frac{B v L}{R}, \quad F_{\text{mag}} = \frac{B^2 L^2 v}{R}, \quad \mathcal{E}_{\text{rot}} = \frac{1}{2} B \omega L^2",
            "common_traps": "1. Mechanical power delivered by external pulling force $P_{\\text{mech}} = F_{\\text{ext}} v$ exactly matches electrical Joule dissipation $I^2 R = \\frac{B^2 L^2 v^2}{R}$. 2. For an arbitrary curved wire, replace it with the straight vector connecting its endpoints.",
            "tips_and_tricks": "Direction of induced EMF follows $\\vec{v} \\times \\vec{B}$. Positive charges accumulate at the end pointed to by $\\vec{v} \\times \\vec{B}$."
        },
        {
            "name": "Self Inductance & RL Transient Circuits",
            "category": "Inductance & Circuits",
            "primary": ["self inductance", "self-inductance", "inductance of", "solenoid", "solenoid coil", "toroid", "choke coil", "time constant", "rl circuit", "energy stored in inductor", "magnetic energy density", "growth of current", "decay of current", "inductor having inductance"],
            "formula_cues": [r"l \frac{di}{dt}", r"l\frac{di}{dt}", r"\frac{1}{2} l i^2", r"\frac{l}{r}", r"\mu_0 n^2"],
            "secondary": ["inductor", "henry", "switch", "steady state", "resistance"],
            "keywords": ["self inductance", "solenoid", "l di/dt", "time constant", "growth of current", "decay of current", "rl circuit", "energy stored"],
            "summary": "Self-inductance $L = \\frac{N\\Phi}{I}$, induced back-EMF $\\mathcal{E} = -L\\frac{dI}{dt}$. Solenoid $L = \\mu_0 n^2 A l$. RL circuit current growth: $I(t) = \\frac{V}{R}(1 - e^{-t/\\tau})$ with inductive time constant $\\tau = \\frac{L}{R}$.",
            "standard_formulas": r"\mathcal{E} = -L \frac{dI}{dt}, \quad L = \mu_0 n^2 A l, \quad U = \frac{1}{2} L I^2, \quad \tau = \frac{L}{R}, \quad I(t) = \frac{V}{R} (1 - e^{-t/\tau})",
            "common_traps": "At $t = 0^+$ (immediately after switch closing), an unenergized inductor acts as an open circuit ($R \\to \\infty$). At $t \\to \\infty$ (steady state), an ideal inductor acts as a zero-resistance short wire.",
            "tips_and_tricks": "Magnetic energy stored: $U_B = \\frac{1}{2} L I^2$; energy density in space: $u_B = \\frac{B^2}{2\\mu_0}$. Inductors resist sudden changes in current, not voltage."
        },
        {
            "name": "Mutual Inductance & Coupled Coils",
            "category": "Coupling",
            "primary": ["mutual inductance", "mutual induction", "coaxial solenoids", "two coils", "two concentric", "coupling coefficient", "coupled coils", "inner loop", "concentric circular loop", "square loop inside", "between circular loop and square"],
            "formula_cues": [r"m \frac{di}{dt}", r"m\frac{di}{dt}", r"k\sqrt{l_1", r"\mu_0 n_1 n_2"],
            "secondary": ["two loops", "secondary", "primary", "coaxial"],
            "keywords": ["mutual inductance", "coaxial solenoids", "coupling", "m di/dt", "two coils"],
            "summary": "Coupled flux in secondary coil $\\Phi_2 = M I_1$, induced EMF $\\mathcal{E}_2 = -M\\frac{dI_1}{dt}$. Coaxial solenoids $M = \\mu_0 n_1 n_2 (\\pi r_{\\text{inner}}^2) l$. Coupling coefficient $M = k\\sqrt{L_1 L_2}$ ($0 \\le k \\le 1$).",
            "standard_formulas": r"\mathcal{E}_2 = -M \frac{dI_1}{dt}, \quad M = \mu_0 n_1 n_2 (\pi r_{\text{inner}}^2) l, \quad M = k \sqrt{L_1 L_2} \quad (0 \le k \le 1)",
            "common_traps": "For concentric coaxial coils, always use the cross-sectional area of the INNER coil ($r_{\\text{inner}}$), because the magnetic field of the outer coil only penetrates the inner core.",
            "tips_and_tricks": "Reciprocity theorem holds: $M_{12} = M_{21}$ regardless of differing geometry or number of turns."
        },
        {
            "name": "Induced Electric Field & Eddy Currents",
            "category": "Field Theory",
            "primary": ["induced electric field", "non-conservative", "eddy current", "eddy currents", "cylindrical region", "circular electric field", "line integral of e", "non-electrostatic"],
            "formula_cues": [r"\oint \vec{e}", r"\frac{r}{2} \frac{db}{dt}", r"\frac{r^2}{2r}"],
            "secondary": ["electric field", "cylindrical", "laminated"],
            "keywords": ["induced electric field", "cylindrical", "non-conservative", "eddy current", "line integral"],
            "summary": "A time-varying magnetic field generates a non-conservative, circular electric field: $\\oint \\vec{E} \\cdot d\\vec{l} = -\\frac{d\\Phi_B}{dt}$. Inside cylinder ($r \\le R$): $E(r) = \\frac{r}{2}\\frac{dB}{dt}$; outside ($r > R$): $E(r) = \\frac{R^2}{2r}\\frac{dB}{dt}$.",
            "standard_formulas": r"\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt}, \quad E(r) = \frac{r}{2} \frac{dB}{dt} \; (r \le R), \quad E(r) = \frac{R^2}{2r} \frac{dB}{dt} \; (r > R)",
            "common_traps": "Induced electric fields are non-electrostatic: field lines form continuous closed loops and work done along a closed circuit is non-zero ($\\oint \\vec{E} \\cdot d\\vec{l} = \\mathcal{E} \\ne 0$)!",
            "tips_and_tricks": "Eddy currents and hysteresis losses in transformer cores are minimized by using thin laminated sheets of silicon steel insulated by varnish."
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
            "summary": "Sinusoidal AC quantities: $I_{\\text{rms}} = \\frac{I_0}{\\sqrt{2}} \\approx 0.707 I_0$, $V_{\\text{rms}} = \\frac{V_0}{\\sqrt{2}}$. Average current over full cycle is $0$; average over half cycle is $I_{\\text{avg, half}} = \\frac{2I_0}{\\pi} \\approx 0.637 I_0$.",
            "standard_formulas": r"I_{\text{rms}} = \frac{I_0}{\sqrt{2}}, \quad V_{\text{rms}} = \frac{V_0}{\sqrt{2}}, \quad I_{\text{avg, half}} = \frac{2 I_0}{\pi}",
            "common_traps": "AC voltmeters and ammeters measure RMS values, not peak values! When JEE specifies '$220\\text{ V AC}$', it always denotes $V_{\\text{rms}}$ (peak voltage is $V_0 = 220\\sqrt{2} \\approx 311\\text{ V}$).",
            "tips_and_tricks": "Instantaneous power $p(t) = v(t)i(t)$ fluctuates at double frequency ($2\\omega$) about average power $P_{\\text{avg}} = V_{\\text{rms}}I_{\\text{rms}}\\cos\\phi$."
        },
        {
            "name": "Reactance: Inductive & Capacitive",
            "category": "Impedance Elements",
            "primary": ["reactance", "inductive reactance", "capacitive reactance", "pure inductor", "pure capacitor", "capacitor in ac", "inductor in ac", "omega l", "1 / omega c", "x_l", "x_c"],
            "formula_cues": [r"x_l", r"x_c", r"\omega l", r"\frac{1}{\omega c}", r"2\pi f l", r"\frac{1}{2\pi f c}"],
            "secondary": ["capacitor", "inductor", "frequency", "microfarad", "millihenry"],
            "keywords": ["reactance", "inductive reactance", "capacitive reactance", "x_l", "x_c", r"\omega l", r"1 / \omega c", "pure inductor", "pure capacitor"],
            "summary": "Pure Inductor: Voltage leads current by $90^\\circ$ ($\\frac{\\pi}{2}$), inductive reactance $X_L = \\omega L = 2\\pi f L$. Pure Capacitor: Current leads voltage by $90^\\circ$, capacitive reactance $X_C = \\frac{1}{\\omega C} = \\frac{1}{2\\pi f C}$.",
            "standard_formulas": r"X_L = \omega L = 2\pi f L, \quad X_C = \frac{1}{\omega C} = \frac{1}{2\pi f C}",
            "common_traps": "In direct current (DC, $f = 0$), an inductor offers zero reactance ($X_L = 0$, short circuit) while a capacitor offers infinite reactance ($X_C \\to \\infty$, blocking DC completely).",
            "tips_and_tricks": "Mnemonic 'CIVIL': In a Capacitor (C), Current (I) leads Voltage (V); in an Inductor (L), Voltage (V) leads Current (I)."
        },
        {
            "name": "Series LCR Circuit & Impedance",
            "category": "Circuits",
            "primary": ["lcr", "series lcr", "l-c-r", "impedance", "phase angle", "tan phi", "voltage across", "phasor", "phasor diagram", "resistor and capacitor in series", "inductor and resistor in series", "rlc"],
            "formula_cues": [r"z = \sqrt", r"\tan\phi", r"\sqrt{r^2 +", r"\sqrt{v_r^2"],
            "secondary": ["resistor", "capacitor", "inductor", "phase", "series"],
            "keywords": ["lcr", "series lcr", "impedance", r"z = \sqrt", "phase angle", "tan phi", "phasor"],
            "summary": "Series LCR impedance $Z = \\sqrt{R^2 + (X_L - X_C)^2}$. Circuit current $I = \\frac{V}{Z}$. Phase angle $\\tan\\phi = \\frac{X_L - X_C}{R}$. Net voltage phasor $V_{\\text{total}} = \\sqrt{V_R^2 + (V_L - V_C)^2}$.",
            "standard_formulas": r"Z = \sqrt{R^2 + (X_L - X_C)^2}, \quad \tan\phi = \frac{X_L - X_C}{R}, \quad V_{\text{total}} = \sqrt{V_R^2 + (V_L - V_C)^2}",
            "common_traps": "Voltages across series AC elements do NOT add algebraically: $V_{\\text{total}} \\ne V_R + V_L + V_C$! Always use phasor vector addition: $V_{\\text{total}} = \\sqrt{V_R^2 + (V_L - V_C)^2}$.",
            "tips_and_tricks": "If $X_L > X_C$, circuit is inductive (voltage leads current by $\\phi$). If $X_C > X_L$, circuit is capacitive (current leads voltage by $\\phi$)."
        },
        {
            "name": "Resonance, Q-Factor & Bandwidth",
            "category": "Resonance",
            "primary": ["resonance", "resonant frequency", "quality factor", "q-factor", "q factor", "bandwidth", "sharpness of resonance", "maximum current", "half power frequencies", "at resonance"],
            "formula_cues": [r"\frac{1}{\sqrt{lc}}", r"\frac{1}{\sqrt{l c}}", r"\frac{\omega_0 l}{r}", r"\frac{1}{r}\sqrt{\frac{l}{c}}", r"\omega_0"],
            "secondary": ["sharpness", "current is maximum", "impedance is minimum"],
            "keywords": ["resonance", "resonant frequency", "quality factor", "q factor", "bandwidth", "sharpness", "maximum current"],
            "summary": "At resonance: $X_L = X_C$, resonant frequency $\\omega_0 = \\frac{1}{\\sqrt{LC}}$ ($f_0 = \\frac{1}{2\\pi\\sqrt{LC}}$). Minimum impedance $Z_{\\min} = R$, maximum current $I_{\\max} = \\frac{V}{R}$. Quality factor $Q = \\frac{\\omega_0 L}{R} = \\frac{1}{\\omega_0 C R} = \\frac{1}{R}\\sqrt{\\frac{L}{C}} = \\frac{\\omega_0}{\\Delta\\omega}$.",
            "standard_formulas": r"\omega_0 = \frac{1}{\sqrt{LC}}, \quad Z_{\min} = R, \quad I_{\max} = \frac{V}{R}, \quad Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 C R} = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{\omega_0}{\Delta\omega}",
            "common_traps": "At resonance, $V_L$ and $V_C$ are NOT zero! In fact, $V_L = V_C = Q \\cdot V_{\\text{supply}}$, which can be substantially higher than supply voltage (voltage magnification)!",
            "tips_and_tricks": "Resonance bandwidth $\\Delta\\omega = \\frac{R}{L}$. To sharpen resonance (higher $Q$), decrease resistance $R$ or increase the $\\frac{L}{C}$ ratio."
        },
        {
            "name": "Power in AC Circuits & Power Factor",
            "category": "Power & Efficiency",
            "primary": ["power factor", "average power", "power dissipated", "wattless current", "apparent power", "cos phi", "cos𝜙", "true power", "power in an ac circuit", "power in the circuit"],
            "formula_cues": [r"\cos\phi", r"v_{rms} i_{rms} \cos", r"\frac{r}{z}"],
            "secondary": ["watt", "power", "energy dissipation"],
            "keywords": ["power factor", "average power", "cos phi", "wattless current", "p = v_rms i_rms", "apparent power"],
            "summary": "Average power dissipated $P_{\\text{avg}} = V_{\\text{rms}} I_{\\text{rms}} \\cos\\phi$. Power factor $\\cos\\phi = \\frac{R}{Z} = \\frac{R}{\\sqrt{R^2 + (X_L - X_C)^2}}$. Wattless current component $I_{\\text{wattless}} = I_{\\text{rms}} \\sin\\phi$.",
            "standard_formulas": r"P_{\text{avg}} = V_{\text{rms}} I_{\text{rms}} \cos\phi, \quad \cos\phi = \frac{R}{Z} = \frac{R}{\sqrt{R^2 + (X_L - X_C)^2}}, \quad I_{\text{wattless}} = I_{\text{rms}} \sin\phi",
            "common_traps": "Power factor is $\\cos\\phi = \\frac{R}{Z}$, NOT $\\tan\\phi$ or $\\frac{R}{X}$! For pure $L$ or pure $C$, $\\phi = 90^\\circ \\implies \\cos\\phi = 0$, so average power dissipation is strictly zero.",
            "tips_and_tricks": "Apparent power $S = V_{\\text{rms}}I_{\\text{rms}}$ (in VA). True power $P = S \\cos\\phi$ (in W). Reactive power $Q = S \\sin\\phi$ (in VAR)."
        },
        {
            "name": "LC Oscillations & Transformers",
            "category": "Devices & Oscillations",
            "primary": ["transformer", "step up", "step down", "turns ratio", "primary coil", "secondary coil", "efficiency of transformer", "lc oscillation", "lc circuit", "energy transferred to the inductor", "energy in the capacitor is transferred"],
            "formula_cues": [r"\frac{v_s}{v_p}", r"\frac{n_s}{n_p}", r"\frac{i_p}{i_s}", r"q(t) = q_0"],
            "secondary": ["primary", "secondary", "core", "efficiency"],
            "keywords": ["transformer", "turns ratio", "step up", "step down", "lc oscillation", "efficiency", "n_s / n_p"],
            "summary": "Ideal transformer equations: $\\frac{V_s}{V_p} = \\frac{N_s}{N_p} = \\frac{I_p}{I_s}$. Efficiency $\\eta = \\frac{P_{\\text{out}}}{P_{\\text{in}}} = \\frac{V_s I_s}{V_p I_p}$. LC tank oscillations: charge $q(t) = q_0 \\cos(\\omega_0 t)$ with total energy conserved $U = \\frac{q^2}{2C} + \\frac{1}{2} L I^2$.",
            "standard_formulas": r"\frac{V_s}{V_p} = \frac{N_s}{N_p} = \frac{I_p}{I_s}, \quad \eta = \frac{P_{\text{out}}}{P_{\text{in}}} = \frac{V_s I_s}{V_p I_p}, \quad q(t) = q_0 \cos(\omega_0 t)",
            "common_traps": "Transformers operate exclusively on AC; in DC, primary flux is static ($\\frac{d\\Phi}{dt} = 0$), producing zero secondary voltage and potentially burning the primary coil!",
            "tips_and_tricks": "In step-up transformers ($N_s > N_p$), voltage increases but current decreases, keeping total power $V I$ conserved under ideal conditions."
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
            "summary": "Scalar product $\\vec{a} \\cdot \\vec{b} = |\\vec{a}||\\vec{b}|\\cos\\theta = a_x b_x + a_y b_y + a_z b_z$. Orthogonality condition: $\\vec{a} \\perp \\vec{b} \\iff \\vec{a} \\cdot \\vec{b} = 0$. Scalar projection of $\\vec{a}$ on $\\vec{b}$: $\\text{Proj}_{\\vec{b}} \\vec{a} = \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{b}|}$.",
            "standard_formulas": r"\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos\theta, \quad \vec{a} \perp \vec{b} \iff \vec{a} \cdot \vec{b} = 0, \quad \text{Proj}_{\vec{b}} \vec{a} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}",
            "common_traps": "1. Vector projection of $\\vec{a}$ along $\\vec{b}$ is $\\left(\\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{b}|^2}\\right)\\vec{b}$. 2. $|\\vec{a} + \\vec{b}|^2 = |\\vec{a}|^2 + |\\vec{b}|^2 + 2(\\vec{a} \\cdot \\vec{b})$ (do not write $2|\\vec{a}||\\vec{b}|$ unless collinear!).",
            "tips_and_tricks": "Unit vector along the angle bisector of $\\vec{a}$ and $\\vec{b}$: $\\hat{u} = \\frac{\\hat{a} + \\hat{b}}{|\\hat{a} + \\hat{b}|}$."
        },
        {
            "name": "Cross Product & Geometric Areas",
            "category": "Vector Product",
            "primary": ["cross product", "vector product", "area of triangle", "area of the triangle", "area of parallelogram", "area of the parallelogram", "adjacent sides", "diagonals of"],
            "formula_cues": [r"\times", r"|\vec{a} \times \vec{b}|", r"|\vec{u} \times \vec{v}|"],
            "secondary": ["parallelogram", "triangle", "normal to the plane"],
            "keywords": ["cross product", "vector product", "area of triangle", "area of parallelogram", "perpendicular unit vector", r"\vec{a} \times \vec{b}"],
            "summary": "Vector cross product $\\vec{a} \\times \\vec{b} = |\\vec{a}||\\vec{b}|\\sin\\theta \\,\\hat{n}$. Collinearity condition: $\\vec{a} \\parallel \\vec{b} \\iff \\vec{a} \\times \\vec{b} = \\vec{0}$. Area of triangle with sides $\\vec{a}, \\vec{b}$ is $\\frac{1}{2}|\\vec{a} \\times \\vec{b}|$; parallelogram area is $|\\vec{a} \\times \\vec{b}|$; parallelogram with diagonals $\\vec{d}_1, \\vec{d}_2$ is $\\frac{1}{2}|\\vec{d}_1 \\times \\vec{d}_2|$.",
            "standard_formulas": r"\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix}, \quad \text{Area}_{\triangle} = \frac{1}{2} |\vec{a} \times \vec{b}|, \quad \hat{n} = \pm \frac{\vec{a} \times \vec{b}}{|\vec{a} \times \vec{b}|}",
            "common_traps": "1. Cross product is anti-commutative: $\\vec{a} \\times \\vec{b} = -(\\vec{b} \\times \\vec{a})$. 2. Lagrange's identity: $|\\vec{a} \\times \\vec{b}|^2 = |\\vec{a}|^2 |\\vec{b}|^2 - (\\vec{a} \\cdot \\vec{b})^2$.",
            "tips_and_tricks": "Area of a parallelogram given diagonal vectors $\\vec{d}_1, \\vec{d}_2$ is $\\frac{1}{2}|\\vec{d}_1 \\times \\vec{d}_2|$, NOT $|\\vec{d}_1 \\times \\vec{d}_2|$!"
        },
        {
            "name": "Scalar Triple Product (Box Product) & Coplanarity",
            "category": "Volume & Coplanarity",
            "primary": ["scalar triple product", "box product", "coplanar", "co-planar", "coplanarity", "volume of parallelepiped", "volume of tetrahedron", "parallelepiped", "tetrahedron"],
            "formula_cues": [r"[\vec{a}", r"[\vec{b}", r"[\vec{u}", r"\cdot (\vec{b} \times", r"\cdot (\vec{a} \times", r"\cdot (\vec{c} \times"],
            "secondary": ["same plane", "lie in plane"],
            "keywords": ["scalar triple product", "box product", "coplanar", "[a b c]", "volume of parallelepiped", "tetrahedron"],
            "summary": "Scalar triple product $[\\vec{a}\\, \\vec{b}\\, \\vec{c}] = \\vec{a} \\cdot (\\vec{b} \\times \\vec{c}) = \\det([a_{ij}])$. Three vectors are coplanar if and only if $[\\vec{a}\\, \\vec{b}\\, \\vec{c}] = 0$. Volume of parallelepiped $V = |[\\vec{a}\\, \\vec{b}\\, \\vec{c}]|$; tetrahedron volume $V_{\\text{tet}} = \\frac{1}{6}|[\\vec{a}\\, \\vec{b}\\, \\vec{c}]|$.",
            "standard_formulas": r"[\vec{a}\; \vec{b}\; \vec{c}] = \vec{a} \cdot (\vec{b} \times \vec{c}) = \begin{vmatrix} a_x & a_y & a_z \\ b_x & b_y & b_z \\ c_x & c_y & c_z \end{vmatrix}, \quad [\vec{a}\; \vec{b}\; \vec{c}] = 0 \iff \text{coplanar}",
            "common_traps": "1. Cyclic order preserves sign: $[\\vec{a}\\, \\vec{b}\\, \\vec{c}] = [\\vec{b}\\, \\vec{c}\\, \\vec{a}] = [\\vec{c}\\, \\vec{a}\\, \\vec{b}]$. Non-cyclic swap negates: $[\\vec{a}\\, \\vec{c}\\, \\vec{b}] = -[\\vec{a}\\, \\vec{b}\\, \\vec{c}]$. 2. If any two vectors are identical or collinear, the box product is strictly $0$.",
            "tips_and_tricks": "Four position points $A, B, C, D$ are coplanar if and only if $[\\vec{AB}\\, \\vec{AC}\\, \\vec{AD}] = 0$."
        },
        {
            "name": "Vector Triple Product & Lagrange Identity",
            "category": "Triple Products",
            "primary": ["vector triple product", "lagrange identity", "lagrange's identity", "triple vector product"],
            "formula_cues": [r"\times (\vec{b} \times", r"\times (\vec{c} \times", r"\times (\vec{a} \times", r"(\vec{a} \times \vec{b}) \times", r"(\vec{b} \times \vec{c}) \times"],
            "secondary": ["bac - cab", "bac cab"],
            "keywords": ["vector triple product", "a x (b x c)", "bac - cab", "lagrange"],
            "summary": "Vector triple product expands via the BAC-CAB identity: $\\vec{a} \\times (\\vec{b} \\times \\vec{c}) = (\\vec{a} \\cdot \\vec{c})\\vec{b} - (\\vec{a} \\cdot \\vec{b})\\vec{c}$. It lies in the plane of $\\vec{b}$ and $\\vec{c}$, perpendicular to $\\vec{a}$.",
            "standard_formulas": r"\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}, \quad (\vec{a} \times \vec{b}) \times \vec{c} = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{b} \cdot \vec{c})\vec{a}",
            "common_traps": "Vector triple product is non-associative: $\\vec{a} \\times (\\vec{b} \\times \\vec{c}) \\ne (\\vec{a} \\times \\vec{b}) \\times \\vec{c}$. Notice that $(\\vec{a} \\times \\vec{b}) \\times \\vec{c} = (\\vec{a} \\cdot \\vec{c})\\vec{b} - (\\vec{b} \\cdot \\vec{c})\\vec{a}$.",
            "tips_and_tricks": "Mnemonic: 'BAC minus CAB' — dot product of outer vectors multiplied by inner vector, minus dot product of first two multiplied by the third."
        },
        {
            "name": "Linear Combination & Vector Equations",
            "category": "Vector Equations",
            "primary": ["linear combination", "vector equation", "find vector", "unknown vector", "vector c be such that", "vector r be such that", "vector v be such that", "vectors c such that", "vector r such that", "linearly dependent", "linearly independent"],
            "formula_cues": [r"\vec{r} \times", r"\vec{r} \cdot", r"\vec{c} = \lambda", r"\lambda\vec{a}+\mu\vec{b}", r"\lambda\overset{⃗}{a}", r"\vec{c} = \alpha", r"2(\vec{a} \times \vec{b})"],
            "secondary": ["plane of vectors", "scalars lambda", "linearly"],
            "keywords": ["linear combination", "coplanar vectors", "vector equation", "find vector r", r"r \times", r"r \cdot"],
            "summary": "Solving vector equations like $\\vec{r} \\times \\vec{a} = \\vec{b}$ and $\\vec{r} \\cdot \\vec{c} = d$. Express $\\vec{r}$ as a linear basis expansion $\\vec{r} = x\\vec{a} + y\\vec{b} + z(\\vec{a} \\times \\vec{b})$ or take vector cross/dot products with known vectors on both sides.",
            "standard_formulas": r"\vec{r} = x \vec{a} + y \vec{b} + z (\vec{a} \times \vec{b}), \quad \text{or take } \vec{a} \times (\vec{r} \times \vec{b}) \text{ to decouple}",
            "common_traps": "When $\\vec{r} \\times \\vec{a} = \\vec{b}$, note that $\\vec{b} \\perp \\vec{a}$ (so $\\vec{a} \\cdot \\vec{b} = 0$). The general solution is $\\vec{r} = \\lambda \\vec{a} + \\frac{\\vec{a} \\times \\vec{b}}{|\\vec{a}|^2}$.",
            "tips_and_tricks": "If $\\vec{r} \\times \\vec{a} = \\vec{b}$, taking the cross product with $\\vec{a}$ gives $\\vec{a} \\times (\\vec{r} \\times \\vec{a}) = \\vec{a} \\times \\vec{b}$, decoupling $\\vec{r}$ directly."
        },
        {
            "name": "Section Formula, Collinearity & Centroids",
            "category": "Geometry & Position Vectors",
            "primary": ["section formula", "collinear", "collinearity", "centroid", "internal division", "external division", "divides the line segment", "points are collinear", "points a, b, c are collinear"],
            "formula_cues": [r"\frac{m\vec{b}", r"\frac{\vec{a}+\vec{b}+\vec{c}}{3}", r"\vec{OP}=", r"\vec{OR}="],
            "secondary": ["midpoint", "equidistant", "origin"],
            "keywords": ["section formula", "collinear", "centroid", "internal division", "external division", "position vector"],
            "summary": "Section formula for point dividing line segment in ratio $m:n$: $\\vec{r} = \\frac{m\\vec{b} + n\\vec{a}}{m + n}$ (internal) and $\\vec{r} = \\frac{m\\vec{b} - n\\vec{a}}{m - n}$ (external). Centroid of triangle $\\vec{G} = \\frac{\\vec{a} + \\vec{b} + \\vec{c}}{3}$. Three points are collinear if $\\vec{AB} = \\lambda \\vec{BC}$.",
            "standard_formulas": r"\vec{r} = \frac{m\vec{b} + n\vec{a}}{m + n}, \quad \vec{G} = \frac{\vec{a} + \vec{b} + \vec{c}}{3}, \quad \vec{a} = \lambda \vec{b} \iff \text{collinear}",
            "common_traps": "Collinear vectors can be antiparallel (negative scalar $\\lambda$). External division formula carries an explicit minus sign in numerator and denominator: $\\frac{m\\vec{b} - n\\vec{a}}{m - n}$.",
            "tips_and_tricks": "In a tetrahedron with vertices $\\vec{a}, \\vec{b}, \\vec{c}, \\vec{d}$, the centroid is $\\vec{G} = \\frac{\\vec{a} + \\vec{b} + \\vec{c} + \\vec{d}}{4}$."
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

    # Check curated taxonomy (strip kcet- prefix if present to share rich taxonomy)
    norm_slug = chapter_slug.replace("kcet-", "")
    taxonomy = CURATED_TAXONOMY.get(norm_slug, CURATED_TAXONOMY.get(chapter_slug, []))
    
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

    # Initialize taxonomy concepts (support kcet- prefix)
    norm_slug = chapter_slug.replace("kcet-", "")
    taxonomy = CURATED_TAXONOMY.get(norm_slug, CURATED_TAXONOMY.get(chapter_slug, []))
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
