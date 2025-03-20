import streamlit as st
import openai
import os

# Try loading API key from Streamlit Secrets or .env (for local execution)
api_key = os.getenv("OPENAI_API_KEY", st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else None)

# Streamlit UI
st.title("🛠️ AI-Powered DBA SQL Query Generator")

# Select Database Type
db_type = st.selectbox("🗄️ Select Database", ["Oracle", "MySQL", "PostgreSQL"])

# DBA Query Type Selection
query_type = st.selectbox("⚙️ Select DBA Task", [
    "Database Health Checks",
    "Security Audits",
    "Disaster Recovery Queries",
    "Tablespace & Storage Analysis"
])

# Natural Language Input
query_description = st.text_area("📝 Describe what you need in plain English:")

if st.button("🚀 Generate DBA Query"):
    if not api_key:
        st.error("❌ OpenAI API key is missing! Add it to Streamlit Secrets or a `.env` file.")
    elif not query_description:
        st.error("❌ Please describe your DBA request!")
    else:
        try:
            # Initialize OpenAI client
            client = openai.OpenAI(api_key=api_key)

    
