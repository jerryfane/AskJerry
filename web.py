from bottle import request, route, run, template, redirect, static_file
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import askjerry

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer_personal = ListTrainer(chatbot)

askjerry.trainJerry(trainer_personal)

# Train based on the english corpus
trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")

@route('/')
def homepage():
    return template('./homepage')

@route('/ask', method='POST')
def ask():
    question = request.forms.get('question')
    response = chatbot.get_response(question)

    info = {'response': response}
    return template('./response', info)



run(host='localhost', port=3000)
