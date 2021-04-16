#!/usr/bin/python3

# standard library
from random import randint

# python3 -m pip install flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello welcome to FlaskGaming"

@app.route("/rps/<player>")
def rps(player):

    t = ["Rock", "Paper", "Scissors"]
    #assign a random play to the computer
    computer = t[randint(0,2)]

    player = player.capitalize()
    if player == computer:
        return "Tie!"
    elif player == "Rock":
        if computer == "Paper":
            return f"You lose! {computer} covers {player}"
        else:
            return f"You win! {player} smashes {computer}"
    elif player == "Paper":
        if computer == "Scissors":
            return f"You lose! {computer} cut {player}"
        else:
            return f"You win! {player} covers {computer}"
    elif player == "Scissors":
        if computer == "Rock":
            return f"You lose... {computer} smashes {player}"
        else:
            return f"You win! {player} cut {computer}"
    else:
        return f"That's not a valid play. Check your spelling!"

@app.route("/matchgame")
def matchgame():
    # if a user goes to /matchgame set a random value from 1 to 100 within
    # a cookie on their system
    # if they already have a cookie with a value, set a new value

    # if a user goes to /matchgame?guess=5
    # pull the value associated with "guess" off
    # get the value out of their cookie
    # compare the two
    # let them know if they need to guess higher or lower
    return


if __name__ == "__main__":
    app.run()
