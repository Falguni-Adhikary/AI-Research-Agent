import streamlit as st

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

st.title("🧠 AI Research Assistant (Internal Agent Prototype)")

text = st.text_area("Paste your research text here:", height=200)

def generate_summary(text):
    sentences = text.split(".")
    short_summary = ". ".join(sentences[:2])
    return short_summary

def extract_key_points(text):
    words = text.split()
    return list(set(words[:5]))

def generate_questions(text):
    return [
        "What is the main objective of the study?",
        "What methodology was used?",
        "What are the key findings?",
        "What are the limitations?",
        "What future scope exists?"
    ]

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
            st.subheader("❓ Possible Questions")
            for q in generate_questions(text):
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