from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance:
chatbot = ChatBot("MyAdvancedChatbot")

# Create a trainer:
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train("chatterbot.corpus.english")

# you can add custom training data here
# For example:
# trainer.train([
#     "How are you?",
#     "I'm good, thanks!",
#     "What's your favorite color?",
#     "I like blue."
# ])
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot.get_response(user_input)
    print(f"Chatbot: {response}")