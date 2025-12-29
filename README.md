# O-RADS Ultrasound Decision Tree

A cross-platform decision tree application for O-RADS (Ovarian-Adnexal Reporting and Data System) ultrasound risk stratification. Built with [Toga/Beeware](https://beeware.org/) for mobile, web, and desktop compatibility.

## Overview

The O-RADS system provides standardized terminology and risk stratification for adnexal (ovarian and para-ovarian) lesions found on ultrasound. This application guides radiologists through an optimized decision tree to arrive at the correct O-RADS score with minimal clicks.

**Key Design Philosophy:**
- Experienced radiologists already know what they're looking at—they just need efficient O-RADS scoring
- The decision tree asks only relevant questions to reach the final score
- Each terminal node provides both the score AND specific follow-up recommendations

## Installation

```bash
# Using uv (recommended)
uv sync
uv run orads        # CLI version
uv run orads-gui    # GUI version

# Or with pip
pip install -e .
orads               # CLI version
orads-gui           # GUI version
```

## Usage

### CLI Mode
```bash
uv run orads
# or
python -m orads.cli
```

### GUI Mode
```bash
uv run orads-gui
# or
python main.py --gui
```

---

# O-RADS Decision Tree Structure

## First Level: "What do you see?"

The decision tree begins with 7 primary categories that capture what an experienced radiologist immediately recognizes:

| # | Category | Destination | Typical Clicks |
|---|----------|-------------|----------------|
| 1 | Normal ovary / Physiologic cyst | → **O-RADS 1** (done) | 1 |
| 2 | Incomplete study | → **O-RADS 0** (done) | 1 |
| 3 | Simple cyst | → Branch A (size/menopause) | 2-3 |
| 4 | Classic benign lesion | → Branch B (which type) | 2-3 |
| 5 | Cystic lesion (non-classic) | → Branch C (complex tree) | 3-5 |
| 6 | Solid mass | → Branch D (contour/shadowing/CS) | 2-3 |
| 7 | Ascites / Peritoneal nodules | → **O-RADS 5** (done) | 1 |

---

## O-RADS Score Summary

| Score | Category | Risk of Malignancy | General Management |
|-------|----------|-------------------|-------------------|
| **0** | Incomplete | N/A | Repeat US or MRI |
| **1** | Normal | N/A | None |
| **2** | Almost Certainly Benign | <1% | Surveillance based on size |
| **3** | Low Risk | 1–<10% | Gynecologist; consider imaging |
| **4** | Intermediate Risk | 10–<50% | US specialist/MRI; gyn-oncology consult |
| **5** | High Risk | ≥50% | Gyn-oncologist |

---

## Branch A: Simple Cyst

```
Simple Cyst
│
├─ Size ≤3 cm
│   ├─ Premenopausal → O-RADS 1 (Follicle)
│   └─ Postmenopausal → O-RADS 2 (No follow-up)
│
├─ Size >3 cm to 5 cm
│   ├─ Premenopausal → O-RADS 2 (No follow-up)
│   └─ Postmenopausal → O-RADS 2 (Follow-up US 12 months)
│
├─ Size >5 cm but <10 cm
│   └─ Any → O-RADS 2 (Follow-up US 12 months)
│
└─ Size ≥10 cm
    └─ Any → O-RADS 3 (Gynecologist; US within 6 months)
```

**Key Insight:** Menopausal status only matters for cysts ≤5 cm, where it affects follow-up timing.

---

## Branch B: Classic Benign Lesions

Classic benign lesions have characteristic appearances that experienced radiologists can identify:

### Hemorrhagic Cyst
- **Definition:** Unilocular, no internal vascularity, with reticular pattern OR retractile clot
- **Premenopausal:**
  - ≤5 cm → O-RADS 2 (No follow-up)
  - >5 cm to <10 cm → O-RADS 2 (Follow-up 2-3 months)
- **Early Postmenopausal (<5 years):**
  - <10 cm → O-RADS 2 (Confirm with follow-up/specialist/MRI)
- **Late Postmenopausal (≥5 years):**
  - → Recategorize (hemorrhagic cysts shouldn't occur)

### Dermoid Cyst (Mature Cystic Teratoma)
- **Definition:** ≤3 locules, no internal vascularity, with:
  - Hyperechoic component with shadowing, OR
  - Hyperechoic lines and dots, OR
  - Floating echogenic spherical structures
- **Scoring by Size:**
  - ≤3 cm → O-RADS 2 (May consider 12-month follow-up)
  - >3 cm to <10 cm → O-RADS 2 (12-month follow-up if not excised)
  - ≥10 cm → O-RADS 3 (Gynecologist consultation)

### Endometrioma
- **Definition:** ≤3 locules, no internal vascularity, homogeneous ground-glass echoes, smooth walls
- **Premenopausal <10 cm:** O-RADS 2 (12-month follow-up)
- **Postmenopausal <10 cm:** O-RADS 2 (Confirm diagnosis first)
- **Any ≥10 cm:** O-RADS 3 (Gynecologist consultation)

### Extraovarian Classic Benign Lesions
All are **O-RADS 2** with no imaging follow-up required:
- **Paraovarian Cyst:** Simple cyst separate from ovary
- **Peritoneal Inclusion Cyst:** Fluid conforming to adjacent organs with ovary at margin
- **Hydrosalpinx:** Anechoic tubular structure (± incomplete septa, ± endosalpingeal folds)

---

## Branch C: Cystic Lesions (Non-Classic)

This is the most complex branch, following radiologists' natural assessment order:

```
Cystic Lesion (Non-Classic)
│
├─ Solid component(s) present? (≥3mm into lumen)
│   │
│   ├─ YES (has solid)
│   │   │
│   │   ├─ Unilocular
│   │   │   ├─ <4 papillary projections (or non-pp solid) → O-RADS 4
│   │   │   └─ ≥4 papillary projections → O-RADS 5
│   │   │
│   │   └─ Bilocular or Multilocular
│   │       ├─ CS 1-2 → O-RADS 4
│   │       └─ CS 3-4 → O-RADS 5
│   │
│   └─ NO (no solid)
│       │
│       ├─ Unilocular
│       │   ├─ Smooth → Size-based scoring
│       │   │   ├─ <10 cm → O-RADS 2
│       │   │   └─ ≥10 cm → O-RADS 3
│       │   └─ Irregular → O-RADS 3
│       │
│       ├─ Bilocular
│       │   ├─ Smooth → Size-based scoring
│       │   │   ├─ <10 cm → O-RADS 2
│       │   │   └─ ≥10 cm → O-RADS 3
│       │   └─ Irregular → O-RADS 4
│       │
│       └─ Multilocular
│           ├─ Irregular (any) → O-RADS 4
│           └─ Smooth
│               ├─ <10 cm, CS <4 → O-RADS 3
│               ├─ ≥10 cm, CS <4 → O-RADS 4
│               └─ Any size, CS 4 → O-RADS 4
```

### Key Definitions for Cystic Lesions

| Term | Definition |
|------|------------|
| **Solid component** | Protrudes ≥3mm into cyst lumen from wall/septation |
| **Papillary projection** | Solid component surrounded by fluid on 3 sides |
| **Smooth** | Uniform/even inner margin |
| **Irregular** | Non-uniform inner margin; focal wall thickening <3mm |
| **Bilocular** | 2 locules (1 complete septation) |
| **Multilocular** | ≥3 locules (≥2 complete septations) |
| **CS (Color Score)** | 1=none, 2=minimal, 3=moderate, 4=very strong flow |

---

## Branch D: Solid Mass (≥80% Solid)

```
Solid Mass
│
├─ External Contour
│   │
│   ├─ IRREGULAR → O-RADS 5 (any size, any CS)
│   │
│   └─ SMOOTH
│       │
│       ├─ Posterior Shadowing?
│       │   │
│       │   ├─ YES (with shadowing)
│       │   │   ├─ CS 1 → O-RADS 3
│       │   │   ├─ CS 2-3 → O-RADS 3
│       │   │   └─ CS 4 → O-RADS 5
│       │   │
│       │   └─ NO (no shadowing)
│       │       ├─ CS 1 → O-RADS 3
│       │       ├─ CS 2-3 → O-RADS 4
│       │       └─ CS 4 → O-RADS 5
```

**Key Insight:** For smooth solid lesions, shadowing + low vascularity suggests benign (fibroma/thecoma).

---

## Important Caveats

1. **Ascites/Peritoneal Nodules:** If present and not explained by other etiologies, upgrades O-RADS 3 and 4 lesions to **O-RADS 5**.

2. **Atypical Features:** If a "classic benign" lesion has atypical features, recategorize using the cystic or solid lexicon descriptors.

3. **Menopausal Status:**
   - Only asked when it changes the recommendation
   - Definition: ≥1 year amenorrhea
   - If uncertain or uterus absent: use age >50 as postmenopausal
   - Early postmenopausal: <5 years (or age 50-55)
   - Late postmenopausal: ≥5 years (or age ≥55)

4. **When Uncertain:** Use the higher risk category to score the lesion.

5. **Size Measurement:** Use single largest diameter for scoring; average linear dimension for interval change.

---

## Management by O-RADS Score

### O-RADS 0 (Incomplete)
- **Imaging:** Repeat US or MRI
- **Clinical:** As indicated

### O-RADS 1 (Normal)
- **Imaging:** None
- **Clinical:** None

### O-RADS 2 (Almost Certainly Benign)
- **Imaging:** Based on specific lesion type and size (see tables)
- **Clinical:** Gynecologist as needed

### O-RADS 3 (Low Risk)
- **Imaging:** Consider follow-up US within 6 months if not excised; may consider US specialist or MRI
- **Clinical:** Gynecologist

### O-RADS 4 (Intermediate Risk)
- **Imaging:** US specialist (if available), OR MRI with O-RADS MRI score, OR per gyn-oncologist
- **Clinical:** Gynecologist with gyn-oncologist consultation

### O-RADS 5 (High Risk)
- **Imaging:** Per gyn-oncologist protocol
- **Clinical:** Gyn-oncologist

---

## References

- O-RADS™ US v2022 Assessment Categories (ACR, November 2022)
- O-RADS™ US v2022 Lexicon Categories, Terms, and Definitions (ACR, January 2023)
- O-RADS™ US v2022 Governing Concepts (ACR, November 2022)

---

## Project Structure

```
o-rads/
├── assets/                    # Reference PDFs and images
│   ├── Assessment_Algorithm.pdf
│   ├── Assessment_Categories.pdf
│   ├── Governing_Concepts.pdf
│   └── Lexicon.pdf
├── orads/
│   ├── __init__.py
│   ├── app.py                # Toga GUI application
│   ├── cli.py                # Terminal CLI application
│   └── decision_tree.py      # Core decision tree logic
├── main.py                   # Entry point
├── pyproject.toml            # Dependencies and scripts
├── PLAN.md                   # Original planning document
└── README.md                 # This file
```

## License

MIT License

## Disclaimer

This application is intended as a reference tool for trained medical professionals. It does not replace clinical judgment or the official O-RADS documentation. Always refer to the original ACR O-RADS publications for the authoritative guidelines.

