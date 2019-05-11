from bottle import request, route, run, template, redirect, static_file
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

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
