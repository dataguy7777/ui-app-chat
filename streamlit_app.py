import streamlit as st
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def main():
    """
    Runs the Streamlit application that acts as a user-friendly mockup chatbot.
    The chatbot guides the user through a series of questions:
    1. Ask for the user's name.
    2. Present a dropdown menu for the user to select an option.
    3. Ask for the user's email address.
    Finally, it displays the collected information in a neat format.

    Example:
        User flow:
        - Input name: "John Doe"
        - Select option: "Option B"
        - Input email: "john.doe@example.com"
        - App displays all collected data

    Returns:
        None
    """

    # Set a nice page title and icon
    st.set_page_config(page_title="Chatbot Mockup", page_icon="🤖")
    st.title("🤖 Welcome to the Chatbot Mockup!")
    st.write("---")

    # Ensure session state initialization
    if 'step' not in st.session_state:
        st.session_state.step = 1
        logging.info("Starting conversation at step 1.")

    # Step 1: Ask for the user's name
    if st.session_state.step == 1:
        st.write("Hello! I'm here to help. Let's get started by getting to know you.")
        name = st.text_input("1️⃣ What's your name?", key='name_input')
        # If the user provides a name, move to the next step
        if name.strip():
            logging.info(f"User entered name: {name}")
            st.session_state.step = 2
            st.experimental_rerun()

    # Step 2: Ask the user to select from a dropdown
    elif st.session_state.step == 2:
        st.write(f"Nice to meet you, **{st.session_state.name_input}**! Let's proceed.")
        options = ["Option A", "Option B", "Option C"]
        selection = st.selectbox("2️⃣ Please select an option from the list:", options, key='selection_input')
        # If the user makes a selection, move to the next step
        if selection:
            logging.info(f"User selected: {selection}")
            st.session_state.step = 3
            st.experimental_rerun()

    # Step 3: Ask for the user's email
    elif st.session_state.step == 3:
        st.write(f"Great choice, **{st.session_state.selection_input}** is quite popular!")
        email = st.text_input("3️⃣ Could you please provide your email address?", key='email_input')
        # If the user provides an email, move to the final step
        if email.strip():
            logging.info(f"User entered email: {email}")
            st.session_state.step = 4
            st.experimental_rerun()

    # Step 4: Display all the collected information
    elif st.session_state.step == 4:
        st.success("🎉 Thank you for providing all the information!")
        st.write("Here is what you've shared with me:")
        st.write(f"**Name:** {st.session_state.name_input}")
        st.write(f"**Selected Option:** {st.session_state.selection_input}")
        st.write(f"**Email:** {st.session_state.email_input}")
        logging.info("User conversation completed.")

        st.write("---")
        st.info("If you wish to start over, please refresh the app.")


if __name__ == "__main__":
    main()
