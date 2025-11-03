from flask import Flask
import random

num = random.randint(0, 9)
url = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
correct_url = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
low_url = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
high_url = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 to 9</h1>"
            f"<img src='{url}'>")

@app.route("/<int:number>")
def find_number(number):
    if number == num:
        return (f"<h1>You got it!</h1>"
                f"<img src='{correct_url}'>")
    else:
        if number <num:
            return (f"<h1>Number is too low</h1>"
                    f"<img src='{low_url}'>")
        else:
            return (f"<h1>Number is too high</h1>"
                    f"<img src='{high_url}'>")

if __name__ == "__main__":
    app.run(debug=True)