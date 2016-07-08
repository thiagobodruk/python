from chatterbot import ChatBot
from chatterbot.training.trainers import ListTrainer
import warnings

warnings.filterwarnings("ignore",category=DeprecationWarning)

chatbot = ChatBot("Johnny Five")
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

response = chatbot.get_response("Thank you!")
print(response)