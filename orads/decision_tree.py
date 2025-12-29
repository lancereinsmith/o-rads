"""O-RADS Decision Tree Data Structure and Logic.

This module contains the complete O-RADS ultrasound decision tree,
optimized for efficient navigation by experienced radiologists.
"""

from dataclasses import dataclass, field
from enum import Enum


class MenopauseStatus(Enum):
    """Menopausal status categories."""

    PREMENOPAUSAL = "premenopausal"
    EARLY_POSTMENOPAUSAL = "early_postmenopausal"  # <5 years or age 50-55
    LATE_POSTMENOPAUSAL = "late_postmenopausal"  # ≥5 years or age ≥55


@dataclass
class ORADSResult:
    """Final result of O-RADS assessment."""

    score: int  # 0-5
    category: str
    risk: str
    description: str
    management: str
    imaging_followup: str = ""
    clinical_followup: str = ""

    def __str__(self) -> str:
        return f"O-RADS {self.score}: {self.category}"


@dataclass
class DecisionNode:
    """A node in the decision tree."""

    id: str
    question: str | None = None  # None means terminal node
    options: list["DecisionOption"] = field(default_factory=list)
    result: ORADSResult | None = None  # Only for terminal nodes

    @property
    def is_terminal(self) -> bool:
        return self.result is not None


@dataclass
class DecisionOption:
    """An option/choice at a decision node."""

    label: str
    description: str = ""
    next_node_id: str | None = None  # ID of the next node to navigate to
    result: ORADSResult | None = None  # If this option leads directly to a result


# =============================================================================
# O-RADS RESULTS DEFINITIONS
# =============================================================================

ORADS_0 = ORADSResult(
    score=0,
    category="Incomplete Evaluation",
    risk="N/A",
    description="Lesion features cannot be accurately characterized due to technical factors",
    management="Repeat US study or MRI",
    imaging_followup="Repeat ultrasound study or consider MRI",
    clinical_followup="As clinically indicated",
)

ORADS_1 = ORADSResult(
    score=1,
    category="Normal Ovary",
    risk="N/A",
    description="No ovarian lesion; physiologic cyst (follicle ≤3cm or corpus luteum)",
    management="None required",
    imaging_followup="None",
    clinical_followup="None",
)

ORADS_5_ASCITES = ORADSResult(
    score=5,
    category="High Risk - Ascites/Peritoneal Nodules",
    risk="≥50%",
    description="Ascites and/or peritoneal nodules (not due to other etiologies)",
    management="Refer to gynecologic oncologist",
    imaging_followup="Per gyn-oncologist protocol",
    clinical_followup="Gyn-oncologist",
)


# Simple Cyst Results
def simple_cyst_result(
    size_category: str, menopause: MenopauseStatus | None
) -> ORADSResult:
    """Generate result for simple cyst based on size and menopausal status."""
    if size_category == "<=3cm":
        if menopause == MenopauseStatus.PREMENOPAUSAL:
            return ORADSResult(
                score=1,
                category="Physiologic - Follicle",
                risk="N/A",
                description="Simple cyst ≤3cm in premenopausal patient (follicle)",
                management="None required",
                imaging_followup="None",
                clinical_followup="None",
            )
        else:
            return ORADSResult(
                score=2,
                category="Almost Certainly Benign",
                risk="<1%",
                description="Simple cyst ≤3cm in postmenopausal patient",
                management="Routine follow-up",
                imaging_followup="None",
                clinical_followup="None",
            )
    elif size_category == ">3cm_to_5cm":
        imaging = (
            "None"
            if menopause == MenopauseStatus.PREMENOPAUSAL
            else "Follow-up US in 12 months"
        )
        return ORADSResult(
            score=2,
            category="Almost Certainly Benign",
            risk="<1%",
            description="Simple cyst >3cm to 5cm",
            management="Imaging surveillance if postmenopausal",
            imaging_followup=imaging,
            clinical_followup="None",
        )
    elif size_category == ">5cm_<10cm":
        return ORADSResult(
            score=2,
            category="Almost Certainly Benign",
            risk="<1%",
            description="Simple cyst >5cm but <10cm",
            management="Imaging surveillance",
            imaging_followup="Follow-up US in 12 months",
            clinical_followup="As clinically indicated",
        )
    else:  # >=10cm
        return ORADSResult(
            score=3,
            category="Low Risk",
            risk="1–<10%",
            description="Simple cyst ≥10cm",
            management="Gynecologist consultation; consider follow-up imaging",
            imaging_followup="Consider follow-up US within 6 months if not surgically excised",
            clinical_followup="Gynecologist",
        )


# Classic Benign Lesion Results
HEMORRHAGIC_CYST_PRE_SMALL = ORADSResult(
    score=2,
    category="Typical Hemorrhagic Cyst",
    risk="<1%",
    description="Hemorrhagic cyst ≤5cm, premenopausal",
    management="None required",
    imaging_followup="None",
    clinical_followup="Gynecologist as needed",
)

HEMORRHAGIC_CYST_PRE_LARGE = ORADSResult(
    score=2,
    category="Typical Hemorrhagic Cyst",
    risk="<1%",
    description="Hemorrhagic cyst >5cm but <10cm, premenopausal",
    management="Short-term follow-up to confirm resolution",
    imaging_followup="Follow-up US in 2-3 months",
    clinical_followup="Gynecologist as needed",
)

HEMORRHAGIC_CYST_EARLY_POST = ORADSResult(
    score=2,
    category="Typical Hemorrhagic Cyst",
    risk="<1%",
    description="Hemorrhagic cyst <10cm, early postmenopausal",
    management="Confirm diagnosis; may need additional imaging",
    imaging_followup="Follow-up US in 2-3 months, or US specialist, or MRI",
    clinical_followup="Gynecologist as needed",
)

HEMORRHAGIC_CYST_LATE_POST = ORADSResult(
    score=3,
    category="Atypical - Recategorize",
    risk="1–<10%",
    description="Should not occur in late postmenopausal; recategorize using other lexicon descriptors",
    management="Recategorize lesion using cystic lesion descriptors",
    imaging_followup="Reassess with other lexicon descriptors",
    clinical_followup="Gynecologist consultation recommended",
)

DERMOID_SMALL = ORADSResult(
    score=2,
    category="Typical Dermoid Cyst",
    risk="<1%",
    description="Dermoid cyst ≤3cm",
    management="May consider surveillance",
    imaging_followup="May consider follow-up US in 12 months",
    clinical_followup="Gynecologist as needed",
)

DERMOID_MEDIUM = ORADSResult(
    score=2,
    category="Typical Dermoid Cyst",
    risk="<1%",
    description="Dermoid cyst >3cm but <10cm",
    management="Surveillance or surgical excision",
    imaging_followup="Follow-up US in 12 months if not surgically excised",
    clinical_followup="Gynecologist as needed",
)

DERMOID_LARGE = ORADSResult(
    score=3,
    category="Typical Dermoid Cyst",
    risk="1–<10%",
    description="Dermoid cyst ≥10cm",
    management="Gynecologist consultation; consider surgery or close follow-up",
    imaging_followup="Consider follow-up US within 6 months if not excised",
    clinical_followup="Gynecologist",
)

ENDOMETRIOMA_PRE = ORADSResult(
    score=2,
    category="Typical Endometrioma",
    risk="<1%",
    description="Endometrioma <10cm, premenopausal",
    management="Surveillance or surgical excision",
    imaging_followup="Follow-up US in 12 months if not surgically excised",
    clinical_followup="Gynecologist as needed",
)

ENDOMETRIOMA_POST = ORADSResult(
    score=2,
    category="Typical Endometrioma",
    risk="<1%",
    description="Endometrioma <10cm, postmenopausal (initial)",
    management="Confirm diagnosis, then surveillance",
    imaging_followup="Follow-up US in 2-3 months (or specialist/MRI), then 12 months if not excised",
    clinical_followup="Gynecologist as needed",
)

ENDOMETRIOMA_LARGE = ORADSResult(
    score=3,
    category="Typical Endometrioma",
    risk="1–<10%",
    description="Endometrioma ≥10cm",
    management="Gynecologist consultation; consider surgery",
    imaging_followup="Consider follow-up US within 6 months if not excised",
    clinical_followup="Gynecologist",
)

PARAOVARIAN_CYST = ORADSResult(
    score=2,
    category="Typical Paraovarian Cyst",
    risk="<1%",
    description="Simple cyst separate from the ovary",
    management="None required (extraovarian)",
    imaging_followup="None",
    clinical_followup="Gynecologist as needed",
)

PERITONEAL_INCLUSION_CYST = ORADSResult(
    score=2,
    category="Typical Peritoneal Inclusion Cyst",
    risk="<1%",
    description="Fluid collection with ovary at margin or suspended within, conforming to adjacent organs",
    management="None required (extraovarian)",
    imaging_followup="None",
    clinical_followup="Gynecologist as needed",
)

HYDROSALPINX = ORADSResult(
    score=2,
    category="Typical Hydrosalpinx",
    risk="<1%",
    description="Anechoic, fluid-filled tubular structure (extraovarian)",
    management="None required (extraovarian)",
    imaging_followup="None",
    clinical_followup="Gynecologist as needed",
)


# Solid Mass Results
def solid_mass_result(contour: str, shadowing: bool, color_score: int) -> ORADSResult:
    """Generate result for solid mass based on characteristics."""
    if contour == "irregular":
        return ORADSResult(
            score=5,
            category="High Risk - Irregular Solid",
            risk="≥50%",
            description="Solid lesion with irregular contour",
            management="Refer to gynecologic oncologist",
            imaging_followup="Per gyn-oncologist protocol",
            clinical_followup="Gyn-oncologist",
        )

    # Smooth contour
    if color_score == 4:
        return ORADSResult(
            score=5,
            category="High Risk - Highly Vascular Solid",
            risk="≥50%",
            description="Solid smooth lesion with CS 4 (very strong flow)",
            management="Refer to gynecologic oncologist",
            imaging_followup="Per gyn-oncologist protocol",
            clinical_followup="Gyn-oncologist",
        )
    elif color_score == 1:
        return ORADSResult(
            score=3,
            category="Low Risk - Avascular Solid",
            risk="1–<10%",
            description="Solid smooth lesion with CS 1 (no flow), ± shadowing",
            management="Consider US specialist or MRI; Gynecologist consultation",
            imaging_followup="Consider follow-up US within 6 months if not excised; may consider US specialist or MRI",
            clinical_followup="Gynecologist",
        )
    elif color_score in [2, 3]:
        if shadowing:
            return ORADSResult(
                score=3,
                category="Low Risk - Shadowing Solid",
                risk="1–<10%",
                description=f"Solid smooth lesion with shadowing and CS {color_score}",
                management="Consider US specialist or MRI; Gynecologist consultation",
                imaging_followup="Consider follow-up US within 6 months if not excised",
                clinical_followup="Gynecologist",
            )
        else:
            return ORADSResult(
                score=4,
                category="Intermediate Risk - Vascular Solid",
                risk="10–<50%",
                description=f"Solid smooth lesion, non-shadowing, CS {color_score}",
                management="US specialist, MRI, or per gyn-oncologist protocol",
                imaging_followup="Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist",
                clinical_followup="Gynecologist with gyn-oncologist consultation",
            )

    # Fallback
    return ORADSResult(
        score=4,
        category="Intermediate Risk - Solid",
        risk="10–<50%",
        description="Solid lesion requiring further characterization",
        management="Further imaging or surgical evaluation",
        imaging_followup="Consider MRI or specialist evaluation",
        clinical_followup="Gynecologist with gyn-oncologist consultation",
    )


# Cystic Lesion Results (Complex Tree)
def cystic_lesion_result(
    locules: str,  # "unilocular", "bilocular", "multilocular"
    has_solid: bool,
    wall_regularity: str,  # "smooth", "irregular"
    size_ge_10cm: bool,
    color_score: int,
    num_papillary_projections: int = 0,
) -> ORADSResult:
    """Generate result for non-classic cystic lesions."""

    if has_solid:
        # Cystic lesion WITH solid component(s)
        if locules == "unilocular":
            if num_papillary_projections >= 4:
                return ORADSResult(
                    score=5,
                    category="High Risk - Multiple Papillary Projections",
                    risk="≥50%",
                    description="Unilocular cyst with ≥4 papillary projections",
                    management="Refer to gynecologic oncologist",
                    imaging_followup="Per gyn-oncologist protocol",
                    clinical_followup="Gyn-oncologist",
                )
            else:
                return ORADSResult(
                    score=4,
                    category="Intermediate Risk - Solid Component",
                    risk="10–<50%",
                    description="Unilocular cyst with <4 papillary projections or non-pp solid component",
                    management="US specialist, MRI, or per gyn-oncologist protocol",
                    imaging_followup="Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist",
                    clinical_followup="Gynecologist with gyn-oncologist consultation",
                )
        else:  # bilocular or multilocular with solid
            if color_score >= 3:
                return ORADSResult(
                    score=5,
                    category="High Risk - Vascular Solid Component",
                    risk="≥50%",
                    description=f"{locules.capitalize()} cyst with solid component(s) and CS {color_score}",
                    management="Refer to gynecologic oncologist",
                    imaging_followup="Per gyn-oncologist protocol",
                    clinical_followup="Gyn-oncologist",
                )
            else:
                return ORADSResult(
                    score=4,
                    category="Intermediate Risk - Solid Component",
                    risk="10–<50%",
                    description=f"{locules.capitalize()} cyst with solid component(s), CS 1-2",
                    management="US specialist, MRI, or per gyn-oncologist protocol",
                    imaging_followup="Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist",
                    clinical_followup="Gynecologist with gyn-oncologist consultation",
                )

    else:
        # Cystic lesion WITHOUT solid component
        if locules == "unilocular":
            if wall_regularity == "irregular":
                return ORADSResult(
                    score=3,
                    category="Low Risk - Irregular Unilocular",
                    risk="1–<10%",
                    description="Unilocular cyst with irregular inner wall (no solid component)",
                    management="Consider US specialist or MRI; Gynecologist consultation",
                    imaging_followup="Consider follow-up US within 6 months if not excised",
                    clinical_followup="Gynecologist",
                )
            else:  # smooth unilocular - this is simple/non-simple cyst, handled separately
                if size_ge_10cm:
                    return ORADSResult(
                        score=3,
                        category="Low Risk - Large Unilocular",
                        risk="1–<10%",
                        description="Unilocular smooth cyst ≥10cm",
                        management="Gynecologist consultation",
                        imaging_followup="Consider follow-up US within 6 months if not excised",
                        clinical_followup="Gynecologist",
                    )
                else:
                    return ORADSResult(
                        score=2,
                        category="Almost Certainly Benign",
                        risk="<1%",
                        description="Unilocular smooth non-simple cyst <10cm",
                        management="Surveillance based on size",
                        imaging_followup="Follow-up US in 6-12 months based on size",
                        clinical_followup="None",
                    )

        elif locules == "bilocular":
            if wall_regularity == "irregular":
                return ORADSResult(
                    score=4,
                    category="Intermediate Risk - Irregular Bilocular",
                    risk="10–<50%",
                    description="Bilocular cyst with irregular inner wall/septation",
                    management="US specialist, MRI, or per gyn-oncologist protocol",
                    imaging_followup="Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist",
                    clinical_followup="Gynecologist with gyn-oncologist consultation",
                )
            else:  # smooth bilocular
                if size_ge_10cm:
                    return ORADSResult(
                        score=3,
                        category="Low Risk - Large Bilocular",
                        risk="1–<10%",
                        description="Bilocular smooth cyst ≥10cm",
                        management="Gynecologist consultation",
                        imaging_followup="Consider follow-up US within 6 months if not excised",
                        clinical_followup="Gynecologist",
                    )
                else:
                    return ORADSResult(
                        score=2,
                        category="Almost Certainly Benign",
                        risk="<1%",
                        description="Bilocular smooth cyst <10cm",
                        management="Surveillance",
                        imaging_followup="Follow-up US in 6 months",
                        clinical_followup="None",
                    )

        else:  # multilocular without solid
            if wall_regularity == "irregular":
                return ORADSResult(
                    score=4,
                    category="Intermediate Risk - Irregular Multilocular",
                    risk="10–<50%",
                    description="Multilocular cyst with irregular inner wall/septations",
                    management="US specialist, MRI, or per gyn-oncologist protocol",
                    imaging_followup="Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist",
                    clinical_followup="Gynecologist with gyn-oncologist consultation",
                )
            elif color_score == 4:
                return ORADSResult(
                    score=4,
                    category="Intermediate Risk - Highly Vascular Multilocular",
                    risk="10–<50%",
                    description="Multilocular smooth cyst with CS 4",
                    management="US specialist, MRI, or per gyn-oncologist protocol",
                    imaging_followup="Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist",
                    clinical_followup="Gynecologist with gyn-oncologist consultation",
                )
            elif size_ge_10cm:
                return ORADSResult(
                    score=4,
                    category="Intermediate Risk - Large Multilocular",
                    risk="10–<50%",
                    description="Multilocular smooth cyst ≥10cm, CS <4",
                    management="US specialist, MRI, or per gyn-oncologist protocol",
                    imaging_followup="Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist",
                    clinical_followup="Gynecologist with gyn-oncologist consultation",
                )
            else:
                return ORADSResult(
                    score=3,
                    category="Low Risk - Multilocular",
                    risk="1–<10%",
                    description="Multilocular smooth cyst <10cm, CS <4",
                    management="Gynecologist consultation",
                    imaging_followup="Consider follow-up US within 6 months if not excised",
                    clinical_followup="Gynecologist",
                )


# =============================================================================
# DECISION TREE STRUCTURE
# =============================================================================


def build_decision_tree() -> dict[str, DecisionNode]:
    """Build and return the complete O-RADS decision tree."""

    nodes: dict[str, DecisionNode] = {}

    # =========================================================================
    # ROOT NODE - First Level Question
    # =========================================================================
    nodes["root"] = DecisionNode(
        id="root",
        question="What do you see?",
        options=[
            DecisionOption(
                label="Normal ovary / Physiologic cyst",
                description="No lesion, follicle ≤3cm, or corpus luteum",
                result=ORADS_1,
            ),
            DecisionOption(
                label="Incomplete study",
                description="Cannot characterize due to technical factors",
                result=ORADS_0,
            ),
            DecisionOption(
                label="Simple cyst",
                description="Unilocular, anechoic, smooth walls",
                next_node_id="simple_cyst_size",
            ),
            DecisionOption(
                label="Classic benign lesion",
                description="Hemorrhagic cyst, dermoid, endometrioma, or extraovarian",
                next_node_id="classic_benign_type",
            ),
            DecisionOption(
                label="Cystic lesion (non-classic)",
                description="Unilocular non-simple, bilocular, or multilocular",
                next_node_id="cystic_solid",
            ),
            DecisionOption(
                label="Solid mass",
                description="≥80% solid lesion",
                next_node_id="solid_contour",
            ),
            DecisionOption(
                label="Ascites / Peritoneal nodules",
                description="Not due to other known etiologies",
                result=ORADS_5_ASCITES,
            ),
        ],
    )

    # =========================================================================
    # BRANCH A: SIMPLE CYST
    # =========================================================================
    nodes["simple_cyst_size"] = DecisionNode(
        id="simple_cyst_size",
        question="What is the size of the simple cyst?",
        options=[
            DecisionOption(label="≤3 cm", next_node_id="simple_cyst_small_menopause"),
            DecisionOption(
                label=">3 cm to 5 cm", next_node_id="simple_cyst_medium_menopause"
            ),
            DecisionOption(
                label=">5 cm but <10 cm", result=simple_cyst_result(">5cm_<10cm", None)
            ),
            DecisionOption(label="≥10 cm", result=simple_cyst_result(">=10cm", None)),
        ],
    )

    nodes["simple_cyst_small_menopause"] = DecisionNode(
        id="simple_cyst_small_menopause",
        question="Menopausal status?",
        options=[
            DecisionOption(
                label="Premenopausal",
                description="Physiologic follicle",
                result=simple_cyst_result("<=3cm", MenopauseStatus.PREMENOPAUSAL),
            ),
            DecisionOption(
                label="Postmenopausal",
                result=simple_cyst_result(
                    "<=3cm", MenopauseStatus.EARLY_POSTMENOPAUSAL
                ),
            ),
        ],
    )

    nodes["simple_cyst_medium_menopause"] = DecisionNode(
        id="simple_cyst_medium_menopause",
        question="Menopausal status?",
        options=[
            DecisionOption(
                label="Premenopausal",
                result=simple_cyst_result(">3cm_to_5cm", MenopauseStatus.PREMENOPAUSAL),
            ),
            DecisionOption(
                label="Postmenopausal",
                result=simple_cyst_result(
                    ">3cm_to_5cm", MenopauseStatus.EARLY_POSTMENOPAUSAL
                ),
            ),
        ],
    )

    # =========================================================================
    # BRANCH B: CLASSIC BENIGN LESIONS
    # =========================================================================
    nodes["classic_benign_type"] = DecisionNode(
        id="classic_benign_type",
        question="Which classic benign lesion?",
        options=[
            DecisionOption(
                label="Hemorrhagic cyst",
                description="Reticular pattern or retractile clot, no internal vascularity",
                next_node_id="hemorrhagic_menopause",
            ),
            DecisionOption(
                label="Dermoid cyst",
                description="Hyperechoic with shadowing, lines/dots, or floating spheres",
                next_node_id="dermoid_size",
            ),
            DecisionOption(
                label="Endometrioma",
                description="Homogeneous ground-glass echoes, smooth walls",
                next_node_id="endometrioma_size",
            ),
            DecisionOption(
                label="Paraovarian cyst",
                description="Simple cyst separate from ovary",
                result=PARAOVARIAN_CYST,
            ),
            DecisionOption(
                label="Peritoneal inclusion cyst",
                description="Fluid conforming to adjacent organs, ovary at margin",
                result=PERITONEAL_INCLUSION_CYST,
            ),
            DecisionOption(
                label="Hydrosalpinx",
                description="Anechoic fluid-filled tubular structure",
                result=HYDROSALPINX,
            ),
        ],
    )

    # Hemorrhagic Cyst Branch
    nodes["hemorrhagic_menopause"] = DecisionNode(
        id="hemorrhagic_menopause",
        question="Menopausal status?",
        options=[
            DecisionOption(label="Premenopausal", next_node_id="hemorrhagic_pre_size"),
            DecisionOption(
                label="Early postmenopausal",
                description="<5 years or age 50-55",
                result=HEMORRHAGIC_CYST_EARLY_POST,
            ),
            DecisionOption(
                label="Late postmenopausal",
                description="≥5 years or age ≥55",
                result=HEMORRHAGIC_CYST_LATE_POST,
            ),
        ],
    )

    nodes["hemorrhagic_pre_size"] = DecisionNode(
        id="hemorrhagic_pre_size",
        question="Size of hemorrhagic cyst?",
        options=[
            DecisionOption(label="≤5 cm", result=HEMORRHAGIC_CYST_PRE_SMALL),
            DecisionOption(label=">5 cm but <10 cm", result=HEMORRHAGIC_CYST_PRE_LARGE),
            DecisionOption(
                label="≥10 cm",
                result=ORADSResult(
                    score=3,
                    category="Typical Hemorrhagic Cyst (Large)",
                    risk="1–<10%",
                    description="Hemorrhagic cyst ≥10cm",
                    management="Gynecologist consultation",
                    imaging_followup="Follow-up US within 6 months if not excised",
                    clinical_followup="Gynecologist",
                ),
            ),
        ],
    )

    # Dermoid Branch
    nodes["dermoid_size"] = DecisionNode(
        id="dermoid_size",
        question="Size of dermoid cyst?",
        options=[
            DecisionOption(label="≤3 cm", result=DERMOID_SMALL),
            DecisionOption(label=">3 cm but <10 cm", result=DERMOID_MEDIUM),
            DecisionOption(label="≥10 cm", result=DERMOID_LARGE),
        ],
    )

    # Endometrioma Branch
    nodes["endometrioma_size"] = DecisionNode(
        id="endometrioma_size",
        question="Size of endometrioma?",
        options=[
            DecisionOption(label="<10 cm", next_node_id="endometrioma_menopause"),
            DecisionOption(label="≥10 cm", result=ENDOMETRIOMA_LARGE),
        ],
    )

    nodes["endometrioma_menopause"] = DecisionNode(
        id="endometrioma_menopause",
        question="Menopausal status?",
        options=[
            DecisionOption(label="Premenopausal", result=ENDOMETRIOMA_PRE),
            DecisionOption(label="Postmenopausal", result=ENDOMETRIOMA_POST),
        ],
    )

    # =========================================================================
    # BRANCH C: CYSTIC LESIONS (Non-Classic) - The Complex Tree
    # =========================================================================
    nodes["cystic_solid"] = DecisionNode(
        id="cystic_solid",
        question="Does the cyst have solid component(s)?",
        options=[
            DecisionOption(
                label="Yes - solid component(s) present",
                description="Solid tissue ≥3mm protruding into lumen",
                next_node_id="cystic_solid_locules",
            ),
            DecisionOption(
                label="No - no solid component",
                description="May have internal echoes or incomplete septa",
                next_node_id="cystic_nosolid_locules",
            ),
        ],
    )

    # WITH Solid Component
    nodes["cystic_solid_locules"] = DecisionNode(
        id="cystic_solid_locules",
        question="Number of locules?",
        options=[
            DecisionOption(label="Unilocular", next_node_id="cystic_solid_uni_pp"),
            DecisionOption(
                label="Bilocular or Multilocular", next_node_id="cystic_solid_multi_cs"
            ),
        ],
    )

    nodes["cystic_solid_uni_pp"] = DecisionNode(
        id="cystic_solid_uni_pp",
        question="Number of papillary projections?",
        options=[
            DecisionOption(
                label="<4 papillary projections (or non-pp solid)",
                result=cystic_lesion_result("unilocular", True, "smooth", False, 1, 0),
            ),
            DecisionOption(
                label="≥4 papillary projections",
                result=cystic_lesion_result("unilocular", True, "smooth", False, 1, 4),
            ),
        ],
    )

    nodes["cystic_solid_multi_cs"] = DecisionNode(
        id="cystic_solid_multi_cs",
        question="Color Score (vascularity)?",
        options=[
            DecisionOption(
                label="CS 1-2 (no/minimal flow)",
                result=cystic_lesion_result("bilocular", True, "smooth", False, 2),
            ),
            DecisionOption(
                label="CS 3-4 (moderate/strong flow)",
                result=cystic_lesion_result("bilocular", True, "smooth", False, 3),
            ),
        ],
    )

    # WITHOUT Solid Component
    nodes["cystic_nosolid_locules"] = DecisionNode(
        id="cystic_nosolid_locules",
        question="Number of locules?",
        options=[
            DecisionOption(
                label="Unilocular",
                description="Non-simple (internal echoes or incomplete septa)",
                next_node_id="cystic_nosolid_uni_wall",
            ),
            DecisionOption(label="Bilocular", next_node_id="cystic_nosolid_bi_wall"),
            DecisionOption(
                label="Multilocular",
                description="≥3 locules",
                next_node_id="cystic_nosolid_multi_wall",
            ),
        ],
    )

    nodes["cystic_nosolid_uni_wall"] = DecisionNode(
        id="cystic_nosolid_uni_wall",
        question="Inner wall character?",
        options=[
            DecisionOption(
                label="Smooth", next_node_id="cystic_nosolid_uni_smooth_size"
            ),
            DecisionOption(
                label="Irregular",
                description="Wall irregularity <3mm height",
                result=cystic_lesion_result("unilocular", False, "irregular", False, 1),
            ),
        ],
    )

    nodes["cystic_nosolid_uni_smooth_size"] = DecisionNode(
        id="cystic_nosolid_uni_smooth_size",
        question="Size?",
        options=[
            DecisionOption(
                label="<10 cm",
                result=cystic_lesion_result("unilocular", False, "smooth", False, 1),
            ),
            DecisionOption(
                label="≥10 cm",
                result=cystic_lesion_result("unilocular", False, "smooth", True, 1),
            ),
        ],
    )

    nodes["cystic_nosolid_bi_wall"] = DecisionNode(
        id="cystic_nosolid_bi_wall",
        question="Inner wall/septation character?",
        options=[
            DecisionOption(
                label="Smooth", next_node_id="cystic_nosolid_bi_smooth_size"
            ),
            DecisionOption(
                label="Irregular",
                result=cystic_lesion_result("bilocular", False, "irregular", False, 1),
            ),
        ],
    )

    nodes["cystic_nosolid_bi_smooth_size"] = DecisionNode(
        id="cystic_nosolid_bi_smooth_size",
        question="Size?",
        options=[
            DecisionOption(
                label="<10 cm",
                result=cystic_lesion_result("bilocular", False, "smooth", False, 1),
            ),
            DecisionOption(
                label="≥10 cm",
                result=cystic_lesion_result("bilocular", False, "smooth", True, 1),
            ),
        ],
    )

    nodes["cystic_nosolid_multi_wall"] = DecisionNode(
        id="cystic_nosolid_multi_wall",
        question="Inner wall/septation character?",
        options=[
            DecisionOption(
                label="Smooth", next_node_id="cystic_nosolid_multi_smooth_size"
            ),
            DecisionOption(
                label="Irregular",
                result=cystic_lesion_result(
                    "multilocular", False, "irregular", False, 1
                ),
            ),
        ],
    )

    nodes["cystic_nosolid_multi_smooth_size"] = DecisionNode(
        id="cystic_nosolid_multi_smooth_size",
        question="Size and Color Score?",
        options=[
            DecisionOption(
                label="<10 cm and CS <4",
                result=cystic_lesion_result("multilocular", False, "smooth", False, 1),
            ),
            DecisionOption(
                label="≥10 cm and CS <4",
                result=cystic_lesion_result("multilocular", False, "smooth", True, 1),
            ),
            DecisionOption(
                label="Any size with CS 4",
                result=cystic_lesion_result("multilocular", False, "smooth", False, 4),
            ),
        ],
    )

    # =========================================================================
    # BRANCH D: SOLID MASS
    # =========================================================================
    nodes["solid_contour"] = DecisionNode(
        id="solid_contour",
        question="External contour of solid mass?",
        options=[
            DecisionOption(label="Smooth", next_node_id="solid_smooth_shadowing"),
            DecisionOption(
                label="Irregular",
                description="Non-uniform/uneven outer margin",
                result=solid_mass_result("irregular", False, 1),
            ),
        ],
    )

    nodes["solid_smooth_shadowing"] = DecisionNode(
        id="solid_smooth_shadowing",
        question="Posterior acoustic shadowing?",
        options=[
            DecisionOption(
                label="Yes - broad/diffuse shadowing",
                next_node_id="solid_smooth_shadow_cs",
            ),
            DecisionOption(
                label="No shadowing", next_node_id="solid_smooth_noshadow_cs"
            ),
        ],
    )

    nodes["solid_smooth_shadow_cs"] = DecisionNode(
        id="solid_smooth_shadow_cs",
        question="Color Score (vascularity)?",
        options=[
            DecisionOption(
                label="CS 1 (no flow)", result=solid_mass_result("smooth", True, 1)
            ),
            DecisionOption(
                label="CS 2-3 (minimal/moderate flow)",
                result=solid_mass_result("smooth", True, 2),
            ),
            DecisionOption(
                label="CS 4 (very strong flow)",
                result=solid_mass_result("smooth", True, 4),
            ),
        ],
    )

    nodes["solid_smooth_noshadow_cs"] = DecisionNode(
        id="solid_smooth_noshadow_cs",
        question="Color Score (vascularity)?",
        options=[
            DecisionOption(
                label="CS 1 (no flow)", result=solid_mass_result("smooth", False, 1)
            ),
            DecisionOption(
                label="CS 2-3 (minimal/moderate flow)",
                result=solid_mass_result("smooth", False, 2),
            ),
            DecisionOption(
                label="CS 4 (very strong flow)",
                result=solid_mass_result("smooth", False, 4),
            ),
        ],
    )

    return nodes


class DecisionTreeNavigator:
    """Navigator for traversing the O-RADS decision tree."""

    def __init__(self):
        self.nodes = build_decision_tree()
        self.history: list[str] = []
        self.current_node_id = "root"

    @property
    def current_node(self) -> DecisionNode:
        return self.nodes[self.current_node_id]

    def select_option(self, option_index: int) -> ORADSResult | None:
        """
        Select an option at the current node.

        Returns:
            ORADSResult if this selection leads to a final result,
            None if navigating to another decision node.
        """
        if option_index < 0 or option_index >= len(self.current_node.options):
            raise IndexError(f"Invalid option index: {option_index}")

        option = self.current_node.options[option_index]
        self.history.append(self.current_node_id)

        if option.result is not None:
            return option.result

        if option.next_node_id is not None:
            self.current_node_id = option.next_node_id
            return None

        raise ValueError("Option has neither result nor next_node_id")

    def go_back(self) -> bool:
        """
        Go back to the previous node.

        Returns:
            True if successfully went back, False if already at root.
        """
        if not self.history:
            return False

        self.current_node_id = self.history.pop()
        return True

    def reset(self):
        """Reset to the root node."""
        self.history.clear()
        self.current_node_id = "root"

    def get_breadcrumbs(self) -> list[str]:
        """Get the path taken through the tree."""
        return [self.nodes[node_id].question or "Start" for node_id in self.history]
