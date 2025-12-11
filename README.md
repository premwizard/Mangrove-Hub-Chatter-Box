# 🌿 Chatter Box - Mangrove Forest AI Assistant

A beautiful, interactive AI chatbot dedicated to teaching users about mangrove forests and their importance to our ecosystem.

## 🎯 Features

### Core Features
- **🤖 AI-Powered Chatbot** - Uses Google Gemini 2.5 Flash for intelligent responses
- **🌳 Mangrove-Focused** - Specialized in answering questions about mangrove forests
- **📱 Responsive Design** - Works seamlessly on desktop and mobile devices
- **🎨 Modern UI** - Beautiful mangrove forest-themed interface with smooth animations

### User Interface
- **Sidebar Quick Questions** - Pre-made questions organized by categories
- **Markdown Support** - Responses rendered with proper formatting
- **Code Highlighting** - Syntax highlighting for code blocks
- **Real-time Loading** - Visual feedback while generating responses
- **Chat History** - Conversation preserved during the session

### Additional Features
- **Search History** - View your past conversations
- **Dark Mode** - Eye-friendly dark theme with green accents
- **Export Chat** - Download conversations as text files
- **Question Suggestions** - AI-powered follow-up question suggestions
- **Copy to Clipboard** - Easy sharing of answers

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Flask
- Google Generative AI API Key

### Installation

1. **Clone or download the project**
   ```bash
   cd d:\chatterbox
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask python-dotenv google-generativeai
   ```

4. **Set up your API key**
   - Get your free Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a `.env` file in the project root
   - Add your API key:
     ```
     GEMINI_API_KEY = your_api_key_here
     ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   - Navigate to `http://127.0.0.1:5000`

## 📂 Project Structure

```
chatterbox/
├── app.py                 # Flask application & API endpoints
├── .env                   # Environment variables (API key)
├── README.md             # This file
├── static/
│   └── style.css         # Styling and layout
├── templates/
│   └── index.html        # Main UI template
└── data/
    └── chat_history.json # Stored conversation history
```

## 🎓 About Mangrove Forests

Mangrove forests are unique ecosystems found in tropical and subtropical coastal areas. They are:
- **Carbon Sinks** - Absorb more carbon than other forest types
- **Nurseries** - Critical breeding grounds for fish and shellfish
- **Protection** - Shield coastal communities from storms and erosion
- **Biodiversity Hotspots** - Home to thousands of species
- **Water Filters** - Naturally purify and filter water

## 🛠️ How It Works

1. **User Input** - User types a question or clicks a quick question button
2. **Processing** - Flask backend validates and processes the question
3. **AI Generation** - Google Gemini API generates an intelligent response
4. **Display** - Response is rendered with markdown formatting and syntax highlighting
5. **History** - Conversation is saved to local storage and JSON file

## 📝 API Endpoints

### POST `/ask`
Generates a response to a user's question about mangrove forests.

**Request:**
```json
{
  "question": "What are mangrove forests?"
}
```

**Response:**
```json
{
  "answer": "Detailed markdown-formatted answer about the question..."
}
```

### GET `/history`
Retrieves the chat history (when implemented).

**Response:**
```json
{
  "conversations": [
    {
      "timestamp": "2025-12-12T10:30:00",
      "question": "...",
      "answer": "..."
    }
  ]
}
```

### GET `/export`
Exports the current chat as a text file (when implemented).

## 🔧 Configuration

Edit `app.py` to customize:
- Model selection (currently: `gemini-2.5-flash`)
- System prompt and chatbot personality
- Topic restrictions
- API timeout settings

## 🌐 Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **AI**: Google Generative AI (Gemini)

## 📱 Responsive Breakpoints

- **Desktop**: Full sidebar layout (280px sidebar + chat area)
- **Tablet**: Adjusted spacing and font sizes
- **Mobile**: Sidebar moves to horizontal scrolling layout

## 🎨 Color Scheme

- **Primary Green**: `#27ae60` - Action buttons and highlights
- **Dark Forest**: `#0a1f0f` - Background and dark elements
- **Forest Accent**: `#0d3d1a` - Secondary backgrounds
- **Light Green**: `#2ecc71` - Text highlights
- **Light Background**: `#f5f9f5` - Chat area background

## 🚦 Status Indicators

- **Spinner Animation** - Shows when AI is generating response
- **Loading Message** - "Exploring mangrove forests..."
- **Error Messages** - Red styled error alerts
- **Success Feedback** - Message sent confirmation

## ⚙️ Environment Variables

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

## 🤝 Contributing

Feel free to enhance this project! Some ideas:
- Add more mangrove-related information sources
- Implement user authentication
- Add multi-language support
- Create educational quizzes
- Add image generation for mangrove illustrations

## 📄 License

This project is open source and available for educational purposes.

## 🐛 Troubleshooting

### Issue: "API key not found"
- Ensure `.env` file exists in project root
- Verify `GEMINI_API_KEY` is set correctly

### Issue: "Model not found"
- Check your API key has access to Gemini models
- Verify you're using the latest model name

### Issue: Slow responses
- Normal for first request (model initialization)
- Subsequent requests should be faster
- Check your internet connection

### Issue: UI not loading properly
- Clear browser cache (Ctrl+Shift+Delete)
- Try a different browser
- Ensure you're using HTTPS or localhost

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review Flask and Gemini API documentation
3. Check console for error messages (F12)

## 🌟 Future Enhancements

- [ ] User authentication & saved conversations
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Educational quiz mode
- [ ] Image generation for mangrove ecosystems
- [ ] Real-time news about mangrove conservation
- [ ] Conversation analytics & statistics
- [ ] Mobile app version
- [ ] Integration with environmental databases

---

Made with 🌿 for mangrove forest education and conservation awareness.
