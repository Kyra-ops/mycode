#!/usr/bin/env python3
round = 0
while True:
    round = round + 1
    print ('Finish the song lyrics, "If it\'s up then it\'s  -----!"')
    answer = input("Your guess--> ")
    if answer == 'Stuck':
        print('Correct')
        break
    elif round == 3:
        print("Sorry the answer was Stuck.")
        break
    else:
        print("Sorry! Try again!")

