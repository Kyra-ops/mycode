#!/usr/bin/python3

# required to make HTTP requests
import requests

def main():
    pokemon = input("What pokemon are we viewing? ") 
    # api goes here
    # example:
    # api = http://api.open-notify.org/astros.json
    api = "http://pokeapi.co/api/v2/pokemon/"   # <--- you have to fill in this!

    # sent HTTP GET and create resp, a response object
    resp = requests.get(api + pokemon)

    # respdata is the JSON attached to our 200+JSON response
    # converted to pythonic list and dictonaries
    respdata = resp.json()

    # display ALL of the data we captured
    print(respdata)


    # spend some time working with dataset
    # see if you can return the data in an interesting format
    # (make it more readable)
    print(respdata.get("abilities"))
main()
