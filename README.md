# 💬 Gemini Streamlit Chatbot

A modern conversational AI chatbot built with Streamlit and powered by Google's Gemini API. This application provides an intuitive chat interface with real-time responses and persistent conversation history.

## ✨ Features

- **Real-time Chat Interface**: Smooth conversation flow with instant responses
- **Persistent Chat History**: Maintains conversation context throughout the session
- **Streamlit Web UI**: Clean, responsive web interface
- **Google Gemini Integration**: Powered by Google's advanced Gemini AI model
- **Streaming Responses**: Real-time response streaming for better user experience
- **Error Handling**: Robust error handling for API responses

## 🛠️ Technologies Used

- **Python 3.7+**
- **Streamlit** - Web framework for the UI
- **Google Generative AI** - Gemini API integration
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

Before running this application, make sure you have:

1. Python 3.7 or higher installed
2. A Google API key for Gemini API access
3. Required Python packages (see installation section)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/gemini-streamlit-chatbot.git
   cd gemini-streamlit-chatbot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

## 🔑 Getting Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the API key and add it to your `.env` file

## 💻 Usage

1. **Run the Streamlit application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Start chatting** by typing your questions in the text input field

## 📁 Project Structure

```
gemini-streamlit-chatbot/
├── app.py              # Main Streamlit application
├── .env                # Environment variables (create this)
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .gitignore         # Git ignore file
```

## 📦 Dependencies

Create a `requirements.txt` file with the following content:

```
streamlit>=1.28.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
```

## 🔧 Configuration

The application uses the following configuration:

- **Model**: `gemma-3-27b-it` (Google's Gemini model)
- **Page Title**: "Q&A Demo"
- **Interface**: Streamlit web interface with form-based input

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Important Notes

- Keep your Google API key secure and never commit it to version control
- The `.env` file is included in `.gitignore` to prevent accidental exposure
- Make sure to monitor your API usage to avoid unexpected charges
- The chat history is session-based and will reset when you refresh the page

## 🐛 Troubleshooting

**API Key Issues:**
- Ensure your Google API key is valid and has Gemini API access
- Check that the `.env` file is in the correct location
- Verify the environment variable name matches `GOOGLE_API_KEY`

**Installation Issues:**
- Make sure you're using Python 3.7+
- Try updating pip: `pip install --upgrade pip`
- Use a virtual environment to avoid package conflicts

**Streamlit Issues:**
- Try running with `streamlit run app.py --server.port 8501`
- Clear Streamlit cache: `streamlit cache clear`

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Search existing issues in the GitHub repository
3. Create a new issue with detailed information about the problem

## 🙏 Acknowledgments

- Google for providing the Gemini API
- Streamlit team for the amazing web framework
- The open-source community for continuous inspiration

---

**Made with ❤️ and Python**
