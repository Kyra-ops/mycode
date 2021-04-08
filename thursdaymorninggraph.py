import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# required to make HTTP requests
import requests

def main():
function=TIME_SERIES_INTRADAY
symbol=DKNG, AAPL, NKE, TMUS, IBM
interval=5min
outputsize=compact
    # api goes here
    # example:
    # api = http://api.open-notify.org/astros.json
    api = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=DKNG&interval=5min&apikey=IXLGYNLS1XWYB6NU"
    api =  "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&apikey=IXLGYNLS1XWYB6NU" # <--- you have to fill in this!
    api =  "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=NKE&interval=5min&apikey=IXLGYNLS1XWYB6NU"
    api =  "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TMUS&interval=5min&apikey=IXLGYNLS1XWYB6NU"
    api =  "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=IXLGYNLS1XWYB6NU"

    
    # sent HTTP GET and create resp, a response object
    resp = requests.get(api)

    # respdata is the JSON attached to our 200+JSON response
    # converted to pythonic list and dictonaries
    respdata = resp.json()

    # display ALL of the data we captured
    print(respdata)

labels = ['DKNG', 'AAPL', 'NKE', 'TMUS', 'IBM']
January = [20, 34, 30, 35, 27]
April = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Open')
rects2 = ax.bar(x + width/2, women_means, width, label='Close')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Cost')
ax.set_title('Price by Open and Close')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
