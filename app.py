import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

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

            # AI prompt customization
            system_prompt = f"You are an expert {db_type} DBA. Generate only {db_type} SQL queries for {query_type} without explanation."
            full_prompt = f"Generate a {query_type} SQL query for {db_type}. {query_description}"

            # Call OpenAI API
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": full_prompt}
                ]
            )

            # Extract response safely
            generated_query = response.choices[0].message.content if response.choices else "⚠️ No query generated."

            # Display Generated Query
            st.subheader("✅ Generated SQL Query:")
            st.code(generated_query, language="sql")

        except openai.OpenAIError as api_err:
            st.error(f"🚨 OpenAI API Error: {api_err}")
        except Exception as e:
            st.error(f"🚨 Unexpected Error: {e}")
