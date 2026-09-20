"""
Curated Concept Taxonomy for all Chemistry Chapters in JEE Main and KCET.
Covers Physical, Inorganic, and Organic Chemistry with standard formulas, reaction traps, and insights.
"""

CHEMISTRY_TAXONOMY = {
    "some-basic-concepts-of-chemistry": [
        {
            "name": "Mole Concept & Stoichiometry",
            "category": "Stoichiometry",
            "primary": ["mole concept", "avogadro", "molar mass", "stoichiometry", "limiting reagent", "percentage yield", "combustion of hydrocarbon", "empirical formula"],
            "formula_cues": [r"n = \frac{w}{M}", r"N_A \approx 6.022 \times 10^{23}", r"\text{moles of gas} = \frac{V}{22.4}"],
            "standard_formulas": r"n = \frac{w}{M} = \frac{N}{N_A} = \frac{V_{\text{STP}}\text{ (L)}}{22.4}, \quad \text{Combustion: } \text{C}_x\text{H}_y + \left(x + \frac{y}{4}\right)\text{O}_2 \to x\text{CO}_2 + \frac{y}{2}\text{H}_2\text{O}",
            "summary": "Mole relationships, mass-volume stoichiometry, empirical vs molecular formulas, and limiting reagent identification.",
            "common_traps": "Always balance the chemical reaction before calculating limiting reagent moles/stoichiometric coefficient ratios.",
            "tips_and_tricks": r"The reactant with the SMALLEST ratio of $\frac{\text{Initial Moles}}{\text{Stoichiometric Coefficient}}$ is the limiting reagent."
        },
        {
            "name": "Concentration Terms (Molarity, Molality, Mole Fraction)",
            "category": "Concentration",
            "primary": ["molarity", "molality", "mole fraction", "ppm", "normality", "dilution", "mass percentage", "volume percentage"],
            "formula_cues": [r"M = \frac{n_{\text{solute}}}{V_{\text{soln}}\text{ (L)}}", r"m = \frac{n_{\text{solute}}}{W_{\text{solvent}}\text{ (kg)}}", r"M_1 V_1 = M_2 V_2", r"x_A + x_B = 1"],
            "standard_formulas": r"M = \frac{w_B \times 1000}{M_B \times V\text{ (mL)}}, \quad m = \frac{w_B \times 1000}{M_B \times W_A\text{ (g)}}, \quad x_B = \frac{n_B}{n_A + n_B}, \quad \text{ppm} = \frac{w_B}{w_{\text{soln}}} \times 10^6",
            "summary": "Formulas for solution concentrations, temperature dependence, and dilution relation $M_1 V_1 = M_2 V_2$.",
            "common_traps": "Molarity ($M$) and Normality ($N$) change with temperature (due to volume expansion), while Molality ($m$) and Mole Fraction ($x$) are temperature INDEPENDENT.",
            "tips_and_tricks": r"Direct conversion formula: $m = \frac{1000 M}{1000 d - M M_B}$, where $d$ is solution density in $\text{g/mL}$."
        }
    ],

    "structure-of-atom": [
        {
            "name": "Bohr's Orbitals & Electronic Transitions",
            "category": "Bohr Model",
            "primary": ["bohr radius", "energy level", "rydberg constant", "wavelength of transition", "spectral lines", "ionization enthalpy of hydrogen", "de-excitation"],
            "formula_cues": [r"r_n = 0.529 \frac{n^2}{Z}", r"E_n = -13.6 \frac{Z^2}{n^2}", r"\bar{\nu} = R Z^2(\frac{1}{n_1^2} - \frac{1}{n_2^2})"],
            "standard_formulas": r"r_n = 0.529 \frac{n^2}{Z}\text{ \AA}, \quad E_n = -13.6 \frac{Z^2}{n^2}\text{ eV}, \quad \bar{\nu} = \frac{1}{\lambda} = R_H Z^2\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)",
            "summary": r"Electronic energy levels in hydrogenic species, wave number $\bar{\nu}$, and emission spectral series.",
            "common_traps": r"Rydberg formula requires multiplication by $Z^2$ for single-electron ions like $\text{He}^+$ ($Z=2$) and $\text{Li}^{2+}$ ($Z=3$).",
            "tips_and_tricks": r"Limiting line (series limit) of any spectral series occurs when $n_2 = \infty \implies \bar{\nu}_{\text{limit}} = \frac{R Z^2}{n_1^2}$."
        },
        {
            "name": "Quantum Numbers & Electronic Configuration",
            "category": "Quantum Numbers",
            "primary": ["quantum numbers", "principal quantum number", "azimuthal", "magnetic quantum number", "spin quantum number", "radial nodes", "angular nodes", "pauli exclusion", "hund's rule", "aufbau"],
            "formula_cues": [r"n - l - 1", r"l", r"2(2l + 1)", r"\sqrt{s(s+1)}"],
            "standard_formulas": r"\text{Radial nodes} = n - l - 1, \quad \text{Angular nodes} = l, \quad \text{Total nodes} = n - 1, \quad \mu_s = \sqrt{n(n+2)}\text{ BM}",
            "summary": r"Orbital shapes, quantum numbers $(n, l, m_l, m_s)$, nodal surfaces, and anomalous configurations ($\text{Cr}: 3d^5 4s^1, \text{Cu}: 3d^{10} 4s^1$).",
            "common_traps": r"Spin-only magnetic moment $\mu = \sqrt{n(n+2)}\text{ BM}$ depends on $n$, which is the number of UNPAIRED electrons, not total electrons!",
            "tips_and_tricks": "Degeneracy of hydrogen atom at energy level $n$ is $n^2$ (without spin) or $2n^2$ (including spin)."
        },
        {
            "name": "Heisenberg Uncertainty & De Broglie Wavelength",
            "category": "Wave Mechanics",
            "primary": ["heisenberg", "uncertainty principle", "de broglie", "matter wave", "simultaneous determination", "position and momentum"],
            "formula_cues": [r"\Delta x \cdot \Delta p \ge \frac{h}{4\pi}", r"\Delta x \cdot \Delta v \ge \frac{h}{4\pi m}", r"\lambda = \frac{h}{mv}"],
            "standard_formulas": r"\Delta x \cdot \Delta p \ge \frac{h}{4\pi} = \frac{\hbar}{2}, \quad \Delta x \cdot m\Delta v \ge \frac{h}{4\pi}, \quad \lambda = \frac{h}{p} = \frac{h}{\sqrt{2mE}}",
            "summary": "Limits of simultaneous precision in position and momentum, and dual wave nature of micro-particles.",
            "common_traps": r"If uncertainty in position and momentum are equal ($\Delta x = \Delta p$), then $\Delta v = \frac{1}{2m}\sqrt{\frac{h}{\pi}}$.",
            "tips_and_tricks": r"De Broglie wavelength of an electron accelerated through potential $V$ volts: $\lambda \approx \frac{12.27}{\sqrt{V}}\text{ \AA}$."
        }
    ],

    "periodic-table-and-periodicity": [
        {
            "name": "Ionization Enthalpy & Electron Gain Enthalpy",
            "category": "Periodic Trends",
            "primary": ["ionization enthalpy", "ionization energy", "successive ionization", "electron gain enthalpy", "electron affinity", "electronegativity", "effective nuclear charge", "shielding effect"],
            "formula_cues": [r"IE_1 < IE_2 < IE_3", r"\Delta_{eg}H", r"Z_{\text{eff}} = Z - \sigma"],
            "standard_formulas": r"Z_{\text{eff}} = Z - \sigma, \quad \Delta_{\text{eg}}H(\text{Cl}) < \Delta_{\text{eg}}H(\text{F}) \text{ (Cl is most negative in periodic table)}",
            "summary": r"Periodic variations of ionization energy, exceptions due to half-filled/fully-filled subshells ($\text{N} > \text{O}, \text{Be} > \text{B}$), and electron gain enthalpy.",
            "common_traps": r"Ionization enthalpy of Nitrogen is HIGHER than Oxygen due to stable half-filled $2p^3$ subshell ($\text{N}: 2s^2 2p^3 > \text{O}: 2s^2 2p^4$).",
            "tips_and_tricks": "Chlorine has MORE negative electron gain enthalpy than Fluorine because of compact size and high inter-electronic repulsion in $2p$ of Fluorine."
        },
        {
            "name": "Atomic & Ionic Radii Trends",
            "category": "Radii",
            "primary": ["atomic radius", "ionic radius", "isoelectronic species", "lanthanoid contraction", "screening effect", "slater rule"],
            "formula_cues": [r"r \propto \frac{1}{Z}", r"\text{radius of isoelectronic}"],
            "standard_formulas": r"\text{For isoelectronic: } r \propto \frac{1}{Z} \implies \text{N}^{3-} > \text{O}^{2-} > \text{F}^- > \text{Na}^+ > \text{Mg}^{2+} > \text{Al}^{3+}",
            "summary": "Covalent, van der Waals, and ionic radii trends across periods and groups, and size shrinkage in isoelectronic ions.",
            "common_traps": "Noble gas radii are measured as van der Waals radii, making them appear abnormally larger than adjacent halogens.",
            "tips_and_tricks": r"Due to lanthanoid contraction (poor shielding of $4f$ electrons), $4d$ and $5d$ transition elements have nearly identical radii (e.g. $\text{Zr} \approx \text{Hf}$). "
        }
    ],

    "chemical-bonding-and-molecular-structure": [
        {
            "name": "VSEPR Theory & Molecular Geometry",
            "category": "Molecular Shape",
            "primary": ["vsepr", "molecular geometry", "shape of molecule", "lone pair", "bond pair", "bent", "trigonal bipyramidal", "see-saw", "t-shaped", "octahedral", "square planar"],
            "formula_cues": [r"\text{Steric Number} = \frac{V + M - C + A}{2}", r"sp^3d", r"sp^3d^2"],
            "standard_formulas": r"\text{Steric Number } H = \frac{1}{2}(V + M - C + A), \quad \text{LP-LP repulsion} > \text{LP-BP} > \text{BP-BP}",
            "summary": "Prediction of molecular shapes and bond angles using steric number and lone pair repulsions.",
            "common_traps": r"$\text{XeF}_4$ has $sp^3d^2$ hybridization with 2 lone pairs; its geometry is octahedral, but its molecular SHAPE is SQUARE PLANAR.",
            "tips_and_tricks": r"In trigonal bipyramidal geometry ($sp^3d$, e.g. $\text{PCl}_5$), lone pairs ALWAYS occupy equatorial positions to minimize $90^\circ$ repulsions."
        },
        {
            "name": "Molecular Orbital Theory (MOT) & Bond Order",
            "category": "MOT",
            "primary": ["molecular orbital", "bond order", "paramagnetic", "diamagnetic", "homonuclear diatomic", "magnetic property", "bmo", "abmo", "n2", "o2"],
            "formula_cues": [r"\text{Bond Order} = \frac{N_b - N_a}{2}", r"\sigma 1s", r"\pi 2p_x", r"\pi^* 2p_x"],
            "standard_formulas": r"\text{Bond Order} = \frac{N_b - N_a}{2}, \quad \text{Stability} \propto \text{Bond Order} \propto \frac{1}{\text{Bond Length}}",
            "summary": r"LCAO principle, molecular orbital filling order for $\le 14$ vs $> 14$ electrons, bond order calculation, and magnetic character.",
            "common_traps": r"$\text{O}_2$ has bond order 2 and is PARAMAGNETIC because it has 2 unpaired electrons in degenerate antibonding $\pi^* 2p_x$ and $\pi^* 2p_y$ orbitals.",
            "tips_and_tricks": r"For species with $\le 14$ electrons ($\text{B}_2, \text{C}_2, \text{N}_2$): $\pi 2p_x = \pi 2p_y$ is filled BEFORE $\sigma 2p_z$ due to $s-p$ mixing."
        },
        {
            "name": "Dipole Moment, Formal Charge & Hydrogen Bonding",
            "category": "Intermolecular",
            "primary": ["dipole moment", "polar", "non-polar", "formal charge", "hydrogen bond", "intramolecular", "intermolecular", "boiling point"],
            "formula_cues": [r"\mu = q \times d", r"\mu_{\text{net}} = \sqrt{\mu_1^2 + \mu_2^2 + 2\mu_1\mu_2\cos\theta}"],
            "standard_formulas": r"\mu = q \times d, \quad \text{Formal Charge} = V - L - \frac{1}{2}S, \quad \mu(\text{NH}_3) > \mu(\text{NF}_3)",
            "summary": "Vector addition of bond dipoles, percentage ionic character, and influence of H-bonding on boiling points.",
            "common_traps": r"Dipole moment of $\text{NH}_3$ is HIGHER than $\text{NF}_3$ because lone pair and $\text{N-H}$ bond moments reinforce each other in $\text{NH}_3$, but oppose in $\text{NF}_3$.",
            "tips_and_tricks": "Intermolecular H-bonding increases boiling point and water solubility (e.g. p-nitrophenol), while intramolecular H-bonding decreases boiling point (o-nitrophenol)."
        }
    ],

    "solutions": [
        {
            "name": "Raoult's Law & Vapor Pressure (Ideal & Non-ideal)",
            "category": "Vapor Pressure",
            "primary": ["raoult", "vapor pressure", "ideal solution", "positive deviation", "negative deviation", "azeotrope", "henry's law", "henry constant"],
            "formula_cues": [r"P = P_A^\circ x_A + P_B^\circ x_B", r"P = K_H \cdot x", r"\Delta V_{\text{mix}}", r"\Delta H_{\text{mix}}"],
            "standard_formulas": r"P_{\text{total}} = P_A^\circ x_A + P_B^\circ x_B, \quad y_A = \frac{P_A}{P_{\text{total}}} = \frac{P_A^\circ x_A}{P_{\text{total}}}, \quad P = K_H \cdot x \text{ (Henry)}",
            "summary": r"Partial pressures of volatile mixtures, Dalton's law in vapor phase ($y_A$), and thermodynamic criteria for deviations ($\Delta H_{\text{mix}}, \Delta V_{\text{mix}}$).",
            "common_traps": r"Mixture of Chloroform and Acetone exhibits NEGATIVE deviation from Raoult's law ($\Delta H_{\text{mix}} < 0, \Delta V_{\text{mix}} < 0$) due to intermolecular hydrogen bonding.",
            "tips_and_tricks": "Higher Henry's law constant $K_H$ at a given pressure signifies LOWER solubility of the gas in liquid."
        },
        {
            "name": "Colligative Properties & Van 't Hoff Factor",
            "category": "Colligative",
            "primary": ["colligative", "relative lowering of vapor pressure", "elevation in boiling point", "depression in freezing point", "osmotic pressure", "van 't hoff", "degree of association", "degree of dissociation"],
            "formula_cues": [r"\frac{P^\circ - P}{P^\circ} = i \cdot x_B", r"\Delta T_b = i K_b m", r"\Delta T_f = i K_f m", r"\Pi = i C R T", r"i = 1 + (n - 1)\alpha"],
            "standard_formulas": r"\frac{P^\circ - P}{P^\circ} = i \cdot x_B, \quad \Delta T_b = i K_b m, \quad \Delta T_f = i K_f m, \quad \Pi = i C R T, \quad i = 1 + (n - 1)\alpha",
            "summary": "Physical properties depending solely on solute particle count, cryoscopic/ebullioscopic constants, and Van 't Hoff factor $i$.",
            "common_traps": r"When determining relative boiling/freezing points of salt solutions, compare effective molality $i \times m$, NOT just nominal molality $m$!",
            "tips_and_tricks": r"For dimerization/association of $n$ molecules: $i = 1 - \left(1 - \frac{1}{n}\right)\alpha \implies i < 1$ (e.g. benzoic acid in benzene, $i \approx 0.5$)."
        }
    ],

    "chemical-kinetics": [
        {
            "name": "Rate Law, Order & Integrated Rate Equations",
            "category": "Rate Laws",
            "primary": ["rate of reaction", "rate law", "order of reaction", "zero order", "first order", "second order", "half life", "pseudo first order"],
            "formula_cues": [r"k = \frac{2.303}{t} \log\frac{[A]_0}{[A]}", r"t_{1/2} = \frac{0.693}{k}", r"t_{1/2} = \frac{[A]_0}{2k}", r"\text{units of } k = \text{mol}^{1-n}\text{L}^{n-1}\text{s}^{-1}"],
            "standard_formulas": r"\text{Zero: } [A] = [A]_0 - kt, \; t_{1/2} = \frac{[A]_0}{2k}, \quad \text{First: } k = \frac{2.303}{t}\log\frac{[A]_0}{[A]}, \; t_{1/2} = \frac{0.693}{k}",
            "summary": "Differential and integrated rate laws, half-life formulas, and overall reaction order determined from initial rates.",
            "common_traps": r"For a first-order reaction, half-life $t_{1/2} = \frac{0.693}{k}$ is strictly INDEPENDENT of initial concentration $[A]_0$.",
            "tips_and_tricks": r"For an $n^{\text{th}}$ order reaction: $t_{1/2} \propto \frac{1}{[A]_0^{n - 1}}$. Units of rate constant $k = \text{mol}^{1-n}\text{L}^{n-1}\text{s}^{-1}$."
        },
        {
            "name": "Arrhenius Equation & Activation Energy",
            "category": "Temperature & Catalysis",
            "primary": ["arrhenius", "activation energy", "catalyst", "collision theory", "frequency factor", "steric factor", "rate constant with temperature"],
            "formula_cues": [r"k = A e^{-E_a/RT}", r"\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}(\frac{1}{T_1} - \frac{1}{T_2})", r"\text{slope} = -\frac{E_a}{2.303R}"],
            "standard_formulas": r"k = A e^{-E_a/RT}, \quad \ln k = \ln A - \frac{E_a}{RT}, \quad \log_{10}\left(\frac{k_2}{k_1}\right) = \frac{E_a}{2.303R}\left(\frac{T_2 - T_1}{T_1 T_2}\right)",
            "summary": r"Temperature dependence of reaction rates, activation energy $E_a$, Arrhenius plot ($\ln k$ vs $1/T$), and catalyst energy profiles.",
            "common_traps": r"A positive catalyst increases rate by LOWERING activation energy $E_a$; it does NOT alter the equilibrium constant $K_{\text{eq}}$ or $\Delta H$!",
            "tips_and_tricks": r"Plot of $\log_{10} k$ vs $\frac{1}{T}$ gives a straight line with slope $= -\frac{E_a}{2.303 R}$ and y-intercept $= \log_{10} A$."
        }
    ],

    "chemical-equilibrium": [
        {
            "name": "Equilibrium Constants (Kp, Kc) & Reaction Quotient",
            "category": "Equilibrium Constants",
            "primary": ["equilibrium constant", "kp", "kc", "reaction quotient", "degree of dissociation", "heterogeneous equilibrium", "extent of reaction"],
            "formula_cues": [r"K_p = K_c(RT)^{\Delta n_g}", r"Q_c < K_c", r"\Delta n_g = \Sigma n_p - \Sigma n_r"],
            "standard_formulas": r"K_p = K_c(RT)^{\Delta n_g}, \quad \Delta G^\circ = -RT\ln K = -2.303RT\log_{10} K, \quad Q < K \implies \text{Forward}",
            "summary": "Relationship between $K_p$ and $K_c$, expression of equilibrium constants, and spontaneous direction based on $Q$ vs $K$.",
            "common_traps": r"In calculating $\Delta n_g$, count ONLY gaseous species: $\Delta n_g = \Sigma n_{\text{gas}}(\text{products}) - \Sigma n_{\text{gas}}(\text{reactants})$. Pure solids and liquids are excluded ($a = 1$).",
            "tips_and_tricks": "If a reaction is multiplied by factor $n$, its new equilibrium constant becomes $K' = K^n$. If reversed, $K' = 1/K$."
        },
        {
            "name": "Le Chatelier's Principle & Stress Factors",
            "category": "Le Chatelier",
            "primary": ["le chatelier", "shift equilibrium", "effect of pressure", "effect of temperature", "addition of inert gas", "constant volume", "constant pressure"],
            "formula_cues": [r"\Delta H > 0", r"\Delta H < 0", r"\Delta n_g > 0"],
            "standard_formulas": r"\ln\left(\frac{K_2}{K_1}\right) = \frac{\Delta H^\circ}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) \text{ (van 't Hoff)}",
            "summary": "Dynamic response of equilibrium systems to variations in concentration, temperature, pressure, and inert gas addition.",
            "common_traps": "Addition of an inert gas at CONSTANT VOLUME has NO effect on equilibrium position because partial pressures remain unchanged!",
            "tips_and_tricks": r"Inert gas addition at CONSTANT PRESSURE shifts equilibrium toward the side with MORE gaseous moles ($\Delta n_g > 0$ shifts forward)."
        }
    ],

    "ionic-equilibrium": [
        {
            "name": "pH Calculation of Acids, Bases & Salts",
            "category": "pH & Hydrolysis",
            "primary": ["ph", "poh", "salt hydrolysis", "strong acid", "weak acid", "weak base", "acidic buffer", "basic buffer", "henderson hasselbalch"],
            "formula_cues": [r"\text{pH} = -\log[H^+]", r"\text{pH} = \text{pK}_a + \log\frac{[\text{salt}]}{[\text{acid}]}", r"\text{pH} = 7 + \frac{1}{2}\text{pK}_a - \frac{1}{2}\text{pK}_b"],
            "standard_formulas": r"\text{pH} = \text{p}K_a + \log\frac{[\text{conjugate base}]}{[\text{acid}]}, \quad \text{Salt of WA-SB: } \text{pH} = 7 + \frac{1}{2}\text{p}K_a + \frac{1}{2}\log c",
            "summary": r"Self-ionization of water ($K_w = 10^{-14}$ at $25^\circ\text{C}$), Ostwald dilution law, buffer solutions, and salt hydrolysis formulas.",
            "common_traps": r"pH of $10^{-8}\text{ M HCl}$ is NOT 8 (cannot be basic!); including water's auto-ionization $[H^+] = 10^{-8} + 10^{-7} \implies \text{pH} \approx 6.79$.",
            "tips_and_tricks": r"Buffer capacity is maximum when $[\text{salt}] = [\text{acid}] \implies \text{pH} = \text{p}K_a$."
        },
        {
            "name": "Solubility Product (Ksp) & Common Ion Effect",
            "category": "Solubility",
            "primary": ["solubility product", "ksp", "common ion", "precipitation", "sparingly soluble", "ionic product", "selective precipitation"],
            "formula_cues": [r"K_{sp} = s^2", r"K_{sp} = 4s^3", r"K_{sp} = 27s^4", r"Q_{sp} > K_{sp}"],
            "standard_formulas": r"A_x B_y \rightleftharpoons x A^{y+} + y B^{x-} \implies K_{sp} = x^x y^y s^{x+y}, \quad Q_{sp} > K_{sp} \implies \text{Precipitation occurs}",
            "summary": "Calculation of molar solubility $s$ from $K_{sp}$, ionic product comparison, and suppression of solubility via common ion effect.",
            "common_traps": r"For $\text{Ag}_2\text{CrO}_4$ ($A_2B$ type): $K_{sp} = (2s)^2(s) = 4s^3 \implies s = \sqrt[3]{K_{sp}/4}$, NOT $s^2$!",
            "tips_and_tricks": r"Common ion effect ALWAYS suppresses the solubility of a sparingly soluble salt (e.g. $\text{AgCl}$ is less soluble in $\text{NaCl}$ than pure water)."
        }
    ],

    "thermodynamics": [
        {
            "name": "Enthalpy, Hess's Law & Bond Energies",
            "category": "Thermochemistry",
            "primary": ["enthalpy", "hess's law", "heat of formation", "heat of combustion", "bond enthalpy", "bond dissociation", "standard enthalpy of reaction"],
            "formula_cues": [r"\Delta H = \Sigma \Delta_f H(\text{prod}) - \Sigma \Delta_f H(\text{react})", r"\Delta H = \Sigma BE(\text{react}) - \Sigma BE(\text{prod})"],
            "standard_formulas": r"\Delta H = \Delta U + \Delta n_g RT, \quad \Delta_r H^\circ = \Sigma \Delta_f H^\circ(\text{products}) - \Sigma \Delta_f H^\circ(\text{reactants})",
            "summary": "State functions, standard enthalpy of formation, Hess's law of constant heat summation, and bond energy calculations.",
            "common_traps": r"Standard enthalpy of formation $\Delta_f H^\circ$ of pure elements in their standard reference state is strictly ZERO (e.g. $\text{O}_{2(g)}, \text{C}_{\text{graphite}}$).",
            "tips_and_tricks": r"When using bond enthalpies: $\Delta H_{\text{reaction}} = \Sigma \text{BE}(\text{bonds broken in reactants}) - \Sigma \text{BE}(\text{bonds formed in products})$."
        },
        {
            "name": "Entropy & Gibbs Free Energy Spontaneity",
            "category": "Spontaneity",
            "primary": ["entropy", "gibbs free energy", "spontaneity", "delta g", "delta s", "second law", "third law", "reversible process"],
            "formula_cues": [r"\Delta G = \Delta H - T\Delta S", r"\Delta S = \frac{q_{\text{rev}}}{T}", r"\Delta G < 0"],
            "standard_formulas": r"\Delta G = \Delta H - T\Delta S, \quad \Delta S_{\text{univ}} = \Delta S_{\text{sys}} + \Delta S_{\text{surr}} > 0, \quad \Delta G^\circ = -RT\ln K",
            "summary": "Second and third laws of thermodynamics, entropy changes in phase transitions, and Gibbs criteria for spontaneous change.",
            "common_traps": r"For an endothermic reaction ($\Delta H > 0$) with $\Delta S > 0$, the reaction is spontaneous ONLY at HIGH temperatures where $T > \frac{\Delta H}{\Delta S}$.",
            "tips_and_tricks": r"At equilibrium: $\Delta G = 0 \implies T_{\text{equilibrium}} = \frac{\Delta H}{\Delta S}$."
        }
    ],

    "coordination-compounds": [
        {
            "name": "IUPAC Nomenclature & Werner's Coordination Theory",
            "category": "Coordination Basics",
            "primary": ["coordination compound", "iupac name", "werner theory", "primary valency", "secondary valency", "ligand", "denticity", "chelate", "coordination number"],
            "formula_cues": [r"[\text{Co}(\text{NH}_3)_6]\text{Cl}_3", r"\text{Primary valency} = \text{Oxidation state}", r"\text{Secondary valency} = \text{CN}"],
            "standard_formulas": r"\text{Primary valency (ionizable, satisfies charge)}, \quad \text{Secondary valency (non-ionizable, directional, satisfies CN)}",
            "summary": "Formulation of complexes, Werner's postulates, precipitable silver chloride fractions, and systematic IUPAC naming conventions.",
            "common_traps": r"In $[\text{Co}(\text{NH}_3)_5\text{Cl}]\text{Cl}_2$, adding excess $\text{AgNO}_3$ precipitates ONLY 2 moles of $\text{AgCl}$ per mole of complex, because one $\text{Cl}^-$ is coordinated.",
            "tips_and_tricks": "Chelating ligands (e.g. en, EDTA) form 5- or 6-membered rings with the central metal ion, imparting exceptional thermodynamic stability (chelate effect)."
        },
        {
            "name": "Crystal Field Theory (CFT) & Isomerism",
            "category": "CFT & Isomerism",
            "primary": ["crystal field", "cft", "crystal field splitting", "spectrochemical series", "strong field ligand", "weak field ligand", "pairing energy", "octahedral", "tetrahedral", "geometrical isomerism", "optical isomerism", "cis trans"],
            "formula_cues": [r"\Delta_o", r"\Delta_t = \frac{4}{9}\Delta_o", r"t_{2g}", r"e_g", r"\text{CFSE} = (-0.4x + 0.6y)\Delta_o"],
            "standard_formulas": r"\Delta_t = \frac{4}{9}\Delta_o, \quad \text{CFSE}_{\text{oct}} = [-0.4 n(t_{2g}) + 0.6 n(e_g)]\Delta_o + n P, \quad \mu = \sqrt{n(n+2)}\text{ BM}",
            "summary": "d-orbital splitting under octahedral and tetrahedral fields, high-spin vs low-spin complexes, spectrochemical series, and optical/geometrical isomerism.",
            "common_traps": r"Tetrahedral complexes NEVER form low-spin complexes because $\Delta_t = \frac{4}{9}\Delta_o < P$ (splitting is always less than pairing energy).",
            "tips_and_tricks": r"$\text{cis-}[\text{Co}(\text{en})_2\text{Cl}_2]^+$ is optically ACTIVE (non-superimposable mirror image), whereas the $\text{trans}$ isomer has a plane of symmetry and is optically INACTIVE."
        }
    ],

    "haloalkanes-and-haloarenes": [
        {
            "name": "SN1 and SN2 Nucleophilic Substitution",
            "category": "Reaction Mechanisms",
            "primary": ["sn1", "sn2", "nucleophilic substitution", "carbocation intermediate", "inversion of configuration", "walden inversion", "racemization", "leaving group", "polar protic", "polar aprotic"],
            "formula_cues": [r"\text{Rate} = k[\text{RX}]", r"\text{Rate} = k[\text{RX}][\text{Nu}^-]", r"3^\circ > 2^\circ > 1^\circ", r"1^\circ > 2^\circ > 3^\circ"],
            "standard_formulas": r"\text{SN1: Rate} \propto [\text{RX}] \; (3^\circ > 2^\circ > 1^\circ, \text{Racemization}), \quad \text{SN2: Rate} \propto [\text{RX}][\text{Nu}] \; (1^\circ > 2^\circ > 3^\circ, \text{Inversion})",
            "summary": "Kinetics, stereochemical outcomes, carbocation rearrangements in SN1, and concerted backside displacement in SN2.",
            "common_traps": r"Polar PROTIC solvents (e.g. $\text{H}_2\text{O}, \text{ROH}$) stabilize carbocations and favor SN1. Polar APROTIC solvents (e.g. acetone, DMSO) favor SN2 by desolvating nucleophiles.",
            "tips_and_tricks": "Allylic and benzylic halides undergo BOTH SN1 (resonance-stabilized carbocation) and SN2 (low steric hindrance) at remarkably high rates."
        },
        {
            "name": "Elimination (E1/E2, Saytzeff vs Hofmann) & Haloarene Reactions",
            "category": "Elimination & Aromatic",
            "primary": ["elimination", "dehydrohalogenation", "saytzeff", "zaitsev", "hofmann", "alcoholic koh", "wurtz", "fittig", "dow process", "electrophilic aromatic substitution of chlorobenzene"],
            "formula_cues": [r"\text{alc. KOH}", r"\text{major alkene}", r"\text{Saytzeff product}"],
            "standard_formulas": r"\text{Saytzeff Rule: Highly substituted, more stable alkene is the major product in dehydrohalogenation}",
            "summary": r"$\beta$-elimination mechanism, Saytzeff vs Hofmann regioselectivity, and unreactivity of haloarenes toward nucleophilic substitution.",
            "common_traps": r"Haloarenes (like chlorobenzene) are extremely UNREACTIVE toward nucleophilic substitution due to partial double bond character ($\text{C-Cl}$ resonance) and $sp^2$ carbon.",
            "tips_and_tricks": r"Presence of electron-withdrawing groups (like $-\text{NO}_2$) at ortho- and para-positions dramatically increases reactivity of haloarenes toward nucleophilic substitution."
        }
    ],

    "alcohols-phenols-and-ethers": [
        {
            "name": "Acidity of Phenols & Distinguishing Tests",
            "category": "Phenols",
            "primary": ["acidity of phenol", "picric acid", "resonance stabilization of phenoxide", "lucas reagent", "lucas test", "neutral fecl3", "kolbe", "reimer tiemann", "salicylic acid", "salicylaldehyde"],
            "formula_cues": [r"\text{Lucas: } \text{conc. HCl} + \text{anh. ZnCl}_2", r"\text{Reimer-Tiemann: } \text{CHCl}_3 + \text{NaOH}", r"\text{Kolbe: } \text{CO}_2 + \text{NaOH}"],
            "standard_formulas": r"\text{Acidity: Picric acid} > \text{p-Nitrophenol} > \text{Phenol} > \text{Water} > \text{Ethanol}, \quad \text{Lucas: } 3^\circ \text{ (turbidity immediately)}, 2^\circ \text{ (5 mins)}, 1^\circ \text{ (no turbidity)}",
            "summary": "Phenoxide resonance stabilization, substituent effects on acidity, Reimer-Tiemann and Kolbe-Schmitt reactions, and Lucas test.",
            "common_traps": r"Electron withdrawing groups ($-\text{NO}_2, -\text{CN}$) INCREASE phenol acidity (especially at ortho and para positions), while electron donating groups ($-\text{CH}_3$) decrease acidity.",
            "tips_and_tricks": r"Reimer-Tiemann reaction involves dichlorocarbene ($:\text{CCl}_2$) as an electrophilic intermediate to convert phenol to salicylaldehyde."
        },
        {
            "name": "Williamson Ether Synthesis & Cleavage by HI",
            "category": "Ethers",
            "primary": ["williamson", "ether synthesis", "cleavage of ether", "reaction with hi", "excess hi", "anisole", "oxonium ion"],
            "formula_cues": [r"\text{R-O-R'} + \text{HI} \to \text{R-I} + \text{R'-OH}", r"\text{R-ONa} + \text{R'-X} \to \text{R-O-R'}"],
            "standard_formulas": r"\text{Williamson: } \text{R-O}^- \text{Na}^+ + \text{R'-X (must be } 1^\circ) \to \text{R-O-R'} + \text{NaX}",
            "summary": r"Alkoxide SN2 displacement on primary halides, and ether cleavage mechanism with concentrated $\text{HI}$.",
            "common_traps": r"In Williamson synthesis, the alkyl halide MUST be primary ($1^\circ$). If a tertiary ($3^\circ$) halide is used, elimination dominates to give an ALKENE instead of an ether!",
            "tips_and_tricks": r"With unsymmetrical ethers + $\text{HI}$: If one alkyl group is tertiary ($3^\circ$), the iodide attaches to the $3^\circ$ carbon (via SN1). If both are $1^\circ$ or $2^\circ$, iodide attacks the less hindered carbon (via SN2)."
        }
    ],

    "aldehydes-ketones-and-carboxylic-acids": [
        {
            "name": "Nucleophilic Addition & Carbonyl Condensation",
            "category": "Carbonyl Reactions",
            "primary": ["nucleophilic addition", "aldol condensation", "cannizzaro", "cross aldol", "grignard reagent", "hemiacetal", "acetal", "cyanohydrin", "sodium bisulphite"],
            "formula_cues": [r"\text{Aldol: Dilute NaOH, } \beta\text{-hydroxy aldehyde}", r"\text{Cannizzaro: Conc. NaOH, no } \alpha\text{-H}", r"\text{C}=\text{O} + \text{HCN} \to \text{Cyanohydrin}"],
            "standard_formulas": r"\text{Aldol: Requires } \alpha\text{-H} \to \alpha,\beta\text{-unsaturated carbonyl}, \quad \text{Cannizzaro: No } \alpha\text{-H} \to \text{Alcohol} + \text{Carboxylate salt}",
            "summary": "Reversible nucleophilic additions, Aldol condensation mechanism, and Cannizzaro disproportionation of non-enolizable aldehydes.",
            "common_traps": r"Benzaldehyde and Formaldehyde lack $\alpha$-hydrogen atoms, so they undergo CANNIZZARO reaction with concentrated $\text{NaOH}$, NOT Aldol condensation!",
            "tips_and_tricks": r"Reactivity toward nucleophilic addition: $\text{HCHO} > \text{CH}_3\text{CHO} > \text{CH}_3\text{COCH}_3$ (decreases with steric crowding and $+I$ electron donation)."
        },
        {
            "name": "Oxidation, Reduction & Identification Tests",
            "category": "Tests & Reductions",
            "primary": ["tollens", "fehling", "silver mirror", "haloform", "iodoform test", "clemmensen reduction", "wolff kishner", "rosenmund reduction", "etard reaction", "dnp test"],
            "formula_cues": [r"\text{Tollens: } [\text{Ag}(\text{NH}_3)_2]^+", r"\text{Iodoform: } \text{I}_2 + \text{NaOH} \to \text{CHI}_3 \downarrow \text{ (yellow)}", r"\text{Clemmensen: } \text{Zn-Hg} / \text{HCl}"],
            "standard_formulas": r"\text{Iodoform test is positive for } \text{CH}_3\text{CO-} \text{ or } \text{CH}_3\text{CH(OH)- groups} \implies \text{CHI}_3 \text{ (yellow ppt)}",
            "summary": r"Silver mirror Tollens' test, Fehling's cuprous reduction, yellow iodoform precipitation, Clemmensen ($\text{Zn-Hg/HCl}$), and Wolff-Kishner ($\text{NH}_2\text{NH}_2/\text{KOH}$) carbonyl deoxygenation.",
            "common_traps": "Benzaldehyde reduces Tollens' reagent to give silver mirror, but does NOT reduce Fehling's solution!",
            "tips_and_tricks": "Clemmensen reduction is suitable for acid-stable compounds. For acid-sensitive carbonyls, use Wolff-Kishner reduction (basic medium)."
        }
    ],

    "compounds-containing-nitrogen": [
        {
            "name": "Basicity of Amines & Gabriel Phthalimide Synthesis",
            "category": "Amine Basics",
            "primary": ["basicity of amines", "inductive effect", "solvation effect", "steric hindrance", "gabriel phthalimide", "hoffmann bromamide", "order of basicity", "aqueous medium"],
            "formula_cues": [r"\text{In water: } 2^\circ > 1^\circ > 3^\circ > \text{NH}_3 \text{ (for } -\text{CH}_3)", r"\text{In water: } 2^\circ > 3^\circ > 1^\circ > \text{NH}_3 \text{ (for } -\text{C}_2\text{H}_5)"],
            "standard_formulas": r"\text{Basicity in water: } (\text{CH}_3)_2\text{NH} > \text{CH}_3\text{NH}_2 > (\text{CH}_3)_3\text{N} > \text{NH}_3 \quad (2^\circ > 1^\circ > 3^\circ > \text{NH}_3)",
            "summary": "Interplay of inductive, steric, and solvation factors on amine basicity in gas vs aqueous phases, and Hoffmann bromamide degradation.",
            "common_traps": r"In gas phase, basicity order is purely inductive: $3^\circ > 2^\circ > 1^\circ > \text{NH}_3$. In aqueous solution, solvation and steric factors disrupt this order.",
            "tips_and_tricks": r"Gabriel phthalimide synthesis yields PURE aliphatic primary amines ($1^\circ$); aromatic amines cannot be prepared because aryl halides do not undergo SN2."
        },
        {
            "name": "Diazonium Salts & Carbylamine Test",
            "category": "Diazonium & Tests",
            "primary": ["diazonium", "sandmeyer", "gattermann", "carbylamine", "isocyanide test", "hinsberg reagent", "coupling reaction", "azo dye", "foul smelling"],
            "formula_cues": [r"\text{Ar-N}_2^+\text{Cl}^-", r"\text{Carbylamine: } \text{R-NH}_2 + \text{CHCl}_3 + \text{KOH} \to \text{R-NC} \text{ (foul smell)}", r"\text{Sandmeyer: } \text{Cu}_2\text{Cl}_2 / \text{HCl}"],
            "standard_formulas": r"\text{Diazotization: } \text{Ar-NH}_2 + \text{NaNO}_2 + 2\text{HCl} \xrightarrow{0-5^\circ\text{C}} \text{Ar-N}_2^+\text{Cl}^- + \text{NaCl} + 2\text{H}_2\text{O}",
            "summary": r"Preparation of benzene diazonium chloride ($0-5^\circ\text{C}$), Sandmeyer/Gattermann halogenation, azo coupling dyes, and Hinsberg separation.",
            "common_traps": r"Carbylamine test gives foul-smelling isocyanide ONLY with primary amines ($1^\circ$); secondary and tertiary amines give NO reaction.",
            "tips_and_tricks": r"Hinsberg reagent ($\text{C}_6\text{H}_5\text{SO}_2\text{Cl}$): $1^\circ$ amine gives product soluble in $\text{KOH}$; $2^\circ$ amine gives product insoluble in $\text{KOH}$; $3^\circ$ amine does not react."
        }
    ],

    "biomolecules": [
        {
            "name": "Carbohydrates (Glucose, Fructose & Glycosidic Linkage)",
            "category": "Carbohydrates",
            "primary": ["glucose", "fructose", "monosaccharide", "disaccharide", "sucrose", "maltose", "lactose", "glycosidic linkage", "reducing sugar", "inversion of cane sugar", "mutarotation"],
            "formula_cues": [r"\text{C}_6\text{H}_{12}\text{O}_6", r"\text{Sucrose: } \alpha\text{-D-glucose} + \beta\text{-D-fructose}", r"[\alpha]_D"],
            "standard_formulas": r"\text{Sucrose (non-reducing)} \xrightarrow{\text{hydrolysis}} \text{D-(+)-glucose} + \text{D-(-)-fructose} \quad \text{(Invert sugar, levorotatory)}",
            "summary": r"Structure of D-glucose and D-fructose, cyclic hemiacetals, anomeric carbons ($\alpha/\beta$), reducing vs non-reducing sugars, and invert sugar.",
            "common_traps": r"Sucrose is a NON-REDUCING sugar because both reducing groups (hemiacetal $-\text{OH}$ of glucose and hemiketal $-\text{OH}$ of fructose) are tied in glycosidic linkage.",
            "tips_and_tricks": r"Hydrolysis of dextrorotatory sucrose produces a levorotatory mixture because fructose has a larger specific rotation ($-92.4^\circ$) than glucose ($+52.5^\circ$)."
        },
        {
            "name": "Amino Acids, Peptide Bonds & Nucleic Acids",
            "category": "Proteins & DNA",
            "primary": ["amino acid", "zwitterion", "isoelectric point", "peptide bond", "primary structure", "secondary structure", "alpha helix", "beta pleated", "denaturation", "dna", "rna", "nucleotide", "purine", "pyrimidine"],
            "formula_cues": [r"\text{-CO-NH-}", r"\text{A-T (2 H-bonds)}", r"\text{G-C (3 H-bonds)}"],
            "standard_formulas": r"\text{Peptide linkage: } -\text{CO-NH}-, \quad \text{Zwitterion: } \text{H}_3\text{N}^+-\text{CHR}-\text{COO}^-, \quad \text{DNA: } \text{A}=\text{T}, \; \text{G}\equiv\text{C}",
            "summary": "Essential amino acids, zwitterionic dipolar character, protein denaturation, double-helix structure of DNA, and hydrogen-bonded base pairs.",
            "common_traps": "Denaturation destroys secondary, tertiary, and quaternary protein structures, but leaves the primary sequence (peptide bonds) INTACT.",
            "tips_and_tricks": r"All naturally occurring $\alpha$-amino acids are optically active EXCEPT Glycine ($\text{H}_2\text{N-CH}_2\text{-COOH}$), which is achiral."
        }
    ]
}
