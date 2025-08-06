# 🤖 Text-to-SQL Chatbot using LLMs

![Image](https://github.com/user-attachments/assets/6bc2171a-fc42-42eb-978c-13c75189b0f7)

Transform natural language into SQL with the power of Large Language Models.

---

## 🧠 Overview

This project builds an intelligent **Text-to-SQL chatbot** designed for **non-technical users** to query SQL databases using natural language. Unlike traditional tools, this chatbot leverages **LLMs** (Large Language Models) to understand queries like _"What is the total revenue in 2025?"_ and converts them into executable SQL statements — without writing a single line of SQL manually.

✅ **Domain-agnostic** — works with any business vertical  
✅ **LLM-powered** — dynamic natural language to SQL translation  
✅ **Scalable** — test across multiple models and evaluation metrics  

---

## 🚩 Problem Statement

Companies of all sizes generate massive datasets. These are typically stored in SQL databases, but **non-technical teams** often lack both access and SQL knowledge to retrieve meaningful insights.

While developers use tools like MySQL Workbench or Snowflake to write SQL manually, the gap for a **conversational interface** for database querying still exists.

---

## 💡 Solution

This project introduces a **Text-to-SQL chatbot interface** backed by a large language model. It bridges the gap between natural language understanding and structured query generation.

### 🎯 Key Features
- Interact with your SQL database via **plain English**
- Convert NL queries → SQL → Results
- Plug-and-play support for **MySQL**, with extensions possible for other RDBMS
- **Evaluate and compare** results against ground truth
- Extendable pipeline to test **multiple LLMs**

---

## 🔧 Tech Stack

| Tool / Framework | Purpose                         |
|------------------|----------------------------------|
| 🐍 Python         | Orchestration & backend logic    |
| 🤖 Langgraph     | Agents    |
| 💬 LLMs (OpenAI, etc.) | Natural language to SQL parsing |
| 🗃️ MySQL Workbench | SQL database creation            |
| 📊 Excel Data     | Source data for testing          |

---

## 🛠️ Project Workflow

1. **Data Preparation**  
   Load multiple Excel sheets (sales, revenue, budget) into a MySQL database.

2. **Schema Analysis**  
   Understand the tables and relationships to prepare realistic business questions.

3. **Question Design**  
   Curate 5–10 NL questions with known ground-truth SQL outputs.

4. **Model Pipeline Setup**  
   Build a backend pipeline to:
   - Connect to MySQL
   - Send user query to LLM
   - Generate SQL
   - Execute and return results

5. **Evaluation & Metrics**  
   Compare model-generated outputs vs. ground-truth using performance metrics.

6. **Model Experimentation**  
   Swap LLMs, tweak parameters, and benchmark performance.

---

## 💻 Sample Code Snippet

```python
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)
cursor = connection.cursor()
