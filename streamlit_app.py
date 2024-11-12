import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Chat App with Feedback", layout="wide")

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
            ],
            "feedback": {}  # Initialize feedback for this message
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
            ],
            "feedback": {}  # Initialize feedback for this message
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
        margin-top: 5px;
    }

    .feedback-buttons button {
        margin-right: 5px;
    }

    .feedback-comment {
        margin-top: 5px;
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

# Function to display bot message with citations and feedback
def display_bot_message(message, citations, msg_index):
    # Generate unique keys for feedback buttons and comment
    like_key = f"like_{msg_index}"
    dislike_key = f"dislike_{msg_index}"
    comment_key = f"comment_{msg_index}"
    submit_key = f"submit_{msg_index}"

    # Retrieve existing feedback if any
    existing_feedback = st.session_state.feedback.get(msg_index, {})

    # Display the message and citations
    citations_html = ""
    for cite in citations:
        citations_html += f'<div class="citation">{cite["description"]} <a href="{cite["url"]}" target="_blank">{cite["title"]}</a></div>'

    st.markdown(f"""
    <div class="bot">
        <div class="bot-message">
            {message}
            {citations_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Feedback Section
    with st.container():
        st.markdown('<div class="feedback-section">', unsafe_allow_html=True)
        # Like and Dislike buttons
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            like = st.button("👍 Like", key=like_key)
        with col2:
            dislike = st.button("👎 Dislike", key=dislike_key)
        with col3:
            # If user has already provided feedback, display it
            if existing_feedback.get("rating"):
                rating = existing_feedback["rating"]
                comment = existing_feedback.get("comment", "")
                st.markdown(f"**Your Feedback:** {rating}")
                if comment:
                    st.markdown(f"**Comment:** {comment}")
            else:
                # Input for comments
                comment = st.text_input("Add a comment (optional):", key=comment_key)
                # Submit feedback
                submit = st.button("Submit Feedback", key=submit_key)
                if submit:
                    if like:
                        rating = "Like"
                    elif dislike:
                        rating = "Dislike"
                    else:
                        rating = None

                    if rating:
                        st.session_state.feedback[msg_index] = {
                            "rating": rating,
                            "comment": comment
                        }
                        st.success("Thank you for your feedback!")
                        st.experimental_rerun()
                    else:
                        st.warning("Please select Like or Dislike before submitting.")
        st.markdown('</div>', unsafe_allow_html=True)

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
st.title("📨 Chat Application with Feedback")

# Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for idx, msg in enumerate(st.session_state.conversation):
    if msg["sender"] == "user":
        display_user_message(msg["message"])
    elif msg["sender"] == "bot":
        # Pass the current index to associate feedback correctly
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
            "citations": bot_response["citations"],
            "feedback": {}  # Initialize feedback for this message
        })

        # Clear the input box and rerun to display the updated conversation
        st.experimental_rerun()

# Display collected feedback (Optional: For debugging or admin purposes)
# Uncomment the following lines if you want to see the feedback data
# st.sidebar.header("📝 Feedback Data")
# st.sidebar.json(st.session_state.feedback)
