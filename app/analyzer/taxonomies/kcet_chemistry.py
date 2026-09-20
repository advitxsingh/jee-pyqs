"""
Dedicated KCET Chemistry Taxonomy.
Tailored specifically to Karnataka CET curriculum, Karnataka PUC I & II syllabus,
and actual past year KCET questions.
"""

from typing import Dict, List, Any

KCET_CHEMISTRY_TAXONOMY: Dict[str, List[Dict[str, Any]]] = {
    "kcet-some-basic-concepts-of-chemistry": [
        {
            "name": "Mole Concept, Molar Mass & Stoichiometry",
            "category": "Quantitative Stoichiometry",
            "primary": ["mole concept", "number of moles", "avogadro", "molar mass", "limiting reagent", "mass of carbon", "stp", "moles of nacl", "percentage composition", "empirical formula"],
            "formula_cues": [r"6.022 \times 10^{23}", r"n = \frac{w}{m}", r"22.4\text{ l}", r"22.4\text{ dm}^3"],
            "secondary": ["grams", "atoms", "molecules", "reaction"],
            "summary": "Mole concept calculations: $n = \\frac{w}{M} = \\frac{N}{N_A} = \\frac{V(\\text{at STP})}{22.4\\text{ L}}$. Stoichiometry and identification of limiting reagents that determine product yield.",
            "standard_formulas": r"n = \frac{w}{M} = \frac{N}{6.022 \times 10^{23}} = \frac{V_{\text{STP}}}{22.4\text{ L}}, \quad \text{Empirical Formula} = (\text{Simplest Ratio})_n",
            "common_traps": "At STP ($1\\text{ bar}, 273.15\\text{ K}$), molar volume of ideal gas is $22.7\\text{ L}$; at standard old STP ($1\\text{ atm}, 0^\\circ\\text{C}$), it is $22.4\\text{ L}$.",
            "tips_and_tricks": "Number of atoms in a sample = $\\text{Moles} \\times N_A \\times \\text{Atomicity}$."
        },
        {
            "name": "Concentration Terms: Molarity, Molality & Mole Fraction",
            "category": "Solutions & Concentrations",
            "primary": ["molarity", "molality", "mole fraction", "normality", "dilution formula", "ppm", "temperature independent"],
            "formula_cues": [r"m = \frac{w_b \times 1000}{m_b \times v(\text{ml})}", r"m = \frac{w_b \times 1000}{m_b \times w_a(\text{g})}", r"m_1 v_1 = m_2 v_2", r"x_a + x_b = 1"],
            "secondary": ["solution", "solvent", "solute", "concentration"],
            "summary": "Molarity $M = \\frac{\\text{moles of solute}}{\\text{Volume of solution (L)}}$ (temperature dependent). Molality $m = \\frac{\\text{moles of solute}}{\\text{Mass of solvent (kg)}}$ (temperature independent). Mole fraction $\\chi_B = \\frac{n_B}{n_A + n_B}$.",
            "standard_formulas": r"M = \frac{w_B \times 1000}{M_B \times V(\text{mL})}, \quad m = \frac{w_B \times 1000}{M_B \times w_A(\text{g})}, \quad M_1 V_1 = M_2 V_2",
            "common_traps": "Molality and mole fraction are independent of temperature because they depend strictly on masses, not solution volume.",
            "tips_and_tricks": "Relation between Molarity ($M$) and Molality ($m$): $m = \\frac{1000 M}{1000 d - M M_B}$ where $d$ is density in $\\text{g/mL}$."
        }
    ],

    "kcet-atomic-structure": [
        {
            "name": "Bohr's Atomic Theory & Hydrogen Spectral Lines",
            "category": "Atomic Models",
            "primary": ["bohr's theory", "radius of bohr", "energy of electron", "rydberg equation", "lyman series", "balmer series", "paschen", "wave number", "quantum numbers", "principal quantum number"],
            "formula_cues": [r"r_n = 0.529 \frac{n^2}{z}\text{ \AA}", r"e_n = -13.6 \frac{z^2}{n^2}\text{ eV}", r"\bar{\nu} = r_h \left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)"],
            "secondary": ["electron", "orbit", "spectral line", "wavelength"],
            "summary": "Bohr model: $r_n = 0.529 \\frac{n^2}{Z}\\text{ \\AA}$, $E_n = -13.6\\frac{Z^2}{n^2}\\text{ eV}$. Wave number $\\bar{\\nu} = \\frac{1}{\\lambda} = R_H Z^2 \\left(\\frac{1}{n_1^2} - \\frac{1}{n_2^2}\\right)$. Lyman series is in UV region, Balmer series is in Visible region.",
            "standard_formulas": r"E_n = -13.6 \frac{Z^2}{n^2}\text{ eV}, \quad \bar{\nu} = 109677 \left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)\text{ cm}^{-1}",
            "common_traps": "Bohr theory is applicable ONLY to single-electron species ($\text{H}, \text{He}^+, \text{Li}^{2+}, \text{Be}^{3+}$); it fails for multi-electron atoms.",
            "tips_and_tricks": "Balmer series: The only hydrogen spectral series visible to the human eye ($n_1 = 2$)."
        },
        {
            "name": "de Broglie, Heisenberg & Quantum Rules (Aufbau, Hund, Pauli)",
            "category": "Quantum Mechanics",
            "primary": ["heisenberg uncertainty", "de broglie", "quantum numbers", "aufbau principle", "hund's rule", "pauli exclusion", "unpaired electrons", "magnetic moment", "orbital angular momentum"],
            "formula_cues": [r"\\Delta x \cdot \\Delta p \ge \frac{h}{4\pi}", r"\lambda = \frac{h}{mv}", r"\mu = \sqrt{n(n+2)}\text{ bm}", r"l = 0, 1, 2, 3"],
            "secondary": ["spin", "azimuthal", "magnetic", "electrons"],
            "summary": "Heisenberg's uncertainty principle: $\\Delta x \\cdot \\Delta p \\ge \\frac{h}{4\\pi}$. Quantum numbers: $n$ (size/energy), $l$ (shape: $s=0, p=1, d=2, f=3$), $m_l$ (orientation, $-l$ to $+l$), $m_s$ (spin $\\pm 1/2$). Aufbau rule fills orbitals in order of increasing $(n+l)$. Pauli exclusion principle: no two electrons can have all 4 quantum numbers identical. Hund's rule: pairing occurs only after every degenerate orbital has one electron with parallel spin.",
            "standard_formulas": r"\\Delta x \cdot \\Delta p \ge \frac{h}{4\pi}, \quad \text{Spin-only } \mu = \sqrt{n(n+2)}\text{ BM}, \quad \text{Max electrons in subshell} = 2(2l+1)",
            "common_traps": "When $(n+l)$ values are equal, the orbital with LOWER $n$ has lower energy and fills first (e.g. $3d$ with $n+l=5$ vs $4p$ with $n+l=5$: $3d$ fills before $4p$).",
            "tips_and_tricks": "Chromium ($Z=24: [\\text{Ar}] 3d^5 4s^1$) and Copper ($Z=29: [\\text{Ar}] 3d^{10} 4s^1$) have anomalous configurations due to extra stability of half-filled and completely-filled $d$-subshells."
        }
    ],

    "kcet-periodic-table-and-periodicity": [
        {
            "name": "Periodic Trends: Radii, Ionization Enthalpy & Electronegativity",
            "category": "Periodic Trends",
            "primary": ["ionization enthalpy", "first ionization", "second ionization", "atomic radius", "ionic radius", "electronegativity", "electron gain enthalpy", "isoelectronic", "effective nuclear charge", "lanthanoid contraction"],
            "formula_cues": [r"\text{ie}_1 < \text{ie}_2 < \text{ie}_3", r"\text{o}^{2-} > \text{f}^- > \text{na}^+ > \text{mg}^{2+}", r"z_{\text{eff}}"],
            "secondary": ["period", "group", "increase", "decrease"],
            "summary": "Periodic trends across a period (left to right): Atomic radius decreases, ionization enthalpy increases, electronegativity increases, electron gain enthalpy generally becomes more negative. Down a group: Atomic radius increases, ionization enthalpy decreases. Isoelectronic ions: size decreases with increasing positive nuclear charge ($Z$). Anomalies: $\\text{IE}_1(\\text{Be}) > \\text{IE}_1(\\text{B})$ (fully filled $2s^2$), $\\text{IE}_1(\\text{N}) > \\text{IE}_1(\\text{O})$ (half-filled $2p^3$).",
            "standard_formulas": r"\text{Isoelectronic Radii: } \text{N}^{3-} > \text{O}^{2-} > \text{F}^- > \text{Na}^+ > \text{Mg}^{2+} > \text{Al}^{3+}",
            "common_traps": "Electron gain enthalpy of Chlorine is MORE negative than Fluorine ($-349\\text{ kJ/mol}$ vs $-328\\text{ kJ/mol}$) due to high electron-electron repulsion in small $2p$ subshell of F!",
            "tips_and_tricks": "Second ionization enthalpy of alkali metals is extraordinarily high because removing a second electron breaks a stable noble gas core."
        }
    ],

    "kcet-chemical-bonding-and-molecular-structure": [
        {
            "name": "VSEPR Theory, Hybridization & Molecular Geometry",
            "category": "Molecular Geometry",
            "primary": ["vsepr", "hybridization", "lone pair", "bond pair", "shape of molecule", "geometry", "sp3d", "sp3d2", "linear", "trigonal bipyramidal", "t-shaped", "see-saw", "square planar"],
            "formula_cues": [r"sp^3", r"sp^3d", r"sp^3d^2", r"\text{sf}_4", r"\text{clf}_3", r"\text{xef}_4", r"\text{xef}_2", r"\text{pcl}_5"],
            "secondary": ["bond angle", "tetrahedral", "octahedral", "repulsion"],
            "summary": "VSEPR theory: Repulsion order: $\\text{lp-lp} > \\text{lp-bp} > \\text{bp-bp}$. Hybridization steric number $H = \\frac{1}{2}[V + M - C + A]$. $\\text{SF}_4$: $sp^3d$, 1 lp, see-saw. $\\text{ClF}_3$: $sp^3d$, 2 lp, T-shaped. $\\text{XeF}_2$: $sp^3d$, 3 lp, linear. $\\text{XeF}_4$: $sp^3d^2$, 2 lp, square planar. $\\text{PCl}_5$: $sp^3d$, trigonal bipyramidal (axial bonds are longer and weaker than equatorial bonds).",
            "standard_formulas": r"\text{Steric Number } = \text{Bond Pairs} + \text{Lone Pairs}, \quad H = \frac{1}{2}(V + M - C + A)",
            "common_traps": "In $\\text{PCl}_5$, the 2 axial $\\text{P-Cl}$ bonds are longer and weaker than the 3 equatorial bonds due to greater repulsion from equatorial electron pairs.",
            "tips_and_tricks": "In $sp^3d$ hybridization, lone pairs ALWAYS occupy EQUATORIAL positions to minimize $90^\\circ$ repulsions (e.g. $\\text{ClF}_3$ has both lone pairs in equatorial positions $\\implies$ T-shape)."
        },
        {
            "name": "Molecular Orbital Theory & Dipole Moments",
            "category": "Bonding Theories",
            "primary": ["molecular orbital theory", "mot", "bond order", "paramagnetic", "diamagnetic", "o2 molecule", "n2 molecule", "dipole moment", "non-polar", "hydrogen bonding"],
            "formula_cues": [r"\text{bond order} = \frac{n_b - n_a}{2}", r"\sigma 2p_z", r"\pi 2p_x = \pi 2p_y", r"\mu = q \times d", r"\mu = 0"],
            "secondary": ["electrons", "bonding", "antibonding", "stability"],
            "summary": "MOT: Bond Order $= \\frac{N_b - N_a}{2}$. For $\\le 14$ electrons ($\text{B}_2, \text{C}_2, \text{N}_2$): $\\pi 2p_x = \\pi 2p_y$ fills before $\\sigma 2p_z$. For $> 14$ electrons ($\text{O}_2, \text{F}_2$): $\\sigma 2p_z$ fills before $\\pi 2p$. $\\text{O}_2$ has 2 unpaired electrons in degenerate antibonding $\\pi^* 2p$ orbitals $\\implies$ paramagnetic with $\\text{Bond Order} = 2$. Dipole moment $\\mu = q \\times d$; symmetrical molecules ($\text{CO}_2, \\text{BF}_3, \\text{CCl}_4$) have $\\mu = 0$.",
            "standard_formulas": r"\text{Bond Order} = \frac{N_b - N_a}{2}, \quad \text{Bond Order} \propto \text{Bond Energy} \propto \frac{1}{\text{Bond Length}}",
            "common_traps": "Liquid $\\text{O}_2$ is attracted into a magnetic field because it is PARAMAGNETIC (a fact that Valence Bond Theory completely failed to explain, but MOT successfully explains).",
            "tips_and_tricks": "If Bond Order $= 0$, the diatomic molecule does not exist (e.g. $\\text{He}_2, \\text{Be}_2$)."
        }
    ],

    "kcet-states-of-matter": [
        {
            "name": "Ideal Gas Laws, Dalton's Law & Graham's Diffusion",
            "category": "Gas Laws",
            "primary": ["boyle's law", "charles's law", "ideal gas equation", "dalton's law of partial pressures", "graham's law of diffusion", "rate of diffusion", "partial pressure", "molar volume"],
            "formula_cues": [r"p v = n r t", r"\frac{r_1}{r_2} = \sqrt{\frac{m_2}{m_1}}", r"p_a = x_a p_{\text{total}}", r"\frac{p_1 v_1}{t_1} = \frac{p_2 v_2}{t_2}"],
            "secondary": ["gas", "pressure", "temperature", "volume"],
            "summary": "Ideal gas equation: $PV = nRT = \\frac{w}{M}RT \\implies P M = d R T$. Dalton's law: $P_{\\text{total}} = \\sum P_i$, where $P_A = \\chi_A P_{\\text{total}}$. Graham's law: rate of diffusion $r \\propto \\frac{1}{\\sqrt{M}} \\propto \\frac{1}{\\sqrt{d}}$.",
            "standard_formulas": r"PV = nRT, \quad P = \frac{dRT}{M}, \quad \frac{r_1}{r_2} = \sqrt{\frac{M_2}{M_1}} = \frac{V_1 / t_1}{V_2 / t_2}",
            "common_traps": "Graham's law uses the inverse square root of molar mass: lighter gas diffuses faster ($\text{H}_2$ diffuses 4 times faster than $\text{O}_2$ because $\\sqrt{32/2} = 4$).",
            "tips_and_tricks": "Gas density formula $d = \\frac{PM}{RT}$. At higher temperature and lower pressure, gas density is minimum."
        },
        {
            "name": "Real Gases & van der Waals Equation",
            "category": "Real Gases",
            "primary": ["van der waals", "compressibility factor", "real gas", "pressure correction", "volume correction", "ideal behavior", "liquefaction", "critical temperature"],
            "formula_cues": [r"\left(p + \frac{an^2}{v^2}\right)(v - nb) = nrt", r"z = \frac{pv}{nrt}", r"t_c = \frac{8a}{27rb}", r"z < 1", r"z > 1"],
            "secondary": ["attraction", "volume", "deviation", "constant"],
            "summary": "Real gas equation: $\\left(P + \\frac{a n^2}{V^2}\\right)(V - nb) = nRT$. Constant $a$ measures magnitude of intermolecular attractive forces; constant $b$ measures effective molecular volume (co-volume $b = 4 V_m$). Compressibility factor $Z = \\frac{PV}{nRT}$: for ideal gas $Z=1$; at low pressure $Z < 1$ (attraction dominates); at high pressure $Z > 1$ (repulsion dominates). Real gases approach ideal behavior at HIGH temperature and LOW pressure.",
            "standard_formulas": r"\left(P + \frac{a}{V_m^2}\right)(V_m - b) = RT, \quad Z = \frac{V_{\text{real}}}{V_{\text{ideal}}}, \quad T_c = \frac{8a}{27Rb}",
            "common_traps": "For Hydrogen and Helium, attractive forces are negligible ($a \\approx 0$), so $Z = 1 + \\frac{Pb}{RT} > 1$ at all ordinary temperatures!",
            "tips_and_tricks": "A gas with higher critical temperature $T_c$ and higher $a$ value is more easily liquefied (e.g. $\\text{NH}_3, \\text{SO}_2$ liquefy more easily than $\\text{N}_2, \\text{H}_2$)."
        }
    ],

    "kcet-thermodynamics": [
        {
            "name": "First Law, Enthalpy & Hess's Law",
            "category": "Thermochemistry",
            "primary": ["first law", "internal energy", "enthalpy change", "delta h", "delta u", "heat of formation", "heat of combustion", "hess's law", "bond enthalpy", "bomb calorimeter"],
            "formula_cues": [r"\\Delta h = \\Delta u + \\Delta n_g r t", r"\\Delta u = q + w", r"w = -p_{\text{ext}}\\Delta v", r"\\Delta h^\\circ_r = \sum \\Delta h_f(\text{prod}) - \sum \\Delta h_f(\text{react})"],
            "secondary": ["work", "system", "joules", "heat"],
            "summary": "First Law $\\Delta U = q + w$. Expansion work against constant pressure $w = -P_{\\text{ext}}\\Delta V$. Relation between $\\Delta H$ and $\\Delta U$: $\\Delta H = \\Delta U + \\Delta n_g R T$. Hess's Law of constant heat summation: overall enthalpy change is independent of intermediate steps. Standard enthalpy of formation of elements in their reference state is defined as zero.",
            "standard_formulas": r"\\Delta H = \\Delta U + \\Delta n_g RT, \quad \\Delta n_g = \sum n_{g,\text{prod}} - \sum n_{g,\text{react}}, \quad \\Delta H_r = \sum \text{BE}(\text{react}) - \sum \text{BE}(\text{prod})",
            "common_traps": "When calculating $\\Delta n_g$, count ONLY gaseous species; completely ignore solids and pure liquids!",
            "tips_and_tricks": "For reactions with $\\Delta n_g = 0$ (e.g. $\\text{H}_2(g) + \\text{I}_2(g) \\rightleftharpoons 2\\text{HI}(g)$), $\\Delta H$ is exactly equal to $\\Delta U$."
        },
        {
            "name": "Entropy, Gibbs Free Energy & Spontaneity",
            "category": "Thermodynamic Spontaneity",
            "primary": ["entropy", "gibbs free energy", "spontaneity", "spontaneous", "equilibrium constant", "delta g", "delta s", "second law", "third law"],
            "formula_cues": [r"\\Delta g = \\Delta h - t\\Delta s", r"\\Delta g^\\circ = -2.303 rt \log k", r"\\Delta s = \frac{q_{\text{rev}}}{t}", r"\\Delta g < 0"],
            "secondary": ["equilibrium", "temperature", "entropy of universe"],
            "summary": "Gibbs-Helmholtz equation: $\\Delta G = \\Delta H - T\\Delta S$. Criteria for spontaneity at constant $T$ and $P$: $\\Delta G < 0$ (spontaneous), $\\Delta G = 0$ (at equilibrium), $\\Delta G > 0$ (non-spontaneous). Spontaneity temperature threshold: $T = \\frac{\\Delta H}{\\Delta S}$. Relation to equilibrium: $\\Delta G^\\circ = -RT\\ln K = -2.303 RT\\log K$.",
            "standard_formulas": r"\\Delta G = \\Delta H - T\\Delta S, \quad \\Delta G^{\\circ} = -2.303 RT \log_{10} K, \quad \\Delta S_{\text{universe}} = \\Delta S_{\text{sys}} + \\Delta S_{\text{surr}} > 0",
            "common_traps": "A reaction with $\\Delta H > 0$ (endothermic) can still be spontaneous if $\\Delta S > 0$ at sufficiently HIGH temperatures ($T > \\Delta H/\\Delta S$).",
            "tips_and_tricks": "If $\\Delta H < 0$ and $\\Delta S > 0$, $\\Delta G$ is negative at ALL temperatures $\\implies$ always spontaneous."
        }
    ],

    "kcet-chemical-equilibrium": [
        {
            "name": "Equilibrium Constants (Kc, Kp) & Le Chatelier's Principle",
            "category": "Chemical Equilibrium",
            "primary": ["equilibrium constant", "kp and kc", "le chatelier", "haber process", "addition of inert gas", "effect of pressure", "effect of temperature", "endothermic", "exothermic", "shift of equilibrium"],
            "formula_cues": [r"k_p = k_c(rt)^{\\Delta n}", r"q_c < k_c", r"\log\frac{k_2}{k_1} = \frac{\\Delta h}{2.303r}\left(\frac{1}{t_1}-\frac{1}{t_2}\right)"],
            "secondary": ["reactants", "products", "yield", "gaseous"],
            "summary": "Equilibrium constant expression $K_p = K_c(RT)^{\\Delta n_g}$. If reaction is multiplied by $n$, new constant is $K' = K^n$; if reversed, $K' = 1/K$. Le Chatelier's principle: Increasing pressure shifts equilibrium toward fewer gas moles; increasing temperature favours endothermic direction. Addition of inert gas at constant volume has NO effect on equilibrium.",
            "standard_formulas": r"K_p = K_c (RT)^{\\Delta n_g}, \quad \text{Reversed Reaction: } K' = \frac{1}{K}, \quad n \times \text{Reaction: } K' = K^n",
            "common_traps": "A catalyst increases the speed of both forward and reverse reactions equally; it does NOT alter the equilibrium constant or the yield of products!",
            "tips_and_tricks": "Addition of an inert gas at constant PRESSURE shifts equilibrium to the side with MORE moles of gas ($\\Delta n_g > 0$ shifts forward)."
        }
    ],

    "kcet-ionic-equilibrum": [
        {
            "name": "pH Scale, Ostwald's Law & Buffer Solutions",
            "category": "Ionic Equilibria",
            "primary": ["ph of solution", "poh", "ostwald's dilution law", "buffer solution", "henderson", "acidic buffer", "basic buffer", "ch3coona", "nh4cl", "conjugate acid-base pair"],
            "formula_cues": [r"\text{ph} = -\log[h^+]", r"\text{ph} + \text{poh} = 14", r"\alpha = \sqrt{\frac{k_a}{c}}", r"\text{ph} = pk_a + \log\frac{[\text{salt}]}{[\text{acid}]}"],
            "secondary": ["salt", "acid", "dissociation", "base"],
            "summary": "pH calculations: $\\text{pH} = -\\log[\\text{H}^+]$, $\\text{pH} + \\text{pOH} = 14$ at $25^\\circ\\text{C}$. Ostwald's dilution law for weak acid: $\\alpha = \\sqrt{\\frac{K_a}{c}}, [\\text{H}^+] = \\sqrt{K_a c}$. Henderson-Hasselbalch equation for acidic buffer: $\\text{pH} = pK_a + \\log\\frac{[\\text{Salt}]}{[\\text{Acid}]}$. Basic buffer: $\\text{pOH} = pK_b + \\log\\frac{[\\text{Salt}]}{[\\text{Base}]}$.",
            "standard_formulas": r"\text{pH} = pK_a + \log_{10}\frac{[\text{Conjugate Base}]}{[\text{Acid}]}, \quad [\text{H}^+] = \sqrt{K_a \cdot c}, \quad K_w = 10^{-14}",
            "common_traps": "A $10^{-8}\\text{ M HCl}$ solution does NOT have $\\text{pH} = 8$ (it is acidic!). Accounting for water dissociation $[\\text{H}^+] = 10^{-8} + 10^{-7} = 1.1 \\times 10^{-7} \\implies \\text{pH} \\approx 6.96$.",
            "tips_and_tricks": "When $[\\text{Salt}] = [\\text{Acid}]$ in a buffer, maximum buffer capacity is achieved and $\\text{pH} = pK_a$."
        },
        {
            "name": "Solubility Product (Ksp) & Salt Hydrolysis",
            "category": "Precipitation & Hydrolysis",
            "primary": ["solubility product", "k_sp", "precipitation occurs", "common ion effect", "ionic product", "hydrolysis of salt", "weak acid strong base", "sparingly soluble"],
            "formula_cues": [r"k_{sp} = s^2", r"k_{sp} = 4s^3", r"k_{sp} = 27s^4", r"q_{\text{ip}} > k_{sp}", r"\text{ph} = 7 + \frac{1}{2}(pk_a - pk_b)"],
            "secondary": ["precipitate", "saturated", "ions"],
            "summary": "Solubility product $K_{sp}$: For $AB$ salt $K_{sp} = S^2$; for $AB_2$ salt $K_{sp} = 4S^3$; for $A_2B_3$ salt $K_{sp} = 108S^5$. Precipitation occurs when ionic product $Q_{\\text{ip}} > K_{sp}$. Salt hydrolysis: Salt of weak acid + strong base ($\text{CH}_3\\text{COONa}$) gives alkaline solution with $\\text{pH} = 7 + \\frac{1}{2}(pK_a + \\log C) > 7$.",
            "standard_formulas": r"\text{For } A_x B_y: K_{sp} = x^x y^y S^{x+y}, \quad Q > K_{sp} \implies \text{Precipitation}, \quad \text{Weak-Weak: } \text{pH} = 7 + \frac{1}{2}(pK_a - pK_b)",
            "common_traps": "Solubility of a sparingly soluble salt (like $\\text{AgCl}$) decreases significantly in the presence of a common ion (like $\\text{NaCl}$) due to Le Chatelier's shift.",
            "tips_and_tricks": "For $AB_2$ salt (e.g. $\\text{CaCl}_2, \\text{Mg(OH)}_2$): $S = \\sqrt[3]{\\frac{K_{sp}}{4}}$."
        }
    ],

    "kcet-redox-reactions": [
        {
            "name": "Oxidation Number Rules & Redox Titrations",
            "category": "Redox Principles",
            "primary": ["oxidation number", "oxidation state", "redox reaction", "oxidizing agent", "reducing agent", "disproportionation", "kmno4", "k2cr2o7", "equivalent weight in redox"],
            "formula_cues": [r"\text{kmno}_4 \xrightarrow{\text{h}^+} \text{mn}^{2+} \ (n=5)", r"\text{cr}_2\text{o}_7^{2-} \to 2\text{cr}^{3+} \ (n=6)", r"\text{eq wt} = \frac{\text{molar mass}}{n\text{-factor}}"],
            "secondary": ["change in oxidation", "electrons transferred", "titration"],
            "summary": "Rules for oxidation states: Peroxides have $\\text{O} = -1$, superoxides $\\text{O} = -1/2$, in $\\text{OF}_2$ oxygen is $+2$. Disproportionation is a reaction where the same element is simultaneously oxidized and reduced (e.g. $\\text{Cl}_2 + \\text{NaOH}$). Equivalent weight $= \\frac{\\text{Molar Mass}}{n\\text{-factor}}$. In acidic medium: $\\text{KMnO}_4 \\to \\text{Mn}^{2+}$ ($n=5$); $\\text{K}_2\\text{Cr}_2\\text{O}_7 \\to 2\\text{Cr}^{3+}$ ($n=6$).",
            "standard_formulas": r"\text{Eq. Wt.} = \frac{M}{n}, \quad n\text{-factor of KMnO}_4: \text{Acidic} = 5, \text{Neutral} = 3, \text{Strongly Basic} = 1",
            "common_traps": "In Caro's acid ($\\text{H}_2\\text{SO}_5$) and Marshall's acid ($\\text{H}_2\\text{S}_2\\text{O}_8$), sulphur has an oxidation state of $+6$, NOT $+8$ or $+7$, because of peroxide linkage ($-O-O-$)!",
            "tips_and_tricks": "Mnemonic for $n$-factors of $\\text{KMnO}_4$: 'BAN 153' (Basic: 1, Acidic: 5, Neutral: 3)."
        }
    ],

    "kcet-hydrogen-and-its-compounds": [
        {
            "name": "Hydrides, Water Hardness & Hydrogen Peroxide",
            "category": "Inorganic Chemistry",
            "primary": ["isotopes of hydrogen", "deuterium", "tritium", "heavy water", "temporary hardness", "permanent hardness", "zeolite", "calgon", "hydrogen peroxide", "volume strength", "perhydrol"],
            "formula_cues": [r"\text{h}_2\text{o}_2", r"\text{d}_2\text{o}", r"\text{cahco}_3", r"\text{volume strength} = 11.2 \times M", r"10\text{ volume}"],
            "secondary": ["water", "hardness", "bleaching", "boiling"],
            "summary": "Hydrogen isotopes: Protium ($^1\\text{H}$), Deuterium ($^2\\text{H}$), Tritium ($^3\\text{H}$, radioactive $\\beta$-emitter). Temporary hardness is caused by bicarbonates of Ca and Mg (removed by boiling or Clark's process with lime). Permanent hardness is caused by chlorides and sulphates of Ca and Mg (removed by washing soda, zeolite or Calgon $\\text{Na}_6\\text{P}_6\\text{O}_{18}$). $\\text{H}_2\\text{O}_2$: non-planar open-book structure; $\\text{Volume Strength} = 11.2 \\times M = 5.6 \\times N$.",
            "standard_formulas": r"\text{Volume Strength of } \text{H}_2\text{O}_2 = 11.2 \times \text{Molarity} = 5.6 \times \text{Normality}, \quad \text{Clark's: } \text{Ca(HCO}_3)_2 + \text{Ca(OH)}_2 \to 2\text{CaCO}_3\downarrow + 2\text{H}_2\text{O}",
            "common_traps": "Calgon is Sodium hexametaphosphate $\\text{Na}_6\\text{P}_6\\text{O}_{18}$; it softens hard water by sequestering $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$ ions into soluble complex anions.",
            "tips_and_tricks": "Heavy water $\\text{D}_2\\text{O}$ has higher boiling point, density, and viscosity than ordinary water $\\text{H}_2\\text{O}$, and is used as a moderator in nuclear reactors."
        }
    ],

    "kcet-s-block-elements": [
        {
            "name": "Alkali & Alkaline Earth Metals: Trends & Compounds",
            "category": "s-Block Chemistry",
            "primary": ["alkali metals", "alkaline earth metals", "flame color", "anomalous behavior of lithium", "diagonal relationship", "solubility of sulphates", "basic nature of hydroxides", "plaster of paris", "washing soda", "caustic soda", "quick lime"],
            "formula_cues": [r"\text{caso}_4 \cdot \frac{1}{2}\text{h}_2\text{o}", r"\text{na}_2\text{co}_3 \cdot 10\text{h}_2\text{o}", r"\text{li}_2\text{co}_3", r"\text{be(oh)}_2"],
            "secondary": ["sodium", "calcium", "magnesium", "solubility"],
            "summary": "Group 1 & 2 trends: Flame colors: Li (crimson), Na (yellow), K (violet), Ca (brick red), Sr (crimson), Ba (apple green). Diagonal relationship of Li with Mg, and Be with Al due to similar charge/radius ratio. Solubility of alkaline earth metal sulphates decreases down the group ($\\text{BeSO}_4 > \\text{MgSO}_4 > \\text{CaSO}_4 > \\text{BaSO}_4$) because hydration energy decreases faster than lattice energy. Plaster of Paris: $\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O}$.",
            "standard_formulas": r"\text{Plaster of Paris: } \text{CaSO}_4 \cdot \frac{1}{2}\text{H}_2\text{O}, \quad \text{Gypsum: } \text{CaSO}_4 \cdot 2\text{H}_2\text{O}, \quad \text{Heating above 393 K} \to \text{Dead Burnt Plaster}",
            "common_traps": "Heating gypsum above $393\\text{ K}$ ($120^\\circ\\text{C}$) forms completely anhydrous dead burnt plaster ($\\text{CaSO}_4$) which loses the setting property with water!",
            "tips_and_tricks": "Alkali metals dissolve in liquid ammonia to give deep blue conducting solutions due to ammoniated electrons; in concentrated solution, the color turns bronze and becomes diamagnetic."
        }
    ],

    "kcet-p-block-elements": [
        {
            "name": "Boron & Carbon Families (Groups 13 & 14)",
            "category": "p-Block Elements",
            "primary": ["diborane", "borax", "borax bead test", "inert pair effect", "boric acid", "allotropes of carbon", "silicones", "silicates", "zeolites", "carbon monoxide"],
            "formula_cues": [r"\text{b}_2\text{h}_6", r"\text{na}_2\text{b}_4\text{o}_7 \cdot 10\text{h}_2\text{o}", r"\text{h}_3\text{bo}_3", r"\text{3c-2e bond}"],
            "secondary": ["banana bond", "oxidation state", "electron deficient"],
            "summary": "Group 13: Diborane $\\text{B}_2\\text{H}_6$ has two 3-center-2-electron ($3c-2e$) banana bridge bonds. Borax bead test: $\\text{NaBO}_2 + \\text{B}_2\\text{O}_3$ forms colored metaborates with transition metal salts. Inert pair effect makes $+1$ oxidation state more stable for Thallium ($\text{Tl}^+$) than $+3$. Group 14: Diamond ($sp^3$, hard insulator) vs Graphite ($sp^2$, planar sheets, conductor). Silicones are organosilicon polymers with $\\text{[-R}_2\\text{SiO-]}_n$ repeating units.",
            "standard_formulas": r"\text{Borax Bead: } \text{Na}_2\text{B}_4\text{O}_7 \cdot 10\text{H}_2\text{O} \xrightarrow{\\Delta} 2\text{NaBO}_2 + \text{B}_2\text{O}_3 \quad (\text{Glassy Bead})",
            "common_traps": "Orthoboric acid $\\text{H}_3\\text{BO}_3$ is NOT a protonic acid; it is a weak monobasic Lewis acid that accepts $\\text{OH}^-$ from water: $\\text{B(OH)}_3 + 2\\text{H}_2\\text{O} \\rightleftharpoons [\\text{B(OH)}_4]^- + \\text{H}_3\\text{O}^+$.",
            "tips_and_tricks": "Due to the inert pair effect, $+1$ is the most stable state for $\\text{Tl}$, and $+2$ is the most stable state for $\\text{Pb}$."
        },
        {
            "name": "Nitrogen, Oxygen & Halogen Families (Groups 15, 16, 17 & 18)",
            "category": "p-Block Chemistry",
            "primary": ["haber process", "ostwald process", "oxoacids of phosphorus", "oxoacids of sulphur", "contact process", "interhalogen compounds", "anomalous fluorine", "xenon fluorides", "noble gases"],
            "formula_cues": [r"\text{h}_3\text{po}_2", r"\text{h}_3\text{po}_3", r"\text{h}_3\text{po}_4", r"\text{h}_2\text{so}_4", r"\text{xef}_4", r"\text{xef}_6"],
            "secondary": ["reducing agent", "basicity", "structure", "lone pair"],
            "summary": "Group 15: Basicity of phosphorus oxoacids: $\\text{H}_3\\text{PO}_2$ is monobasic (has 2 $\\text{P-H}$ bonds $\\implies$ strong reducing agent); $\\text{H}_3\\text{PO}_3$ is dibasic; $\\text{H}_3\\text{PO}_4$ is tribasic. Group 16: Contact process for $\\text{H}_2\\text{SO}_4$ with $\\text{V}_2\\text{O}_5$ catalyst. Group 17: Interhalogens $\\text{XX}'_n$ are more reactive than pure halogens (except $\\text{F}_2$). Group 18: $\\text{XeF}_2$ (linear), $\\text{XeF}_4$ (square planar), $\\text{XeF}_6$ (distorted octahedral).",
            "standard_formulas": r"\text{Basicity of } \text{H}_3\text{PO}_2 = 1, \quad \text{H}_3\text{PO}_3 = 2, \quad \text{H}_3\text{PO}_4 = 3, \quad \text{XeF}_4 \ (\text{Square Planar, } sp^3d^2)",
            "common_traps": "Reducing power of $\\text{H}_3\\text{PO}_2$ is highest because it contains TWO direct $\\text{P-H}$ bonds, whereas $\\text{H}_3\\text{PO}_4$ has zero $\\text{P-H}$ bonds.",
            "tips_and_tricks": "Acidic strength of oxoacids of chlorine increases with increasing oxidation state of $\\text{Cl}$: $\\text{HClO} < \\text{HClO}_2 < \\text{HClO}_3 < \\text{HClO}_4$."
        }
    ],

    "kcet-hydrocarbons": [
        {
            "name": "Alkanes & Alkenes: Additions & Named Reactions",
            "category": "Hydrocarbons",
            "primary": ["wurtz reaction", "markovnikov", "anti-markovnikov", "peroxide effect", "kharasch", "ozonolysis", "saytzeff", "kolbe's electrolytic", "conformations of ethane"],
            "formula_cues": [r"2\text{r-x} + 2\text{na} \xrightarrow{\text{dry ether}} \text{r-r}", r"\text{hbr} / \text{peroxide}", r"\text{o}_3 / \text{zn-h}_2\text{o}"],
            "secondary": ["alkane", "alkene", "double bond", "product"],
            "summary": "Wurtz reaction couples alkyl halides to form symmetrical alkanes. Markovnikov addition: electrophilic proton adds to carbon with more hydrogens. Anti-Markovnikov (peroxide effect) occurs ONLY with $\\text{HBr}$ in the presence of peroxides via free radical mechanism. Ozonolysis cleaves $>\text{C=C}<$ into aldehydes and ketones.",
            "standard_formulas": r"\text{Wurtz: } 2\text{RX} + 2\text{Na} \xrightarrow{\text{dry ether}} \text{R-R} + 2\text{NaX}, \quad \text{Ozonolysis: } >\text{C=C}< \xrightarrow{\text{O}_3, \text{Zn/H}_2\text{O}} >\text{C=O} + \text{O=C}<",
            "common_traps": "The peroxide effect applies strictly to $\\text{HBr}$; it DOES NOT work with $\\text{HCl}$ or $\\text{HI}$ due to thermodynamic and kinetic bond enthalpy constraints.",
            "tips_and_tricks": "Ozonolysis products directly reveal the position of the double bond: replace $>\text{C=O}$ and $\\text{O=C}<$ with a double bond to reconstruct the starting alkene."
        },
        {
            "name": "Alkynes & Aromatic Electrophilic Substitution",
            "category": "Alkynes & Aromatics",
            "primary": ["acidity of alkynes", "terminal alkyne", "sodium acetylide", "hydration of alkynes", "benzene", "nitration", "friedel-crafts", "electrophilic aromatic substitution", "nitronium ion"],
            "formula_cues": [r"\text{ch}\equiv\text{ch} \xrightarrow{\text{hg}^{2+}/\text{h}_2\text{so}_4} \text{ch}_3\text{cho}", r"\text{no}_2^+", r"\text{alcl}_3"],
            "secondary": ["benzene", "electrophile", "reagent"],
            "summary": "Acidity of terminal alkynes: $sp$-hybridized carbon has $50\\%$ $s$-character, making terminal hydrogen acidic enough to react with $\\text{NaNH}_2$ or ammoniacal $\\text{AgNO}_3$. Hydration of acetylene with $\\text{Hg}^{2+}/\\text{H}_2\\text{SO}_4$ gives acetaldehyde; propyne gives acetone. Electrophilic aromatic substitution on benzene: Nitration (electrophile $\\text{NO}_2^+$ generated by $\\text{HNO}_3 + \\text{H}_2\\text{SO}_4$), Friedel-Crafts alkylation/acylation with anhydrous $\\text{AlCl}_3$.",
            "standard_formulas": r"\text{Acidity: } \text{CH}\equiv\text{CH} > \text{CH}_2\text{=CH}_2 > \text{CH}_3\text{-CH}_3, \quad \text{Nitration Electrophile: } \text{NO}_2^+",
            "common_traps": "Aniline cannot undergo Friedel-Crafts reaction because its basic $-\\text{NH}_2$ group coordinates with the Lewis acid catalyst $\\text{AlCl}_3$ to form an inactive salt complex.",
            "tips_and_tricks": "Terminal alkynes give a red precipitate of copper acetylide with ammoniacal cuprous chloride, distinguishing them from non-terminal alkynes."
        }
    ],

    "kcet-environmental-chemistry": [
        {
            "name": "Atmospheric Pollution, Smog & Green Chemistry",
            "category": "Environmental Science",
            "primary": ["tropospheric", "classical smog", "photochemical smog", "pan", "peroxyacetyl nitrate", "acid rain", "greenhouse gases", "ozone depletion", "bod", "cod"],
            "formula_cues": [r"\text{cfc}", r"\text{cf}_2\text{cl}_2", r"\text{so}_2 + \text{no}_2 \to \text{acid rain}"],
            "secondary": ["atmosphere", "pollution", "water", "ozone"],
            "summary": "Classical smog: reducing smog, occurs in cool humid climate, contains smoke, fog and $\\text{SO}_2$. Photochemical smog: oxidizing smog, occurs in warm sunny climate, contains unsaturated hydrocarbons and nitrogen oxides, forming ozone, acrolein, and PAN (peroxyacetyl nitrate). Acid rain: $\\text{pH} < 5.6$ caused by $\\text{SO}_2$ and $\\text{NO}_x$. Water quality: Clean drinking water has $\\text{BOD} < 5\\text{ ppm}$; highly polluted water has $\\text{BOD} > 17\\text{ ppm}$.",
            "standard_formulas": r"\text{Acid Rain: } \text{pH} < 5.6, \quad \text{Photochemical Smog} = \text{O}_3 + \text{PAN} + \text{Acrolein} + \text{NO}_2",
            "common_traps": "Photochemical smog is OXIDIZING in nature, while classical smog is REDUCING in nature!",
            "tips_and_tricks": "Chlorofluorocarbons (CFCs) deplete ozone in the stratosphere via chlorine free radical chain catalysis: one Cl radical can destroy up to 100,000 ozone molecules."
        }
    ],

    "kcet-solid-state": [
        {
            "name": "Crystal Lattices, Unit Cells & Density Formula",
            "category": "Crystallography",
            "primary": ["unit cell", "simple cubic", "body centered cubic", "bcc", "face centered cubic", "fcc", "coordination number", "packing efficiency", "density of unit cell", "radius ratio"],
            "formula_cues": [r"d = \frac{z m}{a^3 n_a}", r"r = \frac{a}{2}", r"r = \frac{\sqrt{3}a}{4}", r"r = \frac{a}{2\sqrt{2}}", r"z=1, 2, 4"],
            "secondary": ["atoms", "cell", "edge length", "lattice"],
            "summary": "Unit cells: Simple cubic ($Z=1$, coordination number 6, packing efficiency $52.4\\%$, $r = a/2$). BCC ($Z=2$, coordination number 8, packing efficiency $68\\%$, $r = \\frac{\\sqrt{3}a}{4}$). FCC ($Z=4$, coordination number 12, packing efficiency $74\\%$, $r = \\frac{a}{2\\sqrt{2}}$). Density formula $d = \\frac{Z M}{a^3 N_A}$.",
            "standard_formulas": r"d = \frac{Z \cdot M}{a^3 \cdot N_A}, \quad \text{BCC: } 4r = \sqrt{3}a, \quad \text{FCC: } 4r = \sqrt{2}a, \quad Z_{\text{fcc}} = 4, Z_{\text{bcc}} = 2",
            "common_traps": "Edge length $a$ in the density formula must be converted to $\\text{cm}$ ($1\\text{ pm} = 10^{-10}\\text{ cm}$) to obtain density in $\\text{g/cm}^3$!",
            "tips_and_tricks": "Packing efficiency order: $\\text{FCC} (74\\%) > \\text{BCC} (68\\%) > \\text{SC} (52.4\\%)$. Space unoccupied (voids) in FCC is $26\\%$, in BCC is $32\\%$, in SC is $47.6\\%$."
        },
        {
            "name": "Point Defects & Magnetic Properties of Solids",
            "category": "Crystal Imperfections",
            "primary": ["schottky defect", "frenkel defect", "f-centers", "metal excess defect", "ferromagnetic", "antiferromagnetic", "ferrimagnetic", "density decreases"],
            "formula_cues": [r"\text{nacl, kcl, cscl}", r"\text{zns, agcl, agbr}", r"\text{f-centre}"],
            "secondary": ["crystal", "defect", "solid", "cation"],
            "summary": "Schottky defect: Equal numbers of cations and anions missing $\\implies$ density decreases (seen in highly ionic salts with high coordination numbers: NaCl, KCl, CsCl). Frenkel defect: Cation displaced to interstitial site $\\implies$ density remains unchanged (seen in salts with large radius difference: ZnS, AgCl). AgBr exhibits BOTH Schottky and Frenkel defects. F-centers are trapped electrons in anion vacancies that impart color to crystals (e.g. yellow color in NaCl).",
            "standard_formulas": r"\text{Schottky: Density Decreases}, \quad \text{Frenkel: Density Unchanged}, \quad \text{AgBr: Shows Both Defects}",
            "common_traps": "Frenkel defect does NOT change the density of the crystal; Schottky defect strictly lowers crystal density.",
            "tips_and_tricks": "AgBr is the classic exam question as the unique compound displaying both Schottky and Frenkel defects."
        }
    ],

    "kcet-liquid-solution": [
        {
            "name": "Raoult's Law & Colligative Properties",
            "category": "Colligative Properties",
            "primary": ["raoult's law", "henry's law", "relative lowering of vapour pressure", "elevation in boiling point", "depression in freezing point", "osmotic pressure", "ideal solution", "azeotrope", "van 't hoff factor"],
            "formula_cues": [r"\frac{p^\\circ - p}{p^\\circ} = \chi_b", r"\\Delta t_b = k_b m", r"\\Delta t_f = k_f m", r"\pi = c r t", r"i = 1 + (n-1)\alpha"],
            "secondary": ["solution", "moles", "vapour pressure", "freezing point"],
            "summary": "Raoult's Law: $P = P_A^\\circ \\chi_A + P_B^\\circ \\chi_B$. Colligative properties depend on the number of solute particles: RLVP $\\frac{P^\\circ - P}{P^\\circ} = i \\chi_B$; boiling point elevation $\\Delta T_b = i K_b m$; freezing point depression $\\Delta T_f = i K_f m$; osmotic pressure $\\pi = i C R T$. Van 't Hoff factor $i = 1 + (n-1)\\alpha$ for dissociation; $i = 1 + (1/n - 1)\\beta$ for association.",
            "standard_formulas": r"\\Delta T_b = i K_b m, \quad \\Delta T_f = i K_f m, \quad \pi = i C R T, \quad i = 1 + (n-1)\alpha",
            "common_traps": "Osmotic pressure is the BEST colligative property for determining molar masses of biomolecules and polymers because measurements are made at room temperature and produce large, easily readable values.",
            "tips_and_tricks": "A $0.1\\text{ M } \\text{Al}_2(\\text{SO}_4)_3$ solution has $i=5$, so it will produce the greatest depression in freezing point (lowest freezing point) among equimolar solutions."
        }
    ],

    "kcet-electrochemistry": [
        {
            "name": "Nernst Equation & Electrochemical Cells",
            "category": "Electrochemical Thermodynamics",
            "primary": ["nernst equation", "standard electrode potential", "cell emf", "daniell cell", "e_cell", "gibbs free energy", "equilibrium constant", "e^circ"],
            "formula_cues": [r"e_{\text{cell}} = e^\\circ - \frac{0.0591}{n}\log q", r"\\Delta g^\\circ = -n f e^\\circ", r"e^\\circ = \frac{0.0591}{n}\log k"],
            "secondary": ["anode", "cathode", "potential", "reduction"],
            "summary": "Nernst equation at $298\\text{ K}$: $E_{\\text{cell}} = E^\\circ_{\\text{cell}} - \\frac{0.0591}{n}\\log Q$. Standard cell potential $E^\\circ_{\\text{cell}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}}$. Thermodynamic link: $\\Delta G^\\circ = -n F E^\\circ_{\\text{cell}} = -2.303 RT\\log K$. More positive reduction potential indicates stronger oxidizing power.",
            "standard_formulas": r"E_{\text{cell}} = E^\\circ_{\text{cell}} - \frac{0.0591}{n}\log_{10} Q, \quad \\Delta G^\\circ = -nFE^\\circ_{\text{cell}}, \quad E^\\circ = \frac{0.0591}{n}\log K",
            "common_traps": "Electrode potentials are intensive properties and CANNOT be added directly when combining half-cells; you must combine Gibbs energies: $\\Delta G_3 = \\Delta G_1 + \\Delta G_2 \\implies n_3 E_3^\\circ = n_1 E_1^\\circ + n_2 E_2^\\circ$.",
            "tips_and_tricks": "At equilibrium, cell potential drops to zero ($E_{\\text{cell}} = 0$) and the battery is completely discharged!"
        },
        {
            "name": "Conductance, Kohlrausch's Law & Faraday's Laws",
            "category": "Conductance & Electrolysis",
            "primary": ["specific conductivity", "molar conductivity", "cell constant", "kohlrausch's law", "limiting molar conductivity", "faraday's laws", "mass deposited", "96500 coulombs", "lead storage battery"],
            "formula_cues": [r"\kappa = \frac{1}{r}\frac{l}{a}", r"\Lambda_m = \frac{1000\kappa}{m}", r"\Lambda_m^\\circ = \nu_+\lambda_+^\\circ + \nu_-\lambda_-^\\circ", r"w = \frac{m i t}{n f}"],
            "secondary": ["solution", "current", "electrolysis", "resistance"],
            "summary": "Conductivity $\\kappa = G \\cdot G^* = \\frac{1}{R}\\left(\\frac{l}{A}\\right)$. Molar conductivity $\\Lambda_m = \\frac{1000\\kappa}{M}$. Kohlrausch's law of independent migration: $\\Lambda_m^\\circ = \\nu_+ \\lambda_+^\\circ + \\nu_- \\lambda_-^\\circ$. Degree of dissociation $\\alpha = \\frac{\\Lambda_m}{\\Lambda_m^\\circ}$. Faraday's law of electrolysis: $w = \\frac{M \\cdot I \\cdot t}{n F}$.",
            "standard_formulas": r"\Lambda_m = \frac{1000\kappa}{M}, \quad \alpha = \frac{\Lambda_m}{\Lambda_m^\\circ}, \quad w = \frac{M I t}{n F}, \quad F \approx 96500\text{ C/mol}",
            "common_traps": "As dilution increases, specific conductivity $\\kappa$ DECREASES (fewer ions per unit volume), but molar conductivity $\\Lambda_m$ INCREASES!",
            "tips_and_tricks": "1 Faraday of charge ($96500\\text{ C}$) deposits exactly 1 gram-equivalent of any substance at an electrode."
        }
    ],

    "kcet-chemical-kinetics": [
        {
            "name": "Rate Law, Order & Integrated Rate Equations",
            "category": "Reaction Kinetics",
            "primary": ["rate of reaction", "order of reaction", "molecularity", "rate constant units", "first order reaction", "half life period", "zero order", "pseudo first order", "inversion of cane sugar"],
            "formula_cues": [r"k = \frac{2.303}{t}\log\frac{a_0}{a}", r"t_{1/2} = \frac{0.693}{k}", r"t_{1/2} \propto \frac{1}{a_0^{n-1}}", r"\text{mol l}^{-1}\text{s}^{-1}", r"\text{s}^{-1}"],
            "secondary": ["concentration", "time", "rate", "initial"],
            "summary": "Rate equation: $\\text{Rate} = k [A]^x [B]^y$. Units of $k$: $(\\text{mol L}^{-1})^{1-n} \\text{s}^{-1}$. Zero order: rate is independent of concentration; $t_{1/2} = \\frac{[A]_0}{2k} \\propto [A]_0$. First order: $k = \\frac{2.303}{t}\\log\\frac{[A]_0}{[A]}$; half-life $t_{1/2} = \\frac{0.693}{k}$ (completely independent of initial concentration). General half-life relation: $t_{1/2} \\propto \\frac{1}{[A]_0^{n-1}}$.",
            "standard_formulas": r"\text{First Order: } t = \frac{2.303}{k}\log\frac{[A]_0}{[A]}, \quad t_{1/2} = \frac{0.693}{k}, \quad t_{75%} = 2 \times t_{50%}, \quad t_{99.9%} = 10 \times t_{50%}",
            "common_traps": "Order of a reaction can be fractional or zero and must be determined experimentally; molecularity is always a positive integer ($1, 2, 3$) and can never be zero or fractional.",
            "tips_and_tricks": "In a first-order reaction: Time required for $75\\%$ completion is exactly $2 \\times t_{1/2}$; for $99.9\\%$ completion is $10 \\times t_{1/2}$!"
        },
        {
            "name": "Arrhenius Equation, Activation Energy & Catalysis",
            "category": "Temperature & Activation",
            "primary": ["arrhenius equation", "activation energy", "temperature coefficient", "collision theory", "effective collisions", "catalyst lowers activation", "e_a"],
            "formula_cues": [r"k = a e^{-e_a/rt}", r"\log\frac{k_2}{k_1} = \frac{e_a}{2.303r}\left(\frac{1}{t_1}-\frac{1}{t_2}\right)", r"\text{slope} = -\frac{e_a}{2.303r}"],
            "secondary": ["temperature", "rate constant", "graph"],
            "summary": "Arrhenius equation: $k = A e^{-E_a/RT} \\implies \\ln k = \\ln A - \\frac{E_a}{RT}$. Graph of $\\log k$ versus $1/T$ is a straight line with slope $= -\\frac{E_a}{2.303 R}$. Temperature coefficient $\\approx 2$ (rate doubles for every $10^\\circ\\text{C}$ rise in temperature). A catalyst provides an alternate reaction pathway with lower activation energy $E_a$.",
            "standard_formulas": r"\log_{10} k = \log_{10} A - \frac{E_a}{2.303 R T}, \quad \log_{10}\frac{k_2}{k_1} = \frac{E_a}{2.303 R}\left(\frac{T_2 - T_1}{T_1 T_2}\right)",
            "common_traps": "A catalyst increases the speed of reaction by lowering $E_a$, but it does NOT alter $\\Delta H$, $\\Delta G$, or the equilibrium constant $K_{eq}$!",
            "tips_and_tricks": "If activation energy $E_a = 0$, the rate constant $k = A$ and the reaction rate is completely independent of temperature."
        }
    ],

    "kcet-surface-chemistry": [
        {
            "name": "Adsorption: Physisorption vs Chemisorption & Freundlich Isotherm",
            "category": "Surface Chemistry",
            "primary": ["adsorption", "physisorption", "chemisorption", "freundlich adsorption isotherm", "adsorbate", "adsorbent", "extent of adsorption", "multilayer"],
            "formula_cues": [r"\frac{x}{m} = k p^{1/n}", r"\log\frac{x}{m} = \log k + \frac{1}{n}\log p", r"0 \le \frac{1}{n} \le 1"],
            "secondary": ["gas", "pressure", "temperature", "reversible"],
            "summary": "Physisorption involves weak van der Waals forces, is reversible, multi-layered, non-specific, and decreases continuously with temperature. Chemisorption involves chemical bond formation, is irreversible, unilayered, highly specific, and initially increases then decreases with temperature. Freundlich isotherm: $\\frac{x}{m} = k P^{1/n}$ ($0 \\le 1/n \\le 1$).",
            "standard_formulas": r"\frac{x}{m} = k P^{1/n}, \quad \log\frac{x}{m} = \log k + \frac{1}{n}\log P \quad (\text{Slope } = 1/n)",
            "common_traps": "Chemisorption has high enthalpy of adsorption ($80-240\\text{ kJ/mol}$), whereas physisorption has low enthalpy ($20-40\\text{ kJ/mol}$).",
            "tips_and_tricks": "Easily liquefiable gases (high critical temperature $T_c$, e.g. $\\text{SO}_2, \\text{NH}_3$) are adsorbed in greater amounts by charcoal than permanent gases ($\text{H}_2, \\text{N}_2$)."
        },
        {
            "name": "Colloids, Tyndall Effect & Hardy-Schulze Rule",
            "category": "Colloidal Chemistry",
            "primary": ["colloid", "lyophilic", "lyophobic", "micelle", "critical micelle concentration", "cmc", "tyndall effect", "brownian movement", "electrophoresis", "hardy-schulze rule", "coagulation value", "gold number"],
            "formula_cues": [r"\text{al}^{3+} > \text{ba}^{2+} > \text{na}^+", r"\text{[fe(cn)}_6]^{4-} > \text{po}_4^{3-} > \text{so}_4^{2-} > \text{cl}^-", r"\text{gold number}"],
            "secondary": ["particles", "flocculation", "charge", "protective"],
            "summary": "Colloid classification: Lyophilic (solvent-loving, reversible, self-stabilizing, e.g. starch, gelatin) vs Lyophobic (solvent-hating, irreversible, e.g. metal sols, $\\text{As}_2\\text{S}_3$). Properties: Tyndall effect (scattering of light), Brownian motion (kinetic motion preventing settling), Electrophoresis (confirms charge on colloidal particles). Hardy-Schulze Rule: Coagulating power of an electrolyte is directly proportional to the 4th power of the valency of the active ion ($Z^4$).",
            "standard_formulas": r"\text{Coagulating Power of Cations: } \text{Al}^{3+} > \text{Ba}^{2+} > \text{Na}^+, \quad \text{Coagulating Value} \propto \frac{1}{\text{Coagulating Power}}",
            "common_traps": "Gold number is INVERSELY proportional to protective power: a protective colloid with a SMALLER gold number has HIGHER protective efficiency (Gelatin has lowest gold number $\\implies$ best protector).",
            "tips_and_tricks": "For negatively charged $\\text{As}_2\\text{S}_3$ sol, $\\text{Al}^{3+}$ has the greatest coagulating power; for positively charged $\\text{Fe(OH)}_3$ sol, $[\\text{Fe(CN)}_6]^{4-}$ has the greatest coagulating power."
        }
    ],

    "kcet-d-and-f-block-elements": [
        {
            "name": "Transition Elements: Properties, Oxidation States & Color",
            "category": "d-Block Chemistry",
            "primary": ["transition elements", "variable oxidation states", "unpaired electrons", "spin-only magnetic moment", "colored ions", "d-d transition", "catalytic properties", "interstitial compounds"],
            "formula_cues": [r"\mu = \sqrt{n(n+2)}\text{ bm}", r"\text{sc}^{3+} \ (d^0)", r"\text{ti}^{4+} \ (d^0)", r"\text{zn}^{2+} \ (d^{10})", r"\text{mn}^{2+} \ (d^5)"],
            "secondary": ["bohr magnetons", "colorless", "configuration"],
            "summary": "Transition metals feature incompletely filled $d$-orbitals. Magnetic moment $\\mu = \\sqrt{n(n+2)}\\text{ BM}$ ($n$ is number of unpaired electrons; $\\text{Mn}^{2+}$ with $3d^5$ has maximum $\\mu = \\sqrt{35} \\approx 5.92\\text{ BM}$). Color arises from $d-d$ transitions (ions with $d^0$ like $\\text{Sc}^{3+}, \\text{Ti}^{4+}$ or $d^{10}$ like $\\text{Zn}^{2+}$ are completely colorless). Highest oxidation state $+7$ is exhibited by Manganese ($\text{KMnO}_4$).",
            "standard_formulas": r"\mu_{\text{spin}} = \sqrt{n(n+2)}\text{ BM}, \quad \text{Colorless: } d^0 \text{ and } d^{10} \text{ ions}",
            "common_traps": "Zinc, Cadmium, and Mercury are NOT considered true transition elements because they possess completely filled $d^{10}$ configurations both in elemental and ionic states.",
            "tips_and_tricks": "Interstitial compounds (e.g. $\\text{TiC, Fe}_3\\text{H}$) retain metallic conductivity, have very high melting points, and are chemically inert and extremely hard."
        },
        {
            "name": "Potassium Dichromate, Permanganate & Lanthanoid Contraction",
            "category": "f-Block & Compounds",
            "primary": ["potassium dichromate", "k2cr2o7", "potassium permanganate", "kmno4", "chromyl chloride test", "lanthanoid contraction", "zirconium and hafnium", "mischmetal"],
            "formula_cues": [r"\text{cr}_2\text{o}_7^{2-} + 14\text{h}^+ + 6e^- \to 2\text{cr}^{3+} + 7\text{h}_2\text{o}", r"\text{cro}_2\text{cl}_2", r"\text{zr} \approx \text{hf}"],
            "secondary": ["orange", "yellow", "oxidation", "radii"],
            "summary": "$\\text{K}_2\\text{Cr}_2\\text{O}_7$: Orange dichromate $\\text{Cr}_2\\text{O}_7^{2-}$ interconverts to yellow chromate $\\text{CrO}_4^{2-}$ in alkaline medium: $\\text{Cr}_2\\text{O}_7^{2-} + 2\\text{OH}^- \\rightleftharpoons 2\\text{CrO}_4^{2-} + \\text{H}_2\\text{O}$. Chromyl chloride test: $\\text{CrO}_2\\text{Cl}_2$ red vapors confirm ionic chloride. Lanthanoid contraction: Steady decrease in atomic/ionic radii due to poor shielding by $4f$ electrons, making pairs like $\\text{Zr}$ ($4d$) and $\\text{Hf}$ ($5d$) have almost identical atomic radii ($160\\text{ pm}$ vs $159\\text{ pm}$).",
            "standard_formulas": r"\text{Dichromate-Chromate Equilibrium: } \text{Cr}_2\text{O}_7^{2-} \ (\text{orange}) \xrightleftharpoons[\text{H}^+]{\text{OH}^-} 2\text{CrO}_4^{2-} \ (\text{yellow})",
            "common_traps": "Dichromate ion $\\text{Cr}_2\\text{O}_7^{2-}$ and permanganate $\\text{MnO}_4^-$ are intensely colored despite having $d^0$ configurations; their color is due to CHARGE TRANSFER spectra, NOT $d-d$ transitions!",
            "tips_and_tricks": "Lanthanoid contraction causes $\\text{Zr}$ and $\\text{Hf}$ to have virtually identical chemical properties, making their separation extremely difficult."
        }
    ],

    "kcet-coordination-compounds": [
        {
            "name": "Werner's Theory, IUPAC Nomenclature & Isomerism",
            "category": "Coordination Principles",
            "primary": ["werner's theory", "primary valency", "secondary valency", "iupac name of complex", "coordination number", "linkage isomerism", "ionization isomerism", "coordination isomerism", "geometrical isomerism", "optical isomerism in complexes"],
            "formula_cues": [r"[\text{co(nh}_3)_6]\text{cl}_3", r"[\text{pt(nh}_3)_2\text{cl}_2]", r"[\text{co(en)}_3]^{3+}", r"\text{agcl ppt}"],
            "secondary": ["ligand", "precipitate", "moles", "complex"],
            "summary": "Werner's theory: Primary valency is ionizable (equals oxidation state, satisfied by negative ions); Secondary valency is non-ionizable (equals coordination number, satisfied by neutral molecules/anions, directional in space). Isomerism: Linkage (ambidentate ligands like $\\text{NO}_2^- / \\text{ONO}^-$), Ionization (exchange between inside/outside coordination sphere), Geometrical ($cis/trans$ in square planar $[\\text{Pt(NH}_3)_2\\text{Cl}_2]$), Optical (seen in octahedral complexes with bidentate ligands like $[\\text{Co(en)}_3]^{3+}$).",
            "standard_formulas": r"[\text{Co(NH}_3)_5\text{Cl}]\text{Cl}_2 + 2\text{AgNO}_3 \to 2\text{AgCl}\downarrow \quad (\text{Only outer sphere ions precipitate})",
            "common_traps": "Square planar complexes of type $MA_4, MA_3B, MA_2B_2$ NEVER exhibit optical isomerism because they always possess a plane of symmetry!",
            "tips_and_tricks": "The number of moles of $\\text{AgCl}$ precipitate formed with excess $\\text{AgNO}_3$ indicates directly the number of ionizable chloride ions outside the square brackets."
        },
        {
            "name": "Valence Bond Theory (VBT) & Crystal Field Theory (CFT)",
            "category": "Bonding in Complexes",
            "primary": ["crystal field theory", "cft", "crystal field splitting", "delta_o", "octahedral", "tetrahedral", "spectrochemical series", "strong field ligand", "weak field ligand", "inner orbital complex", "outer orbital complex", "cfse"],
            "formula_cues": [r"\\Delta_o", r"\\Delta_t = \frac{4}{9}\\Delta_o", r"t_{2g} \text{ and } e_g", r"d^2sp^3", r"sp^3d^2", r"\text{cn}^- > \text{co} > \text{en} > \text{nh}_3 > \text{h}_2\text{o} > \text{f}^- > \text{cl}^-"],
            "secondary": ["hybridization", "pairing energy", "magnetic", "spin"],
            "summary": "CFT: In an octahedral field, $d$-orbitals split into lower $t_{2g}$ ($d_{xy}, d_{yz}, d_{zx}$) and higher $e_g$ ($d_{x^2-y^2}, d_{z^2}$) by $\\Delta_o$. Tetrahedral splitting $\\Delta_t = \\frac{4}{9}\\Delta_o$ (always weak field, no pairing). Spectrochemical series: $\\text{I}^- < \\text{Br}^- < \\text{Cl}^- < \\text{F}^- < \\text{OH}^- < \\text{H}_2\\text{O} < \\text{NH}_3 < \\text{en} < \\text{CN}^- < \\text{CO}$. Strong field ligands ($\\text{CN}^-, \\text{CO}$) cause pairing ($\\Delta_o > P \\implies$ low spin, inner orbital $d^2sp^3$). Weak field ligands ($\\text{H}_2\\text{O}, \\text{F}^-$) do not pair ($\\Delta_o < P \\implies$ high spin, outer orbital $sp^3d^2$).",
            "standard_formulas": r"\\Delta_t = \frac{4}{9}\\Delta_o, \quad \text{Strong Field: } \\Delta_o > P \implies \text{Low Spin}, \quad \text{Weak Field: } \\Delta_o < P \implies \text{High Spin}",
            "common_traps": "Tetrahedral complexes NEVER form low-spin complexes because crystal field splitting $\\Delta_t = \\frac{4}{9}\\Delta_o$ is never large enough to overcome pairing energy.",
            "tips_and_tricks": "$[\\text{Ni(CO)}_4]$: $\\text{CO}$ is a strong field ligand, pairs all electrons into $3d^{10} \\implies sp^3$ tetrahedral and DIAMAGNETIC. $[\\text{Ni(CN)}_4]^{2-}$ is $dsp^2$ square planar and DIAMAGNETIC."
        }
    ],

    "kcet-haloalkanes-and-haloarenes": [
        {
            "name": "SN1 vs SN2 Mechanisms & Elimination Reactions",
            "category": "Alkyl Halide Reactions",
            "primary": ["sn1 mechanism", "sn2 mechanism", "carbocation intermediate", "inversion of configuration", "walden inversion", "racemization", "reactivity order", "saytzeff rule", "alcoholic koh", "grignard reagent"],
            "formula_cues": [r"3^\\circ > 2^\\circ > 1^\\circ \ (\text{sn1})", r"1^\\circ > 2^\\circ > 3^\\circ \ (\text{sn2})", r"\text{r-mg-x}"],
            "secondary": ["nucleophilic substitution", "halide", "leaving group", "alkyl"],
            "summary": "$S_N1$ mechanism: 2 steps, unimolecular, forms planar carbocation intermediate $\\implies$ partial racemization; reactivity order: $3^\\circ > 2^\\circ > 1^\\circ > \\text{CH}_3\\text{X}$. $S_N2$ mechanism: 1 step, bimolecular, backside attack with pentacoordinate transition state $\\implies$ complete Walden inversion; reactivity order: $\\text{CH}_3\\text{X} > 1^\\circ > 2^\\circ > 3^\\circ$. Elimination with alcoholic KOH follows Saytzeff rule (more substituted alkene is major product).",
            "standard_formulas": r"S_N1 \text{ Reactivity: } 3^\\circ > 2^\\circ > 1^\\circ, \quad S_N2 \text{ Reactivity: } \text{CH}_3\text{X} > 1^\\circ > 2^\\circ > 3^\\circ, \quad \text{R-I} > \text{R-Br} > \text{R-Cl} > \text{R-F}",
            "common_traps": "Aqueous KOH causes NUCLEOPHILIC SUBSTITUTION (forms alcohol), whereas alcoholic KOH causes DEHYDROHALOGENATION ELIMINATION (forms alkene)!",
            "tips_and_tricks": "Reaction of alkyl halide with $\\text{KCN}$ gives alkyl cyanide ($\\text{R-CN}$, nitrile) as major product; with $\\text{AgCN}$ it gives alkyl isocyanide ($\\text{R-NC}$) due to covalent nature of $\\text{AgCN}$."
        },
        {
            "name": "Haloarenes: Low Reactivity & Electrophilic Substitutions",
            "category": "Aryl Halides",
            "primary": ["chlorobenzene", "low reactivity of haloarenes", "partial double bond character", "electrophilic aromatic substitution", "ortho-para directing", "wurtz-fittig reaction", "fittig reaction", "ddt"],
            "formula_cues": [r"\text{c}_6\text{h}_5\text{cl}", r"\text{c-cl partial double bond}", r"\text{fittig: } 2\text{ar-x} + 2\text{na} \to \text{ar-ar}"],
            "secondary": ["resonance", "benzene ring", "dipole moment"],
            "summary": "Haloarenes are extremely unreactive toward nucleophilic substitution due to: (1) Resonance delocalization imparting partial double bond character to $\\text{C-Cl}$ bond, (2) $sp^2$ hybridized ring carbon being more electronegative, (3) Instability of phenyl cation. Electrophilic aromatic substitution: Halogen is ortho/para directing due to $+M$ resonance effect, but deactivating due to strong $-I$ inductive effect. Wurtz-Fittig: aryl halide + alkyl halide + Na $\\to$ alkylarene. Fittig: 2 aryl halides + Na $\\to$ diphenyl.",
            "standard_formulas": r"\text{Wurtz-Fittig: } \text{Ar-X} + 2\text{Na} + \text{R-X} \xrightarrow{\text{dry ether}} \text{Ar-R} + 2\text{NaX}",
            "common_traps": "In chlorobenzene, the $-I$ effect dominates over $+M$ resonance effect, making the ring deactivated overall (reacts slower than benzene), yet incoming electrophiles are directed to ortho/para positions.",
            "tips_and_tricks": "DDT (p,p'-dichlorodiphenyltrichloroethane) is synthesized by condensing chlorobenzene with chloral ($\\text{CCl}_3\\text{CHO}$) in presence of concentrated $\\text{H}_2\\text{SO}_4$."
        }
    ],

    "kcet-alcohol-phenols-and-ethers": [
        {
            "name": "Alcohols: Preparation, Lucas Test & Dehydration",
            "category": "Alcohols",
            "primary": ["lucas test", "lucas reagent", "turbidity immediately", "turbidity after 5 minutes", "dehydration of alcohols", "primary alcohol", "secondary alcohol", "tertiary alcohol", "hydroboration oxidation", "fermentation of sugar"],
            "formula_cues": [r"\text{anhy. zncl}_2 + \text{conc. hcl}", r"3^\\circ > 2^\\circ > 1^\\circ \ (\text{lucas})", r"\text{b}_2\text{h}_6 / \text{h}_2\text{o}_2, \text{oh}^-"],
            "secondary": ["turbidity", "cloudiness", "alkene", "acid"],
            "summary": "Lucas reagent (anhydrous $\\text{ZnCl}_2 + \\text{conc. HCl}$) distinguishes alcohols: $3^\\circ$ alcohol gives turbidity immediately; $2^\\circ$ alcohol gives turbidity in 5 minutes; $1^\\circ$ alcohol gives no turbidity at room temperature. Hydroboration-oxidation of alkenes gives anti-Markovnikov alcohol (without rearrangement). Acid-catalyzed dehydration of alcohols follows ease of carbocation: $3^\\circ > 2^\\circ > 1^\\circ$.",
            "standard_formulas": r"\text{Lucas: } 3^\\circ \to \text{Immediate}, \quad 2^\\circ \to 5\text{ mins}, \quad 1^\\circ \to \text{No turbidity at room temp}",
            "common_traps": "Oxidation of $1^\\circ$ alcohol with PCC (pyridinium chlorochromate) yields an aldehyde; oxidation with acidified $\\text{KMnO}_4$ oxidizes it all the way to carboxylic acid.",
            "tips_and_tricks": "Methanol is poisonous because it is oxidized in the liver to methanal (formaldehyde) and then formic acid, which causes blindness and metabolic acidosis."
        },
        {
            "name": "Phenols: Acidity & Named Reactions (Kolbe & Reimer-Tiemann)",
            "category": "Phenols",
            "primary": ["acidity of phenol", "phenoxide ion", "kolbe's reaction", "reimer-tiemann", "salicylic acid", "salicylaldehyde", "bromine water test", "white precipitate", "picric acid", "aspirin"],
            "formula_cues": [r"\text{co}_2 / \text{naoh} \to \text{salicylic acid}", r"\text{chcl}_3 / \text{naoh} \to \text{salicylaldehyde}", r"\text{br}_2 / \text{h}_2\text{o} \to \text{2,4,6-tribromophenol}", r":\text{ccl}_2"],
            "secondary": ["electrophile", "dichlorocarbene", "reaction"],
            "summary": "Phenol is acidic ($pK_a \\approx 10$) because phenoxide ion is resonance stabilized. Electron withdrawing groups (e.g. $-\\text{NO}_2$) increase acidity; picric acid (2,4,6-trinitrophenol) is strongly acidic ($pK_a = 0.38$). Kolbe's reaction: Sodium phenoxide with $\\text{CO}_2$ at $400\\text{ K}$ and $4-7\\text{ atm}$ gives salicylic acid (precursor to aspirin). Reimer-Tiemann reaction: Phenol with $\\text{CHCl}_3 + \\text{aq. NaOH}$ generates dichlorocarbene electrophile ($:\\text{CCl}_2$) to yield salicylaldehyde.",
            "standard_formulas": r"\text{Kolbe: } \text{C}_6\text{H}_5\text{ONa} + \text{CO}_2 \xrightarrow{400\text{K}, 4-7\text{atm}} \text{Salicylic Acid}, \quad \text{Reimer-Tiemann: } \text{Phenol} + \text{CHCl}_3/\text{NaOH} \to \text{Salicylaldehyde}",
            "common_traps": "The reactive electrophilic intermediate in Reimer-Tiemann reaction is DICHLOROCARBENE ($:\\text{CCl}_2$), an electron-deficient neutral species with 6 valence electrons.",
            "tips_and_tricks": "Phenol reacts with bromine water to give a white precipitate of 2,4,6-tribromophenol; with neutral $\\text{FeCl}_3$, it gives a characteristic violet coloration."
        },
        {
            "name": "Ethers: Williamson Synthesis & Cleavage with HI",
            "category": "Ethers",
            "primary": ["williamson ether synthesis", "cleavage of ethers", "concentrated hi", "anisole", "electrophilic aromatic substitution of anisole", "unsymmetrical ether"],
            "formula_cues": [r"\text{r-ona} + \text{r'-x} \to \text{r-o-r'}", r"\text{r-o-r'} + \text{hi} \to \text{r-i} + \text{r'-oh}"],
            "secondary": ["iodide", "alcohol", "sodium alkoxide"],
            "summary": "Williamson Synthesis: Reaction of sodium alkoxide with $1^\\circ$ alkyl halide via $S_N2$ mechanism. Cleavage with concentrated $\\text{HI}$: With unsymmetrical ethers containing $1^\\circ$ and $2^\\circ$ alkyl groups, the smaller alkyl group forms alkyl iodide via $S_N2$. If one alkyl group is $3^\\circ$ (e.g. tert-butyl methyl ether), the $3^\\circ$ group forms the iodide via $S_N1$ carbocation mechanism!",
            "standard_formulas": r"\text{Williamson: } \text{R-O}^-\text{Na}^+ + \text{R'-X} (1^\\circ) \xrightarrow{S_N2} \text{R-O-R'}, \quad \text{Cleavage of Anisole}: \text{C}_6\text{H}_5\text{OCH}_3 + \text{HI} \to \text{C}_6\text{H}_5\text{OH} + \text{CH}_3\text{I}",
            "common_traps": "In Williamson synthesis, using a $3^\\circ$ alkyl halide with sodium alkoxide yields an ALKENE via elimination, NOT an ether!",
            "tips_and_tricks": "Cleavage of anisole ($\text{C}_6\text{H}_5\text{OCH}_3$) with $\\text{HI}$ always yields Phenol and Methyl Iodide because $\\text{C}_6\\text{H}_5\\text{-O}$ partial double bond cannot be broken."
        }
    ],

    "kcet-compounds-containing-nitrogen": [
        {
            "name": "Basicity of Amines & Hoffmann Bromamide Degradation",
            "category": "Amine Reactions",
            "primary": ["basicity of amines", "hoffmann bromamide degradation", "carbylamine reaction", "hinsberg's reagent", "primary amine", "foul smell", "benzenesulphonyl chloride"],
            "formula_cues": [r"\text{r-conh}_2 + \text{br}_2 + 4\text{naoh} \to \text{r-nh}_2", r"\text{r-nh}_2 + \text{chcl}_3 + 3\text{koh} \to \text{r-nc} + 3\text{kcl} + 3\text{h}_2\text{o}", r"2^\\circ > 1^\\circ > 3^\\circ > \text{nh}_3"],
            "secondary": ["amide", "isocyanide", "nitrogen"],
            "summary": "Hoffmann bromamide reaction converts primary amides to primary amines with ONE FEWER carbon atom: $\\text{R-CONH}_2 + \\text{Br}_2 + 4\\text{NaOH} \\to \\text{R-NH}_2 + \\text{Na}_2\\text{CO}_3 + 2\\text{NaBr} + 2\\text{H}_2\\text{O}$. Carbylamine test: $1^\\circ$ amines heated with $\\text{CHCl}_3 + \\text{alc. KOH}$ produce extremely foul-smelling isocyanides ($\\text{R-NC}$). Hinsberg's test (benzenesulphonyl chloride $\\text{C}_6\\text{H}_5\\text{SO}_2\\text{Cl}$) distinguishes $1^\\circ, 2^\\circ, 3^\\circ$ amines.",
            "standard_formulas": r"\text{Hoffmann: } \text{R-CONH}_2 \xrightarrow{\text{Br}_2 / 4\text{NaOH}} \text{R-NH}_2 \ (\text{Degradation by 1 Carbon})",
            "common_traps": "Carbylamine test is given ONLY by primary ($1^\\circ$) amines (both aliphatic and aromatic); $2^\\circ$ and $3^\\circ$ amines do NOT respond.",
            "tips_and_tricks": "Basicity order in aqueous medium: For ethyl group: $2^\\circ > 3^\\circ > 1^\\circ > \\text{NH}_3$ (231); for methyl group: $2^\\circ > 1^\\circ > 3^\\circ > \\text{NH}_3$ (213)."
        },
        {
            "name": "Diazonium Salts & Coupling Reactions",
            "category": "Diazonium Chemistry",
            "primary": ["benzene diazonium chloride", "diazotization", "sandmeyer reaction", "gattermann reaction", "azo dye", "coupling reaction", "orange dye", "yellow dye"],
            "formula_cues": [r"\text{c}_6\text{h}_5\text{n}_2^+\text{cl}^-", r"\text{nano}_2 + \text{hcl} \ (0-5^\\circ\text{c})", r"\text{cu}_2\text{cl}_2/\text{hcl}", r"\text{cu/hcl}", r"\text{hbf}_4"],
            "secondary": ["aniline", "phenol", "nitrogen gas"],
            "summary": "Diazotization: Aniline reacts with $\\text{NaNO}_2 + \\text{HCl}$ at $0-5^\\circ\\text{C}$ ($273-278\\text{ K}$) to form benzene diazonium chloride. Sandmeyer reaction uses $\\text{Cu}_2\\text{X}_2 / \\text{HX}$ to yield haloarenes; Gattermann reaction uses $\\text{Cu} / \\text{HX}$. Azo coupling: Diazonium salt couples with phenol in weakly alkaline medium to give orange dye (p-hydroxyazobenzene); with aniline in weakly acidic medium to give yellow dye (p-aminoazobenzene).",
            "standard_formulas": r"\text{Sandmeyer: } \text{ArN}_2^+\text{Cl}^- \xrightarrow{\text{Cu}_2\text{Cl}_2/\text{HCl}} \text{Ar-Cl} + \text{N}_2, \quad \text{Coupling with Phenol} \to \text{p-hydroxyazobenzene (Orange Dye)}",
            "common_traps": "Diazonium salts must be prepared and kept cold at $0-5^\\circ\\text{C}$; on warming with water, benzene diazonium chloride hydrolyzes immediately into PHENOL and nitrogen gas!",
            "tips_and_tricks": "Treatment of $\\text{C}_6\\text{H}_5\\text{N}_2^+\\text{Cl}^-$ with $\\text{H}_3\\text{PO}_2$ (hypophosphorous acid) or $\\text{CH}_3\\text{CH}_2\\text{OH}$ reduces it cleanly to BENZENE."
        }
    ],

    "kcet-biomolecules": [
        {
            "name": "Carbohydrates: Monosaccharides, Disaccharides & Glycosidic Linkages",
            "category": "Carbohydrates",
            "primary": ["glucose", "fructose", "sucrose", "maltose", "lactose", "glycosidic linkage", "reducing sugar", "inversion of cane sugar", "mutarotation", "glycogen", "starch", "cellulose"],
            "formula_cues": [r"\text{c}_6\text{h}_{12}\text{o}_6", r"\text{c}_{12}\text{h}_{22}\text{o}_{11}", r"\alpha\text{-d-glucose}", r"\beta\text{-d-fructose}"],
            "secondary": ["hydrolysis", "hemiacetal", "tollen"],
            "summary": "Glucose: aldohexose, exists in $\\alpha$ and $\\beta$ pyranose cyclic hemiacetal forms. Fructose: ketohexose, forms furanose ring. Disaccharides linked via oxide glycosidic bond: Sucrose ($\\alpha$-D-glucose + $\\beta$-D-fructose, non-reducing sugar, hydrolysis produces 'invert sugar'); Maltose (two $\\alpha$-D-glucose units, reducing sugar); Lactose ($\\beta$-D-galactose + $\\beta$-D-glucose, reducing sugar). Starch is polymer of $\\alpha$-glucose (amylose + amylopectin); Cellulose is linear polymer of $\\beta$-glucose.",
            "standard_formulas": r"\text{Sucrose: Non-reducing disaccharide} \ (\alpha\text{-glucose} + \beta\text{-fructose} \ \text{via } C_1-C_2 \ \text{linkage})",
            "common_traps": "Sucrose is dextrorotatory, but its hydrolysis product mixture is LEVOROTATORY because the levorotation of fructose ($-92.4^\\circ$) exceeds the dextrorotation of glucose ($+52.5^\\circ$) $\\implies$ Invert sugar.",
            "tips_and_tricks": "All monosaccharides (whether aldoses or ketoses) are REDUCING sugars and give positive Tollens' and Fehling's tests."
        },
        {
            "name": "Amino Acids, Proteins & Nucleic Acids",
            "category": "Proteins & Genetics",
            "primary": ["amino acid", "zwitterion", "isoelectric point", "essential amino acid", "peptide bond", "denaturation of protein", "primary structure", "secondary structure", "dna", "rna", "nucleotide", "nucleoside", "vitamins"],
            "formula_cues": [r"\text{h}_3\text{n}^+-\text{ch(r)-coo}^-", r"\text{-co-nh-}", r"\text{adenine, thymine, guanine, cytosine, uracil}", r"\text{a=t, g}\equiv\text{c}"],
            "secondary": ["helix", "base", "hydrogen bonding", "sugar"],
            "summary": "Amino acids exist as dipolar zwitterions. Glycine is the only optically INACTIVE natural amino acid (no chiral carbon). Peptide bond is $-\\text{CO-NH}-$. Denaturation of proteins destroys secondary and tertiary structures (coagulation of egg white), but leaves primary structure intact. DNA contains bases Adenine (A), Guanine (G), Cytosine (C), Thymine (T); RNA contains Uracil (U) instead of Thymine. Chargaff's rule in DNA: $A = T$ (2 hydrogen bonds) and $G \\equiv C$ (3 hydrogen bonds).",
            "standard_formulas": r"\text{Chargaff's Rule: } [A] = [T], \quad [G] = [C], \quad \text{Nucleotide} = \text{Base} + \text{Sugar} + \text{Phosphate}",
            "common_traps": "In denaturation of proteins, primary structure (the sequence of amino acids) remains completely UNCHANGED!",
            "tips_and_tricks": "Water-soluble vitamins are Vitamin B-complex and Vitamin C (cannot be stored in body, excreted in urine); Fat-soluble vitamins are A, D, E, and K (ADEK)."
        }
    ],

    "kcet-practical-organic-chemistry": [
        {
            "name": "Qualitative & Quantitative Organic Analysis",
            "category": "Practical Analysis",
            "primary": ["lassaigne's test", "prussian blue", "sodium fusion extract", "kjeldahl's method", "carius method", "dumas method", "blood red color", "detection of nitrogen"],
            "formula_cues": [r"\text{fe}_4[\text{fe(cn)}_6]_3", r"\text{fescn}^{2+}", r"% \text{N} = \frac{1.4 \times N \times V}{w}", r"% \text{Cl} = \frac{35.5 \times m_{\text{agcl}}}{143.5 \times w} \times 100"],
            "secondary": ["organic compound", "nitrogen", "halogens", "sulphur"],
            "summary": "Lassaigne's test for nitrogen gives Prussian blue precipitate of ferric ferrocyanide $\\text{Fe}_4[\\text{Fe(CN)}_6]_3$. If both nitrogen and sulphur are present, sodium fusion gives blood-red $\\text{Fe(SCN)}^{2+}$. Kjeldahl's method for nitrogen: $%\\text{N} = \\frac{1.4 \\times N \\times V}{w}$. Carius method for halogens uses concentrated $\\text{HNO}_3 + \\text{AgNO}_3$ to precipitate $\\text{AgX}$.",
            "standard_formulas": r"\text{Kjeldahl: } %\text{N} = \frac{1.4 \times N \times V}{w}, \quad \text{Prussian Blue: } \text{Fe}_4[\text{Fe(CN)}_6]_3",
            "common_traps": "Kjeldahl's method is NOT applicable to compounds containing nitrogen in nitro ($-\\text{NO}_2$), azo ($-\\text{N=N}-$), or ring nitrogen (pyridine) because they do not form ammonium sulphate.",
            "tips_and_tricks": "Lassaigne's test fails for hydrazine ($\\text{NH}_2\\text{NH}_2$) because it contains no carbon to form cyanide ion ($\\text{CN}^-$)."
        }
    ],

    "kcet-salt-analysis": [
        {
            "name": "Systematic Qualitative Inorganic Salt Analysis",
            "category": "Inorganic Analysis",
            "primary": ["salt analysis", "group reagent", "cation", "anion", "brown ring test", "ferrous sulphate", "chromyl chloride", "flame test", "magnesia mixture", "nessler's reagent"],
            "formula_cues": [r"[\text{fe(h}_2\text{o)}_5(\text{no})]\text{so}_4", r"\text{k}_2[\text{hgi}_4]", r"\text{cro}_2\text{cl}_2"],
            "secondary": ["solution", "precipitate", "reagent", "test"],
            "summary": "Group reagents for cations: Group I ($\\text{Pb}^{2+}$, dil. HCl), Group II ($\\text{Cu}^{2+}, \\text{Pb}^{2+}$, $\\text{H}_2\\text{S}$ in acidic medium), Group III ($\\text{Fe}^{3+}, \\text{Al}^{3+}$, $\\text{NH}_4\\text{OH}$ in presence of $\\text{NH}_4\\text{Cl}$), Group IV ($\\text{Zn}^{2+}, \\text{Mn}^{2+}, \\text{Ni}^{2+}$, $\\text{H}_2\\text{S}$ in ammoniacal medium). Anion confirmatory tests: Brown ring test for nitrate ($\\text{NO}_3^-$) forms $[\\text{Fe(H}_2\\text{O)}_5(\\text{NO})]\\text{SO}_4$. Nessler's reagent ($\\text{K}_2[\\text{HgI}_4]$) gives brown precipitate with ammonium salts.",
            "standard_formulas": r"\text{Brown Ring Complex: } [\text{Fe(H}_2\text{O)}_5(\text{NO})]^{2+} \ (\text{Fe has } +1 \text{ oxidation state})",
            "common_traps": "In the brown ring complex $[\\text{Fe(H}_2\\text{O)}_5(\\text{NO})]\\text{SO}_4$, iron has an anomalous oxidation state of $+1$ ($\\text{NO}$ acts as neutral/positive $\\text{NO}^+$ ligand).",
            "tips_and_tricks": "Group III cations require $\\text{NH}_4\\text{Cl}$ before $\\text{NH}_4\\text{OH}$ to suppress $\\text{OH}^-$ concentration via common ion effect, preventing precipitation of Group IV hydroxides."
        }
    ],

    "kcet-nuclear-chemistry": [
        {
            "name": "Radioactivity, Nuclear Fission & Fusion",
            "category": "Nuclear Chemistry",
            "primary": ["radioactive", "nuclear fission", "nuclear fusion", "half life", "decay", "radioactivity", "alpha emission", "beta emission", "uranium", "moderator"],
            "formula_cues": [r"_{92}^{235}\text{u} + _0^1\text{n} \to \text{fission}", r"t_{1/2} = \frac{0.693}{\lambda}", r"e = \\Delta m c^2"],
            "secondary": ["neutrons", "energy", "nucleus"],
            "summary": "Radioactive decay modes: $\\alpha$-emission lowers mass number by 4 and atomic number by 2; $\\beta^-$-emission increases atomic number by 1 at constant mass number. Nuclear fission: $^{235}\\text{U}$ captures thermal neutron, splits into lighter nuclei with release of $\\approx 200\\text{ MeV}$ and 2-3 neutrons. Nuclear fusion: lighter hydrogen nuclei combine at extreme temperatures to form helium with huge energy release.",
            "standard_formulas": r"t_{1/2} = \frac{0.693}{\lambda}, \quad \text{Activity } A = \lambda N = -\frac{dN}{dt}",
            "common_traps": "In $\\beta^-$ decay, a neutron converts to a proton and an electron inside the nucleus: $n \\to p + e^- + \\bar{\\nu}_e$; the emitted electron does NOT come from atomic orbital shells!",
            "tips_and_tricks": "Heavy water ($\\text{D}_2\\text{O}$) and high-purity graphite are used as moderators to slow down fast neutrons in fission reactors."
        }
    ],
    # ==========================================
    # SPECIAL KCET SPECIFIC CHAPTERS
    # ==========================================
    "kcet-aldehyde-and-ketone": [   {   'category': 'Reactions & Mechanisms',
        'common_traps': 'In semicarbazide $\\text{H}_2\\text{N-CO-NH-NH}_2$, only the hydrazine $\\text{NH}_2$ reacts; '
                        'the amide $\\text{NH}_2$ is deactivated by resonance with $>\text{C=O}$.',
        'formula_cues': ['\\text{nh}_2\\text{oh}', '\\text{hcn}', '\\text{nahso}_3', '\\text{c=o}', '\\text{c=n-oh}'],
        'name': 'Carbonyl Nucleophilic Addition & Ammonia Derivatives',
        'primary': [   'carbonyl',
                       'nucleophilic addition',
                       'ammonia derivatives',
                       'hydroxylamine',
                       'hydrazine',
                       'phenylhydrazine',
                       'semicarbazide',
                       'cyanohydrin',
                       'sodium bisulphite',
                       'hemiacetal',
                       'acetal',
                       'oxime',
                       'hydrazone',
                       '2,4-dnp'],
        'secondary': ['aldehyde', 'ketone', 'reagent', 'product'],
        'standard_formulas': '>\\text{C=O} + \\text{H}_2\\text{N-Z} \\xrightarrow{\\text{H}^+} >\\text{C=N-Z} + '
                             '\\text{H}_2\\text{O}',
        'summary': 'Nucleophilic addition to $>\text{C=O}$: addition of $\\text{HCN}$ gives cyanohydrins, addition of '
                   '$\\text{NaHSO}_3$ gives crystalline bisulphite adducts. Reaction with ammonia derivatives '
                   '$\\text{H}_2\\text{N-Z}$ eliminates water to give crystalline derivatives (oximes with '
                   '$\\text{NH}_2\\text{OH}$, hydrazones with $\\text{NH}_2\\text{NH}_2$, 2,4-DNP derivatives).',
        'tips_and_tricks': 'Reactivity order toward nucleophilic addition: $\\text{HCHO} > \\text{RCHO} > '
                           '\\text{RCOR}$.'},
    {   'category': 'Named Reactions & Tests',
        'common_traps': 'Acetophenone ($\text{C}_6\text{H}_5\text{COCH}_3$) gives positive iodoform test, while '
                        'benzophenone does not.',
        'formula_cues': [   '\\text{chi}_3',
                            '\\text{dilute naoh}',
                            '\\text{conc. koh}',
                            '\\text{zn-hg/hcl}',
                            '\\text{nh}_2\\text{nh}_2/\\text{koh}'],
        'name': 'Named Condensation Reactions & Diagnostic Tests',
        'primary': [   'aldol condensation',
                       'cannizzaro',
                       'iodoform test',
                       'tollens',
                       'fehling',
                       'clemmensen',
                       'wolff-kishner',
                       'rosenmund',
                       'etard',
                       'stephen',
                       'yellow precipitate',
                       'ch3c=o'],
        'secondary': ['alpha hydrogen', 'yellow ppt', 'test', 'reduction'],
        'standard_formulas': '2\\text{CH}_3\\text{CHO} \\xrightarrow{\\text{dil. NaOH}} '
                             '\\text{CH}_3\\text{CH(OH)CH}_2\\text{CHO} \\xrightarrow{\\Delta} '
                             '\\text{CH}_3\\text{CH=CHCHO}',
        'summary': 'Aldol condensation requires $\\alpha$-hydrogen. Cannizzaro occurs for aldehydes lacking '
                   '$\\alpha$-H (disproportionation into alcohol + carboxylate). Iodoform test: positive for compounds '
                   "containing $\\text{CH}_3\\text{CO-}$ or $\\text{CH}_3\\text{CH(OH)-}$ group. Tollens' & Fehling's "
                   'tests oxidize aldehydes, not ketones.',
        'tips_and_tricks': 'Clemmensen uses acidic conditions (Zn-Hg / conc. HCl); Wolff-Kishner uses basic conditions '
                           '($\\text{NH}_2\\text{NH}_2$ / KOH / glycol).'}],

    "kcet-carboxylic-acids-and-its-derivatives": [   {   'category': 'Acid-Base Properties',
        'common_traps': 'Formic acid (HCOOH) is more acidic than acetic acid ($\text{CH}_3\text{COOH}$) because the '
                        'methyl group exerts an acid-weakening $+I$ effect.',
        'formula_cues': ['\\text{rcooh}', '\\text{rcoo}^-', '-i \\text{ effect}', '+i \\text{ effect}'],
        'name': 'Acidity of Carboxylic Acids & Substituent Effects',
        'primary': [   'carboxylic acid',
                       'acidity',
                       'more acidic than phenols',
                       'conjugate base',
                       'carboxylate ion',
                       'electron withdrawing group',
                       'substituent',
                       'pk_a',
                       'benzoic acid',
                       'formic acid',
                       'acetic acid'],
        'secondary': ['acid', 'resonance', 'strongest', 'weaker'],
        'standard_formulas': '\\text{Acidity: } \\text{HCOOH} > \\text{CH}_3\\text{COOH} > '
                             '\\text{CH}_3\\text{CH}_2\\text{COOH}',
        'summary': 'Carboxylic acids are much more acidic than phenols because the negative charge in carboxylate ion '
                   'is delocalized over two highly electronegative oxygen atoms. Electron withdrawing groups ($-I, '
                   '-M$) increase acidity; electron donating groups ($+I, +M$) decrease acidity.',
        'tips_and_tricks': 'Carboxylic acids effervesce with $\\text{NaHCO}_3$ (liberating $\\text{CO}_2$ gas), '
                           'whereas phenols (except picric acid) do not.'},
    {   'category': 'Syntheses & Reactions',
        'common_traps': 'Benzoic acid and formic acid cannot undergo HVZ reaction because they possess no '
                        '$\\alpha$-hydrogens.',
        'formula_cues': [   '\\text{br}_2/\\text{red p}',
                            '\\text{naoh + cao}',
                            '\\text{dibal-h}',
                            "\\text{rcoor}'",
                            '\\text{pci}_5'],
        'name': 'Reactions of Carboxylic Acids & Derivatives',
        'primary': [   'hell-volhard-zelinsky',
                       'hvz',
                       'decarboxylation',
                       'soda lime',
                       'ester',
                       'esterification',
                       'dibal-h',
                       'acid chloride',
                       'acid anhydride',
                       'amide',
                       'hydrolysis'],
        'secondary': ['product', 'reagent', 'reduction'],
        'standard_formulas': '\\text{R-CH}_2\\text{-COOH} \\xrightarrow{\\text{Br}_2 / \\text{Red P}} '
                             '\\text{R-CH(Br)-COOH} \\quad (\\text{HVZ Reaction})',
        'summary': 'HVZ reaction: $\\alpha$-halogenation of carboxylic acids with $\\text{X}_2 / \\text{Red P}$. '
                   'Decarboxylation with soda lime ($\text{NaOH} + \\text{CaO}$, $3:1$) yields alkane with one fewer '
                   'carbon. Reduction of esters with DIBAL-H at low temperature gives aldehydes selectively.',
        'tips_and_tricks': 'DIBAL-H reduces esters and nitriles to aldehydes, not to alcohols or amines.'}],

    "kcet-general-organic-chemistry": [   {   'category': 'Core Principles',
        'common_traps': 'In homolytic cleavage, each atom takes one bonding electron; in heterolytic cleavage, the '
                        'more electronegative atom takes both electrons.',
        'formula_cues': ['\\text{c}^+', '\\text{c}^-', '\\text{r}^\\bullet', '+i', '-i', '+m', '-m'],
        'name': 'Reaction Intermediates & Electronic Effects',
        'primary': [   'intermediate',
                       'heteropolar',
                       'homolytic',
                       'heterolytic',
                       'carbocation',
                       'carbanion',
                       'free radical',
                       'inductive effect',
                       'resonance effect',
                       'hyperconjugation',
                       'electromeric'],
        'secondary': ['bond fission', 'stability', 'electron'],
        'standard_formulas': '\\text{Carbocation Stability: } 3^\\circ > 2^\\circ > 1^\\circ > \\text{CH}_3^+, \\quad '
                             '\\text{Carbanion Stability: } \\text{CH}_3^- > 1^\\circ > 2^\\circ > 3^\\circ',
        'summary': 'Heterolytic fission creates ions (carbocations, carbanions); homolytic fission creates neutral '
                   'free radicals. Stability of carbocations: $3^\\circ > 2^\\circ > 1^\\circ > \\text{CH}_3^+$ '
                   '(governed by hyperconjugation and $+I$). Stability of carbanions: $\\text{CH}_3^- > 1^\\circ > '
                   '2^\\circ > 3^\\circ$.',
        'tips_and_tricks': 'Resonance stabilization always dominates over inductive effect, EXCEPT for halogens on '
                           'benzene rings where $-I$ dominates.'},
    {   'category': 'Physical-Chemical Properties',
        'common_traps': 'Cyclooctatetraene ($8\\pi$) is non-planar (tub-shaped), hence it is non-aromatic, NOT '
                        'anti-aromatic!',
        'formula_cues': ['4n+2', '\\pi \\text{ electrons}', '\\text{c}_6\\text{h}_5\\text{nh}_2'],
        'name': "Acidity, Basicity & Aromaticity (Huckel's Rule)",
        'primary': [   'aromatic',
                       'aromaticity',
                       'huckel',
                       '4n+2',
                       'strongest base',
                       'more basic than aniline',
                       'decreasing order of acidic',
                       'pyridine',
                       'pyrrole',
                       'aliphatic amine'],
        'secondary': ['base', 'acid', 'lone pair', 'delocalization'],
        'standard_formulas': '\\text{Aromatic: } (4n+2)\\pi \\text{ electrons}, \\quad \\text{Anti-aromatic: } 4n\\pi '
                             '\\text{ electrons}',
        'summary': "Hückel's Rule: Cyclic, planar, completely conjugated systems with $(4n+2)\\pi$ electrons are "
                   'aromatic ($2, 6, 10, 14\\pi$). Basicity of amines: Aliphatic amines are more basic than aniline '
                   "because aniline's lone pair is delocalized into the benzene ring by resonance.",
        'tips_and_tricks': 'In gas phase, amine basicity follows strictly $+I$: $3^\\circ > 2^\\circ > 1^\\circ > '
                           '\\text{NH}_3$.'}],

    "kcet-isomerism": [   {   'category': 'Isomerism',
        'common_traps': 'Functional isomers: Alcohols and Ethers; Aldehydes and Ketones; Carboxylic acids and Esters.',
        'formula_cues': ['\\text{c}_5\\text{h}_{12}', '\\text{c}_6\\text{h}_{14}', '\\text{c}_4\\text{h}_{10}'],
        'name': 'Structural Isomerism: Chain, Position & Functional',
        'primary': [   'isomers',
                       'chain isomers',
                       'position isomers',
                       'functional isomers',
                       'metamerism',
                       'c5h12',
                       'c6h14',
                       'number of chain isomers',
                       'isomers of hexane',
                       'boiling point'],
        'secondary': ['molecular formula', 'different', 'hydrocarbon'],
        'standard_formulas': '\\text{Isomer Count: } \\text{C}_4\\text{H}_{10} \\implies 2, \\quad '
                             '\\text{C}_5\\text{H}_{12} \\implies 3, \\quad \\text{C}_6\\text{H}_{14} \\implies 5, '
                             '\\quad \\text{C}_7\\text{H}_{16} \\implies 9',
        'summary': 'Structural isomerism: compounds having the same molecular formula but different structural '
                   'arrangements. Pentane ($\\text{C}_5\\text{H}_{12}$) has 3 isomers ($n$-pentane, isopentane, '
                   'neopentane). Hexane ($\\text{C}_6\\text{H}_{14}$) has 5 chain isomers.',
        'tips_and_tricks': 'Boiling points of chain isomers decrease with increasing branching.'},
    {   'category': 'Stereochemistry',
        'common_traps': 'Propene cannot show geometrical isomerism because one of the double-bonded carbons has two '
                        'identical hydrogens.',
        'formula_cues': ['\\text{cis-trans}', '2^n'],
        'name': 'Stereoisomerism: Geometrical & Optical Isomerism',
        'primary': [   'cis',
                       'trans',
                       'geometrical isomerism',
                       'optical isomerism',
                       'chiral',
                       'asymmetric carbon',
                       'enantiomers',
                       'diastereomers',
                       'meso',
                       'plane polarized light'],
        'secondary': ['restricted rotation', 'optically active'],
        'standard_formulas': '\\text{Number of optical isomers for molecule with } n \\text{ asymmetric carbons: } 2^n',
        'summary': 'Geometrical isomerism ($cis/trans$) arises due to restricted rotation about $>\text{C=C}<$ or ring '
                   'with two different groups on each carbon. Optical isomerism requires non-superimposable mirror '
                   'images (chiral center with 4 different groups, lack of plane of symmetry).',
        'tips_and_tricks': 'Meso compounds contain chiral carbons but possess an internal plane of symmetry, making '
                           'them optically inactive.'}],

    "kcet-iupac-nomenclature": [   {   'category': 'Nomenclature',
        'common_traps': 'In numbering when double and triple bonds are at identical positions from opposite ends, '
                        "double bond gets the lower locant ('en' before 'yne').",
        'formula_cues': ['\\text{iupac}', '\\text{-oic acid}', '\\text{-al}', '\\text{-one}', '\\text{-ol}'],
        'name': 'IUPAC Nomenclature & Functional Group Priority',
        'primary': [   'iupac name',
                       'iupac nomenclature',
                       'longest continuous carbon chain',
                       'principal functional group',
                       'suffix',
                       'prefix',
                       'locant',
                       'lowest locant rule'],
        'secondary': ['substituent', 'numbering', 'chain'],
        'standard_formulas': '\\text{IUPAC Format: } \\text{Prefix} + \\text{Root Word} + \\text{Primary Suffix} + '
                             '\\text{Secondary Suffix}',
        'summary': 'IUPAC rules: Identify longest continuous carbon chain containing the principal functional group. '
                   'Priority order of functional groups: $-\\text{COOH} > -\\text{SO}_3\\text{H} > -\\text{COOR} > '
                   '-\\text{COCl} > -\\text{CONH}_2 > -\\text{CN} > -\\text{CHO} > >\\text{C=O} > -\\text{OH} > '
                   '-\\text{NH}_2 > >\\text{C=C}< > -\\text{C}\\equiv\\text{C}-$.',
        'tips_and_tricks': 'Look at the principal suffix like -oic acid vs -oate vs -al to eliminate options quickly.'}],

    "kcet-metallurgy": [   {   'category': 'Metallurgical Processes',
        'common_traps': 'Calcination is heating in absence of air (for carbonates and hydrated oxides); roasting is '
                        'heating in excess air (for sulphides).',
        'formula_cues': [   '\\text{nacn}',
                            '\\text{cufes}_2',
                            '\\text{cu}_2\\text{s} + 2\\text{cu}_2\\text{o} \\to 6\\text{cu} + \\text{so}_2',
                            '\\text{fe}_2\\text{o}_3 + 3\\text{co} \\to 2\\text{fe} + 3\\text{co}_2'],
        'name': 'Ore Concentration & Pyrometallurgy Extraction',
        'primary': [   'froth floatation',
                       'potassium ethyl xanthate',
                       'collector',
                       'depressant',
                       'roasting',
                       'calcination',
                       'blast furnace',
                       'copper pyrites',
                       'copper matte',
                       'blister copper',
                       'smelting'],
        'secondary': ['ore', 'sulphide', 'gas x', 'furnace'],
        'standard_formulas': '\\text{Self Reduction: } \\text{Cu}_2\\text{S} + 2\\text{Cu}_2\\text{O} \\to 6\\text{Cu} '
                             '+ \\text{SO}_2 \\quad (\\text{Blister Copper})',
        'summary': 'Concentration of sulphide ores by froth flotation: collectors (pine oil, fatty acids, xanthates) '
                   'make mineral particles water-repellent; depressants (NaCN) separate ZnS from PbS. Roasting '
                   'converts sulphide ores to oxides with $\\text{SO}_2$ gas release. Extraction of copper from copper '
                   'pyrites involves reverberatory furnace, copper matte ($\\text{Cu}_2\\text{S} + \\text{FeS}$), and '
                   'self-reduction in Bessemer converter.',
        'tips_and_tricks': 'Blister copper gets its blistered appearance from the evolution of escaping $\\text{SO}_2$ '
                           'gas during cooling.'},
    {   'category': 'Thermodynamics & Refining',
        'common_traps': 'In Hall-Héroult process, the carbon anodes are consumed by reacting with liberated oxygen to '
                        'form $\\text{CO}$ and $\\text{CO}_2$.',
        'formula_cues': [   '\\delta g^\\circ',
                            '\\text{al}_2\\text{o}_3',
                            '\\text{na}_3\\text{alf}_6',
                            '\\text{ni(co)}_4',
                            '\\text{zri}_4'],
        'name': 'Ellingham Diagram, Hall-Heroult Process & Refining',
        'primary': [   'ellingham diagram',
                       'hall-heroult',
                       'hall heroult',
                       'delta g',
                       'carbon reduction',
                       'zone refining',
                       'mond',
                       'van arkel',
                       'liquation',
                       'cryolite'],
        'secondary': ['refining', 'temperature', 'graphite', 'anode'],
        'standard_formulas': '\\text{Hall-Héroult: } 2\\text{Al}_2\\text{O}_3 + 3\\text{C} \\to 4\\text{Al} + '
                             '3\\text{CO}_2, \\quad \\text{Mond: } \\text{Ni} + 4\\text{CO} '
                             '\\xrightarrow{330\\text{K}} \\text{Ni(CO)}_4 \\xrightarrow{450\\text{K}} \\text{Ni} + '
                             '4\\text{CO}',
        'summary': 'Ellingham diagram plots $\\Delta G^\\circ$ vs $T$. A metal can reduce the oxide of any other metal '
                   'located higher in the diagram. Hall-Héroult process: electrolysis of molten '
                   '$\\text{Al}_2\\text{O}_3$ with cryolite ($\\text{Na}_3\\text{AlF}_6$) and $\\text{CaF}_2$ to lower '
                   'melting point and increase conductivity. Refining: Zone refining (semiconductors Ge, Si), Mond '
                   'process for Ni, Van Arkel for Zr and Ti.',
        'tips_and_tricks': 'Zone refining is based on the principle that impurities are more soluble in the molten '
                           'state than in the solid state of the metal.'}],

    "kcet-polymers": [   {   'category': 'Polymer Chemistry',
        'common_traps': 'Nylon 6 is made from caprolactam alone, while Nylon 6,6 is made from two different 6-carbon '
                        'monomers.',
        'formula_cues': [   '\\text{nylon 6,6}',
                            '\\text{caprolactam}',
                            '\\text{adipic acid}',
                            '\\text{hexamethylenediamine}'],
        'name': 'Classification of Polymers & Monomer Units',
        'primary': [   'polymer',
                       'monomer',
                       'nylon',
                       'nylon 6,6',
                       'nylon 6',
                       'terylene',
                       'dacron',
                       'bakelite',
                       'melamine',
                       'neoprene',
                       'buna-s',
                       'buna-n',
                       'adipic acid',
                       'hexamethylenediamine',
                       'caprolactam',
                       'terephthalic acid'],
        'secondary': ['synthetic', 'addition', 'condensation'],
        'standard_formulas': '\\text{Nylon 6,6: } n\\text{HOOC(CH}_2)_4\\text{COOH} + '
                             'n\\text{H}_2\\text{N(CH}_2)_6\\text{NH}_2 \\to '
                             '\\text{[-CO(CH}_2)_4\\text{CONH(CH}_2)_6\\text{NH-]}_n + 2n\\text{H}_2\\text{O}',
        'summary': 'Monomers of important polymers: Nylon 6,6 from adipic acid + hexamethylenediamine. Nylon 6 from '
                   'caprolactam. Terylene (Dacron) from ethylene glycol + terephthalic acid. Bakelite from phenol + '
                   'formaldehyde. Buna-S from 1,3-butadiene + styrene. Neoprene from chloroprene '
                   '(2-chloro-1,3-butadiene).',
        'tips_and_tricks': 'Thermoplastics soften on heating (polythene, PVC); thermosetting plastics undergo '
                           'irreversible cross-linking (Bakelite, melamine).'},
    {   'category': 'Applied Polymers',
        'common_traps': 'Natural rubber is the cis-isomer of 1,4-polyisoprene; the trans-isomer is Gutta-Percha.',
        'formula_cues': ['\\text{phbv}', '\\text{cis-1,4-polyisoprene}', '\\text{3-hydroxybutanoic acid}'],
        'name': 'Biodegradable Polymers & Vulcanization',
        'primary': [   'biodegradable polymer',
                       'phbv',
                       'nylon 2-nylon 6',
                       'vulcanization of rubber',
                       'sulphur cross links',
                       'natural rubber',
                       'isoprene',
                       'cis-1,4-polyisoprene',
                       'gutta-percha'],
        'secondary': ['rubber', 'sulphur', 'polymer'],
        'standard_formulas': '\\text{Natural Rubber: } [\\text{-CH}_2\\text{-C(CH}_3)\\text{=CH-CH}_2\\text{-}]_n '
                             '\\quad (\\text{cis-isomer})',
        'summary': 'Biodegradable polymers: PHBV from 3-hydroxybutanoic acid + 3-hydroxypentanoic acid; Nylon 2-nylon '
                   '6 from glycine + amino caproic acid. Natural rubber is cis-1,4-polyisoprene. Vulcanization '
                   'involves heating raw rubber with 5% sulphur to introduce cross-links.',
        'tips_and_tricks': 'PHBV is widely used in speciality packaging and controlled drug release.'}],

    "kcet-chemistry-in-everyday-life": [   {   'category': 'Pharmaceutical Chemistry',
        'common_traps': 'Phenol acts as an antiseptic at 0.2% concentration, but acts as a disinfectant at 1.0% '
                        'concentration!',
        'formula_cues': [   '\\text{aspirin}',
                            '\\text{paracetamol}',
                            '\\text{chloroxylenol + terpineol}',
                            '0.2\\% \\text{ phenol}'],
        'name': 'Therapeutic Drug Classes: Analgesics, Antibiotics & Antiseptics',
        'primary': [   'analgesic',
                       'narcotic',
                       'non-narcotic',
                       'aspirin',
                       'paracetamol',
                       'morphine',
                       'antibiotic',
                       'penicillin',
                       'bactericidal',
                       'bacteriostatic',
                       'antiseptic',
                       'disinfectant',
                       'dettol',
                       'chloroxylenol',
                       'bithionol',
                       'tincture of iodine'],
        'secondary': ['drug', 'used', 'action'],
        'standard_formulas': '\\text{Aspirin: 2-acetoxybenzoic acid}, \\quad \\text{Dettol: Chloroxylenol} + '
                             '\\alpha\\text{-Terpineol}',
        'summary': 'Analgesics relieve pain: non-narcotics (aspirin, paracetamol) inhibit prostaglandin synthesis; '
                   'narcotics (morphine, codeine) are habit-forming pain-relievers. Antiseptics: Dettol (chloroxylenol '
                   '+ terpineol), bithionol (added to soaps), tincture of iodine (2-3% iodine in alcohol-water). '
                   'Disinfectants: 1% phenol solution (0.2% phenol is antiseptic).',
        'tips_and_tricks': 'Bactericidal antibiotics kill bacteria (penicillin, ofloxacin); bacteriostatic antibiotics '
                           'inhibit bacterial growth (erythromycin, tetracycline).'},
    {   'category': 'Household Chemistry',
        'common_traps': 'Aspartame cannot be used in baking or cooked foods because it decomposes at elevated '
                        'temperatures.',
        'formula_cues': [   '\\text{aspartame}',
                            '\\text{sucralose}',
                            '\\text{c}_{16}\\text{h}_{33}\\text{n}^+(\\text{ch}_3)_3\\text{br}^-'],
        'name': 'Food Additives, Artificial Sweeteners & Detergents',
        'primary': [   'artificial sweetener',
                       'aspartame',
                       'saccharin',
                       'sucralose',
                       'alitame',
                       'food preservative',
                       'sodium benzoate',
                       'cationic detergent',
                       'anionic detergent',
                       'non-ionic detergent',
                       'cetyltrimethylammonium bromide'],
        'secondary': ['cleansing', 'sweetness', 'soap'],
        'standard_formulas': '\\text{Cationic: } [\\text{CH}_3(\\text{CH}_2)_{15}\\text{N(CH}_3)_3]^+\\text{Br}^-, '
                             '\\quad \\text{Anionic: } \\text{CH}_3(\\text{CH}_2)_{11}\\text{OSO}_3^-\\text{Na}^+',
        'summary': 'Artificial sweeteners: Aspartame (unstable at cooking temperatures), Saccharin (550x sweeter), '
                   'Sucralose (stable at cooking temperatures), Alitame (high potency, 2000x sweeter). Detergents: '
                   'Anionic (sodium lauryl sulphate), Cationic (cetyltrimethylammonium bromide, germicidal), Non-ionic '
                   '(polyethylene glycol stearate).',
        'tips_and_tricks': 'Cationic detergents have germicidal properties and are used in hair conditioners and '
                           'hospital sanitation.'}],

}
