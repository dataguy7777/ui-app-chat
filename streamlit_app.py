import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(page_title="Chat App with Enhanced Feedback", layout="wide")

# Initialize session state for conversation and feedback
if 'conversation' not in st.session_state:
    st.session_state.conversation = [
        {
            "sender": "user",
            "message": "Hello! Can you explain the concept of machine learning?"
        },
        {
            "sender": "bot",
            "message": "Certainly! Machine learning is a subset of artificial intelligence that focuses on building systems that learn from data to improve their performance over time.",
            "citations": [
                {
                    "description": "For a comprehensive overview, refer to:",
                    "title": "What is Machine Learning?",
                    "url": "https://www.example.com/machine-learning"
                },
                {
                    "description": "To understand the basics, see:",
                    "title": "Machine Learning Basics",
                    "url": "https://www.example.com/ml-basics"
                }
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
                {
                    "description": "Read more about the differences here:",
                    "title": "Supervised vs Unsupervised Learning",
                    "url": "https://www.example.com/supervised-unsupervised"
                },
                {
                    "description": "Understand the types of machine learning in detail:",
                    "title": "Understanding Machine Learning Types",
                    "url": "https://www.example.com/ml-types"
                }
            ]
        }
    ]

# Initialize session state for feedback tracking
if 'feedback' not in st.session_state:
    st.session_state.feedback = {}  # Key: Message Index, Value: Feedback Data

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
        position: relative;
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
        font-size: 0.9em;
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

    /* Feedback section styling */
    .feedback-section {
        margin-top: 10px;
        background-color: #E0E0E0; /* Grey background for feedback section */
        padding: 10px;
        border-radius: 10px;
    }

    .feedback-buttons button {
        margin-right: 10px;
        border: none;
        background: none;
        cursor: pointer;
        font-size: 1.2em;
    }

    .feedback-buttons button:hover {
        opacity: 0.7;
    }

    .feedback-actions {
        display: flex;
        align-items: center;
        margin-top: 10px;
    }

    .feedback-actions .clip-button {
        margin-right: 10px;
    }

    /* Success message styling */
    .success-message {
        color: green;
        font-weight: bold;
        margin-top: 10px;
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

# Function to display bot message with citations and integrated feedback
def display_bot_message(message, citations, msg_index):
    # Display the message and citations
    citations_html = ""
    for cite in citations:
        citations_html += f'<div class="citation">{cite["description"]} <a href="{cite["url"]}" target="_blank">{cite["title"]}</a></div>'

    st.markdown(f"""
    <div class="bot">
        <div class="bot-message">
            {message}
            {citations_html}
            <div class="feedback-section">
    """, unsafe_allow_html=True)

    # Check if feedback already exists for this message
    existing_feedback = st.session_state.feedback.get(msg_index, {})
    has_feedback = "rating" in existing_feedback

    if has_feedback:
        # Display existing feedback
        rating = existing_feedback.get("rating")
        comment = existing_feedback.get("comment", "")
        st.markdown(f"**Your Feedback:** {rating}")
        if comment:
            st.markdown(f"**Comment:** {comment}")
        # Display uploaded image if exists
        if "image" in existing_feedback and existing_feedback["image"] is not None:
            st.image(existing_feedback["image"], caption="Attached Image", use_column_width=True)
    else:
        # Display Like and Dislike buttons
        with st.container():
            col1, col2, col3, col4 = st.columns([1,1,1,2])
            with col1:
                like = st.button("👍 Like", key=f"like_{msg_index}")
            with col2:
                dislike = st.button("👎 Dislike", key=f"dislike_{msg_index}")
            with col3:
                attach = st.button("📎", key=f"attach_{msg_index}")  # Clip button
            with col4:
                submit = st.button("Submit Feedback", key=f"submit_feedback_{msg_index}")

        # Handle Like button click
        if like:
            st.session_state.feedback[msg_index] = {"rating": "Like", "comment": "", "image": None}

        # Handle Dislike button click
        if dislike:
            st.session_state.feedback[msg_index] = {"rating": "Dislike", "comment": "", "image": None}

        # Handle Attach Image button click
        if attach:
            uploaded_file = st.file_uploader("Attach an image to your feedback (optional):", type=["png", "jpg", "jpeg"], key=f"uploader_{msg_index}")
            if uploaded_file is not None:
                st.session_state.feedback[msg_index] = {
                    "rating": existing_feedback.get("rating", ""),
                    "comment": "",
                    "image": uploaded_file
                }

        # Handle Submit Feedback button click
        if submit:
            if msg_index in st.session_state.feedback and st.session_state.feedback[msg_index].get("rating"):
                with st.container():
                    comment = st.text_area("Your Comment:", key=f"comment_{msg_index}")
                    # Optional: Allow users to upload image here as well
                    # Already handled above
                    st.session_state.feedback[msg_index]["comment"] = comment.strip()
                    st.success("Thank you for your feedback!")
            else:
                st.warning("Please select Like or Dislike before submitting feedback.")

        # After Like or Dislike is clicked, show comment input and image uploader
        if msg_index in st.session_state.feedback and st.session_state.feedback[msg_index].get("rating"):
            with st.expander("Add a comment (optional)"):
                comment = st.text_area("Your Comment:", key=f"comment_expander_{msg_index}")
                # Attach image within expander if not already attached
                if st.session_state.feedback[msg_index].get("image") is None:
                    uploaded_file = st.file_uploader("Attach an image to your feedback (optional):", type=["png", "jpg", "jpeg"], key=f"uploader_expander_{msg_index}")
                    if uploaded_file is not None:
                        st.session_state.feedback[msg_index]["image"] = uploaded_file
                submit_key = f"submit_feedback_expander_{msg_index}"
                submit = st.button("Submit Feedback", key=submit_key)
                if submit:
                    st.session_state.feedback[msg_index]["comment"] = comment.strip()
                    st.success("Thank you for your feedback!")

    # Close the feedback section div
    st.markdown("""
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Function to generate bot response (Placeholder)
def generate_bot_response(user_message):
    # Placeholder for actual bot logic. Replace with API calls or model inference.
    response = {
        "message": f"You said: {user_message}. (This is a placeholder response.)",
        "citations": [
            {
                "description": "For more information, visit:",
                "title": "Example Citation 1",
                "url": "https://www.example.com/doc1"
            },
            {
                "description": "You can also check out:",
                "title": "Example Citation 2",
                "url": "https://www.example.com/doc2"
            }
        ]
    }
    return response

# Display the chat interface
st.title("📨 Chat Application with Enhanced Feedback")

# Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for idx, msg in enumerate(st.session_state.conversation):
    if msg["sender"] == "user":
        display_user_message(msg["message"])
    elif msg["sender"] == "bot":
        display_bot_message(msg["message"], msg.get("citations", []), idx)

st.markdown('</div>', unsafe_allow_html=True)

# Input area for new messages
st.markdown("---")
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input.strip() != "":
        # Append user message to conversation
        st.session_state.conversation.append({
            "sender": "user",
            "message": user_input
        })

        # Generate bot response
        bot_response = generate_bot_response(user_input)

        # Append bot response to conversation with initialized feedback
        st.session_state.conversation.append({
            "sender": "bot",
            "message": bot_response["message"],
            "citations": bot_response["citations"]
        })

        # Clear the input box by resetting the key
        st.session_state.user_input = ""
        st.experimental_rerun()

# Display collected feedback (Optional: For debugging or admin purposes)
# Uncomment the following lines if you want to see the feedback data
# st.sidebar.header("📝 Feedback Data")
# st.sidebar.json(st.session_state.feedback)
