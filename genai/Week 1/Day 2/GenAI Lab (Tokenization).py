# Databricks notebook source
# MAGIC %md
# MAGIC ## Step 1️⃣ — Install & Import

# COMMAND ----------

# MAGIC %pip install tiktoken

# COMMAND ----------

import tiktoken

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2️⃣ — Load a tokenizer

# COMMAND ----------

enc = tiktoken.get_encoding("cl100k_base")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3️⃣ — Tokenize simple text vs number

# COMMAND ----------

text_word = "Data"
text_number = "794625452451"

print("Word tokens:", enc.encode(text_word))
print("Number tokens:", enc.encode(text_number))

print("Word token count:", len(enc.encode(text_word)))
print("Number token count:", len(enc.encode(text_number)))

# COMMAND ----------

# MAGIC %md
# MAGIC **Output:**
# MAGIC ```
# MAGIC Word tokens: [1061]
# MAGIC Number tokens: [25926, 15894, 21098, 20360]
# MAGIC Word token count: 1
# MAGIC Number token count: 4
# MAGIC ```

# COMMAND ----------

enc.encode("2024-09-18T12:45:33Z")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🧠 WHY THIS HAPPENS (This is the core insight)
# MAGIC **LLM tokenizers are:**
# MAGIC - Optimized for natural language
# MAGIC - Trained on common word patterns
# MAGIC - BAD at long, random-looking numbers
# MAGIC
# MAGIC **So:**
# MAGIC - `Data` → seen millions of times → single token
# MAGIC - `794625452451` → rare pattern → split into chunks