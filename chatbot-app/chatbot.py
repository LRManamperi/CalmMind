import nltk
from nltk.chat.util import Chat, reflections

# Define a list of mental health-related patterns and responses
pairs = [
    (r"Hi|Hello|Hey", [
        "Hello there 🌼 I'm here to support you. How are you feeling today?",
        "Hi! I'm glad you're here. How can I help you right now?"
    ]),

    (r"My name is (.*)", [
        "Nice to meet you, %1. I'm here to listen and support you. How have you been?"
    ]),

    (r"I feel (.*)", [
        "I'm sorry to hear you're feeling %1. Want to talk more about it?",
        "Feeling %1 is totally valid. Would you like to share more with me?",
        "Thanks for sharing that you're feeling %1. You're not alone."
    ]),

    (r"I am feeling (.*)", [
        "It’s okay to feel %1. I'm here for you.",
        "Thanks for opening up. What do you think is making you feel %1?",
        "I'm listening. Do you want to talk about why you feel %1?"
    ]),

    (r"(.*) anxious(.*)", [
        "Anxiety can be really tough. Have you tried deep breathing or grounding exercises?",
        "You’re not alone. Would you like some tips on calming anxiety?",
        "I'm here to listen. Talking about what's making you anxious can help."
    ]),

    (r"(.*) sad(.*)", [
        "It's okay to feel sad sometimes. Would you like to talk about it?",
        "I'm really sorry you're feeling sad. I'm here for you.",
        "Sadness is part of being human. Talking can help lighten the load."
    ]),

    (r"(.*) stressed(.*)", [
        "Stress can be overwhelming. Have you tried taking a short break or deep breaths?",
        "It's okay to feel stressed. Can I offer some mindfulness tips?",
        "Want to talk about what's causing the stress?"
    ]),

    (r"(.*) lonely(.*)", [
        "You're not alone. I'm here with you. Want to talk about how you're feeling?",
        "Feeling lonely is really tough. I'm glad you reached out.",
        "Sometimes talking about it can help. I'm listening."
    ]),

    (r"quit|exit|bye", [
        "Take care of yourself. You're doing your best 💚",
        "Goodbye for now. Remember, you’re not alone.",
        "Wishing you peace and strength. Reach out anytime!"
    ]),

    (r"(.*)", [
        "Thank you for sharing. Would you like to tell me more?",
        "That sounds important. I'm here to listen.",
        "Can you explain that a bit more so I can better support you?"
    ])
]

# Create a Chat object with the updated pairs and reflections
chatbot = Chat(pairs, reflections)

# Function to interact with the chatbot
def chat():
    print("🌱 Hello! I’m your mental health support bot.\nType 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Bot: Goodbye! Take care of yourself 🌿")
            break
        response = chatbot.respond(user_input)
        print("Bot:", response)

# Run the chat function
if __name__ == "__main__":
    chat()
