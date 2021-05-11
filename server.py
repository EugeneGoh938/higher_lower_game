from flask import Flask
import random
random_number = random.randint(0, 9)
print(random_number)
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://i.pinimg.com/originals/5a/78/6c/5a786cb6570dcd01677676d3859c0135.gif' width=1000>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/Y8b6jyisoj5gA/giphy.gif' width=1500>"
    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/ZDOXnhXvESwSY/giphy.gif' width=1000>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=800>"

if __name__ == "__main__":
    app.run(debug=True)
