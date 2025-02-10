# 🚀 GROQ Bot - AI Chatbot Powered by Groq API 🤖 - 🔴[LIVE](https://groq-bots-web-app.streamlit.app/)

![GROQ Bot](https://groq.com/wp-content/uploads/2024/03/PBG-mark1-color.svg)

## 🎯 Introduction

GROQ Bot is an interactive AI chatbot application built using **Streamlit** and powered by the **Groq API**. It allows users to select from multiple AI models and interact with them in a chat-based interface.

## 🎯 Purpose

The main objective of this chatbot is to provide users with an AI-powered assistant that can answer their queries in real-time. Users can switch between different AI models and clear the chat history whenever needed.

## 🌟 Features

✅ **Multi-Model Selection**: Users can choose from available AI models via a sidebar dropdown.<br>
✅ **Interactive Chat**: Seamless user interaction through Streamlit's chat interface.<br>
✅ **Chat History Management**: Option to clear the conversation history.<br>
✅ **Dynamic Model Response**: AI-generated responses based on the selected model.<br>
✅ **User-Friendly Interface**: Wide layout for better readability and usability.<br>

## ⚙️ Setup & Installation

### Prerequisites 📌

Ensure you have the following installed:

- 🐍 Python 3.8+
- 🛠 Virtual Environment (optional but recommended)

### Steps to Run Locally 🚀

#### 1. **Clone the Repository** 📂

```bash
git clone https://github.com/yourusername/groq-bot.git
cd groq-bot
```

#### 2. **Create a Virtual Environment (Optional)** 🏗️

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

#### 3. **Install Dependencies** 📦

requirements.txt is not present along with the code please use the following code for the same

```bash
groq
python-dotenv
streamlit
```

run the following command to install the dependencies

```bash
pip install -r requirements.txt
```

4. **Set Up Environment Variables** 🔑

Create a `.env` file in the project directory and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

5. **Run the Application** ▶️

```bash
streamlit run app.py
```

6. **Interact with the Bot** 💬
- Select an AI model from the sidebar.
- Start chatting and get responses.
- Clear chat history using the "Clear History" button.

## 📝 Notes

- If an AI model is unavailable, an appropriate error message is displayed.
- The chatbot always begins with a system message to guide interactions.

## 🙌 A Note of Thanks

Thank you for checking out **GROQ Bot**! 🎉 Feel free to contribute, raise issues, or suggest improvements. If you found this helpful, don’t forget to ⭐ the repository!

Happy Coding! 💻✨
