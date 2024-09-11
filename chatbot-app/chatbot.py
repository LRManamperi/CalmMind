import nltk
from nltk.chat.util import Chat, reflections

# Define a list of pairs of patterns and responses
pairs = [
    (r"Hi|Hello", ["Hello! How can I help you today?"]),
    (r"My name is (.*)", ["Hello %1, How can I assist you?"]),
    (r"(.*)", ["I'm not sure how to respond to that."])
]

# Create a Chat object with the defined pairs and reflections
chatbot = Chat(pairs, reflections)

# Function to interact with the chatbot
def chat():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Bot:", response)

# Run the chat function
if __name__ == "__main__":
    chat()
