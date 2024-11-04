# import streamlit as st
# import pandas as pd

# # Streamlit page configuration
# st.set_page_config(
#     page_title="Text-to-SQL Chatbot Mockup",
#     page_icon="💬",
#     layout="wide",
# )

# # Hide Streamlit's default footer and menu
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             .css-1aumxhk {padding: 1rem 1rem 10rem;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# # Initialize session state to store the conversation
# if 'conversation' not in st.session_state:
#     st.session_state.conversation = []

# # Sidebar for chat history
# with st.sidebar:
#     st.title("🗂️ Chat History")
#     for i, entry in enumerate(st.session_state.conversation):
#         role = "🧑‍💻 You" if entry['role'] == 'user' else "🤖 Bot"
#         st.markdown(f"**{role}:** {entry['content']}")
#     if st.button("Clear Conversation"):
#         st.session_state.conversation = []
#         st.experimental_rerun()

# # Main area
# st.title("💬 Text-to-SQL Chatbot Mockup")

# # Input form for user question
# with st.form(key='user_input_form'):
#     user_question = st.text_input("Ask your question here...")
#     submit_button = st.form_submit_button(label='Send')

# # Function to generate mocked SQL query and dataframe
# def generate_mocked_response(question):
#     # Default mocked SQL query and dataframe
#     mocked_sql_query = f"-- Mocked SQL Query for: '{question}'\nSELECT * FROM sample_table;"
#     df = pd.DataFrame()

#     # Check if the question is about revenues
#     if any(keyword in question.lower() for keyword in ['revenue', 'sales', 'income', 'profit']):
#         # Generate a complex SQL query related to revenues
#         mocked_sql_query = f"""-- Mocked SQL Query for: '{question}'
# WITH total_sales AS (
#     SELECT customer_id, SUM(amount) AS total_amount
#     FROM sales
#     WHERE sale_date BETWEEN '2021-01-01' AND '2021-12-31'
#     GROUP BY customer_id
# ),
# customer_info AS (
#     SELECT c.id, c.name, c.region
#     FROM customers c
#     WHERE c.status = 'active'
# )
# SELECT ci.name, ci.region, ts.total_amount
# FROM customer_info ci
# JOIN total_sales ts ON ci.id = ts.customer_id
# WHERE ts.total_amount > 10000
# ORDER BY ts.total_amount DESC;
# """

#         # Create a sample dataframe corresponding to the complex query
#         data = {
#             'Name': ['Alice', 'Bob', 'Charlie'],
#             'Region': ['North', 'East', 'West'],
#             'Total_Amount': [15000, 12000, 11000]
#         }
#         df = pd.DataFrame(data)
#     else:
#         # For other queries, provide a simpler SQL and dataframe
#         mocked_sql_query = f"""-- Mocked SQL Query for: '{question}'
# SELECT *
# FROM sample_table
# WHERE condition = 'value';
# """
#         data = {
#             'ID': [1, 2, 3],
#             'Name': ['Sample A', 'Sample B', 'Sample C'],
#             'Value': [100, 200, 300]
#         }
#         df = pd.DataFrame(data)
    
#     return mocked_sql_query, df

# # Process user input and display mocked responses
# if submit_button and user_question:
#     # Append user input to conversation
#     st.session_state.conversation.append({'role': 'user', 'content': user_question})

#     # Generate mocked SQL query and dataframe
#     mocked_sql_query, df = generate_mocked_response(user_question)

#     # Append bot response to conversation
#     st.session_state.conversation.append({'role': 'bot', 'content': mocked_sql_query})

#     # Display the user's question and mocked responses
#     st.markdown(f"**🧑‍💻 You:** {user_question}")
#     st.markdown("**🤖 Bot:**")
#     st.code(mocked_sql_query, language='sql')
#     st.markdown("**📊 Dataframe Response:**")
#     st.dataframe(df)


# pages/1_Chat_App.py

import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Chat App", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    /* Container for user messages */
    .user-message {
        background-color: #DCF8C6;
        padding: 10px;
        border-radius: 10px;
        max-width: 70%;
        margin: 5px 0;
    }

    /* Container for chatbot messages */
    .bot-message {
        background-color: #F1F0F0;
        padding: 10px;
        border-radius: 10px;
        max-width: 70%;
        margin: 5px 0;
    }

    /* Align user messages to the left */
    .user {
        display: flex;
        justify-content: flex-start;
    }

    /* Align bot messages to the right */
    .bot {
        display: flex;
        justify-content: flex-end;
    }

    /* Styling for citations */
    .citation {
        background-color: #FFFFFF;
        border-left: 4px solid #4CAF50;
        padding: 5px 10px;
        margin-top: 10px;
    }

    /* Ensure links are styled appropriately */
    a {
        color: #1E90FF;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    /* Scrollable chat container */
    .chat-container {
        max-height: 70vh;
        overflow-y: auto;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #FAFAFA;
    }
    </style>
""", unsafe_allow_html=True)

# Function to display user message
def display_user_message(message):
    st.markdown(f"""
    <div class="user">
        <div class="user-message">{message}</div>
    </div>
    """, unsafe_allow_html=True)

# Function to display bot message with citations
def display_bot_message(message, citations):
    citations_html = ""
    for cite in citations:
        citations_html += f'<div class="citation"><a href="{cite["url"]}" target="_blank">{cite["title"]}</a></div>'
    
    st.markdown(f"""
    <div class="bot">
        <div class="bot-message">
            {message}
            {citations_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

# Sample conversation
conversation = [
    {
        "sender": "user",
        "message": "Hello! Can you explain the concept of machine learning?"
    },
    {
        "sender": "bot",
        "message": "Certainly! Machine learning is a subset of artificial intelligence that focuses on building systems that learn from data to improve their performance over time.",
        "citations": [
            {"title": "What is Machine Learning?", "url": "https://www.example.com/machine-learning"},
            {"title": "Machine Learning Basics", "url": "https://www.example.com/ml-basics"}
        ]
    },
    {
        "sender": "user",
        "message": "How does supervised learning differ from unsupervised learning?"
    },
    {
        "sender": "bot",
        "message": "Supervised learning uses labeled data to train models, whereas unsupervised learning works with unlabeled data to find hidden patterns or intrinsic structures.",
        "citations": [
            {"title": "Supervised vs Unsupervised Learning", "url": "https://www.example.com/supervised-unsupervised"},
            {"title": "Understanding Machine Learning Types", "url": "https://www.example.com/ml-types"}
        ]
    }
]

# Display the chat interface
st.title("📨 Chat Application")

# Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in conversation:
    if msg["sender"] == "user":
        display_user_message(msg["message"])
    elif msg["sender"] == "bot":
        display_bot_message(msg["message"], msg.get("citations", []))

st.markdown('</div>', unsafe_allow_html=True)

# Input area for new messages
st.markdown("---")
user_input = st.text_input("You:", key="user_input")

# Note: For a fully functional chat app, implement input handling and dynamic responses.
# This mockup displays a static conversation.
