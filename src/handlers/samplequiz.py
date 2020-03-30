from bottle import get, post, request
from datetime import datetime
import random
import requests

from lib.template import render
from . import redirect_if_not_logged_in


@get('/samplequiz')
def samplequiz():
    redirect_if_not_logged_in()

    # This will be a list.
    history = requests.get('https://api.spacexdata.com/v3/history').json()

    # Randomize the order of items in the list.
    random.shuffle(history)

    # Use the first one in the randomized list as the question to ask.
    question = history[0]

    title = question['title']
    details = question['details']
    correct_answer = datetime.fromtimestamp(question['event_date_unix']).year
    possible_answers = range(2000, 2021)

    # Sometimes the date is in the question, so remove the year portion.
    details = details.replace(str(correct_answer), '????')

    return render('samplequiz.html', {
        'title': title,
        'details': details,
        'correct_answer': correct_answer,
        'possible_answers': possible_answers,
    })


@post('/samplequiz')
def samplequiz():
    redirect_if_not_logged_in()

    title = request.POST['title']
    details = request.POST['details']
    user_answer = request.POST['user_answer']
    correct_answer = request.POST['correct_answer']

    return render('samplequiz.html', {
        'title': title,
        'details': details,
        'user_answer': user_answer,
        'correct_answer': correct_answer,
    })
