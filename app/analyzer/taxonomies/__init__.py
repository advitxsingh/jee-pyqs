"""
Central Syllabus Taxonomy Module for JEE Main and KCET.
Merges Physics, Chemistry, and Mathematics taxonomies, resolves slug aliases,
and guarantees rich multi-concept generation for every chapter.
"""

from typing import Dict, List, Any
from .physics_taxonomy import PHYSICS_TAXONOMY
from .chemistry_taxonomy import CHEMISTRY_TAXONOMY
from .math_taxonomy import MATH_TAXONOMY
from .kcet_taxonomy import KCET_TAXONOMY, get_kcet_taxonomy

# Merge all three subjects
MASTER_TAXONOMY: Dict[str, List[Dict[str, Any]]] = {}
MASTER_TAXONOMY.update(PHYSICS_TAXONOMY)
MASTER_TAXONOMY.update(CHEMISTRY_TAXONOMY)
MASTER_TAXONOMY.update(MATH_TAXONOMY)

# Canonical slug aliases mapping KCET/JEE variants to the canonical key
CANONICAL_ALIASES = {
    # Chemistry
    "liquid-solution": "solutions",
    "atomic-structure": "structure-of-atom",
    "aldehyde-and-ketone": "aldehydes-ketones-and-carboxylic-acids",
    "carboxylic-acids-and-its-derivatives": "aldehydes-ketones-and-carboxylic-acids",
    "alcohol-phenols-and-ethers": "alcohols-phenols-and-ethers",
    "chemical-kinetics-and-nuclear-chemistry": "chemical-kinetics",
    "nuclear-chemistry": "chemical-kinetics",
    "ionic-equilibrum": "ionic-equilibrium",
    "hydrogen-and-its-compounds": "hydrogen",
    "metallurgy": "isolation-of-elements",
    "general-organic-chemistry": "basics-of-organic-chemistry",
    "isomerism": "basics-of-organic-chemistry",
    "iupac-nomenclature": "basics-of-organic-chemistry",
    "states-of-matter": "gaseous-state",

    # Mathematics
    "three-dimensional-geometry": "3d-geometry",
    "differentiation": "limits-continuity-and-differentiability",
    "indefinite-integration": "indefinite-integrals",
    "logarithms": "logarithm",
    "properties-of-triangles": "properties-of-triangle",
    "quadratic-equations": "quadratic-equation-and-inequalities",
    "trigonometric-equations": "trigonometric-functions-and-equations",
    "trigonometric-ratios-and-identities": "trigonometric-ratio-and-identites",

    # Physics
    "geometrical-optics": "ray-optics",
    "units-and-measurement-and-dimensions": "units-and-measurements",
    "work-power-and-energy": "work-energy-and-power",
    "magnetics": "moving-charges-and-magnetism",
    "magnetism-and-matter": "magnetic-properties-of-matter",
    "semiconductor-devices-and-logic-gates": "electronic-devices",
    "elasticity": "properties-of-matter",
    "fluid-mechanics": "properties-of-matter",
}


def normalize_slug(slug: str) -> str:
    """Normalize a chapter slug by removing prefixes and resolving aliases."""
    clean = slug.lower().replace("kcet-", "").strip()
    return CANONICAL_ALIASES.get(clean, clean)


def get_taxonomy_for_chapter(slug: str) -> List[Dict[str, Any]]:
    """
    Retrieve or dynamically synthesize a multi-concept taxonomy for any chapter.
    Guarantees tailored KCET concept taxonomy for all KCET chapters,
    and rich multi-concept generation for JEE Main chapters.
    """
    # 1. Dedicated KCET taxonomy priority
    if slug.startswith("kcet-") or slug in KCET_TAXONOMY:
        kcet_list = get_kcet_taxonomy(slug)
        if kcet_list:
            return kcet_list

    norm = normalize_slug(slug)
    if norm in MASTER_TAXONOMY:
        return MASTER_TAXONOMY[norm]

    # Generate a sensible 3-tier taxonomy based on the chapter title
    title = norm.replace("-", " ").title()
    return [
        {
            "name": f"{title} — Core Principles & Governing Laws",
            "category": "Core Principle",
            "primary": [norm, title.lower(), "definition", "law", "principle", "state function", "theorem", "property"],
            "formula_cues": [],
            "standard_formulas": "",
            "summary": f"Fundamental definitions, core postulates, and governing physical/chemical relations in {title}.",
            "common_traps": f"Carefully verify units, standard reference states, and sign conventions in {title}.",
            "tips_and_tricks": f"Focus on high-yield formulas and standard limiting approximations tested in {title} PYQs."
        },
        {
            "name": f"{title} — Standard Calculations & Problem Archetypes",
            "category": "Quantitative Analysis",
            "primary": ["calculate", "value of", "ratio", "find the", "determine", "magnitude", "percentage"],
            "formula_cues": [],
            "standard_formulas": "",
            "summary": f"Quantitative numerical problem-solving techniques and standard question patterns frequently seen in {title}.",
            "common_traps": f"Watch for algebraic rounding, stoichiometric balancing, and boundary condition checks.",
            "tips_and_tricks": f"Dimensional consistency checks and ratio comparisons can quickly eliminate incorrect options."
        },
        {
            "name": f"{title} — Applied Cases, Reactions & Traps",
            "category": "Applied Topics",
            "primary": ["reaction", "compound", "condition", "incorrect", "correct statement", "exception", "application"],
            "formula_cues": [],
            "standard_formulas": "",
            "summary": f"Special cases, experimental observations, and conceptual traps designed to test deep understanding of {title}.",
            "common_traps": f"Read questions carefully for keywords like 'incorrect', 'not true', or non-standard conditions.",
            "tips_and_tricks": f"Elimination of extreme or unphysical answer choices improves accuracy in assertion-reason and multiple-statement questions."
        }
    ]
