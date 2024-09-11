
from flask import Flask, request, jsonify, render_template
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Define your chatbot's patterns and responses
pairs = [
    (r"Hi|Hello", ["Hello! How are you feeling today?"]),
    (r"My name is (.*)", ["Hello %1, I'm here to listen. How can I support you today?"]),
    (r"(What is your name\?|Who are you\?)", ["I am a mental health support chatbot. How can I assist you today?"]),
    (r"(.*)(help|assist)", ["I’m here to help. Feel free to share what’s on your mind, and I’ll do my best to support you."]),
    (r"(How are you\?)", ["I’m here for you. How are you feeling today?"]),
    (r"(.*) sad|depressed|down", [
        "I'm really sorry you're feeling this way. It's okay to talk about it. You're not alone in this.",
        "It's tough, but remember that you don't have to go through this by yourself. I'm here to listen."
    ]),
    (r"(.*) anxious|worried|nervous", [
        "I understand that anxiety can be overwhelming. Let’s talk about what’s on your mind. Maybe try taking a deep breath, and I’ll be here to listen.",
        "Anxiety can make things feel difficult, but talking about it can help. How can I support you right now?"
    ]),
    (r"(.*) lonely", [
        "I'm sorry to hear you're feeling lonely. It’s completely okay to reach out and talk about it. I'm here for you.",
        "Loneliness is tough, but you’re not alone here. Let’s talk about it."
    ]),
    (r"(.*) stressed|overwhelmed", [
        "I can understand feeling stressed can be overwhelming. What’s been weighing on your mind?",
        "It’s okay to feel stressed, and it’s good that you’re sharing it. What’s been the most stressful thing for you?"
    ]),
    (r"(.*) support|need someone to talk to", [
        "I’m here to listen, no matter what you’re going through. What’s on your mind?",
        "I’m always available for you. Please feel free to share anything you’re comfortable with."
    ]),
    (r"(.*) suicidal|want to give up", [
        "I’m really sorry you’re feeling this way, and I want to help you. Please contact a crisis hotline or a mental health professional. Here’s the number for the Suicide Prevention Hotline: 1-800-273-8255.",
        "It sounds like you're going through an extremely tough time. You don’t have to face it alone—please reach out to a mental health professional."
    ]),
    (r"(.*)", [
        "I’m here to listen and support you. If you’d like to share more, I’m here to help.",
        "Sometimes just talking can help. Let me know if you’d like to share anything."
    ]),
    (r"(.*) joke", [
     "Here’s a light joke to brighten your day: Why did the scarecrow win an award? Because he was outstanding in his field!",
     "How about this one: Why don't skeletons fight each other? They don't have the guts!"
]),
    (r"(.*) thank you|thanks", [
     "I'm always here for you"
]),

]



chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
