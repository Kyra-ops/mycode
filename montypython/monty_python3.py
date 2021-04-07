#!/usr/bin/env python3
""" fill this in """

def main():
    """ runtime code """
    counter = 0
    answer = " "

    while counter < 3 and answer  != "Stuck":
        counter += 1
        answer = input('Finish the song lyrics," If it\'s up then it\'s -----!": ')
        if answer == 'Stuck':
            print('Correct')
        elif counter == 3:
            print("Sorry the answer was Stuck.")
        else:
            print("Sorry! Try again!")

main()
