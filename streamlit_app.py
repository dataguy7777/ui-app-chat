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
    st.markdown("These are the files providing detailed information related to the response above. Expand to view the sources:")

    # Function to simulate retrieving file sources
    def get_sources():
        return [
            {
                "title": "Red Sea Crisis Data Analysis",
                "link": "https://example.com/files/red_sea_crisis_data.xlsx",
                "summary": "Comprehensive data analysis of the Red Sea crisis events since October 2023.",
                "publisher": "Powerplexity Analytics",
                "date": "October 19, 2023",
                "file_type": "excel"
            },
            {
                "title": "Houthi Movement Impact Report",
                "link": "https://example.com/files/houthi_impact_report.pdf",
                "summary": "Detailed report on the Houthi movement's activities and their impact on regional stability.",
                "publisher": "Middle East Research Institute",
                "date": "October 7, 2024",
                "file_type": "pdf"
            },
            {
                "title": "Maritime Trade Disruption Statistics",
                "link": "https://example.com/files/maritime_trade_stats.xlsx",
                "summary": "Statistical overview of maritime trade disruptions in the Red Sea and Gulf of Aden.",
                "publisher": "Global Trade Watch",
                "date": "November 1, 2023",
                "file_type": "excel"
            },
            {
                "title": "Red Sea Crisis Presentation",
                "link": "https://example.com/files/red_sea_crisis_presentation.pptx",
                "summary": "Presentation slides detailing the key aspects of the Red Sea crisis.",
                "publisher": "Powerplexity Strategy",
                "date": "December 5, 2023",
                "file_type": "pptx"
            },
            {
                "title": "Houthi Operations Overview",
                "link": "https://example.com/files/houthi_operations.docx",
                "summary": "Word document outlining the operations of the Houthi movement in the Red Sea region.",
                "publisher": "Middle East Analysis Group",
                "date": "January 10, 2024",
                "file_type": "docx"
            },
        ]

    sources = get_sources()

    # Mapping of file types to realistic icons
    file_icons = {
        "excel": "https://img.icons8.com/color/48/000000/microsoft-excel-2019--v1.png",
        "pdf": "https://img.icons8.com/color/48/000000/pdf-2--v1.png",
        "pptx": "https://img.icons8.com/color/48/000000/microsoft-powerpoint-2019--v1.png",
        "docx": "https://img.icons8.com/color/48/000000/microsoft-word-2019--v1.png"
    }

    # Displaying each source with appropriate file icon and mock file link
    for source in sources:
        icon_url = file_icons.get(source["file_type"], "https://img.icons8.com/ios-filled/50/000000/file.png")  # Default icon if file type not found
        # Construct the markdown with the icon and the clickable title
        source_markdown = f"""
        <div style="display: flex; align-items: center;">
            <img src="{icon_url}" alt="{source['file_type']} icon" style="width:24px;height:24px;margin-right:10px;">
            <a href="{source['link']}" target="_blank" style="font-size: 18px; text-decoration: none; color: #2e7bcf;">{source['title']}</a>
        </div>
        <div style="margin-left:34px;">
            <strong>Publisher:</strong> {source['publisher']}  
            <strong>Date:</strong> {source['date']}  
            <strong>Summary:</strong> {source['summary']}
        </div>
        <hr style="border: 0; height: 1px; background-color: #ccc; margin: 10px 0;">
        """
        st.markdown(source_markdown, unsafe_allow_html=True)

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
