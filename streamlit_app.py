import streamlit as st
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def main():
    """
    Runs the Streamlit application that acts as a mock-up chatbot.
    The chatbot will ask the user for their name, their choice from a dropdown, and their email address.
    After collecting all information, it will display the results.

    The flow of the chatbot:
    1. Ask user's name (text input).
    2. Ask user to select from a dropdown of predefined options.
    3. Ask user to input their email.
    4. Display the collected information.

    Example:
        After all steps are complete, user sees a summary of their input.

    Returns:
        None
    """
    st.title("Simple Chatbot - Mockup")

    # Session state to track progress of conversation
    if 'step' not in st.session_state:
        st.session_state.step = 1
        logging.info("Starting conversation at step 1.")

    # Step 1: Ask for name
    if st.session_state.step == 1:
        st.write("Hello! Let's get started.")
        name = st.text_input("What's your name?", key='name_input')
        if name:
            logging.info(f"User entered name: {name}")
            st.session_state.step = 2

    # Step 2: Ask user to select from a dropdown
    elif st.session_state.step == 2:
        st.write(f"Nice to meet you, {st.session_state.name_input}!")
        options = ["Option A", "Option B", "Option C"]
        selection = st.selectbox("Please select an option from the list:", options, key='selection_input')
        if selection:
            logging.info(f"User selected: {selection}")
            st.session_state.step = 3

    # Step 3: Ask for email
    elif st.session_state.step == 3:
        st.write("Great choice!")
        email = st.text_input("Could you please provide your email address?", key='email_input')
        if email:
            logging.info(f"User entered email: {email}")
            st.session_state.step = 4

    # Step 4: Display all the collected information
    elif st.session_state.step == 4:
        st.write("Thank you! Here is the information you provided:")
        st.write(f"**Name:** {st.session_state.name_input}")
        st.write(f"**Selected Option:** {st.session_state.selection_input}")
        st.write(f"**Email:** {st.session_state.email_input}")
        logging.info("User conversation completed.")

        st.write("Feel free to modify the inputs by refreshing the app.")

if __name__ == "__main__":
    main()
