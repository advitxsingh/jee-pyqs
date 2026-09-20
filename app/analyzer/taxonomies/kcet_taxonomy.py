"""
Aggregated KCET Taxonomy Registry.
Merges Physics, Chemistry, and Mathematics taxonomies tailored specifically for Karnataka CET.
Covers 100% of the 95 KCET chapters with authentic concepts, formulas, traps, and speed tricks.
"""

from typing import Dict, List, Any
from .kcet_physics import KCET_PHYSICS_TAXONOMY
from .kcet_chemistry import KCET_CHEMISTRY_TAXONOMY
from .kcet_math import KCET_MATH_TAXONOMY

KCET_TAXONOMY: Dict[str, List[Dict[str, Any]]] = {}

# Merge all three subjects
KCET_TAXONOMY.update(KCET_PHYSICS_TAXONOMY)
KCET_TAXONOMY.update(KCET_CHEMISTRY_TAXONOMY)
KCET_TAXONOMY.update(KCET_MATH_TAXONOMY)


def get_kcet_taxonomy(slug: str) -> List[Dict[str, Any]]:
    """
    Retrieve dedicated KCET concepts for a given chapter slug.
    Guarantees tailored Karnataka CET concept taxonomy for all 95 chapters.
    """
    # 1. Exact slug match (e.g. 'kcet-electrochemistry')
    if slug in KCET_TAXONOMY:
        return KCET_TAXONOMY[slug]

    # 2. Normalized prefix check
    clean = slug.lower().strip()
    if not clean.startswith("kcet-"):
        clean = f"kcet-{clean}"

    if clean in KCET_TAXONOMY:
        return KCET_TAXONOMY[clean]

    return []
