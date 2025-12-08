# 🚀 **Day 1: Foundation & Optimization**

**Phase:** Week 1 (Core Engineering & Architecture)
**Focus:** Algorithmic Patterns, Spark Internals, and Local AI Inference.
**Estimated Time:** 2 Hours

---

### **1. Objectives**
* **Algorithmic Proficiency:** Master the "Key Generation" pattern for handling grouped data, a prerequisite for understanding distributed shuffle operations.
* **Data Engineering Internals:** Deepen understanding of **Data Skew**, its impact on distributed systems, and remediation strategies like **Salting**.
* **AI Engineering Setup:** Establish a local Large Language Model (LLM) environment for private, cost-free inference.

---

### **2. Technical Execution Tasks**

#### **2.1 Algorithmic Challenge (DSA)**
* **Problem:** Group Anagrams (LeetCode #49).
* **Engineering Context:** This problem simulates the logic required for **MapReduce** and **Spark Shuffle** operations (grouping data by a derived key).
* **Requirement:** Implement a solution using a Hash Map strategy where `Key = Signature` (e.g., sorted string or character count) and `Value = List of Strings`.
* **Success Metric:** Pass all test cases with optimal time complexity ($O(N \cdot K)$ or $O(N \cdot K \log K)$).

#### **2.2 Spark Optimization (Architecture)**
* **Topic:** Performance Tuning in Distributed Systems.
* **Resource:** Databricks Academy / Official Documentation.
* **Key Concepts to Master:**
    * **Data Skew:** Identification of straggler tasks in the Spark UI.
    * **Salting:** The architectural pattern of adding high-cardinality noise to keys to force uniform partition distribution.
    * **Catalyst Optimizer:** High-level understanding of join strategies (Broadcast vs. Sort-Merge).

#### **2.3 GenAI Environment (Local Inference)**
* **Tool:** Ollama / Local LLM.
* **Action:**
    1.  Deploy a local model (e.g., `llama3`, `mistral`).
    2.  Develop a Python interface script to query the model programmatically.
* **Validation:** Successfully execute a prompt asking for a technical definition (e.g., *"Explain Data Lakehouse architecture"*).

---

### **3. Portfolio Deliverables**

To complete Day 1, the following artifacts must be committed to the repository `data-engineering-portfolio-2026`:

1.  **`DSA/Group_Anagrams.py`**:
    * Contains the optimized Python solution for the algorithm.
    * Includes comments explaining the Time/Space complexity.

2.  **`Week1/Day1/JOURNAL.md`**:
    * **Engineering Log:** A structured summary of the day's work.
    * **Optimization Notes:** A concise explanation (3-5 bullet points) of **how Salting mitigates Data Skew**.
    * **AI Validation:** A log entry confirming the local model's successful response.

---

### **4. Self-Review Checklist**
- [ ] Algorithm passes all edge cases (empty strings, single characters).
- [ ] "Salting" concept is clearly understood and documented.
- [ ] Local AI environment is operational for future agentic workflows.
- [ ] All artifacts are pushed to the `main` branch.

---

### 🛡️ **Mentor Check-In (Unlock Day 2)**

**To proceed to Day 2, please submit:**
1.  The link to your `JOURNAL.md` file.
2.  A brief answer to this verification question:
    * *"In a Salted Join, if you salt the skew key with a range of 1-5, by what factor does the size of the skewed partition theoretically decrease?"*
