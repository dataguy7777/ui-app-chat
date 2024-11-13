import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(page_title="Powerplexity Chat Enhanced Mockup", page_icon="💬", layout="wide")

# Function to simulate retrieving sources
def get_sources():
    return [
        {"title": "Red Sea crisis - Wikipedia", "link": "en.wikipedia.org", "ref_number": 1},
        {"title": "Houthi Red Sea attacks still torment global trade", "link": "aljazeera.com", "ref_number": 2},
        {"title": "Who are the Houthis and why are they attacking Red Sea ships?", "link": "bbc.com", "ref_number": 3},
    ]

# Sidebar (optional)
with st.sidebar:
    st.title("Powerplexity Enhanced Chat")
    st.markdown("**Mockup Chat Application with Enhanced Features**")
    st.markdown("---")
    st.markdown("🔍 **Explore**")
    st.button("Sources")
    st.button("Related Questions")

# Main content: Chat Mockup
st.title("💬 Powerplexity Chat Enhanced Mockup")
st.write("")

# Displaying the response
response = """
The **Red Sea crisis** has emerged as a significant geopolitical conflict since October 19, 2023, 
when the Iran-backed Houthi movement in Yemen initiated a series of missile and drone attacks targeting Israel and commercial vessels in the Red Sea. 
This escalation is closely linked to the ongoing Israel-Hamas war, which began shortly before the Houthis' actions, 
as they declared solidarity with Hamas and aimed to disrupt maritime trade in response to Israel's military operations in Gaza. 
The international community is closely monitoring these developments due to their potential implications for global trade and regional stability. 
"""

st.markdown(response)

# Displaying sources as cards with numbers
st.subheader("📌 Sources")
sources = get_sources()
cols = st.columns(len(sources))

for index, source in enumerate(sources):
    with cols[index]:
        st.markdown(f"**[{source['title']}]({source['link']})**")
        st.markdown(f"Reference: [{source['ref_number']}]")
        st.button(f"View Source {source['ref_number']}")

# Feedback Button & Options
with st.expander("Provide Feedback"):
    st.markdown("### 🛠️ Help us improve this response")
    feedback_options = ["Imprecise", "Not updated", "Too short", "Too long", "Harmful or offensive", "Not useful"]
    feedback = st.multiselect("Select all that apply:", feedback_options)
    additional_feedback = st.text_area("How can we improve the response?", "")
    if st.button("Submit Feedback"):
        if feedback:
            st.success("Thank you for your feedback!")
        else:
            st.warning("Please select at least one feedback option.")

# Related Content Section
st.subheader("🔗 Related Questions")
related_questions = [
    "What is the current status of the Houthi movement?",
    "How are Red Sea maritime routes impacted by recent conflicts?",
    "Who are the key stakeholders in the Red Sea geopolitical situation?"
]
for question in related_questions:
    st.markdown(f"- {question}")

# Footer Section
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    color: #333;
    text-align: center;
    padding: 10px;
}
</style>
<div class="footer">
    <p>© 2024 Powerplexity. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
