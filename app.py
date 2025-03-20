import streamlit as st
import openai

# Streamlit UI
st.title("🛠️ AI-Powered DBA SQL Query Generator")

# API Key Input
api_key = st.text_input("🔑 Enter your OpenAI API key:", type="password")

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
        st.error("❌ Please enter your OpenAI API key!")
    elif not query_description:
        st.error("❌ Please describe your DBA request!")
    else:
        try:
            # Set API Key
            openai.api_key = api_key

            # System instruction for AI
            system_prompt = f"You are an expert {db_type} DBA. Generate only {db_type} SQL queries for {query_type} without explanation."

            # Full user request
            full_prompt = f"Generate a {query_type} SQL query for {db_type}. {query_description}"

            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": full_prompt}
                ]
            )

            # Display Generated Query
            st.subheader("✅ Generated SQL Query:")
            st.code(response["choices"][0]["message"]["content"], language="sql")

        except Exception as e:
            st.error(f"🚨 Error: {e}")
