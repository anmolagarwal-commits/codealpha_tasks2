import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you ?", ["I'm doing well, thank you!", "I'm great! How about you?"]],
    ["what is your name ?", ["I'm a chatbot made by Anmol !", "I am Anmol's assistant."]],
    ["bye|goodbye", ["Goodbye!", "See you later!", "Have a great day!"]],
    ["(.*)", ["I'm not sure how to respond to that."]]
]


chatbot = Chat(pairs, reflections)

print("Hello! I am a chatbot made by Anmol Agarwal . Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot.respond(user_input)
    print(f"Chatbot: {response}")