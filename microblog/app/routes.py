from app import app
from flask import render_template, request
from random import  choice
symbols = ["🍒", "🔔", "🍋", "⭐", "🍇"]

def spin():
    return choice(symbols), choice(symbols), choice(symbols)

def check_win(symbol1, symbol2, symbol3):
    if symbol1 == symbol2 == symbol3:
        if symbol1 == "🍒":
            return "Вы выиграли 5x ставку!", 5
        elif symbol1 == "🔔":
            return "Вы выиграли 3x ставку!", 3
        else:
            return "Вы выиграли 2x ставку!", 2
    else:
        return "Попробуйте еще раз.", 0

@app.route('/', methods=['GET', 'POST'])
def index():
    message = "жми"
    symbols = ("", "🤗", "")
    if request.method == 'POST':
        symbols = spin()
        message, multiplier = check_win(symbols[0],symbols[1],symbols[2])
    return render_template('index.html', message=message, symbols=symbols)

