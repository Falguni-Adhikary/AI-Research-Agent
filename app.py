import streamlit as st
from utils import generate_summary, extract_key_points, generate_questions

st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.markdown("### 🔄 Workflow")
st.markdown("""
1. Input Research Text  
2. System Analyzes Structure  
3. Generates Summary  
4. Extracts Keywords  
5. Creates Analytical Questions  
""")

st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.title("🧠 AI Research Assistant")
st.markdown("Transform research text into structured insights.")
st.divider()

text = st.text_area("Paste your research text here:", height=200)


if st.button("Generate Insights"):
    if text.strip() == "":
        st.warning("Please paste some text.")
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📌 Summary")
            st.write(generate_summary(text))

            st.subheader("🔑 Key Points")
            for point in extract_key_points(text):
                st.write(f"- {point}")

        with col2:
            st.subheader("❓ Analytical Questions")
            for q in generate_questions():
                st.write(f"- {q}")

        st.success("Insights Generated Successfully!")
        st.markdown("---")
st.markdown("### 🧩 Agent Design Logic")
st.markdown("""
This prototype simulates an internal AI research assistant designed to:
- Process long-form academic content
- Extract structured insights
- Generate analytical prompts
- Support decision-making workflows

Future enhancements would include LLM integration and PDF ingestion.
""")