"""
Converted from Jupyter Notebook
"""

# ============================
# All Imports
# ============================

import os
from typing import List, Dict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
from chonkie import OpenAIEmbeddings

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)


# ============================
# Set the API Key
# ============================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



# ============================
# Embeddings
# ============================
embeddings=OpenAIEmbeddings()
text="Hello Testing the embedding"
test_vector=embeddings.embed(text)

print(f"Embedding Dimebsion:{len(test_vector)}")
print(f"Sample embeddings :{test_vector[:5]}")


# ============================
# Reading Files
# ============================

with open ("new_data/sample_research_paper.txt","r") as file:
    research_paper_text=file.read()

with open("new_data/sample_code.py","r")as file:
    code_text=file.read()

with open("new_data/sample_table.md","r")as file:
    table_text=file.read()

with open("new_data/sample_technical_doc.txt","r")as file:
    technical_doc_text=file.read()

print(f"Technical Doc: {len(technical_doc_text):,} characters")
print(f"Research Paper: {len(research_paper_text):,} characters")
print(f"Code Sample: {len(code_text):,} characters")
print(f"Table Sample: {len(table_text):,} characters")