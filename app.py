import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Search Engine Tool/Agent"

# Initialize search tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=2000)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

search = DuckDuckGoSearchRun(name="Search")

# Streamlit UI
st.set_page_config(page_title="Search Engine", layout="wide")
st.title("🔎 Search Engine Tool/Agent")
st.sidebar.title("Settings")

# API Key input
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")
if not api_key:
    st.warning("⚠️ Please enter your API key to continue.")

# Select model
model_name = st.sidebar.selectbox("Select ChatGroq Model:", ["Llama3-8b-8192", "Llama3-70b-8192", "llama-3.3-70b-versatile", "Gemma2-9b-it"])

# Select search tools
tools_selected = st.sidebar.multiselect(
    "Select search tools:",
    ["DuckDuckGo", "Arxiv", "Wikipedia"],
    default=["DuckDuckGo", "Arxiv", "Wikipedia"]
)

tools = []
if "DuckDuckGo" in tools_selected:
    tools.append(search)
if "Arxiv" in tools_selected:
    tools.append(arxiv)
if "Wikipedia" in tools_selected:
    tools.append(wiki)

# Clear chat button
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state["messages"] = []
    st.rerun()

# Credits section at the bottom of the sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("**Powered by [LangChain](https://github.com/langchain-ai/streamlit-agent)**")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Display welcome message if chat is empty
if not st.session_state.messages:
    st.write("👋 Hi, I'm a chatbot who can search the web. How can I help you?")

# Handle user input
if prompt := st.chat_input(placeholder="Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    if not api_key:
        st.error("❌ API key is required to proceed.", icon="⚠️")
    else:
        try:
            llm = ChatGroq(groq_api_key=api_key, model_name=model_name, streaming=True)
            search_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)
            
            # Pass conversation history to maintain context
            conversation_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
            
            with st.chat_message("assistant"), st.spinner("🔍 Searching..."):
                st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
                response = search_agent.run(conversation_history, callbacks=[st_cb])
                st.session_state.messages.append({'role': 'assistant', "content": response})
                st.write(response)
        except Exception as e:
            st.error(f"❌ An error occurred: {e}", icon="🚨")