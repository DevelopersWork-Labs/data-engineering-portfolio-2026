Got it — here is a **clean, fresh, non-concluded Day 1 Task Card**, written as if **nothing has been started yet**.
No references to previous screenshots, no assumptions — fully reset, ready to begin **from scratch at 7 Dec 2025**.

---

# ⭐ **DAY 1 TASK CARD — 7 DEC 2025 (Weekend Mode, Fresh Start)**

**Total Time: ~5 Hours**
**Goal:** Begin the 12-week journey with a strong, structured foundation across repo setup, PySpark, DSA, and GenAI fundamentals.

---

# ✅ **SECTION A — Repo + Databricks Setup (60–75 mins)**

### **1. Create a new GitHub repository**

**Name:** `data-engineering-portfolio`

Create these folders inside it:

```
week1/
project1_lakehouse/
project2_streaming/
project3_genai_rag/
notebooks/
dsa/
docs/
```

### **2. Add a README.md**

Include:

* Short introduction
* Goals of the 12-week journey
* Placeholder for projects

### **3. Open Databricks Free Edition**

Go to: [https://www.databricks.com/try-databricks](https://www.databricks.com/try-databricks)

Then:

* Click **Workspace → Add → Notebook**
* Name: `day1_intro_pyspark`
* Language: **Python**
* Compute: **Serverless SQL Warehouse** (it supports PySpark)

### **4. Test PySpark Execution**

Run:

```python
spark.range(5).show()
```

---

# 🔥 **SECTION B — DSA Warm-up (75–90 mins)**

Solve **6 problems today** in total:

### **Hashing (2 easy)**

Examples:

* Check if array contains duplicate
* Frequency mapping problem

### **Arrays (2 easy)**

Examples:

* Reverse array
* Find max/min

### **Arrays (2 medium)**

Examples:

* Two Sum
* Move Zeroes
* Pair sum (two pointers)
* Kadane (intro level)

### **Create DSA Notes File**

Path: `dsa/notes_day1.md`

Write short notes on:

* What hashing is used for
* Two pointers pattern
* Sliding window basics

---

# 🔧 **SECTION C — PySpark Hands-On (90 mins)**

Create folder:
`notebooks/day1/`

### **Notebook #1 — PySpark Basics**

Include:

```python
df = spark.createDataFrame([(1, "A"), (2, "B")], ["id", "val"])
df.show()
df.select("val").show()
df.withColumn("id2", df.id * 10).show()
df.explain()
```

### **Notebook #2 — Joins + Explain Plan**

Include:

```python
df1 = spark.createDataFrame([(1, "x"), (2, "y")], ["id", "val1"])
df2 = spark.createDataFrame([(1, "p"), (3, "q")], ["id", "val2"])

df1.join(df2, "id", "inner").show()
df1.join(df2, "id", "left").show()

from pyspark.sql.functions import broadcast
df1.join(broadcast(df2), "id").explain("formatted")
```

Add both notebooks to GitHub.

---

# 🧠 **SECTION D — GenAI Light Foundations (45 mins)**

Add a section in your notes (Master Notes):

Write definitions for:

* Embeddings
* Cosine similarity
* Chunking
* Retrieval
* RAG (Retrieval-Augmented Generation) 5-step workflow

### **Optional Small Experiment**

If you want to try embeddings:

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
model.encode(["Day 1 embedding test"])
```

---

# 🏗 **SECTION E — Project 1 Setup (30 mins)**

Inside `project1_lakehouse/`, create:

```
bronze/
silver/
gold/
docs/
notebooks/
```

Create a file:
`project1_lakehouse/docs/architecture.md`

Start with:

* What is Medallion Architecture
* Bronze layer purpose
* Silver layer purpose
* Gold layer purpose

---

# 🎯 **DAY 1 – REQUIRED PROOFS BEFORE WE UNLOCK DAY 2**

At the end of today, send:

### ✔ GitHub repo link

### ✔ Screenshot of PySpark notebook running `spark.range(5).show()`

### ✔ Screenshots of Notebook #1 and Notebook #2

### ✔ Screenshots of 6 solved DSA problems

### ✔ Screenshot of GenAI notes

### ✔ Screenshot of `architecture.md` (with at least a draft)

---

# 🔋 **Optional Stretch Tasks**

If your energy is good:

* Add a Medallion Architecture diagram using draw.io
* Add `.gitignore` to repo
* Solve one extra medium DSA problem

---

# 📝 **Daily Check-in Template (Use at end of Day 1)**

```
📅 Daily Check-in – Day 1 (7 Dec 2025)

1️⃣ Completed Today:
- 
- 
- 

2️⃣ Proofs:
- GitHub link:
- DSA screenshots:
- PySpark notebook screenshots:
- Notes screenshots:

3️⃣ Blockers:
-

4️⃣ Energy Level:
Low / Medium / High
```

---

If you need a **Day 1 PDF**, just say:

**“Generate Day 1 Task Card PDF”**
