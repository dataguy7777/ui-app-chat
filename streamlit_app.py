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
            .css-1aumxhk {padding: 1rem 1rem 10rem;}
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

# Function to generate mocked SQL query and dataframe
def generate_mocked_response(question):
    # Default mocked SQL query and dataframe
    mocked_sql_query = f"-- Mocked SQL Query for: '{question}'\nSELECT * FROM sample_table;"
    df = pd.DataFrame()

    # Check if the question is about revenues
    if any(keyword in question.lower() for keyword in ['revenue', 'sales', 'income', 'profit']):
        # Generate a complex SQL query related to revenues
        mocked_sql_query = f"""-- Mocked SQL Query for: '{question}'
WITH total_sales AS (
    SELECT customer_id, SUM(amount) AS total_amount
    FROM sales
    WHERE sale_date BETWEEN '2021-01-01' AND '2021-12-31'
    GROUP BY customer_id
),
customer_info AS (
    SELECT c.id, c.name, c.region
    FROM customers c
    WHERE c.status = 'active'
)
SELECT ci.name, ci.region, ts.total_amount
FROM customer_info ci
JOIN total_sales ts ON ci.id = ts.customer_id
WHERE ts.total_amount > 10000
ORDER BY ts.total_amount DESC;
"""

        # Create a sample dataframe corresponding to the complex query
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Region': ['North', 'East', 'West'],
            'Total_Amount': [15000, 12000, 11000]
        }
        df = pd.DataFrame(data)
    else:
        # For other queries, provide a simpler SQL and dataframe
        mocked_sql_query = f"""-- Mocked SQL Query for: '{question}'
SELECT *
FROM sample_table
WHERE condition = 'value';
"""
        data = {
            'ID': [1, 2, 3],
            'Name': ['Sample A', 'Sample B', 'Sample C'],
            'Value': [100, 200, 300]
        }
        df = pd.DataFrame(data)
    
    return mocked_sql_query, df

# Process user input and display mocked responses
if submit_button and user_question:
    # Append user input to conversation
    st.session_state.conversation.append({'role': 'user', 'content': user_question})

    # Generate mocked SQL query and dataframe
    mocked_sql_query, df = generate_mocked_response(user_question)

    # Append bot response to conversation
    st.session_state.conversation.append({'role': 'bot', 'content': mocked_sql_query})

    # Display the user's question and mocked responses
    st.markdown(f"**🧑‍💻 You:** {user_question}")
    st.markdown("**🤖 Bot:**")
    st.code(mocked_sql_query, language='sql')
    st.markdown("**📊 Dataframe Response:**")
    st.dataframe(df)

