import streamlit as st

# Set page configuration
st.set_page_config(page_title="Chat App with Simplified Feedback", layout="wide")

# Initialize session state for conversation and feedback
if 'conversation' not in st.session_state:
    st.session_state.conversation = [
        {
            "sender": "user",
            "message": "Hello! Can you explain the concept of machine learning?"
        },
        {
            "sender": "bot",
            "message": "Machine learning is a subset of artificial intelligence that focuses on building systems that learn from data to improve their performance over time.",
            "citations": [
                {"description": "Learn more:", "title": "Machine Learning Basics", "url": "https://example.com/ml-basics"}
            ]
        }
    ]

# Initialize feedback state
if 'feedback' not in st.session_state:
    st.session_state.feedback = {}

# Custom CSS for styling
st.markdown("""
    <style>
    .bot-message {
        background-color: #F1F0F0;
        padding: 10px;
        border-radius: 10px;
        max-width: 70%;
        margin: 5px 0;
    }
    .feedback-buttons {
        display: flex;
        gap: 10px;
        margin-top: 10px;
    }
    .feedback-section {
        margin-top: 10px;
        background-color: #E0E0E0;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Function to display user message
def display_user_message(message):
    st.markdown(f"<div style='background-color:#DCF8C6; padding:10px; border-radius:10px;'>{message}</div>", unsafe_allow_html=True)

# Function to display bot message and feedback
def display_bot_message(message, citations, msg_index):
    st.markdown(f"<div class='bot-message'>{message}</div>", unsafe_allow_html=True)
    for cite in citations:
        st.markdown(f"📖 [{cite['title']}]({cite['url']})")

    # Display Like and Dislike buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        like = st.button("👍 Like", key=f"like_{msg_index}")
    with col2:
        dislike = st.button("👎 Dislike", key=f"dislike_{msg_index}")

    # Handle Like/Dislike button clicks
    if like or dislike:
        feedback_type = "Like" if like else "Dislike"
        st.session_state.feedback[msg_index] = {"rating": feedback_type, "comment": "", "image": None}

        # Display feedback input area
        with st.expander("Provide additional feedback (optional)"):
            comment = st.text_area("Your Comment:", key=f"comment_{msg_index}")
            uploaded_file = st.file_uploader("Attach an image (optional):", type=["png", "jpg", "jpeg"], key=f"upload_{msg_index}")

            # Update session state with comment and image
            st.session_state.feedback[msg_index]["comment"] = comment.strip()
            if uploaded_file is not None:
                st.session_state.feedback[msg_index]["image"] = uploaded_file

            st.success("Your feedback has been recorded!")

# Generate bot response (placeholder function)
def generate_bot_response(user_message):
    return {
        "message": f"You asked: {user_message}. (This is a mock response.)",
        "citations": [{"description": "Learn more:", "title": "Example Link", "url": "https://example.com"}]
    }

# Main chat display
st.title("Chat Application with Simplified Feedback")

# Display conversation
for idx, msg in enumerate(st.session_state.conversation):
    if msg["sender"] == "user":
        display_user_message(msg["message"])
    elif msg["sender"] == "bot":
        display_bot_message(msg["message"], msg.get("citations", []), idx)

# User input area
user_input = st.text_input("Your message:")
if st.button("Send"):
    if user_input.strip():
        st.session_state.conversation.append({"sender": "user", "message": user_input})
        bot_response = generate_bot_response(user_input)
        st.session_state.conversation.append({"sender": "bot", "message": bot_response["message"], "citations": bot_response["citations"]})
        st.experimental_rerun()

# Optional sidebar to display feedback data
# Uncomment for debugging
# st.sidebar.write(st.session_state.feedback)
