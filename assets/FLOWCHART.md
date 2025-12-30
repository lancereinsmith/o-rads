# O-RADS Decision Tree - Complete Path Reference

This document lists **every possible path** through the O-RADS decision tree application, along with the resulting O-RADS score and management recommendations.

---

## Table of Contents

1. [Quick Reference: O-RADS Score Summary](#quick-reference-o-rads-score-summary)
2. [Path 1: Normal Ovary / Physiologic Cyst](#path-1-normal-ovary--physiologic-cyst)
3. [Path 2: Incomplete Study](#path-2-incomplete-study)
4. [Path 3: Simple Cyst (Branch A)](#path-3-simple-cyst-branch-a)
5. [Path 4: Classic Benign Lesions (Branch B)](#path-4-classic-benign-lesions-branch-b)
6. [Path 5: Cystic Lesion Non-Classic (Branch C)](#path-5-cystic-lesion-non-classic-branch-c)
7. [Path 6: Solid Mass (Branch D)](#path-6-solid-mass-branch-d)
8. [Path 7: Ascites / Peritoneal Nodules](#path-7-ascites--peritoneal-nodules)

---

## Quick Reference: O-RADS Score Summary

| Score | Category | Risk | Color |
|-------|----------|------|-------|
| **0** | Incomplete Evaluation | N/A | ⬜ Gray |
| **1** | Normal Ovary | N/A | 🟢 Green |
| **2** | Almost Certainly Benign | <1% | 🟢 Light Green |
| **3** | Low Risk | 1–<10% | 🟡 Yellow |
| **4** | Intermediate Risk | 10–<50% | 🟠 Orange |
| **5** | High Risk | ≥50% | 🔴 Red |

---

## Path 1: Normal Ovary / Physiologic Cyst

**Clicks: 1**

```
ROOT → "Normal ovary / Physiologic cyst"
```

### Result: O-RADS 1

| Field | Value |
|-------|-------|
| **Score** | 1 |
| **Category** | Normal Ovary |
| **Risk** | N/A |
| **Description** | No ovarian lesion; physiologic cyst (follicle ≤3cm or corpus luteum) |
| **Management** | None required |
| **Imaging Follow-up** | None |
| **Clinical Follow-up** | None |
| **IMPRESSION** | No ovarian lesion; physiologic cyst (follicle ≤3cm or corpus luteum) (O-RADS 1): No further imaging follow-up. |

---

## Path 2: Incomplete Study

**Clicks: 1**

```
ROOT → "Incomplete study"
```

### Result: O-RADS 0

| Field | Value |
|-------|-------|
| **Score** | 0 |
| **Category** | Incomplete Evaluation |
| **Risk** | N/A |
| **Description** | Lesion features cannot be accurately characterized due to technical factors |
| **Management** | Repeat US study or MRI |
| **Imaging Follow-up** | Repeat ultrasound study or consider MRI |
| **Clinical Follow-up** | As clinically indicated |
| **IMPRESSION** | Lesion features cannot be accurately characterized due to technical factors (O-RADS 0): Repeat ultrasound study or consider MRI |

---

## Path 3: Simple Cyst (Branch A)

### Path 3.1: Simple Cyst ≤3 cm, Premenopausal

**Clicks: 3**

```
ROOT → "Simple cyst" → "≤3 cm" → "Premenopausal"
```

#### Result: O-RADS 1

| Field | Value |
|-------|-------|
| **Score** | 1 |
| **Category** | Physiologic - Follicle |
| **Risk** | N/A |
| **Description** | Simple cyst ≤3cm in premenopausal patient (follicle) |
| **Management** | None required |
| **Imaging Follow-up** | None |
| **Clinical Follow-up** | None |
| **IMPRESSION** | Simple cyst ≤3cm in premenopausal patient (follicle) (O-RADS 1): No further imaging follow-up. |

---

### Path 3.2: Simple Cyst ≤3 cm, Postmenopausal

**Clicks: 3**

```
ROOT → "Simple cyst" → "≤3 cm" → "Postmenopausal"
```

#### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Almost Certainly Benign |
| **Risk** | <1% |
| **Description** | Simple cyst ≤3cm in postmenopausal patient |
| **Management** | Routine follow-up |
| **Imaging Follow-up** | None |
| **Clinical Follow-up** | None |
| **IMPRESSION** | Simple cyst ≤3cm in postmenopausal patient (O-RADS 2): No further imaging follow-up. |

---

### Path 3.3: Simple Cyst >3 cm to 5 cm, Premenopausal

**Clicks: 3**

```
ROOT → "Simple cyst" → ">3 cm to 5 cm" → "Premenopausal"
```

#### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Almost Certainly Benign |
| **Risk** | <1% |
| **Description** | Simple cyst >3cm to 5cm |
| **Management** | Imaging surveillance if postmenopausal |
| **Imaging Follow-up** | None |
| **Clinical Follow-up** | None |
| **IMPRESSION** | Simple cyst >3cm to 5cm (O-RADS 2): No further imaging follow-up. |

---

### Path 3.4: Simple Cyst >3 cm to 5 cm, Postmenopausal

**Clicks: 3**

```
ROOT → "Simple cyst" → ">3 cm to 5 cm" → "Postmenopausal"
```

#### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Almost Certainly Benign |
| **Risk** | <1% |
| **Description** | Simple cyst >3cm to 5cm |
| **Management** | Imaging surveillance if postmenopausal |
| **Imaging Follow-up** | Follow-up US in 12 months |
| **Clinical Follow-up** | None |
| **IMPRESSION** | Simple cyst >3cm to 5cm (O-RADS 2): Follow-up US in 12 months |

---

### Path 3.5: Simple Cyst >5 cm but <10 cm

**Clicks: 2**

```
ROOT → "Simple cyst" → ">5 cm but <10 cm"
```

#### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Almost Certainly Benign |
| **Risk** | <1% |
| **Description** | Simple cyst >5cm but <10cm |
| **Management** | Imaging surveillance |
| **Imaging Follow-up** | Follow-up US in 12 months |
| **Clinical Follow-up** | As clinically indicated |
| **IMPRESSION** | Simple cyst >5cm but <10cm (O-RADS 2): Follow-up US in 12 months |

---

### Path 3.6: Simple Cyst ≥10 cm

**Clicks: 2**

```
ROOT → "Simple cyst" → "≥10 cm"
```

#### Result: O-RADS 3

| Field | Value |
|-------|-------|
| **Score** | 3 |
| **Category** | Low Risk |
| **Risk** | 1–<10% |
| **Description** | Simple cyst ≥10cm |
| **Management** | Gynecologist consultation; consider follow-up imaging |
| **Imaging Follow-up** | Consider follow-up US within 6 months if not surgically excised |
| **Clinical Follow-up** | Gynecologist |
| **IMPRESSION** | Simple cyst ≥10cm (O-RADS 3): Consider follow-up US within 6 months if not surgically excised |

---

## Path 4: Classic Benign Lesions (Branch B)

### Path 4.1: Hemorrhagic Cyst

#### Path 4.1.1: Hemorrhagic Cyst, Premenopausal, ≤5 cm

**Clicks: 4**

```
ROOT → "Classic benign lesion" → "Hemorrhagic cyst" → "Premenopausal" → "≤5 cm"
```

##### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Typical Hemorrhagic Cyst |
| **Risk** | <1% |
| **Description** | Hemorrhagic cyst ≤5cm, premenopausal |
| **Management** | None required |
| **Imaging Follow-up** | None |
| **Clinical Follow-up** | Gynecologist as needed |
| **IMPRESSION** | Hemorrhagic cyst ≤5cm, premenopausal (O-RADS 2): No further imaging follow-up. |

---

#### Path 4.1.2: Hemorrhagic Cyst, Premenopausal, >5 cm but <10 cm

**Clicks: 4**

```
ROOT → "Classic benign lesion" → "Hemorrhagic cyst" → "Premenopausal" → ">5 cm but <10 cm"
```

##### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Typical Hemorrhagic Cyst |
| **Risk** | <1% |
| **Description** | Hemorrhagic cyst >5cm but <10cm, premenopausal |
| **Management** | Short-term follow-up to confirm resolution |
| **Imaging Follow-up** | Follow-up US in 2-3 months |
| **Clinical Follow-up** | Gynecologist as needed |
| **IMPRESSION** | Hemorrhagic cyst >5cm but <10cm, premenopausal (O-RADS 2): Follow-up US in 2-3 months |

---

#### Path 4.1.3: Hemorrhagic Cyst, Premenopausal, ≥10 cm

**Clicks: 4**

```
ROOT → "Classic benign lesion" → "Hemorrhagic cyst" → "Premenopausal" → "≥10 cm"
```

##### Result: O-RADS 3

| Field | Value |
|-------|-------|
| **Score** | 3 |
| **Category** | Typical Hemorrhagic Cyst (Large) |
| **Risk** | 1–<10% |
| **Description** | Hemorrhagic cyst ≥10cm |
| **Management** | Gynecologist consultation |
| **Imaging Follow-up** | Follow-up US within 6 months if not excised |
| **Clinical Follow-up** | Gynecologist |
| **IMPRESSION** | Hemorrhagic cyst ≥10cm (O-RADS 3): Follow-up US within 6 months if not excised |

---

#### Path 4.1.4: Hemorrhagic Cyst, Early Postmenopausal

**Clicks: 3**

```
ROOT → "Classic benign lesion" → "Hemorrhagic cyst" → "Early postmenopausal"
```

##### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Typical Hemorrhagic Cyst |
| **Risk** | <1% |
| **Description** | Hemorrhagic cyst <10cm, early postmenopausal |
| **Management** | Confirm diagnosis; may need additional imaging |
| **Imaging Follow-up** | Follow-up US in 2-3 months, or US specialist, or MRI |
| **Clinical Follow-up** | Gynecologist as needed |
| **IMPRESSION** | Hemorrhagic cyst <10cm, early postmenopausal (O-RADS 2): Follow-up US in 2-3 months, or US specialist, or MRI |

---

#### Path 4.1.5: Hemorrhagic Cyst, Late Postmenopausal

**Clicks: 3**

```
ROOT → "Classic benign lesion" → "Hemorrhagic cyst" → "Late postmenopausal"
```

##### Result: O-RADS 3

| Field | Value |
|-------|-------|
| **Score** | 3 |
| **Category** | Atypical - Recategorize |
| **Risk** | 1–<10% |
| **Description** | Should not occur in late postmenopausal; recategorize using other lexicon descriptors |
| **Management** | Recategorize lesion using cystic lesion descriptors |
| **Imaging Follow-up** | Reassess with other lexicon descriptors |
| **Clinical Follow-up** | Gynecologist consultation recommended |
| **IMPRESSION** | Should not occur in late postmenopausal; recategorize using other lexicon descriptors (O-RADS 3): Reassess with other lexicon descriptors |

---

### Path 4.2: Dermoid Cyst

#### Path 4.2.1: Dermoid Cyst ≤3 cm

**Clicks: 3**

```
ROOT → "Classic benign lesion" → "Dermoid cyst" → "≤3 cm"
```

##### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Typical Dermoid Cyst |
| **Risk** | <1% |
| **Description** | Dermoid cyst ≤3cm |
| **Management** | May consider surveillance |
| **Imaging Follow-up** | May consider follow-up US in 12 months |
| **Clinical Follow-up** | Gynecologist as needed |
| **IMPRESSION** | Dermoid cyst ≤3cm (O-RADS 2): May consider follow-up US in 12 months |

---

#### Path 4.2.2: Dermoid Cyst >3 cm but <10 cm

**Clicks: 3**

```
ROOT → "Classic benign lesion" → "Dermoid cyst" → ">3 cm but <10 cm"
```

##### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Typical Dermoid Cyst |
| **Risk** | <1% |
| **Description** | Dermoid cyst >3cm but <10cm |
| **Management** | Surveillance or surgical excision |
| **Imaging Follow-up** | Follow-up US in 12 months if not surgically excised |
| **Clinical Follow-up** | Gynecologist as needed |
| **IMPRESSION** | Dermoid cyst >3cm but <10cm (O-RADS 2): Follow-up US in 12 months if not surgically excised |

---

#### Path 4.2.3: Dermoid Cyst ≥10 cm

**Clicks: 3**

```
ROOT → "Classic benign lesion" → "Dermoid cyst" → "≥10 cm"
```

##### Result: O-RADS 3

| Field | Value |
|-------|-------|
| **Score** | 3 |
| **Category** | Typical Dermoid Cyst |
| **Risk** | 1–<10% |
| **Description** | Dermoid cyst ≥10cm |
| **Management** | Gynecologist consultation; consider surgery or close follow-up |
| **Imaging Follow-up** | Consider follow-up US within 6 months if not excised |
| **Clinical Follow-up** | Gynecologist |
| **IMPRESSION** | Dermoid cyst ≥10cm (O-RADS 3): Consider follow-up US within 6 months if not excised |

---

### Path 4.3: Endometrioma

#### Path 4.3.1: Endometrioma <10 cm, Premenopausal

**Clicks: 4**

```
ROOT → "Classic benign lesion" → "Endometrioma" → "<10 cm" → "Premenopausal"
```

##### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Typical Endometrioma |
| **Risk** | <1% |
| **Description** | Endometrioma <10cm, premenopausal |
| **Management** | Surveillance or surgical excision |
| **Imaging Follow-up** | Follow-up US in 12 months if not surgically excised |
| **Clinical Follow-up** | Gynecologist as needed |
| **IMPRESSION** | Endometrioma <10cm, premenopausal (O-RADS 2): Follow-up US in 12 months if not surgically excised |

---

#### Path 4.3.2: Endometrioma <10 cm, Postmenopausal

**Clicks: 4**

```
ROOT → "Classic benign lesion" → "Endometrioma" → "<10 cm" → "Postmenopausal"
```

##### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Typical Endometrioma |
| **Risk** | <1% |
| **Description** | Endometrioma <10cm, postmenopausal (initial) |
| **Management** | Confirm diagnosis, then surveillance |
| **Imaging Follow-up** | Follow-up US in 2-3 months (or specialist/MRI), then 12 months if not excised |
| **Clinical Follow-up** | Gynecologist as needed |
| **IMPRESSION** | Endometrioma <10cm, postmenopausal (initial) (O-RADS 2): Follow-up US in 2-3 months (or specialist/MRI), then 12 months if not excised |

---

#### Path 4.3.3: Endometrioma ≥10 cm

**Clicks: 3**

```
ROOT → "Classic benign lesion" → "Endometrioma" → "≥10 cm"
```

##### Result: O-RADS 3

| Field | Value |
|-------|-------|
| **Score** | 3 |
| **Category** | Typical Endometrioma |
| **Risk** | 1–<10% |
| **Description** | Endometrioma ≥10cm |
| **Management** | Gynecologist consultation; consider surgery |
| **Imaging Follow-up** | Consider follow-up US within 6 months if not excised |
| **Clinical Follow-up** | Gynecologist |
| **IMPRESSION** | Endometrioma ≥10cm (O-RADS 3): Consider follow-up US within 6 months if not excised |

---

### Path 4.4: Paraovarian Cyst

**Clicks: 2**

```
ROOT → "Classic benign lesion" → "Paraovarian cyst"
```

#### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Typical Paraovarian Cyst |
| **Risk** | <1% |
| **Description** | Simple cyst separate from the ovary |
| **Management** | None required (extraovarian) |
| **Imaging Follow-up** | None |
| **Clinical Follow-up** | Gynecologist as needed |
| **IMPRESSION** | Simple cyst separate from the ovary (O-RADS 2): No further imaging follow-up. |

---

### Path 4.5: Peritoneal Inclusion Cyst

**Clicks: 2**

```
ROOT → "Classic benign lesion" → "Peritoneal inclusion cyst"
```

#### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Typical Peritoneal Inclusion Cyst |
| **Risk** | <1% |
| **Description** | Fluid collection with ovary at margin or suspended within, conforming to adjacent organs |
| **Management** | None required (extraovarian) |
| **Imaging Follow-up** | None |
| **Clinical Follow-up** | Gynecologist as needed |
| **IMPRESSION** | Fluid collection with ovary at margin or suspended within, conforming to adjacent organs (O-RADS 2): No further imaging follow-up. |

---

### Path 4.6: Hydrosalpinx

**Clicks: 2**

```
ROOT → "Classic benign lesion" → "Hydrosalpinx"
```

#### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Typical Hydrosalpinx |
| **Risk** | <1% |
| **Description** | Anechoic, fluid-filled tubular structure (extraovarian) |
| **Management** | None required (extraovarian) |
| **Imaging Follow-up** | None |
| **Clinical Follow-up** | Gynecologist as needed |
| **IMPRESSION** | Anechoic, fluid-filled tubular structure (extraovarian) (O-RADS 2): No further imaging follow-up. |

---

## Path 5: Cystic Lesion Non-Classic (Branch C)

### Path 5.1: With Solid Component(s)

#### Path 5.1.1: Unilocular with Solid, <4 Papillary Projections

**Clicks: 4**

```
ROOT → "Cystic lesion (non-classic)" → "Yes - solid component(s) present" → "Unilocular" → "<4 papillary projections (or non-pp solid)"
```

##### Result: O-RADS 4

| Field | Value |
|-------|-------|
| **Score** | 4 |
| **Category** | Intermediate Risk - Solid Component |
| **Risk** | 10–<50% |
| **Description** | Unilocular cyst with <4 papillary projections or non-pp solid component |
| **Management** | US specialist, MRI, or per gyn-oncologist protocol |
| **Imaging Follow-up** | Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |
| **Clinical Follow-up** | Gynecologist with gyn-oncologist consultation |
| **IMPRESSION** | Unilocular cyst with <4 papillary projections or non-pp solid component (O-RADS 4): Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |

---

#### Path 5.1.2: Unilocular with Solid, ≥4 Papillary Projections

**Clicks: 4**

```
ROOT → "Cystic lesion (non-classic)" → "Yes - solid component(s) present" → "Unilocular" → "≥4 papillary projections"
```

##### Result: O-RADS 5

| Field | Value |
|-------|-------|
| **Score** | 5 |
| **Category** | High Risk - Multiple Papillary Projections |
| **Risk** | ≥50% |
| **Description** | Unilocular cyst with ≥4 papillary projections |
| **Management** | Refer to gynecologic oncologist |
| **Imaging Follow-up** | Per gyn-oncologist protocol |
| **Clinical Follow-up** | Gyn-oncologist |
| **IMPRESSION** | Unilocular cyst with ≥4 papillary projections (O-RADS 5): Per gyn-oncologist protocol |

---

#### Path 5.1.3: Bi/Multilocular with Solid, CS 1-2

**Clicks: 4**

```
ROOT → "Cystic lesion (non-classic)" → "Yes - solid component(s) present" → "Bilocular or Multilocular" → "CS 1-2 (no/minimal flow)"
```

##### Result: O-RADS 4

| Field | Value |
|-------|-------|
| **Score** | 4 |
| **Category** | Intermediate Risk - Solid Component |
| **Risk** | 10–<50% |
| **Description** | Bilocular cyst with solid component(s), CS 1-2 |
| **Management** | US specialist, MRI, or per gyn-oncologist protocol |
| **Imaging Follow-up** | Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |
| **Clinical Follow-up** | Gynecologist with gyn-oncologist consultation |
| **IMPRESSION** | Bilocular cyst with solid component(s), CS 1-2 (O-RADS 4): Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |

---

#### Path 5.1.4: Bi/Multilocular with Solid, CS 3-4

**Clicks: 4**

```
ROOT → "Cystic lesion (non-classic)" → "Yes - solid component(s) present" → "Bilocular or Multilocular" → "CS 3-4 (moderate/strong flow)"
```

##### Result: O-RADS 5

| Field | Value |
|-------|-------|
| **Score** | 5 |
| **Category** | High Risk - Vascular Solid Component |
| **Risk** | ≥50% |
| **Description** | Bilocular cyst with solid component(s) and CS 3 |
| **Management** | Refer to gynecologic oncologist |
| **Imaging Follow-up** | Per gyn-oncologist protocol |
| **Clinical Follow-up** | Gyn-oncologist |
| **IMPRESSION** | Bilocular cyst with solid component(s) and CS 3 (O-RADS 5): Per gyn-oncologist protocol |

---

### Path 5.2: Without Solid Component - Unilocular

#### Path 5.2.1: Unilocular, Smooth, <10 cm

**Clicks: 5**

```
ROOT → "Cystic lesion (non-classic)" → "No - no solid component" → "Unilocular" → "Smooth" → "<10 cm"
```

##### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Almost Certainly Benign |
| **Risk** | <1% |
| **Description** | Unilocular smooth non-simple cyst <10cm |
| **Management** | Surveillance based on size |
| **Imaging Follow-up** | Follow-up US in 6-12 months based on size |
| **Clinical Follow-up** | None |
| **IMPRESSION** | Unilocular smooth non-simple cyst <10cm (O-RADS 2): Follow-up US in 6-12 months based on size |

---

#### Path 5.2.2: Unilocular, Smooth, ≥10 cm

**Clicks: 5**

```
ROOT → "Cystic lesion (non-classic)" → "No - no solid component" → "Unilocular" → "Smooth" → "≥10 cm"
```

##### Result: O-RADS 3

| Field | Value |
|-------|-------|
| **Score** | 3 |
| **Category** | Low Risk - Large Unilocular |
| **Risk** | 1–<10% |
| **Description** | Unilocular smooth cyst ≥10cm |
| **Management** | Gynecologist consultation |
| **Imaging Follow-up** | Consider follow-up US within 6 months if not excised |
| **Clinical Follow-up** | Gynecologist |
| **IMPRESSION** | Unilocular smooth cyst ≥10cm (O-RADS 3): Consider follow-up US within 6 months if not excised |

---

#### Path 5.2.3: Unilocular, Irregular

**Clicks: 4**

```
ROOT → "Cystic lesion (non-classic)" → "No - no solid component" → "Unilocular" → "Irregular"
```

##### Result: O-RADS 3

| Field | Value |
|-------|-------|
| **Score** | 3 |
| **Category** | Low Risk - Irregular Unilocular |
| **Risk** | 1–<10% |
| **Description** | Unilocular cyst with irregular inner wall (no solid component) |
| **Management** | Consider US specialist or MRI; Gynecologist consultation |
| **Imaging Follow-up** | Consider follow-up US within 6 months if not excised |
| **Clinical Follow-up** | Gynecologist |
| **IMPRESSION** | Unilocular cyst with irregular inner wall (no solid component) (O-RADS 3): Consider follow-up US within 6 months if not excised |

---

### Path 5.3: Without Solid Component - Bilocular

#### Path 5.3.1: Bilocular, Smooth, <10 cm

**Clicks: 5**

```
ROOT → "Cystic lesion (non-classic)" → "No - no solid component" → "Bilocular" → "Smooth" → "<10 cm"
```

##### Result: O-RADS 2

| Field | Value |
|-------|-------|
| **Score** | 2 |
| **Category** | Almost Certainly Benign |
| **Risk** | <1% |
| **Description** | Bilocular smooth cyst <10cm |
| **Management** | Surveillance |
| **Imaging Follow-up** | Follow-up US in 6 months |
| **Clinical Follow-up** | None |
| **IMPRESSION** | Bilocular smooth cyst <10cm (O-RADS 2): Follow-up US in 6 months |

---

#### Path 5.3.2: Bilocular, Smooth, ≥10 cm

**Clicks: 5**

```
ROOT → "Cystic lesion (non-classic)" → "No - no solid component" → "Bilocular" → "Smooth" → "≥10 cm"
```

##### Result: O-RADS 3

| Field | Value |
|-------|-------|
| **Score** | 3 |
| **Category** | Low Risk - Large Bilocular |
| **Risk** | 1–<10% |
| **Description** | Bilocular smooth cyst ≥10cm |
| **Management** | Gynecologist consultation |
| **Imaging Follow-up** | Consider follow-up US within 6 months if not excised |
| **Clinical Follow-up** | Gynecologist |
| **IMPRESSION** | Bilocular smooth cyst ≥10cm (O-RADS 3): Consider follow-up US within 6 months if not excised |

---

#### Path 5.3.3: Bilocular, Irregular

**Clicks: 4**

```
ROOT → "Cystic lesion (non-classic)" → "No - no solid component" → "Bilocular" → "Irregular"
```

##### Result: O-RADS 4

| Field | Value |
|-------|-------|
| **Score** | 4 |
| **Category** | Intermediate Risk - Irregular Bilocular |
| **Risk** | 10–<50% |
| **Description** | Bilocular cyst with irregular inner wall/septation |
| **Management** | US specialist, MRI, or per gyn-oncologist protocol |
| **Imaging Follow-up** | Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |
| **Clinical Follow-up** | Gynecologist with gyn-oncologist consultation |
| **IMPRESSION** | Bilocular cyst with irregular inner wall/septation (O-RADS 4): Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |

---

### Path 5.4: Without Solid Component - Multilocular

#### Path 5.4.1: Multilocular, Smooth, <10 cm, CS <4

**Clicks: 5**

```
ROOT → "Cystic lesion (non-classic)" → "No - no solid component" → "Multilocular" → "Smooth" → "<10 cm and CS <4"
```

##### Result: O-RADS 3

| Field | Value |
|-------|-------|
| **Score** | 3 |
| **Category** | Low Risk - Multilocular |
| **Risk** | 1–<10% |
| **Description** | Multilocular smooth cyst <10cm, CS <4 |
| **Management** | Gynecologist consultation |
| **Imaging Follow-up** | Consider follow-up US within 6 months if not excised |
| **Clinical Follow-up** | Gynecologist |
| **IMPRESSION** | Multilocular smooth cyst <10cm, CS <4 (O-RADS 3): Consider follow-up US within 6 months if not excised |

---

#### Path 5.4.2: Multilocular, Smooth, ≥10 cm, CS <4

**Clicks: 5**

```
ROOT → "Cystic lesion (non-classic)" → "No - no solid component" → "Multilocular" → "Smooth" → "≥10 cm and CS <4"
```

##### Result: O-RADS 4

| Field | Value |
|-------|-------|
| **Score** | 4 |
| **Category** | Intermediate Risk - Large Multilocular |
| **Risk** | 10–<50% |
| **Description** | Multilocular smooth cyst ≥10cm, CS <4 |
| **Management** | US specialist, MRI, or per gyn-oncologist protocol |
| **Imaging Follow-up** | Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |
| **Clinical Follow-up** | Gynecologist with gyn-oncologist consultation |
| **IMPRESSION** | Multilocular smooth cyst ≥10cm, CS <4 (O-RADS 4): Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |

---

#### Path 5.4.3: Multilocular, Smooth, Any Size, CS 4

**Clicks: 5**

```
ROOT → "Cystic lesion (non-classic)" → "No - no solid component" → "Multilocular" → "Smooth" → "Any size with CS 4"
```

##### Result: O-RADS 4

| Field | Value |
|-------|-------|
| **Score** | 4 |
| **Category** | Intermediate Risk - Highly Vascular Multilocular |
| **Risk** | 10–<50% |
| **Description** | Multilocular smooth cyst with CS 4 |
| **Management** | US specialist, MRI, or per gyn-oncologist protocol |
| **Imaging Follow-up** | Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |
| **Clinical Follow-up** | Gynecologist with gyn-oncologist consultation |
| **IMPRESSION** | Multilocular smooth cyst with CS 4 (O-RADS 4): Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |

---

#### Path 5.4.4: Multilocular, Irregular

**Clicks: 4**

```
ROOT → "Cystic lesion (non-classic)" → "No - no solid component" → "Multilocular" → "Irregular"
```

##### Result: O-RADS 4

| Field | Value |
|-------|-------|
| **Score** | 4 |
| **Category** | Intermediate Risk - Irregular Multilocular |
| **Risk** | 10–<50% |
| **Description** | Multilocular cyst with irregular inner wall/septations |
| **Management** | US specialist, MRI, or per gyn-oncologist protocol |
| **Imaging Follow-up** | Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |
| **Clinical Follow-up** | Gynecologist with gyn-oncologist consultation |
| **IMPRESSION** | Multilocular cyst with irregular inner wall/septations (O-RADS 4): Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |

---

## Path 6: Solid Mass (Branch D)

### Path 6.1: Irregular Contour

**Clicks: 2**

```
ROOT → "Solid mass" → "Irregular"
```

#### Result: O-RADS 5

| Field | Value |
|-------|-------|
| **Score** | 5 |
| **Category** | High Risk - Irregular Solid |
| **Risk** | ≥50% |
| **Description** | Solid lesion with irregular contour |
| **Management** | Refer to gynecologic oncologist |
| **Imaging Follow-up** | Per gyn-oncologist protocol |
| **Clinical Follow-up** | Gyn-oncologist |
| **IMPRESSION** | Solid lesion with irregular contour (O-RADS 5): Per gyn-oncologist protocol |

---

### Path 6.2: Smooth Contour with Shadowing

#### Path 6.2.1: Smooth, Shadowing, CS 1

**Clicks: 4**

```
ROOT → "Solid mass" → "Smooth" → "Yes - broad/diffuse shadowing" → "CS 1 (no flow)"
```

##### Result: O-RADS 3

| Field | Value |
|-------|-------|
| **Score** | 3 |
| **Category** | Low Risk - Avascular Solid |
| **Risk** | 1–<10% |
| **Description** | Solid smooth lesion with CS 1 (no flow), ± shadowing |
| **Management** | Consider US specialist or MRI; Gynecologist consultation |
| **Imaging Follow-up** | Consider follow-up US within 6 months if not excised; may consider US specialist or MRI |
| **Clinical Follow-up** | Gynecologist |
| **IMPRESSION** | Solid smooth lesion with CS 1 (no flow), ± shadowing (O-RADS 3): Consider follow-up US within 6 months if not excised; may consider US specialist or MRI |

---

#### Path 6.2.2: Smooth, Shadowing, CS 2-3

**Clicks: 4**

```
ROOT → "Solid mass" → "Smooth" → "Yes - broad/diffuse shadowing" → "CS 2-3 (minimal/moderate flow)"
```

##### Result: O-RADS 3

| Field | Value |
|-------|-------|
| **Score** | 3 |
| **Category** | Low Risk - Shadowing Solid |
| **Risk** | 1–<10% |
| **Description** | Solid smooth lesion with shadowing and CS 2 |
| **Management** | Consider US specialist or MRI; Gynecologist consultation |
| **Imaging Follow-up** | Consider follow-up US within 6 months if not excised |
| **Clinical Follow-up** | Gynecologist |
| **IMPRESSION** | Solid smooth lesion with shadowing and CS 2 (O-RADS 3): Consider follow-up US within 6 months if not excised |

---

#### Path 6.2.3: Smooth, Shadowing, CS 4

**Clicks: 4**

```
ROOT → "Solid mass" → "Smooth" → "Yes - broad/diffuse shadowing" → "CS 4 (very strong flow)"
```

##### Result: O-RADS 5

| Field | Value |
|-------|-------|
| **Score** | 5 |
| **Category** | High Risk - Highly Vascular Solid |
| **Risk** | ≥50% |
| **Description** | Solid smooth lesion with CS 4 (very strong flow) |
| **Management** | Refer to gynecologic oncologist |
| **Imaging Follow-up** | Per gyn-oncologist protocol |
| **Clinical Follow-up** | Gyn-oncologist |
| **IMPRESSION** | Solid smooth lesion with CS 4 (very strong flow) (O-RADS 5): Per gyn-oncologist protocol |

---

### Path 6.3: Smooth Contour without Shadowing

#### Path 6.3.1: Smooth, No Shadowing, CS 1

**Clicks: 4**

```
ROOT → "Solid mass" → "Smooth" → "No shadowing" → "CS 1 (no flow)"
```

##### Result: O-RADS 3

| Field | Value |
|-------|-------|
| **Score** | 3 |
| **Category** | Low Risk - Avascular Solid |
| **Risk** | 1–<10% |
| **Description** | Solid smooth lesion with CS 1 (no flow), ± shadowing |
| **Management** | Consider US specialist or MRI; Gynecologist consultation |
| **Imaging Follow-up** | Consider follow-up US within 6 months if not excised; may consider US specialist or MRI |
| **Clinical Follow-up** | Gynecologist |
| **IMPRESSION** | Solid smooth lesion with CS 1 (no flow), ± shadowing (O-RADS 3): Consider follow-up US within 6 months if not excised; may consider US specialist or MRI |

---

#### Path 6.3.2: Smooth, No Shadowing, CS 2-3

**Clicks: 4**

```
ROOT → "Solid mass" → "Smooth" → "No shadowing" → "CS 2-3 (minimal/moderate flow)"
```

##### Result: O-RADS 4

| Field | Value |
|-------|-------|
| **Score** | 4 |
| **Category** | Intermediate Risk - Vascular Solid |
| **Risk** | 10–<50% |
| **Description** | Solid smooth lesion, non-shadowing, CS 2 |
| **Management** | US specialist, MRI, or per gyn-oncologist protocol |
| **Imaging Follow-up** | Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |
| **Clinical Follow-up** | Gynecologist with gyn-oncologist consultation |
| **IMPRESSION** | Solid smooth lesion, non-shadowing, CS 2 (O-RADS 4): Options: US specialist, MRI with O-RADS MRI score, or per gyn-oncologist |

---

#### Path 6.3.3: Smooth, No Shadowing, CS 4

**Clicks: 4**

```
ROOT → "Solid mass" → "Smooth" → "No shadowing" → "CS 4 (very strong flow)"
```

##### Result: O-RADS 5

| Field | Value |
|-------|-------|
| **Score** | 5 |
| **Category** | High Risk - Highly Vascular Solid |
| **Risk** | ≥50% |
| **Description** | Solid smooth lesion with CS 4 (very strong flow) |
| **Management** | Refer to gynecologic oncologist |
| **Imaging Follow-up** | Per gyn-oncologist protocol |
| **Clinical Follow-up** | Gyn-oncologist |
| **IMPRESSION** | Solid smooth lesion with CS 4 (very strong flow) (O-RADS 5): Per gyn-oncologist protocol |

---

## Path 7: Ascites / Peritoneal Nodules

**Clicks: 1**

```
ROOT → "Ascites / Peritoneal nodules"
```

### Result: O-RADS 5

| Field | Value |
|-------|-------|
| **Score** | 5 |
| **Category** | High Risk - Ascites/Peritoneal Nodules |
| **Risk** | ≥50% |
| **Description** | Ascites and/or peritoneal nodules (not due to other etiologies) |
| **Management** | Refer to gynecologic oncologist |
| **Imaging Follow-up** | Per gyn-oncologist protocol |
| **Clinical Follow-up** | Gyn-oncologist |
| **IMPRESSION** | Ascites and/or peritoneal nodules (not due to other etiologies) (O-RADS 5): Per gyn-oncologist protocol |

---

## Summary Statistics

### Total Unique Paths: 41

| Branch | Number of Paths |
|--------|-----------------|
| Normal/Incomplete/Ascites | 3 |
| Simple Cyst | 6 |
| Classic Benign | 14 |
| Cystic Non-Classic | 12 |
| Solid Mass | 7 |

### Results by O-RADS Score

| Score | Count | Percentage |
|-------|-------|------------|
| O-RADS 0 | 1 | 2.4% |
| O-RADS 1 | 2 | 4.9% |
| O-RADS 2 | 16 | 39.0% |
| O-RADS 3 | 12 | 29.3% |
| O-RADS 4 | 6 | 14.6% |
| O-RADS 5 | 4 | 9.8% |

### Click Depth Distribution

| Clicks | Count |
|--------|-------|
| 1 | 3 |
| 2 | 6 |
| 3 | 9 |
| 4 | 16 |
| 5 | 7 |

---

## Glossary

| Term | Definition |
|------|------------|
| **CS** | Color Score - degree of intralesional vascularity (1=none, 2=minimal, 3=moderate, 4=very strong) |
| **Solid component** | Protrudes ≥3mm into cyst lumen from wall/septation |
| **Papillary projection** | Solid component surrounded by fluid on 3 sides |
| **Unilocular** | Single locule (no complete septa) |
| **Bilocular** | 2 locules (1 complete septation) |
| **Multilocular** | ≥3 locules (≥2 complete septations) |
| **Smooth** | Uniform/even inner margin |
| **Irregular** | Non-uniform inner margin; focal wall thickening <3mm |
| **Shadowing** | Broad or diffuse hypoechogenicity posterior to lesion |
| **Postmenopausal** | ≥1 year amenorrhea (or age >50 if uncertain) |
| **Early postmenopausal** | <5 years postmenopausal (or age 50-55) |
| **Late postmenopausal** | ≥5 years postmenopausal (or age ≥55) |

---

*Generated from O-RADS US v2022 (ACR, November 2022)*
