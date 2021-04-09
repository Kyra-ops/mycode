#!/usr/bin/python3
""" Fill this in :) """

# for graphing
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# required to make HTTP requests
import requests


# pull in API keys
def apikey():
    #place your APIkey within /home/student/alphavantage.cred
    with open("/home/student/alphavantage.cred", "r") as nc:
        apikey = nc.readline()
        return apikey.rstrip("/n")   # remove any "extra" characters

def main():
    """run-time code"""

    # stock labels to search on via a loop
    # labels = ['DKNG', 'AAPL', 'NKE', 'TMUS', 'IBM']  
    labels = ['AAPL', 'NKE', 'TMUS', 'IBM']
    stockhigh = [] # seed an empty list
    stocklow = []  # seed an empyt list

    for label in labels:
        api = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={label}&apikey={apikey()}"
        # example:
        # api = http://api.open-notify.org/astros.json
        #apiDKNG = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=DKNG&apikey={apikey()}"
        #apiAAPL =  f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey={apikey()}" # <--- you have to fill in this!
        #apiNKE =  f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NKE&apikey={apikey()}"
        #apiTMUS =  f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TMUS&apikey={apikey()}"

        resp = requests.get(api)
        # respdata is the JSON attached to our 200+JSON response
        # converted to pythonic list and dictonaries
        quotedata = resp.json() # strip off our response)

        # add caputred data to our lists for graphing
        stockhigh.append(quotedata.get("Global Quote").get("03. high"))
        stocklow.append(quotedata.get("Global Quote").get("04. low"))


    print(labels)
    print(stockhigh)
    print(stocklow)
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, stockhigh, width, label='High Price')
    rects2 = ax.bar(x + width/2, stocklow, width, label='Low Price')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Price is USD')
    ax.set_title('High and Low Price by Stock Label')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    #ax.bar_label(rects1, padding=1)
    #ax.bar_label(rects2, padding=1)

    fig.tight_layout()

    # save out graph
    plt.savefig("/home/student/static/mygraph.png")

if __name__ == "__main__":
    main()

