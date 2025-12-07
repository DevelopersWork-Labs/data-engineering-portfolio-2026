# ⭐ **DAY 1 QUICK TASK CARD — 7 DEC 2025 (Weekend Mode)**

**Total Time: ~5 hours**
**Goal: Strong foundation + repo setup + PySpark warm-up + DSA + GenAI basics**

---

# ✅ **SECTION A — Repo + Environment Setup (60–75 mins)**

### ✔ Tasks

* ☐ Create GitHub repo: **`data-engineering-portfolio`**
* ☐ Add folders:

  ```
  week1/
  project1_lakehouse/
  project2_streaming/
  project3_genai_rag/
  notebooks/
  dsa/
  docs/
  ```
* ☐ Add README.md (short intro + goals)
* ☐ Open Databricks Community Edition
* ☐ Create cluster: **`de-learning-cluster`**
* ☐ Create notebook `day1_intro_pyspark`
* ☐ Run:

  ```python
  spark.range(5).show()
  ```

---

# 🔥 **SECTION B — DSA Deep Warm-up (75–90 mins)**

### ✔ Tasks

Solve **6 problems**:

* ☐ 2 × Hashing (easy)
* ☐ 2 × Arrays (easy)
* ☐ 2 × Arrays (medium: two pointers/sliding window)

### ✔ Notes

* ☐ Create `dsa/notes_day1.md`
* ☐ Add short notes on:

  * Hashing
  * Two pointers
  * Sliding window

---

# 🔧 **SECTION C — PySpark Hands-on (90 mins)**

### ✔ Notebook #1 — PySpark Basics

* ☐ DataFrame creation
* ☐ select / filter / withColumn
* ☐ `.explain()` → screenshot it

### ✔ Notebook #2 — Joins

* ☐ inner join
* ☐ left join
* ☐ broadcast join
* ☐ `.explain(mode="formatted")` → compare

Upload both notebooks to `/notebooks/day1/`.

---

# 🧠 **SECTION D — GenAI Light Foundations (45 mins)**

### ✔ Add to Master Notes:

* ☐ What is an embedding?
* ☐ What is cosine similarity?
* ☐ What is chunking?
* ☐ What is retrieval?
* ☐ RAG 5-step flow

### (Optional but recommended)

* ☐ Run HuggingFace embedding test:

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
model.encode(["Day 1 embedding test"])
```

---

# 🏗 **SECTION E — Project 1 Setup (30 mins)**

### ✔ Tasks

Inside `project1_lakehouse/` add:

```
bronze/
silver/
gold/
docs/
notebooks/
```

* ☐ Create **architecture.md**
  Include:

  * Medallion architecture explanation
  * Bronze → Silver → Gold definitions

---

# 🎯 **REQUIRED PROOFS TO SUBMIT FOR DAY 1 COMPLETION**

When done, send:

### ✔ GitHub repo link

### ✔ Screenshot of Databricks CE workspace

### ✔ Screenshot of `spark.range(5).show()`

### ✔ 6 DSA problems (screenshots)

### ✔ Notebooks #1 & #2 (upload + link or screenshot)

### ✔ GenAI notes screenshot

### ✔ `architecture.md` screenshot
