import streamlit as st

# Page configuration
st.set_page_config(page_title="Powerplexity Enhanced Chat", page_icon="💬", layout="wide")

# Feedback Modal Configuration
if 'open_modal' not in st.session_state:
    st.session_state['open_modal'] = False

if 'show_sources' not in st.session_state:
    st.session_state['show_sources'] = False

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

# Button to Open the Sources Modal View
if st.button("📚 View Sources"):
    st.session_state['show_sources'] = True

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
        # Additional sources can be added here...
    ]

# Check if we need to show the sources modal
if st.session_state['show_sources']:
    st.subheader("🔍 Sources")
    st.markdown("These are the sources for the information provided in the response above. Select any that you'd like to explore further:")

    sources = get_sources()

    # Displaying each source with detailed information
    for source in sources:
        st.checkbox(
            label=f"**{source['title']}**",
            value=False,
            key=source['title']
        )
        st.markdown(f"Publisher: {source['publisher']}")
        st.markdown(f"Date: {source['date']}")
        st.markdown(f"Summary: {source['summary']}")
        st.markdown(f"[View full article]({source['link']})", unsafe_allow_html=True)
        st.markdown("---")

    # Button to close the modal
    if st.button("Close Sources"):
        st.session_state['show_sources'] = False

# Feedback Button to Open Feedback Modal
if st.button("🛠️ Provide Feedback"):
    st.session_state['open_modal'] = True

# Display the Feedback Modal
if st.session_state['open_modal']:
    with st.expander("🛠️ Help us improve this response", expanded=True):
        st.markdown("### 🛠️ Help us improve this response")
        st.write("Select all that apply:")
        feedback_options = [
            "Imprecise", 
            "Not updated", 
            "Too short", 
            "Too long", 
            "Harmful or offensive", 
            "Not useful"
        ]
        selected_feedback = [st.checkbox(option) for option in feedback_options]
        additional_feedback = st.text_area("How can we improve the response? (Optional)")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Submit Feedback"):
                if any(selected_feedback):
                    st.success("Thank you for your feedback!")
                    st.session_state['open_modal'] = False
                else:
                    st.warning("Please select at least one feedback option.")
        with col2:
            if st.button("Cancel Feedback"):
                st.session_state['open_modal'] = False

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
