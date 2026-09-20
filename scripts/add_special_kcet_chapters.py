"""
Adds the 16 special KCET chapters to kcet_physics, kcet_chemistry, and kcet_math.
"""

import sys
sys.path.insert(0, '.')

from app.analyzer.taxonomies.kcet_physics import KCET_PHYSICS_TAXONOMY
from app.analyzer.taxonomies.kcet_chemistry import KCET_CHEMISTRY_TAXONOMY
from app.analyzer.taxonomies.kcet_math import KCET_MATH_TAXONOMY
import app.analyzer.taxonomies.kcet_taxonomy as kcet_tax

# The 16 special chapters:
SPECIAL_PHYSICS = {
    "kcet-elasticity": [
        {
            "name": "Hooke's Law & Young's Modulus of Wires",
            "category": "Elastic Moduli",
            "primary": ["young's modulus", "youngs modulus", "wire", "elongation", "stretch", "diameter", "ratio of lengths", "ratio of diameters", "extension", "breaking stress"],
            "formula_cues": [r"\frac{fl}{a \delta l}", r"\frac{f l}{a \delta l}", r"\pi r^2", r"2 \times 10^{11}"],
            "secondary": ["stress", "strain", "tension", "length", "radius"],
            "summary": "Hooke's law in 1D: Longitudinal stress $\\sigma = \\frac{F}{A}$ and strain $\\epsilon = \\frac{\\Delta L}{L}$. Young's modulus $Y = \\frac{F L}{A \\Delta L} = \\frac{F L}{\\pi r^2 \\Delta L}$.",
            "standard_formulas": r"Y = \frac{F L}{A \Delta L} = \frac{M g L}{\pi r^2 \Delta L}, \quad \Delta L \propto \frac{L}{r^2} \propto \frac{L}{d^2}",
            "common_traps": "Ratio problems with diameter: remember $A \\propto d^2$, so $\\Delta L \\propto \\frac{L}{d^2}$. If diameter is doubled, elongation becomes 1/4!",
            "tips_and_tricks": "For two wires under equal tension: $\\frac{\\Delta L_1}{\\Delta L_2} = \\left(\\frac{L_1}{L_2}\\right) \\left(\\frac{d_2}{d_1}\\right)^2 \\left(\\frac{Y_2}{Y_1}\\right)$."
        },
        {
            "name": "Elastic Potential Energy & Wire Elongation Due to Weight",
            "category": "Energy & Special Cases",
            "primary": ["own weight", "density rho", "potential energy", "work done in stretching", "energy stored", "energy density", "poisson's ratio", "poissons ratio", "lateral strain"],
            "formula_cues": [r"\frac{1}{2} f \delta l", r"\frac{\rho g l^2}{2y}", r"\sigma = \frac{\text{lateral}}{\text{longitudinal}}", r"\sigma = 0.25"],
            "secondary": ["volume", "half", "work", "stored"],
            "summary": "Work done in stretching a wire $W = U = \\frac{1}{2} F \\Delta L = \\frac{1}{2} Y (\\text{strain})^2 \\times \\text{Volume}$. Elongation of a hanging wire under its own weight $\\Delta L = \\frac{\\rho g L^2}{2 Y}$. Poisson's ratio $\\sigma = -\\frac{\\Delta r / r}{\\Delta L / L}$.",
            "standard_formulas": r"U = \frac{1}{2} F \Delta L, \quad u = \frac{1}{2} \text{Stress} \times \text{Strain}, \quad \Delta L_{\text{self}} = \frac{\rho g L^2}{2 Y}, \quad \sigma = \frac{\Delta d / d}{\Delta L / L}",
            "common_traps": "Elongation due to own weight has factor 1/2 in denominator because effective center of gravity acts at L/2!",
            "tips_and_tricks": "Poisson's ratio theoretical limits: $-1 \\le \\sigma \\le 0.5$. For practical materials, $0 \\le \\sigma \\le 0.5$."
        }
    ],

    "kcet-fluid-mechanics": [
        {
            "name": "Hydrostatics, Pascal's Principle & Archimedes' Buoyancy",
            "category": "Fluid Statics",
            "primary": ["hydrostatic", "pascal", "hydraulic lift", "gauge pressure", "atmospheric pressure", "buoyant force", "upthrust", "apparent weight", "floating", "density of liquid"],
            "formula_cues": [r"p = \rho g h", r"\rho g h", r"f_1 / a_1 = f_2 / a_2", r"w_{\text{app}} = w - \rho v g"],
            "secondary": ["manometer", "depth", "density", "liquid"],
            "summary": "Fluid pressure variation with depth $P = P_0 + \\rho g h$. Pascal's law of pressure transmission in hydraulic machines: $\\frac{F_1}{A_1} = \\frac{F_2}{A_2}$. Archimedes' principle: buoyant upthrust $F_B = \\rho_{\\text{fluid}} V_{\\text{displaced}} g$.",
            "standard_formulas": r"P = P_0 + \rho g h, \quad \frac{F_1}{A_1} = \frac{F_2}{A_2}, \quad F_B = \rho_L V_{\text{sub}} g",
            "common_traps": "Total absolute pressure is $P = P_0 + \\rho g h$; gauge pressure is only $\\rho g h$. Watch whether the question asks for gauge or absolute pressure.",
            "tips_and_tricks": "Fraction of volume submerged for a floating body: $\\frac{V_{\\text{sub}}}{V_{\\text{total}}} = \\frac{\\rho_{\\text{body}}}{\\rho_{\\text{liquid}}}$."
        },
        {
            "name": "Continuity Equation & Bernoulli's Principle",
            "category": "Fluid Dynamics",
            "primary": ["streamline", "equation of continuity", "cross-sectional area", "bernoulli", "horizontal pipe", "speed of flow", "venturi", "carburetor", "torricelli", "velocity of efflux"],
            "formula_cues": [r"a_1 v_1 = a_2 v_2", r"p + \frac{1}{2}\rho v^2", r"\sqrt{2gh}", r"v = \sqrt{2gh}"],
            "secondary": ["velocity", "pipe", "pressure", "narrow"],
            "summary": "Conservation of mass for incompressible fluid: $A_1 v_1 = A_2 v_2$. Bernoulli's equation $P + \\frac{1}{2}\\rho v^2 + \\rho g h = \\text{constant}$. Torricelli's speed of efflux $v = \\sqrt{2gh}$. Carburetor / atomizer suction operates on Bernoulli's principle.",
            "standard_formulas": r"A_1 v_1 = A_2 v_2, \quad P_1 + \frac{1}{2}\rho v_1^2 = P_2 + \frac{1}{2}\rho v_2^2, \quad v_{\text{efflux}} = \sqrt{2gh}",
            "common_traps": "Where fluid velocity is highest (narrow section), static pressure is lowest, NOT highest!",
            "tips_and_tricks": "In horizontal pipes, $\\Delta P = \\frac{1}{2}\\rho (v_2^2 - v_1^2)$. If radius is halved, area is 1/4, velocity is 4x."
        },
        {
            "name": "Viscosity, Stokes' Law & Surface Tension",
            "category": "Surface & Transport Phenomena",
            "primary": ["coefficient of viscosity", "stokes", "terminal velocity", "spherical steel ball", "viscous force", "surface tension", "capillary tube", "capillarity", "rise in capillary", "excess pressure", "soap bubble"],
            "formula_cues": [r"6\pi \eta r v", r"v_t = \frac{2 r^2 (\rho - \sigma) g}{9 \eta}", r"h = \frac{2t\cos\theta}{\rho g r}", r"\frac{2t}{r}", r"\frac{4t}{r}"],
            "secondary": ["liquid", "radius", "water", "droplet"],
            "summary": "Stokes' drag $F = 6\\pi \\eta r v$. Terminal velocity $v_t = \\frac{2 r^2 (\\rho - \\sigma) g}{9 \\eta} \\propto r^2$. Excess pressure $\\Delta P = \\frac{2T}{R}$ (liquid drop), $\\Delta P = \\frac{4T}{R}$ (soap bubble). Capillary rise $h = \\frac{2T\\cos\\theta}{\\rho g r}$.",
            "standard_formulas": r"v_t = \frac{2 r^2 (\rho - \sigma) g}{9 \eta}, \quad \Delta P_{\text{drop}} = \frac{2T}{R}, \quad \Delta P_{\text{bubble}} = \frac{4T}{R}, \quad h = \frac{2T\cos\theta}{\rho g r}",
            "common_traps": "1. Terminal velocity depends on $r^2$, NOT $r$! If radius is doubled, $v_t$ quadruples. 2. A bubble inside a liquid has only 1 surface ($2T/R$), while a soap bubble in air has 2 surfaces ($4T/R$).",
            "tips_and_tricks": "In an artificial satellite or free-fall weightlessness ($g=0$), capillary water rises to the very top of the tube, no matter how long the tube is ($h \\to L$)."
        }
    ],

    "kcet-capacitor": [
        {
            "name": "Parallel Plate Capacitance & Dielectric Slabs",
            "category": "Core Principle",
            "primary": ["parallel plate capacitor", "capacitance", "dielectric slab", "dielectric constant", "dielectric in between", "distance between the plates", "battery remains connected", "battery disconnected"],
            "formula_cues": [r"c = \frac{\epsilon_0 a}{d}", r"c' = k c", r"q = c v", r"\epsilon_0"],
            "secondary": ["electric field", "charge", "plates", "potential difference"],
            "summary": "Capacitance of parallel plate capacitor $C_0 = \\frac{\\varepsilon_0 A}{d}$. With dielectric slab of constant $K$, $C = K C_0$. If battery disconnected: charge $Q$ is constant, potential $V = V_0/K$, electric field $E = E_0/K$. If battery connected: $V$ is constant, $Q = K Q_0$.",
            "standard_formulas": r"C = \frac{K \varepsilon_0 A}{d}, \quad E = \frac{V}{d} = \frac{\sigma}{\varepsilon_0}, \quad Q = C V",
            "common_traps": "Distinguish whether the battery is kept connected ($V = \\text{const}$) or disconnected ($Q = \\text{const}$) before inserting the dielectric slab.",
            "tips_and_tricks": "KCET Rule of Thumb: Disconnected battery $\\implies Q$ stays constant. Connected battery $\\implies V$ stays constant."
        },
        {
            "name": "Capacitor Combinations, Energy Stored & Charge Sharing",
            "category": "Circuits & Energy",
            "primary": ["equivalent capacitance", "series", "parallel", "energy stored", "potential difference across", "sharing of charge", "common potential", "loss of energy", "bridge", "microfarad"],
            "formula_cues": [r"\frac{1}{c_s} = \sum \frac{1}{c_i}", r"c_p = \sum c_i", r"\frac{1}{2} c v^2", r"\frac{q^2}{2c}", r"\Delta u = \frac{c_1 c_2}{2(c_1+c_2)}(v_1-v_2)^2"],
            "secondary": ["battery", "circuit", "voltage", "joules"],
            "summary": "Series combination $\\frac{1}{C_s} = \\frac{1}{C_1} + \\frac{1}{C_2}$ (charge $Q$ is same). Parallel combination $C_p = C_1 + C_2$ ($V$ is same). Energy stored $U = \\frac{1}{2} C V^2 = \\frac{Q^2}{2C}$. Common potential on connecting two capacitors: $V_{\\text{common}} = \\frac{C_1 V_1 + C_2 V_2}{C_1 + C_2}$.",
            "standard_formulas": r"C_p = \sum C_i, \quad \frac{1}{C_s} = \sum \frac{1}{C_i}, \quad U = \frac{1}{2} C V^2, \quad \Delta U_{\text{loss}} = \frac{C_1 C_2}{2(C_1+C_2)}(V_1 - V_2)^2",
            "common_traps": "In series capacitors, voltage divides inversely to capacitance: $V_1 = V \\left(\\frac{C_2}{C_1 + C_2}\\right)$. Smaller capacitor takes larger voltage!",
            "tips_and_tricks": "For $n$ identical capacitors of capacitance $C$: $C_{\\text{parallel}} / C_{\\text{series}} = n^2$."
        }
    ],

    "kcet-semiconductor-devices-and-logic-gates": [
        {
            "name": "Semiconductor Physics: Doping, p-n Junction & Rectifiers",
            "category": "Device Physics",
            "primary": ["p-type", "n-type", "doping", "arsenic", "indium", "germanium", "silicon", "majority carriers", "depletion region", "barrier potential", "reverse biased", "forward biased", "half-wave rectifier", "full-wave rectifier"],
            "formula_cues": [r"n_e n_h = n_i^2", r"\text{group 13}", r"\text{group 15}", r"d_1 \text{ and } d_2"],
            "secondary": ["diode", "electrons", "holes", "current", "conduction"],
            "summary": "Doping with pentavalent impurities (As, P, Sb) creates n-type (electrons majority). Doping with trivalent impurities (In, B, Al) creates p-type (holes majority). Mass action law $n_e n_h = n_i^2$. Depletion layer contains immobile uncompensated ions. Forward bias reduces barrier; reverse bias widens barrier. Ideal diode acts as closed switch in forward bias, open switch in reverse bias.",
            "standard_formulas": r"n_e n_h = n_i^2, \quad f_{\text{ripple, half}} = f_{\text{in}}, \quad f_{\text{ripple, full}} = 2 f_{\text{in}}",
            "common_traps": "In the depletion region of an unbiased p-n junction, there are NO free electrons or holes—only immobile positive and negative donor/acceptor ions!",
            "tips_and_tricks": "In reverse biased circuits with ideal diodes, replace the reverse-biased diode with an open circuit (break the wire) to simplify the circuit instantly."
        },
        {
            "name": "Logic Gates, Truth Tables & De Morgan's Laws",
            "category": "Digital Electronics",
            "primary": ["logic gate", "truth table", "nand gate", "nor gate", "universal gate", "and gate", "or gate", "not gate", "boolean expression", "de morgan", "output y", "inputs a and b"],
            "formula_cues": [r"y = \overline{a \cdot b}", r"y = \overline{a + b}", r"\overline{a+b} = \overline{a} \cdot \overline{b}", r"\overline{a \cdot b} = \overline{a} + \overline{b}"],
            "secondary": ["binary", "low", "high", "output"],
            "summary": "Basic gates: AND ($Y = A \\cdot B$), OR ($Y = A + B$), NOT ($Y = \\bar{A}$). Universal gates: NAND ($Y = \\overline{A \\cdot B}$) and NOR ($Y = \\overline{A + B}$). De Morgan's laws: $\\overline{A + B} = \\bar{A} \\cdot \\bar{B}$ and $\\overline{A \\cdot B} = \\bar{A} + \\bar{B}$.",
            "standard_formulas": r"\text{NAND: } Y = \overline{A \cdot B}, \quad \text{NOR: } Y = \overline{A + B}, \quad \overline{A + B} = \bar{A} \cdot \bar{B}, \quad \overline{A \cdot B} = \bar{A} + \bar{B}",
            "common_traps": "NAND with all inputs tied together acts as a NOT gate. NOR with all inputs tied together also acts as a NOT gate.",
            "tips_and_tricks": "KCET Speed Trick: To identify mystery gate circuits, test inputs $(A=0, B=0)$ and $(A=1, B=1)$ first. This eliminates 2 out of 4 options in under 10 seconds."
        }
    ]
}

SPECIAL_CHEMISTRY = {
    "kcet-aldehyde-and-ketone": [
        {
            "name": "Carbonyl Nucleophilic Addition & Ammonia Derivatives",
            "category": "Reactions & Mechanisms",
            "primary": ["carbonyl", "nucleophilic addition", "ammonia derivatives", "hydroxylamine", "hydrazine", "phenylhydrazine", "semicarbazide", "cyanohydrin", "sodium bisulphite", "hemiacetal", "acetal", "oxime", "hydrazone", "2,4-dnp"],
            "formula_cues": [r"\text{nh}_2\text{oh}", r"\text{hcn}", r"\text{nahso}_3", r"\text{c=o}", r"\text{c=n-oh}"],
            "secondary": ["aldehyde", "ketone", "reagent", "product"],
            "summary": "Nucleophilic addition to $>\text{C=O}$: addition of $\\text{HCN}$ gives cyanohydrins, addition of $\\text{NaHSO}_3$ gives crystalline bisulphite adducts. Reaction with ammonia derivatives $\\text{H}_2\\text{N-Z}$ eliminates water to give crystalline derivatives (oximes with $\\text{NH}_2\\text{OH}$, hydrazones with $\\text{NH}_2\\text{NH}_2$, 2,4-DNP derivatives).",
            "standard_formulas": r">\text{C=O} + \text{H}_2\text{N-Z} \xrightarrow{\text{H}^+} >\text{C=N-Z} + \text{H}_2\text{O}",
            "common_traps": "In semicarbazide $\\text{H}_2\\text{N-CO-NH-NH}_2$, only the hydrazine $\\text{NH}_2$ reacts; the amide $\\text{NH}_2$ is deactivated by resonance with $>\text{C=O}$.",
            "tips_and_tricks": "Reactivity order toward nucleophilic addition: $\\text{HCHO} > \\text{RCHO} > \\text{RCOR}$."
        },
        {
            "name": "Named Condensation Reactions & Diagnostic Tests",
            "category": "Named Reactions & Tests",
            "primary": ["aldol condensation", "cannizzaro", "iodoform test", "tollens", "fehling", "clemmensen", "wolff-kishner", "rosenmund", "etard", "stephen", "yellow precipitate", "ch3c=o"],
            "formula_cues": [r"\text{chi}_3", r"\text{dilute naoh}", r"\text{conc. koh}", r"\text{zn-hg/hcl}", r"\text{nh}_2\text{nh}_2/\text{koh}"],
            "secondary": ["alpha hydrogen", "yellow ppt", "test", "reduction"],
            "summary": "Aldol condensation requires $\\alpha$-hydrogen. Cannizzaro occurs for aldehydes lacking $\\alpha$-H (disproportionation into alcohol + carboxylate). Iodoform test: positive for compounds containing $\\text{CH}_3\\text{CO-}$ or $\\text{CH}_3\\text{CH(OH)-}$ group. Tollens' & Fehling's tests oxidize aldehydes, not ketones.",
            "standard_formulas": r"2\text{CH}_3\text{CHO} \xrightarrow{\text{dil. NaOH}} \text{CH}_3\text{CH(OH)CH}_2\text{CHO} \xrightarrow{\Delta} \text{CH}_3\text{CH=CHCHO}",
            "common_traps": "Acetophenone ($\text{C}_6\text{H}_5\text{COCH}_3$) gives positive iodoform test, while benzophenone does not.",
            "tips_and_tricks": "Clemmensen uses acidic conditions (Zn-Hg / conc. HCl); Wolff-Kishner uses basic conditions ($\\text{NH}_2\\text{NH}_2$ / KOH / glycol)."
        }
    ],

    "kcet-carboxylic-acids-and-its-derivatives": [
        {
            "name": "Acidity of Carboxylic Acids & Substituent Effects",
            "category": "Acid-Base Properties",
            "primary": ["carboxylic acid", "acidity", "more acidic than phenols", "conjugate base", "carboxylate ion", "electron withdrawing group", "substituent", "pk_a", "benzoic acid", "formic acid", "acetic acid"],
            "formula_cues": [r"\text{rcooh}", r"\text{rcoo}^-", r"-i \text{ effect}", r"+i \text{ effect}"],
            "secondary": ["acid", "resonance", "strongest", "weaker"],
            "summary": "Carboxylic acids are much more acidic than phenols because the negative charge in carboxylate ion is delocalized over two highly electronegative oxygen atoms. Electron withdrawing groups ($-I, -M$) increase acidity; electron donating groups ($+I, +M$) decrease acidity.",
            "standard_formulas": r"\text{Acidity: } \text{HCOOH} > \text{CH}_3\text{COOH} > \text{CH}_3\text{CH}_2\text{COOH}",
            "common_traps": "Formic acid (HCOOH) is more acidic than acetic acid ($\text{CH}_3\text{COOH}$) because the methyl group exerts an acid-weakening $+I$ effect.",
            "tips_and_tricks": "Carboxylic acids effervesce with $\\text{NaHCO}_3$ (liberating $\\text{CO}_2$ gas), whereas phenols (except picric acid) do not."
        },
        {
            "name": "Reactions of Carboxylic Acids & Derivatives",
            "category": "Syntheses & Reactions",
            "primary": ["hell-volhard-zelinsky", "hvz", "decarboxylation", "soda lime", "ester", "esterification", "dibal-h", "acid chloride", "acid anhydride", "amide", "hydrolysis"],
            "formula_cues": [r"\text{br}_2/\text{red p}", r"\text{naoh + cao}", r"\text{dibal-h}", r"\text{rcoor}'", r"\text{pci}_5"],
            "secondary": ["product", "reagent", "reduction"],
            "summary": "HVZ reaction: $\\alpha$-halogenation of carboxylic acids with $\\text{X}_2 / \\text{Red P}$. Decarboxylation with soda lime ($\text{NaOH} + \\text{CaO}$, $3:1$) yields alkane with one fewer carbon. Reduction of esters with DIBAL-H at low temperature gives aldehydes selectively.",
            "standard_formulas": r"\text{R-CH}_2\text{-COOH} \xrightarrow{\text{Br}_2 / \text{Red P}} \text{R-CH(Br)-COOH} \quad (\text{HVZ Reaction})",
            "common_traps": "Benzoic acid and formic acid cannot undergo HVZ reaction because they possess no $\\alpha$-hydrogens.",
            "tips_and_tricks": "DIBAL-H reduces esters and nitriles to aldehydes, not to alcohols or amines."
        }
    ],

    "kcet-general-organic-chemistry": [
        {
            "name": "Reaction Intermediates & Electronic Effects",
            "category": "Core Principles",
            "primary": ["intermediate", "heteropolar", "homolytic", "heterolytic", "carbocation", "carbanion", "free radical", "inductive effect", "resonance effect", "hyperconjugation", "electromeric"],
            "formula_cues": [r"\text{c}^+", r"\text{c}^-", r"\text{r}^\bullet", r"+i", r"-i", r"+m", r"-m"],
            "secondary": ["bond fission", "stability", "electron"],
            "summary": "Heterolytic fission creates ions (carbocations, carbanions); homolytic fission creates neutral free radicals. Stability of carbocations: $3^\circ > 2^\circ > 1^\circ > \\text{CH}_3^+$ (governed by hyperconjugation and $+I$). Stability of carbanions: $\\text{CH}_3^- > 1^\circ > 2^\circ > 3^\circ$.",
            "standard_formulas": r"\text{Carbocation Stability: } 3^\circ > 2^\circ > 1^\circ > \text{CH}_3^+, \quad \text{Carbanion Stability: } \text{CH}_3^- > 1^\circ > 2^\circ > 3^\circ",
            "common_traps": "In homolytic cleavage, each atom takes one bonding electron; in heterolytic cleavage, the more electronegative atom takes both electrons.",
            "tips_and_tricks": "Resonance stabilization always dominates over inductive effect, EXCEPT for halogens on benzene rings where $-I$ dominates."
        },
        {
            "name": "Acidity, Basicity & Aromaticity (Huckel's Rule)",
            "category": "Physical-Chemical Properties",
            "primary": ["aromatic", "aromaticity", "huckel", "4n+2", "strongest base", "more basic than aniline", "decreasing order of acidic", "pyridine", "pyrrole", "aliphatic amine"],
            "formula_cues": [r"4n+2", r"\pi \text{ electrons}", r"\text{c}_6\text{h}_5\text{nh}_2"],
            "secondary": ["base", "acid", "lone pair", "delocalization"],
            "summary": "Hückel's Rule: Cyclic, planar, completely conjugated systems with $(4n+2)\\pi$ electrons are aromatic ($2, 6, 10, 14\\pi$). Basicity of amines: Aliphatic amines are more basic than aniline because aniline's lone pair is delocalized into the benzene ring by resonance.",
            "standard_formulas": r"\text{Aromatic: } (4n+2)\pi \text{ electrons}, \quad \text{Anti-aromatic: } 4n\pi \text{ electrons}",
            "common_traps": "Cyclooctatetraene ($8\\pi$) is non-planar (tub-shaped), hence it is non-aromatic, NOT anti-aromatic!",
            "tips_and_tricks": "In gas phase, amine basicity follows strictly $+I$: $3^\circ > 2^\circ > 1^\circ > \\text{NH}_3$."
        }
    ],

    "kcet-isomerism": [
        {
            "name": "Structural Isomerism: Chain, Position & Functional",
            "category": "Isomerism",
            "primary": ["isomers", "chain isomers", "position isomers", "functional isomers", "metamerism", "c5h12", "c6h14", "number of chain isomers", "isomers of hexane", "boiling point"],
            "formula_cues": [r"\text{c}_5\text{h}_{12}", r"\text{c}_6\text{h}_{14}", r"\text{c}_4\text{h}_{10}"],
            "secondary": ["molecular formula", "different", "hydrocarbon"],
            "summary": "Structural isomerism: compounds having the same molecular formula but different structural arrangements. Pentane ($\\text{C}_5\\text{H}_{12}$) has 3 isomers ($n$-pentane, isopentane, neopentane). Hexane ($\\text{C}_6\\text{H}_{14}$) has 5 chain isomers.",
            "standard_formulas": r"\text{Isomer Count: } \text{C}_4\text{H}_{10} \implies 2, \quad \text{C}_5\text{H}_{12} \implies 3, \quad \text{C}_6\text{H}_{14} \implies 5, \quad \text{C}_7\text{H}_{16} \implies 9",
            "common_traps": "Functional isomers: Alcohols and Ethers; Aldehydes and Ketones; Carboxylic acids and Esters.",
            "tips_and_tricks": "Boiling points of chain isomers decrease with increasing branching."
        },
        {
            "name": "Stereoisomerism: Geometrical & Optical Isomerism",
            "category": "Stereochemistry",
            "primary": ["cis", "trans", "geometrical isomerism", "optical isomerism", "chiral", "asymmetric carbon", "enantiomers", "diastereomers", "meso", "plane polarized light"],
            "formula_cues": [r"\text{cis-trans}", r"2^n"],
            "secondary": ["restricted rotation", "optically active"],
            "summary": "Geometrical isomerism ($cis/trans$) arises due to restricted rotation about $>\text{C=C}<$ or ring with two different groups on each carbon. Optical isomerism requires non-superimposable mirror images (chiral center with 4 different groups, lack of plane of symmetry).",
            "standard_formulas": r"\text{Number of optical isomers for molecule with } n \text{ asymmetric carbons: } 2^n",
            "common_traps": "Propene cannot show geometrical isomerism because one of the double-bonded carbons has two identical hydrogens.",
            "tips_and_tricks": "Meso compounds contain chiral carbons but possess an internal plane of symmetry, making them optically inactive."
        }
    ],

    "kcet-iupac-nomenclature": [
        {
            "name": "IUPAC Nomenclature & Functional Group Priority",
            "category": "Nomenclature",
            "primary": ["iupac name", "iupac nomenclature", "longest continuous carbon chain", "principal functional group", "suffix", "prefix", "locant", "lowest locant rule"],
            "formula_cues": [r"\text{iupac}", r"\text{-oic acid}", r"\text{-al}", r"\text{-one}", r"\text{-ol}"],
            "secondary": ["substituent", "numbering", "chain"],
            "summary": "IUPAC rules: Identify longest continuous carbon chain containing the principal functional group. Priority order of functional groups: $-\\text{COOH} > -\\text{SO}_3\\text{H} > -\\text{COOR} > -\\text{COCl} > -\\text{CONH}_2 > -\\text{CN} > -\\text{CHO} > >\\text{C=O} > -\\text{OH} > -\\text{NH}_2 > >\\text{C=C}< > -\\text{C}\\equiv\\text{C}-$.",
            "standard_formulas": r"\text{IUPAC Format: } \text{Prefix} + \text{Root Word} + \text{Primary Suffix} + \text{Secondary Suffix}",
            "common_traps": "In numbering when double and triple bonds are at identical positions from opposite ends, double bond gets the lower locant ('en' before 'yne').",
            "tips_and_tricks": "Look at the principal suffix like -oic acid vs -oate vs -al to eliminate options quickly."
        }
    ],

    "kcet-metallurgy": [
        {
            "name": "Ore Concentration & Pyrometallurgy Extraction",
            "category": "Metallurgical Processes",
            "primary": ["froth floatation", "potassium ethyl xanthate", "collector", "depressant", "roasting", "calcination", "blast furnace", "copper pyrites", "copper matte", "blister copper", "smelting"],
            "formula_cues": [r"\text{nacn}", r"\text{cufes}_2", r"\text{cu}_2\text{s} + 2\text{cu}_2\text{o} \to 6\text{cu} + \text{so}_2", r"\text{fe}_2\text{o}_3 + 3\text{co} \to 2\text{fe} + 3\text{co}_2"],
            "secondary": ["ore", "sulphide", "gas x", "furnace"],
            "summary": "Concentration of sulphide ores by froth flotation: collectors (pine oil, fatty acids, xanthates) make mineral particles water-repellent; depressants (NaCN) separate ZnS from PbS. Roasting converts sulphide ores to oxides with $\\text{SO}_2$ gas release. Extraction of copper from copper pyrites involves reverberatory furnace, copper matte ($\\text{Cu}_2\\text{S} + \\text{FeS}$), and self-reduction in Bessemer converter.",
            "standard_formulas": r"\text{Self Reduction: } \text{Cu}_2\text{S} + 2\text{Cu}_2\text{O} \to 6\text{Cu} + \text{SO}_2 \quad (\text{Blister Copper})",
            "common_traps": "Calcination is heating in absence of air (for carbonates and hydrated oxides); roasting is heating in excess air (for sulphides).",
            "tips_and_tricks": "Blister copper gets its blistered appearance from the evolution of escaping $\\text{SO}_2$ gas during cooling."
        },
        {
            "name": "Ellingham Diagram, Hall-Heroult Process & Refining",
            "category": "Thermodynamics & Refining",
            "primary": ["ellingham diagram", "hall-heroult", "hall heroult", "delta g", "carbon reduction", "zone refining", "mond", "van arkel", "liquation", "cryolite"],
            "formula_cues": [r"\delta g^\circ", r"\text{al}_2\text{o}_3", r"\text{na}_3\text{alf}_6", r"\text{ni(co)}_4", r"\text{zri}_4"],
            "secondary": ["refining", "temperature", "graphite", "anode"],
            "summary": "Ellingham diagram plots $\\Delta G^\\circ$ vs $T$. A metal can reduce the oxide of any other metal located higher in the diagram. Hall-Héroult process: electrolysis of molten $\\text{Al}_2\\text{O}_3$ with cryolite ($\\text{Na}_3\\text{AlF}_6$) and $\\text{CaF}_2$ to lower melting point and increase conductivity. Refining: Zone refining (semiconductors Ge, Si), Mond process for Ni, Van Arkel for Zr and Ti.",
            "standard_formulas": r"\text{Hall-Héroult: } 2\text{Al}_2\text{O}_3 + 3\text{C} \to 4\text{Al} + 3\text{CO}_2, \quad \text{Mond: } \text{Ni} + 4\text{CO} \xrightarrow{330\text{K}} \text{Ni(CO)}_4 \xrightarrow{450\text{K}} \text{Ni} + 4\text{CO}",
            "common_traps": "In Hall-Héroult process, the carbon anodes are consumed by reacting with liberated oxygen to form $\\text{CO}$ and $\\text{CO}_2$.",
            "tips_and_tricks": "Zone refining is based on the principle that impurities are more soluble in the molten state than in the solid state of the metal."
        }
    ],

    "kcet-polymers": [
        {
            "name": "Classification of Polymers & Monomer Units",
            "category": "Polymer Chemistry",
            "primary": ["polymer", "monomer", "nylon", "nylon 6,6", "nylon 6", "terylene", "dacron", "bakelite", "melamine", "neoprene", "buna-s", "buna-n", "adipic acid", "hexamethylenediamine", "caprolactam", "terephthalic acid"],
            "formula_cues": [r"\text{nylon 6,6}", r"\text{caprolactam}", r"\text{adipic acid}", r"\text{hexamethylenediamine}"],
            "secondary": ["synthetic", "addition", "condensation"],
            "summary": "Monomers of important polymers: Nylon 6,6 from adipic acid + hexamethylenediamine. Nylon 6 from caprolactam. Terylene (Dacron) from ethylene glycol + terephthalic acid. Bakelite from phenol + formaldehyde. Buna-S from 1,3-butadiene + styrene. Neoprene from chloroprene (2-chloro-1,3-butadiene).",
            "standard_formulas": r"\text{Nylon 6,6: } n\text{HOOC(CH}_2)_4\text{COOH} + n\text{H}_2\text{N(CH}_2)_6\text{NH}_2 \to \text{[-CO(CH}_2)_4\text{CONH(CH}_2)_6\text{NH-]}_n + 2n\text{H}_2\text{O}",
            "common_traps": "Nylon 6 is made from caprolactam alone, while Nylon 6,6 is made from two different 6-carbon monomers.",
            "tips_and_tricks": "Thermoplastics soften on heating (polythene, PVC); thermosetting plastics undergo irreversible cross-linking (Bakelite, melamine)."
        },
        {
            "name": "Biodegradable Polymers & Vulcanization",
            "category": "Applied Polymers",
            "primary": ["biodegradable polymer", "phbv", "nylon 2-nylon 6", "vulcanization of rubber", "sulphur cross links", "natural rubber", "isoprene", "cis-1,4-polyisoprene", "gutta-percha"],
            "formula_cues": [r"\text{phbv}", r"\text{cis-1,4-polyisoprene}", r"\text{3-hydroxybutanoic acid}"],
            "secondary": ["rubber", "sulphur", "polymer"],
            "summary": "Biodegradable polymers: PHBV from 3-hydroxybutanoic acid + 3-hydroxypentanoic acid; Nylon 2-nylon 6 from glycine + amino caproic acid. Natural rubber is cis-1,4-polyisoprene. Vulcanization involves heating raw rubber with 5% sulphur to introduce cross-links.",
            "standard_formulas": r"\text{Natural Rubber: } [\text{-CH}_2\text{-C(CH}_3)\text{=CH-CH}_2\text{-}]_n \quad (\text{cis-isomer})",
            "common_traps": "Natural rubber is the cis-isomer of 1,4-polyisoprene; the trans-isomer is Gutta-Percha.",
            "tips_and_tricks": "PHBV is widely used in speciality packaging and controlled drug release."
        }
    ],

    "kcet-chemistry-in-everyday-life": [
        {
            "name": "Therapeutic Drug Classes: Analgesics, Antibiotics & Antiseptics",
            "category": "Pharmaceutical Chemistry",
            "primary": ["analgesic", "narcotic", "non-narcotic", "aspirin", "paracetamol", "morphine", "antibiotic", "penicillin", "bactericidal", "bacteriostatic", "antiseptic", "disinfectant", "dettol", "chloroxylenol", "bithionol", "tincture of iodine"],
            "formula_cues": [r"\text{aspirin}", r"\text{paracetamol}", r"\text{chloroxylenol + terpineol}", r"0.2\% \text{ phenol}"],
            "secondary": ["drug", "used", "action"],
            "summary": "Analgesics relieve pain: non-narcotics (aspirin, paracetamol) inhibit prostaglandin synthesis; narcotics (morphine, codeine) are habit-forming pain-relievers. Antiseptics: Dettol (chloroxylenol + terpineol), bithionol (added to soaps), tincture of iodine (2-3% iodine in alcohol-water). Disinfectants: 1% phenol solution (0.2% phenol is antiseptic).",
            "standard_formulas": r"\text{Aspirin: 2-acetoxybenzoic acid}, \quad \text{Dettol: Chloroxylenol} + \alpha\text{-Terpineol}",
            "common_traps": "Phenol acts as an antiseptic at 0.2% concentration, but acts as a disinfectant at 1.0% concentration!",
            "tips_and_tricks": "Bactericidal antibiotics kill bacteria (penicillin, ofloxacin); bacteriostatic antibiotics inhibit bacterial growth (erythromycin, tetracycline)."
        },
        {
            "name": "Food Additives, Artificial Sweeteners & Detergents",
            "category": "Household Chemistry",
            "primary": ["artificial sweetener", "aspartame", "saccharin", "sucralose", "alitame", "food preservative", "sodium benzoate", "cationic detergent", "anionic detergent", "non-ionic detergent", "cetyltrimethylammonium bromide"],
            "formula_cues": [r"\text{aspartame}", r"\text{sucralose}", r"\text{c}_{16}\text{h}_{33}\text{n}^+(\text{ch}_3)_3\text{br}^-"],
            "secondary": ["cleansing", "sweetness", "soap"],
            "summary": "Artificial sweeteners: Aspartame (unstable at cooking temperatures), Saccharin (550x sweeter), Sucralose (stable at cooking temperatures), Alitame (high potency, 2000x sweeter). Detergents: Anionic (sodium lauryl sulphate), Cationic (cetyltrimethylammonium bromide, germicidal), Non-ionic (polyethylene glycol stearate).",
            "standard_formulas": r"\text{Cationic: } [\text{CH}_3(\text{CH}_2)_{15}\text{N(CH}_3)_3]^+\text{Br}^-, \quad \text{Anionic: } \text{CH}_3(\text{CH}_2)_{11}\text{OSO}_3^-\text{Na}^+",
            "common_traps": "Aspartame cannot be used in baking or cooked foods because it decomposes at elevated temperatures.",
            "tips_and_tricks": "Cationic detergents have germicidal properties and are used in hair conditioners and hospital sanitation."
        }
    ]
}

SPECIAL_MATH = {
    "kcet-linear-programming": [
        {
            "name": "Objective Function, Constraints & Feasible Region",
            "category": "Core Principle",
            "primary": ["feasible region", "constraints", "objective function", "linear inequalities", "non-negative", "unbounded", "bounded region", "infeasible"],
            "formula_cues": [r"z = ax + by", r"z=px+qy", r"x \ge 0", r"y \ge 0", r"x+y \le"],
            "secondary": ["region", "linear", "inequality", "statement"],
            "summary": "Formulation of LPP: linear objective function $Z = ax + by$, linear constraints, non-negative restrictions $x, y \\ge 0$, and identification of bounded vs unbounded feasible regions.",
            "standard_formulas": r"Z = ax + by, \quad \text{Feasible Region: Intersection of all half-planes determined by constraints}",
            "common_traps": "If the feasible region is unbounded, the minimum or maximum value of $Z$ may not exist unless the open half-plane has no common points with the feasible region.",
            "tips_and_tricks": "In KCET, sketch the constraint boundary lines quickly using intercept form $\\frac{x}{a} + \\frac{y}{b} = 1$."
        },
        {
            "name": "Corner Point Theorem & Optimal Solutions",
            "category": "Optimization Archetypes",
            "primary": ["corner point", "corner points", "maximum value of z", "minimum value of z", "optimal", "same maximum value", "infinite number of points", "line segment"],
            "formula_cues": [r"z = 3x+4y", r"max z", r"min z", r"(0, 10)", r"(15, 15)"],
            "secondary": ["vertices", "evaluate", "value of z", "points"],
            "summary": "Corner Point Method: If an optimal value exists, it occurs at a vertex. If the maximum/minimum occurs at two distinct corner points, it attains the same optimal value at every point along the line segment joining them.",
            "standard_formulas": r"\text{If } Z(A) = Z(B) = Z_{\max}, \text{ then } Z \text{ is maximized at all points on segment } AB",
            "common_traps": "Assuming optimal solution is only at integer points—fractional coordinates of corner points are valid.",
            "tips_and_tricks": "When $Z = px + qy$ attains the same maximum at $(x_1, y_1)$ and $(x_2, y_2)$, equate $p x_1 + q y_1 = p x_2 + q y_2$ to find $p/q$ directly."
        }
    ],

    "kcet-differentiation": [
        {
            "name": "Standard Derivatives & Inverse Trigonometric Substitutions",
            "category": "Differentiation Techniques",
            "primary": ["derivative of", "sin^{-1}", "cos^{-1}", "tan^{-1}", "substitution", "with respect to", "f'(x)", "f'(1/2)", "chain rule"],
            "formula_cues": [r"\sin^{-1}\left(\frac{2x}{1+x^2}\right)", r"\cos^{-1}(4x^3-3x)", r"\cos^{-1}(2x^2-1)", r"\tan^{-1}\left(\frac{3x-x^3}{1-3x^2}\right)"],
            "secondary": ["differentiate", "function", "angle"],
            "summary": "Differentiation of composite functions and inverse trigonometric forms using standard substitutions: $x = \\tan\\theta$ for $\\sin^{-1}\\frac{2x}{1+x^2} = 2\\tan^{-1}x$; $x = \\cos\\theta$ for $\\cos^{-1}(2x^2-1) = 2\\cos^{-1}x$ and $\\cos^{-1}(4x^3-3x) = 3\\cos^{-1}x$.",
            "standard_formulas": r"\frac{d}{dx}[\sin^{-1}\frac{2x}{1+x^2}] = \frac{2}{1+x^2}, \quad \frac{d}{dx}[\cos^{-1}(4x^3-3x)] = -\frac{3}{\sqrt{1-x^2}}",
            "common_traps": "Check the given interval of $x$ before writing the simplified inverse trigonometric form.",
            "tips_and_tricks": "Derivative of $u(x)$ with respect to $v(x)$ is simply $\\frac{du/dx}{dv/dx}$."
        },
        {
            "name": "Implicit, Logarithmic & Higher Order Derivatives",
            "category": "Advanced Calculus",
            "primary": ["second order derivative", "d^2y/dx^2", "implicit differentiation", "logarithmic differentiation", "dy/dx", "y =", "x dy/dx - y = 0", "infinite root series"],
            "formula_cues": [r"\frac{dy}{dx}", r"\frac{d^2y}{dx^2}", r"x\frac{dy}{dx} = y", r"y^3 = \tan x + y", r"(x+y)^n"],
            "secondary": ["take log", "cube both sides", "with respect to x"],
            "summary": "Implicit differentiation: differentiate both sides with respect to $x$. Logarithmic differentiation for $y = f(x)^{g(x)}$ or products/quotients. Second order derivatives $\\frac{d^2y}{dx^2}$. For parametric equations $x = f(t), y = g(t)$, $\\frac{d^2y}{dx^2} = \\frac{d}{dt}\\left(\\frac{dy}{dx}\\right) \\frac{1}{dx/dt}$.",
            "standard_formulas": r"\frac{d}{dx}[u^v] = u^v \left[\frac{v}{u}\frac{du}{dx} + \ln u \frac{dv}{dx}\right], \quad \frac{d^2y}{dx^2} = \frac{\frac{d}{dt}(dy/dx)}{dx/dt}",
            "common_traps": "For parametric second derivatives, remember the final chain rule step $\\times \\frac{dt}{dx}$!",
            "tips_and_tricks": "For homogeneous implicit equations $x^p y^q = (x+y)^{p+q}$, $\\frac{dy}{dx} = \\frac{y}{x}$, and $\\frac{d^2y}{dx^2} = 0$."
        }
    ],

    "kcet-indefinite-integration": [
        {
            "name": "Integration by Substitution & Standard Integrals",
            "category": "Integration Methods",
            "primary": ["substitute", "indefinite integral", "evaluate", "int", "dx", "standard form", "sec^2", "sin x", "cos x"],
            "formula_cues": [r"\int \frac{dx}{x^2 + a^2}", r"\int \frac{dx}{\sqrt{a^2 - x^2}}", r"\int f'(x)[f(x)]^n dx", r"\int \frac{f'(x)}{f(x)} dx"],
            "secondary": ["function", "constant of integration", "c"],
            "summary": "Method of substitution: $\\int f(g(x))g'(x)dx = \\int f(u)du$. Standard algebraic and trigonometric forms: $\\int \\frac{dx}{x^2+a^2} = \\frac{1}{a}\\tan^{-1}\\frac{x}{a}$, $\\int \\frac{dx}{\\sqrt{a^2-x^2}} = \\sin^{-1}\\frac{x}{a}$, $\\int \\frac{f'(x)}{f(x)}dx = \\ln|f(x)|$.",
            "standard_formulas": r"\int \frac{f'(x)}{f(x)}dx = \ln|f(x)| + C, \quad \int \frac{dx}{x^2+a^2} = \frac{1}{a}\tan^{-1}\frac{x}{a} + C",
            "common_traps": "Forgetting the factor $1/a$ in $\\frac{1}{a}\\tan^{-1}\\frac{x}{a}$, or adding $1/a$ to $\\sin^{-1}\\frac{x}{a}$.",
            "tips_and_tricks": "For $\\int e^x [f(x) + f'(x)] dx$, the answer is immediately $e^x f(x) + C$."
        },
        {
            "name": "Integration by Parts & Partial Fractions",
            "category": "Advanced Integration",
            "primary": ["integration by parts", "partial fractions", "product rule for integration", "ilate", "rational function", "linear factors"],
            "formula_cues": [r"\int u v dx", r"u \int v dx - \int", r"\frac{a}{x-a} + \frac{b}{x-b}", r"e^x[f(x)+f'(x)]"],
            "secondary": ["first function", "second function", "algebraic"],
            "summary": "Integration by parts $\\int u v dx = u \\int v dx - \\int (u' \\int v dx) dx$ guided by the ILATE priority rule. Resolution into partial fractions for proper rational functions.",
            "standard_formulas": r"\int u v dx = u \int v dx - \int \left(\frac{du}{dx} \int v dx\right) dx, \quad \int e^x[f(x) + f'(x)]dx = e^x f(x) + C",
            "common_traps": "Applying partial fractions to improper rational functions without dividing numerator by denominator first.",
            "tips_and_tricks": "In KCET, differentiate the four given options if finding the integral takes more than 1 minute."
        }
    ],

    "kcet-definite-integration": [
        {
            "name": "Properties of Definite Integrals & King's Rule",
            "category": "Definite Integral Properties",
            "primary": ["definite integral", "king's rule", "f(a+b-x)", "f(a-x)", "odd function", "even function", "properties of definite", "pi/4", "pi/2", "0 to pi/2"],
            "formula_cues": [r"\int_0^a f(x)dx = \int_0^a f(a-x)dx", r"\int_{-a}^a f(x)dx", r"\int_0^{\pi/2} \frac{\sin^n x}{\sin^n x + \cos^n x} dx"],
            "secondary": ["limits", "upper limit", "lower limit", "symmetry"],
            "summary": "King's property: $\\int_a^b f(x)dx = \\int_a^b f(a+b-x)dx$. For symmetric limits: $\\int_{-a}^a f(x)dx = 0$ if $f(x)$ is odd, and $2\\int_0^a f(x)dx$ if $f(x)$ is even. Integral of periodic functions: $\\int_0^{nT} f(x)dx = n\\int_0^T f(x)dx$.",
            "standard_formulas": r"\int_a^b f(x)dx = \int_a^b f(a+b-x)dx, \quad \int_0^{\pi/2} \frac{\sin^n x}{\sin^n x + \cos^n x} dx = \frac{\pi}{4}",
            "common_traps": "Applying the odd function property $\\int_{-a}^a f(x)dx = 0$ without verifying that the limits are exactly symmetric $[-a, a]$.",
            "tips_and_tricks": "Any integral of the form $\\int_a^b \\frac{f(x)}{f(x) + f(a+b-x)} dx$ is directly equal to $\\frac{b-a}{2}$."
        }
    ]
}

# Add into the files directly
def append_to_file(filepath, dict_data):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We find the last closing brace
    last_brace = content.rfind('}')
    if last_brace == -1:
        return
    
    # Format the additions
    additions = ""
    for k, v in dict_data.items():
        # format key and value
        import pprint
        formatted = pprint.pformat(v, indent=4, width=120)
        additions += f'    "{k}": {formatted},\n\n'
    
    new_content = content[:last_brace] + "    # ==========================================\n    # SPECIAL KCET SPECIFIC CHAPTERS\n    # ==========================================\n" + additions + content[last_brace:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath} with {len(dict_data)} chapters!")

append_to_file("app/analyzer/taxonomies/kcet_physics.py", SPECIAL_PHYSICS)
append_to_file("app/analyzer/taxonomies/kcet_chemistry.py", SPECIAL_CHEMISTRY)
append_to_file("app/analyzer/taxonomies/kcet_math.py", SPECIAL_MATH)

print("Finished appending special chapters!")
