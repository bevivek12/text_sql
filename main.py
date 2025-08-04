
import streamlit as st
from langchain.utilities import SQLDatabase
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import create_sql_query_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from urllib.parse import quote_plus
from langchain_core.prompts import ChatPromptTemplate
import pymysql
import ast
import sqlparse

# === Streamlit UI ===
st.title("🧠 Text_to_sql by vivek kumar ganji")
st.subheader("this application is able to connect all tables in seleted database /n and generate required query")

# Database selection
db_options = ['Enterprise_SaaS', 'E_Commerce', 'Analytics']
selected_db = st.selectbox("Choose a database schema", db_options)

# NL query input
user_question = st.text_input("Enter your natural language query")

# --- Configuration ---
host = '127.0.0.1'
port = '3306'
username = 'root'
password = 'Vivek@143'
encoded_password = quote_plus(password)

# --- LangChain SQL Setup ---
mysql_uri = f"mysql+pymysql://{username}:{encoded_password}@{host}:{port}/{selected_db}"
db = SQLDatabase.from_uri(mysql_uri, sample_rows_in_table_info=1)

def get_schema(db):
    return db.get_table_info()

# Prompt template
template = """Based on the table schema below, write a SQL query that would answer the user's question:
Remember : Only provide me the sql query dont include anything else.
           Provide me sql query in a single line dont add line breaks.
Table Schema:
{schema}

Question: {question}
SQL Query:
"""
prompt = ChatPromptTemplate.from_template(template)

# LLM setup
llm = ChatGroq(
    model="moonshotai/Kimi-K2-Instruct",
    api_key=""
)

sql_chain = (
    RunnablePassthrough.assign(schema=lambda _: get_schema(db))
    | prompt
    | llm.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)

# === Button to trigger query ===
if st.button("Generate SQL and Run"):
    if not user_question.strip():
        st.warning("Please enter a natural language query.")
    else:
        with st.spinner("Generating SQL..."):
            try:
                # Step 1: Generate SQL query
                sql_query = sql_chain.invoke({"question": user_question})
                formatted_sql = sqlparse.format(sql_query, reindent=True, keyword_case='upper')
                st.code(formatted_sql, language="sql")

                # Step 2: Run SQL and display result
                result_df = db.run(sql_query)
                if isinstance(result_df, str):
                    lst = ast.literal_eval(result_df)    
                    value = lst

                st.write(value)

            except Exception as e:
                st.error(f"Error: {e}")
