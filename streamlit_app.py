import streamlit as st
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

st.set_page_config(page_title="Chatbot Mockup", page_icon="🤖")

def main():
    """
    Runs a Streamlit chatbot-style application using st.chat_message and st.chat_input.
    The chatbot asks the user a series of questions:
    1. User's name
    2. A selection (A/B/C)
    3. User's email
    Finally, displays the collected information in a chat format.

    The conversation flow is managed via session_state:
    - step 1: ask for name
    - step 2: ask for choice
    - step 3: ask for email
    - step 4: summarize

    Example:
        Conversation:
            Bot: What's your name?
            User: John Doe
            Bot: Nice to meet you, John Doe! Please select from A, B, or C.
            User: B
            Bot: Great choice! Now, what's your email?
            User: john@example.com
            Bot: Thanks! Here is what you provided: ...
    """

    # Initialize session state
    if 'step' not in st.session_state:
        st.session_state.step = 1
    if 'name_input' not in st.session_state:
        st.session_state.name_input = ''
    if 'selection_input' not in st.session_state:
        st.session_state.selection_input = ''
    if 'email_input' not in st.session_state:
        st.session_state.email_input = ''

    # Display chat messages based on the current step
    # We will only show the entire conversation so far each time to create a chat-like feel.

    # Step 1: Ask for name
    if st.session_state.step == 1:
        with st.chat_message("assistant"):
            st.write("Hello! I'm here to help. What's your name?")
    
    # If user provided name previously
    if st.session_state.name_input and st.session_state.step >= 2:
        with st.chat_message("assistant"):
            st.write(f"Nice to meet you, **{st.session_state.name_input}**! Please select from A, B, or C (just type A, B, or C).")

    # If user provided selection previously
    if st.session_state.selection_input and st.session_state.step >= 3:
        with st.chat_message("assistant"):
            st.write(f"Great choice! Now, what's your email?")
    
    # If user provided email previously
    if st.session_state.email_input and st.session_state.step >= 4:
        with st.chat_message("assistant"):
            st.write("🎉 Thanks for providing all the information!")
            st.write(f"**Name:** {st.session_state.name_input}")
            st.write(f"**Selected Option:** {st.session_state.selection_input}")
            st.write(f"**Email:** {st.session_state.email_input}")
            st.write("If you wish to start over, please refresh the app.")

    # Chat input for user's response
    user_input = st.chat_input("Your answer:", key='chat_input')
    if user_input:
        user_input = user_input.strip()
        with st.chat_message("user"):
            st.write(user_input)

        # Process user's input based on step
        if st.session_state.step == 1:
            # User just provided the name
            st.session_state.name_input = user_input
            logging.info(f"User entered name: {st.session_state.name_input}")
            st.session_state.step = 2

        elif st.session_state.step == 2:
            # User should provide A, B, or C
            valid_options = ['A', 'B', 'C']
            if user_input.upper() in valid_options:
                st.session_state.selection_input = user_input.upper()
                logging.info(f"User selected: {st.session_state.selection_input}")
                st.session_state.step = 3
            else:
                # Invalid input, ask again
                with st.chat_message("assistant"):
                    st.write("Please type A, B, or C.")
                
        elif st.session_state.step == 3:
            # User provides email
            st.session_state.email_input = user_input
            logging.info(f"User entered email: {st.session_state.email_input}")
            st.session_state.step = 4

        # Clear chat_input after processing
        st.session_state.chat_input = ""

if __name__ == "__main__":
    main()
