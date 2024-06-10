# %%
# Import necessary libraries
import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",],
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",],
    ],
    [
        r"what is your name ?",
        ["I'm a bot. I'm called Part-time Bot.",]
    ],
    [
        r"(.*) (happy|glad|excited) (.*)",
        ["That's great to hear", "%1 %2 %3? That's good!",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(.*) age?",
        ["I'm a bot, I don't have an age",]
    ],
    [
        r"what is the weather in (.*)?",
        ["I'm sorry, I cannot provide weather information as I don't have access to the internet.",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a bot, I don't have the ability to play or watch sports/games.",]
    ],
    [
        r"who (.*) (president|prime minister)?",
        ["I'm sorry, I cannot provide current world information as I don't have access to the internet.",]
    ],
    [
        r"quit",
        ["Bye. It was nice talking to you. See you soon :)"]
    ],
]

# Function to add a new pattern and response
def add_pattern(pattern, response):
    pairs.append([pattern, response])

# Create Chat Bot
def chatbot():
    print("Hi, I'm the chatbot you built")

chat = Chat(pairs, reflections)
chatbot()
chat.converse()


