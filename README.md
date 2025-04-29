# LangChain Chatbot

This repository contains a chatbot application built using LangChain, Streamlit, and LangSmith for tracing interactions. The chatbot uses a language model to provide helpful responses to user queries.

## Features

- **LangChain Integration**: Utilizes LangChain's prompt templates and output parsers.
- **Streamlit UI**: Provides an interactive user interface for querying the chatbot.
- **LangSmith Tracing**: Logs interactions for debugging and analysis.
- **Environment Configuration**: Configurable via `.env` file.

## Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd LangChain/Chatbot

2. Install dependencies:
    pip install -r requirements.txt

3. Set up the environment variables by creating a .env file in the root directory (if not already present) with the following content:
    LANGCHAIN_TRACING_V2="true"
    LANGCHAIN_API_KEY="<your-langchain-api-key>"
    LANGCHAIN_PROJECT="first-project"

## Usage

1. Run the Streamlit application:
    streamlit run app.py
2. Open the application in your browser at http://localhost:8501.
3. Enter a query in the text input field and view the chatbot's response.

## File Structure
.env                  # Environment variables
[app.py](http://_vscodecontentref_/0)                # Main application file
[requirements.txt](http://_vscodecontentref_/1)      # Python dependencies
README.md             # Project documentation

## Environment Variables
- LANGCHAIN_TRACING_V2: Enables<vscode_annotation           details='%5B%7B%22title%22%3A%22hardcoded-credentials%22%2C%22description%22%3A%22Embedding%20credentials%20in%20source%20code%20risks%20unauthorized%20access%22%7D%5D'> Lang</vscode_annotation>Chain tracing.  
- LANGCHAIN_API_KEY: API key for LangChain.
- LANGCHAIN_PROJECT: Name of the LangChain project.

## Dependencies
The application uses the following Python libraries:
- langchain_openai
- langchain_core
- langchain_community
- langserve
- python-dotenv
- streamlit

## How It Works
1. Prompt Template: The chatbot uses a ChatPromptTemplate to define the structure of the conversation.
2. Language Model: The Ollama model is used to generate responses.
3. Output Parsing: The StrOutputParser processes the model's output.
4. Tracing: The @traceable decorator from LangSmith logs interactions for debugging and analysis.

## Acknowledgments
- LangChain
- Streamlit
- LangSmith
