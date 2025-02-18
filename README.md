---
license: apache-2.0
title: Search Engine
sdk: streamlit
emoji: 🌍
colorFrom: green
colorTo: red
short_description: This is a Streamlit-based chatbot powered by LangChain, Groq
---

# LangChain Search Agent

### Overview

This is a Streamlit-based chatbot powered by LangChain, Groq API, and multiple search tools, including DuckDuckGo, Arxiv, and Wikipedia. The chatbot can answer queries using a selected LLM model and retrieve real-time information from various sources.

### Features

🔎 Web Search Capabilities: Uses DuckDuckGo, Arxiv, and Wikipedia for retrieving information.

🤖 Multiple LLM Models: Supports different ChatGroq models, selectable from the sidebar.

💬 Conversational Context: Maintains chat history for better response continuity.

⚙️ User Configurable: Allows users to select models and search tools from the sidebar.

🎨 Enhanced UI: Includes improved design, error handling, and interactive messages.

🔄 Chat Reset Option: Users can clear chat history using a button.

🔗 Credits Section: Acknowledges LangChain with a link to their GitHub repository.

### Installation

#### Prerequisites

- Ensure you have Python installed and set up a virtual environment:

```python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install Dependencies

```pip install -r requirements.txt```

### Usage

- Set Up API Key

- Obtain a Groq API Key.

- Enter it in the sidebar under "Settings".

- Select a Model

- Choose from available LLM models (e.g., Llama3-8b-8192, Llama3-70b-8192, llama-3.3-70b-versatile, Gemma2-9b-it).

- **Select Search Tools** - Pick from DuckDuckGo, Arxiv, and Wikipedia to refine search scope.

- Start Chatting

- Type your queries in the chat input box.

- The chatbot will respond with relevant information.

- **Clear Chat** - Reset conversation history by clicking the "Clear Chat" button in the sidebar.

### File Structure

```
📂 project_root
│-- app.py  # Main Streamlit application
│-- .env  # Environment variables (API Key)
│-- requirements.txt  # Dependencies
│-- README.md  # Project documentation
```

### Error Handling

- 🚨 Missing API Key: Prompts users to enter their API key.

- ⚠️ Invalid Input: Displays user-friendly errors for invalid inputs.

- 🔄 Processing Issues: Provides feedback if an error occurs during response generation.

### Credits

This project is built using LangChain and integrates various AI tools for enhanced search capabilities.

### License

This project is open-source and available under the apache2.0 License.

### Contributing

Feel free to submit issues or contribute improvements via pull requests on GitHub!
