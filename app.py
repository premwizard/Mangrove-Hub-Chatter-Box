from flask import Flask, render_template, request, jsonify, send_file
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
from datetime import datetime
from pathlib import Path
import io

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure your Gemini API key (set this in your environment)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if API key is set
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the .env file!")

# Initialize Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Sample questions for quick access
SAMPLE_QUESTIONS = [
    "What are mangrove forests?",
    "What is the structure of a mangrove forest?",
    "How do mangroves adapt to salt water?",
    "How do mangroves help the environment?",
    "How do mangroves protect coastal areas?",
    "What wildlife lives in mangrove forests?",
    "Where are mangrove forests found in the world?",
    "Why are mangroves endangered?",
    "How can we protect and restore mangrove forests?"
]

# Data directory for storing chat history
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
HISTORY_FILE = DATA_DIR / "chat_history.json"

def load_chat_history():
    """Load chat history from file"""
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_chat_history(history):
    """Save chat history to file"""
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def add_to_history(question, answer):
    """Add a question-answer pair to history"""
    history = load_chat_history()
    history.append({
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "answer": answer
    })
    save_chat_history(history)

@app.route('/')
def home():
    return render_template('index.html', sample_questions=SAMPLE_QUESTIONS)

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question', '').strip()
    
    if not user_input:
        return jsonify({"answer": "❌ Please enter a question."})

    # Restrict topic: only Mangrove-related questions
    if "mangrove" not in user_input.lower() and "forest" not in user_input.lower() and "environment" not in user_input.lower():
        return jsonify({
            "answer": "🌿 I can only answer questions related to Mangrove forests and the environment. Please ask about mangroves!",
            "suggestions": []
        })

    # Generate response using Gemini
    try:
        prompt = f"""You are a friendly and knowledgeable chatbot expert about Mangrove forests. 
Answer the following question clearly, concisely, and in simple words. Use formatting like bullet points and bold text where appropriate.

User Question: {user_input}

Provide a helpful and engaging response:"""
        
        response = model.generate_content(prompt, stream=False)
        reply = response.text.strip()
        
        # Add to history
        add_to_history(user_input, reply)
        
        # Generate follow-up suggestions
        suggestions = generate_suggestions(user_input)
        
        return jsonify({
            "answer": reply,
            "suggestions": suggestions
        })
    except Exception as e:
        reply = f"❌ Error generating response: {str(e)}"
        return jsonify({
            "answer": reply,
            "suggestions": []
        })

def generate_suggestions(question):
    """Generate follow-up question suggestions"""
    try:
        prompt = f"""Based on this question about mangrove forests: "{question}"
Generate 2-3 brief follow-up questions (each under 10 words) that would help deepen understanding.
Format as a simple numbered list like:
1. Question one?
2. Question two?"""
        
        response = model.generate_content(prompt, stream=False)
        suggestions_text = response.text.strip()
        
        # Parse suggestions
        suggestions = []
        for line in suggestions_text.split('\n'):
            line = line.strip()
            if line and line[0].isdigit():
                # Remove number and period
                suggestion = line.split('.', 1)[-1].strip() if '.' in line else line
                suggestions.append(suggestion)
        
        return suggestions[:3]  # Return max 3 suggestions
    except Exception as e:
        return []

@app.route('/history', methods=['GET'])
def get_history():
    """Get chat history"""
    history = load_chat_history()
    return jsonify({"conversations": history})

@app.route('/clear-history', methods=['POST'])
def clear_history():
    """Clear chat history"""
    save_chat_history([])
    return jsonify({"success": True, "message": "Chat history cleared"})

@app.route('/export', methods=['GET'])
def export_chat():
    """Export chat history as text file"""
    history = load_chat_history()
    
    # Create formatted text content
    content = "🌿 Chatter Box - Mangrove Forest Chat History\n"
    content += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    content += "=" * 60 + "\n\n"
    
    for i, conv in enumerate(history, 1):
        content += f"Question {i}: {conv['question']}\n"
        content += f"Timestamp: {conv['timestamp']}\n"
        content += f"Answer:\n{conv['answer']}\n"
        content += "-" * 60 + "\n\n"
    
    # Create file response
    byte_io = io.BytesIO(content.encode('utf-8'))
    
    return send_file(
        byte_io,
        mimetype='text/plain',
        as_attachment=True,
        download_name=f'mangrove_chat_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    )

@app.route('/stats', methods=['GET'])
def get_stats():
    """Get chat statistics"""
    history = load_chat_history()
    return jsonify({
        "total_questions": len(history),
        "total_conversations": len(history)
    })

if __name__ == '__main__':
    app.run(debug=True)
