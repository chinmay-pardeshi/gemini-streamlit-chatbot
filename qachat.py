from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from datetime import datetime
import time

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Load Gemini model
model = genai.GenerativeModel("models/gemma-3-27b-it")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    return chat.send_message(question, stream=True)

# Custom CSS for enhanced UI
st.markdown("""
<style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container styling */
    .main {
        padding-top: 1rem;
    }
    
    /* Chat container */
    .chat-container {
        max-height: 500px;
        overflow-y: auto;
        padding: 1rem;
        border-radius: 10px;
        background-color: #f8f9fa;
        margin-bottom: 1rem;
        border: 1px solid #e9ecef;
    }
    
    /* User message styling */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 16px;
        border-radius: 18px 18px 5px 18px;
        margin: 8px 0 8px 20%;
        max-width: 80%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        word-wrap: break-word;
        float: right;
        clear: both;
    }
    
    /* Bot message styling */
    .bot-message {
        background: white;
        color: #333;
        padding: 12px 16px;
        border-radius: 18px 18px 18px 5px;
        margin: 8px 20% 8px 0;
        max-width: 80%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        border-left: 4px solid #4CAF50;
        word-wrap: break-word;
        float: left;
        clear: both;
    }
    
    /* Message timestamp */
    .timestamp {
        font-size: 0.75rem;
        color: #888;
        margin-top: 4px;
        text-align: right;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        border-radius: 25px;
        border: 2px solid #e9ecef;
        padding: 10px 15px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 10px 30px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        color: #333;
        margin-bottom: 2rem;
        padding: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Stats container */
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin-bottom: 1rem;
        padding: 1rem;
        background: white;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .stat-item {
        text-align: center;
        padding: 0.5rem;
    }
    
    .stat-number {
        font-size: 1.5rem;
        font-weight: bold;
        color: #667eea;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #666;
    }
    
    /* Clear float helper */
    .clearfix::after {
        content: "";
        display: table;
        clear: both;
    }
    
    /* Typing indicator */
    .typing-indicator {
        display: flex;
        align-items: center;
        margin: 10px 20% 10px 0;
        max-width: 80%;
    }
    
    .typing-dots {
        background: white;
        padding: 12px 16px;
        border-radius: 18px 18px 18px 5px;
        border-left: 4px solid #4CAF50;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    .dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #4CAF50;
        margin: 0 2px;
        animation: typing 1.4s infinite ease-in-out both;
    }
    
    .dot:nth-child(1) { animation-delay: -0.32s; }
    .dot:nth-child(2) { animation-delay: -0.16s; }
    .dot:nth-child(3) { animation-delay: 0s; }
    
    @keyframes typing {
        0%, 80%, 100% {
            transform: scale(0.8);
            opacity: 0.5;
        }
        40% {
            transform: scale(1);
            opacity: 1;
        }
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .user-message, .bot-message {
            margin: 8px 5%;
            max-width: 90%;
        }
    }
</style>
""", unsafe_allow_html=True)

# Streamlit app config
st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize chat history and other session states
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'message_count' not in st.session_state:
    st.session_state['message_count'] = 0
if 'session_start' not in st.session_state:
    st.session_state['session_start'] = datetime.now()

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 Gemini AI Chatbot</h1>
    <p>Powered by Google's Gemini AI • Ask me anything!</p>
</div>
""", unsafe_allow_html=True)

# Stats section
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="stat-item">
        <div class="stat-number">{}</div>
        <div class="stat-label">Messages</div>
    </div>
    """.format(len(st.session_state['chat_history'])), unsafe_allow_html=True)

with col2:
    session_duration = datetime.now() - st.session_state['session_start']
    minutes = int(session_duration.total_seconds() // 60)
    st.markdown("""
    <div class="stat-item">
        <div class="stat-number">{}</div>
        <div class="stat-label">Minutes</div>
    </div>
    """.format(minutes), unsafe_allow_html=True)

with col3:
    bot_messages = len([msg for role, msg, timestamp in st.session_state['chat_history'] if role == "Bot"])
    st.markdown("""
    <div class="stat-item">
        <div class="stat-number">{}</div>
        <div class="stat-label">AI Responses</div>
    </div>
    """.format(bot_messages), unsafe_allow_html=True)

# Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display chat history
if st.session_state['chat_history']:
    for i, (role, text, timestamp) in enumerate(st.session_state['chat_history']):
        if role == "You":
            st.markdown(f"""
            <div class="user-message">
                {text}
                <div class="timestamp">{timestamp}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="bot-message">
                {text}
                <div class="timestamp">🤖 {timestamp}</div>
            </div>
            """, unsafe_allow_html=True)
else:
    # Welcome message
    st.markdown("""
    <div class="bot-message">
        👋 Hello! I'm your Gemini AI assistant. How can I help you today?
        <div class="timestamp">🤖 Ready</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Input section
st.markdown("### 💭 What's on your mind?")

# Use form to enable Enter key functionality
with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_input(
            label="Message", 
            placeholder="Type your message here...",
            key="user_input_field",
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.form_submit_button("Send 🚀", use_container_width=True)

# Handle input submission
if send_button and user_input and user_input.strip():
    # Add user message with timestamp
    current_time = datetime.now().strftime("%H:%M")
    st.session_state['chat_history'].append(("You", user_input.strip(), current_time))
    
    # Show typing indicator
    with st.container():
        st.markdown("""
        <div class="typing-indicator">
            <div class="typing-dots">
                <span class="dot"></span>
                <span class="dot"></span>
                <span class="dot"></span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Get AI response
    try:
        response_stream = get_gemini_response(user_input.strip())
        full_response = ""
        
        # Create a placeholder for streaming response
        response_placeholder = st.empty()
        
        for chunk in response_stream:
            try:
                if chunk.text:
                    full_response += chunk.text
                    # Update the response in real-time (optional)
                    # response_placeholder.markdown(f"🤖 **Bot:** {full_response}...")
            except Exception as e:
                st.warning(f"⚠️ Skipped a chunk: {e}")
        
        # Clear typing indicator and add final response
        response_placeholder.empty()
        
        if full_response:
            bot_time = datetime.now().strftime("%H:%M")
            st.session_state['chat_history'].append(("Bot", full_response, bot_time))
        else:
            bot_time = datetime.now().strftime("%H:%M")
            st.session_state['chat_history'].append(("Bot", "Sorry, I couldn't generate a response. Please try again.", bot_time))
            
    except Exception as e:
        st.error(f"❌ Error: {e}")
        error_time = datetime.now().strftime("%H:%M")
        st.session_state['chat_history'].append(("Bot", "I encountered an error. Please try again later.", error_time))
    
    # Increment message count
    st.session_state['message_count'] += 1
    
    # Rerun to update the interface
    st.rerun()

# Sidebar with additional features
with st.sidebar:
    st.markdown("## 🛠️ Chat Controls")
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state['chat_history'] = []
        st.session_state['message_count'] = 0
        st.session_state['session_start'] = datetime.now()
        st.rerun()
    
    if st.button("📥 Export Chat", use_container_width=True):
        if st.session_state['chat_history']:
            chat_export = "\n\n".join([f"{role} ({timestamp}): {text}" for role, text, timestamp in st.session_state['chat_history']])
            st.download_button(
                label="💾 Download Chat",
                data=chat_export,
                file_name=f"gemini_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        else:
            st.info("No chat history to export")
    
    st.markdown("---")
    st.markdown("## 📊 Session Info")
    st.info(f"""
    **Session Started:** {st.session_state['session_start'].strftime('%H:%M:%S')}
    
    **Model:** Gemma 3-27B-IT
    
    **Status:** 🟢 Connected
    """)
    
    st.markdown("---")
    st.markdown("## 💡 Tips")
    st.markdown("""
    - Ask specific questions for better responses
    - Use **bold** or *italic* text in your messages
    - Try different conversation topics
    - Export your chat to save important conversations
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>Made with ❤️ using Streamlit & Google Gemini AI</div>", 
    unsafe_allow_html=True
)
