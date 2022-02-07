from all_words import all_wordle_words as all_words
from all_words import get_word_by_day
from wordle_solver import *
from flask import Flask, render_template, request, redirect

from datetime import date
from datetime import datetime


import os, twit

STARTING_DATE = date(2022, 1, 1)

BLACK, YELLOW, GREEN, CROSS = '\U00002B1B', '\U0001F7E8', '\U0001F7E9', '\U0000274C'

app = Flask(__name__)

def make_tweet(col, number):
    if col[1] > 6: step_required = CROSS
    else: step_required = str( col[1] )

    pattern = ''
    cnt = 0
    for i in col[2]:
        if cnt >= 6: break
        for letter in i:
            if letter == 'G': pattern += GREEN
            elif letter == 'B': pattern += BLACK
            elif letter == 'Y': pattern += YELLOW
        pattern += '\n'
    return 'Wordle #' + str( number + 196 ) + ' ' + str( step_required ) + '/6\n' + pattern


@app.route('/')
def main():
    return 'twitter-wordle-bot'

@app.route('/tweet/<PASS>')
def tweet(PASS):
    if(PASS != twit.get_pass()):
        print("Not Authorized")
        return redirect('/')
    date_and_time = datetime.today()
    current_date = date(date_and_time.year, date_and_time.month, date_and_time.day)

    day = (current_date - STARTING_DATE).days

    word = get_word_by_day(day)

    try:
        twit.tweet( make_tweet( solver2( word, all_words.copy(), "adieu" ), day ) )
    except Exception as e:
        print(e)
    return redirect('/')

if __name__ == "__main__":
    port = 5000
    app.run(port=port, debug=True)