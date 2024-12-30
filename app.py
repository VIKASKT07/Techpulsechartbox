# import os
# import json 
# import streamlit as st
# from groq import Groq

# # Streamlit page configuration
# st.set_page_config(
#     page_title="Coder Connects LLAMA 3.1",
#     page_icon="🦙",
#     layout="centered"
# )

# # Define the working directory and load the data
# working_dir = os.path.dirname(os.path.abspath(__file__))
# config_data = json.load(open(f"{working_dir}/config.json"))

# # Retrieve and set API key from config
# GROQ_API_KEY = config_data.get("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")

# # Validate the API key if it exists
# if not GROQ_API_KEY:
#     st.error("API key is missing in the config.json file.")
#     st.stop()

# # Save the API key to the environment variable
# os.environ["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"] = GROQ_API_KEY

# # Initialize the Groq client with API key
# try:
#     client = Groq(api_key=os.environ["gsk_qnrUWiGg4Mp48ronT4kHWGdyb3FY75hbWJwQkx5JDGES8ZpjzoklY"])
# except Exception as e:
#     st.error(f"Failed to initialize Groq client: {e}")
#     st.stop()

# # Initialize the chat history in Streamlit session state 
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Streamlit page title
# st.title("🦙 Coder Connects LLAMA 3.1 Chat bot for you to assist")

# # Display the chat history
# for message in st.session_state.chat_history:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Input field for user message
# user_prompt = st.chat_input("Ask Coder Connects LLAMA 3.1.....")

# if user_prompt:
#     st.chat_message("user").markdown(user_prompt)
#     st.session_state.chat_history.append({"role": "user", "content": user_prompt})

#     # Send user's message to LLM and get a response
#     messages = [
#         {"role": "system", "content": "You are a helpful assistant"},
#         *st.session_state.chat_history
#     ]

#     try:
#         response = client.chat.completions.create(
#             model="llama3-8b-8192",
#             messages=messages
#         )

#         assistant_response = response.choices[0].message.content
#         st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

#         # Display the LLM response
#         with st.chat_message("assistant"):
#             st.markdown(assistant_response)

#     except Exception as e:
#         st.error(f"Error while fetching the response from GROQ: {e}")




        
# import os
# import json
# import streamlit as st
# from groq import Groq
# from io import StringIO
# from fpdf import FPDF

# # Streamlit page configuration
# st.set_page_config(
#     page_title="TechPulse Chatbot",
#     page_icon="💻",
#     layout="centered"
# )

# # Define the working directory and load the data
# working_dir = os.path.dirname(os.path.abspath(__file__))
# config_data = json.load(open(f"{working_dir}/config.json"))

# # Retrieve and set API key from config
# GROQ_API_KEY = config_data.get("GROQ_API_KEY")

# # Validate the API key if it exists
# if not GROQ_API_KEY:
#     st.error("API key is missing in the config.json file.")
#     st.stop()

# # Save the API key to the environment variable
# os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# # Initialize the Groq client with API key
# try:
#     client = Groq(api_key=os.environ["GROQ_API_KEY"])
# except Exception as e:
#     st.error(f"Failed to initialize Groq client: {e}")
#     st.stop()

# # Initialize the chat history in Streamlit session state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Streamlit page title
# st.title("💻 TechPulse Chatbot")

# # Function to validate user prompt (tech-related topics only)
# def is_valid_prompt(prompt):
#     # Keywords related to technical aspects (programming, AI, tech news, etc.)
#     tech_keywords = ["programming", "algorithm", "AI", "machine learning", "data science", "software", "technology", "development", "tech news", "coding", "app development", "tech stack", "database", "python", "java", "javascript"]
#     return any(keyword in prompt.lower() for keyword in tech_keywords)

# # Function to create PDF
# def create_pdf(content):
#     try:
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_auto_page_break(auto=True, margin=15)
#         pdf.set_font("Arial", size=12)
#         # Encode content to handle special characters
#         encoded_content = content.encode('latin-1', 'replace').decode('latin-1')
#         pdf.multi_cell(0, 10, encoded_content)
#         return pdf.output(dest='S').encode('latin-1')
#     except Exception as e:
#         st.error(f"Error creating PDF: {e}")
#         return None

# # Display the chat history
# for i, message in enumerate(st.session_state.chat_history):
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
        
#         # Add download buttons for assistant responses
#         if message["role"] == "assistant":
#             response_text = message["content"]
#             col1, col2 = st.columns(2)
            
#             # Text download in column 1
#             with col1:
#                 download_filename = f"response_{i+1}.txt"
#                 st.download_button(
#                     label="Download as Text",
#                     data=response_text,
#                     file_name=download_filename,
#                     mime="text/plain"
#                 )
            
#             # PDF download in column 2
#             with col2:
#                 pdf_bytes = create_pdf(response_text)
#                 if pdf_bytes:
#                     st.download_button(
#                         label="Download as PDF",
#                         data=pdf_bytes,
#                         file_name=f"response_{i+1}.pdf",
#                         mime="application/pdf"
#                     )

# # Input field for user message
# user_prompt = st.chat_input("Ask about technology, programming, AI, or development...")

# if user_prompt:
#     if is_valid_prompt(user_prompt):
#         st.chat_message("user").markdown(user_prompt)
#         st.session_state.chat_history.append({"role": "user", "content": user_prompt})

#         # Send user's message to LLM and get a response
#         messages = [
#             {"role": "system", "content": "You are a chatbot that provides accurate and concise information about technical topics, including programming, AI, software development, machine learning, technology news, coding practices, and more. You must not respond to queries unrelated to technical subjects."},
#             *st.session_state.chat_history
#         ]

#         try:
#             response = client.chat.completions.create(
#                 model="llama3-8b-8192",
#                 messages=messages
#             )

#             assistant_response = response.choices[0].message.content
#             st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

#             # Display the LLM response
#             with st.chat_message("assistant"):
#                 st.markdown(assistant_response)

#                 # Add download buttons in columns
#                 col1, col2 = st.columns(2)
                
#                 # Text download in column 1
#                 with col1:
#                     st.download_button(
#                         label="Download as Text",
#                         data=assistant_response,
#                         file_name="response_latest.txt",
#                         mime="text/plain"
#                     )
                
#                 # PDF download in column 2
#                 with col2:
#                     pdf_bytes = create_pdf(assistant_response)
#                     if pdf_bytes:
#                         st.download_button(
#                             label="Download as PDF",
#                             data=pdf_bytes,
#                             file_name="response_latest.pdf",
#                             mime="application/pdf"
#                         )

#         except Exception as e:
#             st.error(f"Error while fetching the response from GROQ: {e}")
#     else:
#         # Inform the user about invalid queries
#         st.error("Please ask questions related to technical topics such as programming, AI, development, or tech news.")




import os
import json
import streamlit as st
from groq import Groq
from io import StringIO
from fpdf import FPDF

# Streamlit page configuration
st.set_page_config(
    page_title="TechPulse Chatbot",
    page_icon="💻",
    layout="centered"
)

# Define the working directory and load the data
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))

# Retrieve and set API key from config
GROQ_API_KEY = config_data.get("GROQ_API_KEY")

# Validate the API key if it exists
if not GROQ_API_KEY:
    st.error("API key is missing in the config.json file.")
    st.stop()

# Save the API key to the environment variable
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Initialize the Groq client with API key
try:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
except Exception as e:
    st.error(f"Failed to initialize Groq client: {e}")
    st.stop()

# Initialize the chat history in Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Streamlit page title
st.title("💻 TechPulse Chatbot")

# Function to create PDF
def create_pdf(content):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        # Encode content to handle special characters
        encoded_content = content.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 10, encoded_content)
        return pdf.output(dest='S').encode('latin-1')
    except Exception as e:
        st.error(f"Error creating PDF: {e}")
        return None

# Display the chat history
for i, message in enumerate(st.session_state.chat_history):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        # Add download buttons for assistant responses
        if message["role"] == "assistant":
            response_text = message["content"]
            col1, col2 = st.columns(2)

            # Text download in column 1
            with col1:
                download_filename = f"response_{i+1}.txt"
                st.download_button(
                    label="Download as Text",
                    data=response_text,
                    file_name=download_filename,
                    mime="text/plain"
                )

            # PDF download in column 2
            with col2:
                pdf_bytes = create_pdf(response_text)
                if pdf_bytes:
                    st.download_button(
                        label="Download as PDF",
                        data=pdf_bytes,
                        file_name=f"response_{i+1}.pdf",
                        mime="application/pdf"
                    )

# Input field for user message
user_prompt = st.chat_input("Ask about technology, AI, machine learning, software development, and more...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Send user's message to LLM and get a response
    messages = [
        {"role": "system", "content": "You are a chatbot that provides accurate and concise information about technical topics, including AI, machine learning, programming, software development, tech news, algorithms, coding practices, and other technological advancements. You should answer all questions related to technology, AI, or development, but you must not respond to queries unrelated to these topics."},
        *st.session_state.chat_history
    ]

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages
        )

        assistant_response = response.choices[0].message.content
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

        # Display the LLM response
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

            # Add download buttons in columns
            col1, col2 = st.columns(2)

            # Text download in column 1
            with col1:
                st.download_button(
                    label="Download as Text",
                    data=assistant_response,
                    file_name="response_latest.txt",
                    mime="text/plain"
                )

            # PDF download in column 2
            with col2:
                pdf_bytes = create_pdf(assistant_response)
                if pdf_bytes:
                    st.download_button(
                        label="Download as PDF",
                        data=pdf_bytes,
                        file_name="response_latest.pdf",
                        mime="application/pdf"
                    )

    except Exception as e:
        st.error(f"Error while fetching the response from GROQ: {e}")

