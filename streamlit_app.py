import streamlit as st
import pandas as pd

# Streamlit page configuration
st.set_page_config(
    page_title="Text-to-SQL Chatbot Mockup",
    page_icon="💬",
    layout="wide",
)

# Hide Streamlit's default footer and menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Initialize session state to store the conversation
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Sidebar for chat history
with st.sidebar:
    st.title("🗂️ Chat History")
    for i, entry in enumerate(st.session_state.conversation):
        role = "🧑‍💻 You" if entry['role'] == 'user' else "🤖 Bot"
        st.markdown(f"**{role}:** {entry['content']}")
    if st.button("Clear Conversation"):
        st.session_state.conversation = []
        st.experimental_rerun()

# Main area
st.title("💬 Text-to-SQL Chatbot Mockup")

# Input form for user question
with st.form(key='user_input_form'):
    user_question = st.text_input("Ask your question here...")
    submit_button = st.form_submit_button(label='Send')

# Process user input and display mocked responses
if submit_button and user_question:
    # Append user input to conversation
    st.session_state.conversation.append({'role': 'user', 'content': user_question})

    # Mocked SQL query response
    mocked_sql_query = f"-- Mocked SQL Query for: '{user_question}'\nSELECT * FROM sample_table WHERE condition;"

    # Mocked dataframe response
    mocked_data = {
        'ID': [1, 2, 3],
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Value': [100, 200, 300]
    }
    df = pd.DataFrame(mocked_data)

    # Append bot response to conversation
    st.session_state.conversation.append({'role': 'bot', 'content': mocked_sql_query})

    # Display the user's question and mocked responses
    st.markdown(f"**🧑‍💻 You:** {user_question}")
    st.markdown("**🤖 Bot:**")
    st.code(mocked_sql_query, language='sql')
    st.markdown("**📊 Dataframe Response:**")
    st.dataframe(df)

