from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, Trainer
chatbot = ChatBot('Celal Şengör')

Trainer = ChatterBotCorpusTrainer(chatbot)
Trainer.train("chatterbot.corpus.english")

while True:
    request = input('Ben :')
    response = chatbot.get_response(request)
    print('Celal şengör:',response)