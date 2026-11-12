
import streamlit as st
import sys
from pathlib import Path

# Add the project root directory to Python's import path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from main import run_research


# Page configuration
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# Application title
st.title("🤖 AI Research Assistant")

st.write(
    "Enter a topic and let our AI agents research, "
    "analyze, and generate a detailed report."
)

# Topic input
topic = st.text_input(
    "Enter your research topic",
    placeholder="Example: Generative AI in Healthcare"
)

# Generate report button
if st.button("Generate Research Report"):

    if topic.strip():

        with st.spinner("Our AI agents are working..."):

            try:
                result = run_research(topic)

                st.success("Research report generated successfully!")

                st.subheader("Your Research Report")
                st.markdown(str(result))

            except Exception as e:
                st.error(f"Something went wrong: {e}")

    else:
        st.warning("Please enter a research topic.")
