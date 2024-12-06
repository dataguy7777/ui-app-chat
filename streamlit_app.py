import streamlit as st
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

st.set_page_config(page_title="Chatbot Mockup", page_icon="🤖")

def main():
    """
    Runs the Streamlit application that acts as a user-friendly mockup chatbot.
    The chatbot guides the user through a series of questions:
    1. Ask for the user's name.
    2. Present a dropdown menu for the user to select an option.
    3. Ask for the user's email address.
    Finally, it displays the collected information in a neat format.

    Flow:
        - The interface updates dynamically as the user provides each piece of info.
        - Once the name is given, the dropdown appears.
        - Once the dropdown choice is made, the email input appears.
        - Once the email is given, the summary is displayed.

    Returns:
        None
    """

    if 'name_input' not in st.session_state:
        st.session_state.name_input = ''
    if 'selection_input' not in st.session_state:
        st.session_state.selection_input = ''
    if 'email_input' not in st.session_state:
        st.session_state.email_input = ''

    st.title("🤖 Welcome to the Chatbot Mockup!")
    st.write("---")

    # Step 1: Ask for the user's name
    st.write("Hello! I'm here to help. Let's get started by getting to know you.")
    st.session_state.name_input = st.text_input("1️⃣ What's your name?", value=st.session_state.name_input)

    # Proceed only if name is provided
    if st.session_state.name_input.strip():
        logging.info(f"User entered name: {st.session_state.name_input}")
        st.write(f"Nice to meet you, **{st.session_state.name_input}**! Let's proceed.")

        # Step 2: Ask the user to select from a dropdown
        options = ["Option A", "Option B", "Option C"]
        st.session_state.selection_input = st.selectbox("2️⃣ Please select an option from the list:",
                                                        options,
                                                        index=options.index(st.session_state.selection_input) if st.session_state.selection_input in options else 0)

        if st.session_state.selection_input:
            logging.info(f"User selected: {st.session_state.selection_input}")
            st.write(f"Great choice, **{st.session_state.selection_input}** is quite popular!")

            # Step 3: Ask for the user's email
            st.session_state.email_input = st.text_input("3️⃣ Could you please provide your email address?", value=st.session_state.email_input)

            if st.session_state.email_input.strip():
                logging.info(f"User entered email: {st.session_state.email_input}")

                # Step 4: Display all the collected information
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
