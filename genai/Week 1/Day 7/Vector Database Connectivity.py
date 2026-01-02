# Databricks notebook source
# MAGIC %md
# MAGIC ## 1️⃣ Install & import

# COMMAND ----------

# MAGIC %pip install pinecone

# COMMAND ----------

import pinecone

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2️⃣ Initialize client

# COMMAND ----------

# MAGIC %env PINECONE_API_KEY=<PINECONE_API_KEY>

# COMMAND ----------

import os
from pinecone import Pinecone

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
assert PINECONE_API_KEY is not None

pc = Pinecone(api_key=PINECONE_API_KEY)

# COMMAND ----------

# MAGIC %md
# MAGIC ## ✅ Step 3: Create a Demo Index (Hello Vector)

# COMMAND ----------

from pinecone import ServerlessSpec

index_name = "day7-hello-vector"
if index_name not in pc.list_indexes():
  pc.create_index(
    name=index_name,
    dimension=3,
    metric="cosine",
    spec=ServerlessSpec(
      cloud="aws",
      region="us-east-1"
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## ✅ Step 4: Upsert a Dummy Vector

# COMMAND ----------

index = pc.Index(index_name)

index.upsert([
    ("vec1", [0.1, 0.2, 0.3], {"text": "hello vector db"})
])


# COMMAND ----------

# MAGIC %md
# MAGIC ## ✅ Step 5: Query It Back

# COMMAND ----------

index.query(
    vector=[0.1, 0.2, 0.29],
    top_k=1,
    include_metadata=True
)