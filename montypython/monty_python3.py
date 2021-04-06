#!/usr/bin/env python3
round = 0
answer = " "

while round < 3 and answer  != "Stuck":
    round += 1 
    answer = input('Finish the song lyrics," If it\'s up then it\'s -----!": ')
    if answer == 'Stuck':
        print('Correct')
    elif round == 3:
        print("Sorry the answer was Stuck.")
    else:
        print("Sorry! Try again!")
