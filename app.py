import streamlit as st
from chatbot import Chatbot

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>

    /*   MAIN APP */
   
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }

    .main {
        background-color: #0F172A;
    }
    

     /*  HEADINGS */
       
    .chat-title {
        color: #F8FAFC !important;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .chat-subtitle {
        color: #94A3B8 !important;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    /* CHAT MESSAGES */

    /* General chat message text */
    [data-testid="stChatMessage"] {
        color: #F8FAFC !important;
    }

    [data-testid="stChatMessage"] p {
        color: #F8FAFC !important;
    }

    [data-testid="stChatMessage"] div {
        color: #F8FAFC !important;
    }


    /* User message */
    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-user"]
    ) {
        background-color: #1E293B;
        border-radius: 12px;
    }


    /* Assistant message */
    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-assistant"]
    ) {
        background-color: #172554;
        border-radius: 12px;
    }


    /* CHAT INPUT */
    div[data-testid="stChatInput"] {
        background-color: #1E293B !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
    }

    div[data-testid="stChatInput"] textarea {
        background-color: #1E293B !important;
        color: #F8FAFC !important;
        caret-color: #60A5FA !important;
        min-height: 55px !important;
    }

    div[data-testid="stChatInput"] textarea::placeholder {
        color: #94A3B8 !important;
        opacity: 1 !important;
    }
    
     /* BUTTON */
      
    .stButton > button {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px;
    }

    .stButton > button:hover {
        background-color: #1D4ED8 !important;
        color: #FFFFFF !important;
    }

     /*  DIVIDER */      

    hr {
        border-color: #1E293B !important;
    }

</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="chat-title">🤖 AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="chat-subtitle">'
    'An intelligent chatbot using NLP and AI'
    '</div>',
    unsafe_allow_html=True
)

chatbot = Chatbot()

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []


if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    # store user message
    st.session_state.messages.append({
        "role":"user",
        "content":user_input
    })

    # Generate chatbot response
    response = chatbot.get_response(user_input)

    # Display chatbot response
    with st.chat_message("assistant"):
        st.write(response)

    # store chatbot response
    st.session_state.messages.append({
        "role":"assistant",
        "content":response
    })



        