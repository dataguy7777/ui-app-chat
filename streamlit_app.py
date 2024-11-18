import streamlit as st

# Page configuration
st.set_page_config(page_title="Powerplexity Enhanced Chat", page_icon="💬", layout="wide")

# Initialize session state for feedback selections
if 'selected_feedback' not in st.session_state:
    st.session_state['selected_feedback'] = []

# Sidebar (optional)
with st.sidebar:
    st.title("Powerplexity Chat")
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

# Roll/Unroll all sources using st.expander (without nesting)
with st.expander("📚 Sources", expanded=False):
    st.markdown("These are the sources for the information provided in the response above. Expand to view the sources:")

    # Function to simulate retrieving sources
    def get_sources():
        return [
            {
                "title": "Red Sea crisis - Wikipedia",
                "link": "https://en.wikipedia.org/wiki/Red_Sea_crisis",
                "summary": "The Red Sea crisis began in October 2023, involving Houthi movements in Yemen launching attacks at Israel.",
                "publisher": "Wikipedia",
                "date": "October 19, 2023"
            },
            {
                "title": "Houthi Red Sea attacks still torment global trade, a year after October 7",
                "link": "https://www.aljazeera.com/news/houthi-red-sea-attacks",
                "summary": "Yemen's rebel group has launched over 130 attacks in the Red Sea since October 7.",
                "publisher": "Al Jazeera",
                "date": "October 7, 2024"
            },
            {
                "title": "Who are the Houthis and why are they attacking Red Sea ships?",
                "link": "https://www.bbc.com/news/houthis-red-sea",
                "summary": "The Houthis have launched over 40 attacks on commercial ships in the Red Sea and Gulf of Aden.",
                "publisher": "BBC",
                "date": "November 1, 2023"
            },
        ]

    sources = get_sources()

    # Displaying each source without nested expanders
    for source in sources:
        st.markdown(f"### 🔗 [{source['title']}]({source['link']})")
        st.markdown(f"**Publisher**: {source['publisher']}")
        st.markdown(f"**Date**: {source['date']}")
        st.markdown(f"**Summary**: {source['summary']}")
        st.markdown("---")

# Feedback Section using st.expander
with st.expander("🛠️ Provide Feedback", expanded=False):
    st.markdown("**Help Us Improve This Response**")
    st.markdown("Select all that apply:")

    # Feedback options
    feedback_options = {
        "imprecise": "⚠️ Imprecise",
        "not_updated": "🔄 Not updated",
        "too_short": "📏 Too short",
        "too_long": "📜 Too long",
        "harmful_offensive": "🚨 Harmful or offensive",
        "not_useful": "❌ Not useful"
    }

    # Arrange checkboxes in three columns
    cols = st.columns(3)
    for idx, (key, label) in enumerate(feedback_options.items()):
        with cols[idx % 3]:
            if st.checkbox(label, key=f"checkbox_{key}"):
                if key not in st.session_state['selected_feedback']:
                    st.session_state['selected_feedback'].append(key)
            else:
                if key in st.session_state['selected_feedback']:
                    st.session_state['selected_feedback'].remove(key)

    # Additional feedback textarea
    additional_feedback = st.text_area("How can we improve the response? (Optional)", height=100, key="additional_feedback_expander")

    # Submit and Cancel buttons
    submit_cancel_cols = st.columns(2)
    with submit_cancel_cols[0]:
        if st.button("Submit Feedback", key="submit_feedback_expander"):
            if st.session_state['selected_feedback']:
                # Handle the feedback (e.g., save to database or send via email)
                st.success("Thank you for your feedback!")
                # Reset feedback state
                st.session_state['selected_feedback'] = []
                st.experimental_rerun()
            else:
                st.warning("Please select at least one feedback option.")
    with submit_cancel_cols[1]:
        if st.button("Cancel Feedback", key="cancel_feedback_expander"):
            st.session_state['selected_feedback'] = []
            st.experimental_rerun()

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

