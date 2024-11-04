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

