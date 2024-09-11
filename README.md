# Mental Health Support Chatbot

A simple mental health chatbot built with Flask and NLTK, designed to offer empathetic support through conversations. The chatbot provides a safe space for users to express their feelings and receive comforting responses.

## Features
- Responds to user input based on predefined patterns using NLTK's `Chat` module.
- Provides supportive responses for a range of mental health topics including anxiety, stress, loneliness, and more.
- Suggests crisis resources when detecting critical phrases (e.g., suicidal thoughts).
- Simple, user-friendly web interface with real-time chat functionality.
- User can send messages by clicking the "Send" button or pressing "Enter".

## Tech Stack
- **Backend**: Flask (Python), NLTK (Natural Language Toolkit)
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Designed for a calm, supportive user experience with soft colors and rounded elements.

## Requirements
- Python 3.12
- Flask
- NLTK

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/mental-health-chatbot.git
    cd mental-health-chatbot
    ```

2. **Create and activate a virtual environment (optional but recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download NLTK data**
    ```bash
    python -m nltk.downloader punkt
    ```

## Running the Chatbot

1. **Start the Flask app**
    ```bash
    flask run
    ```

2. **Open your browser** and go to `http://127.0.0.1:5000/` to start interacting with the chatbot.

## Project Structure
```bash
.
├── app.py             # Main Flask app
├── templates
│   └── index.html     # Frontend template
├── static
│   └── style.css      # Custom styles for the chatbot UI
├── README.md          # This file
├── requirements.txt   # Python dependencies
└── .gitignore         # Git ignore file
