@ -0,0 +1,55 @@
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

# set plot style: grey grid in the background:
sns.set(style="darkgrid")

# load dataset
tips = sns.load_dataset("tips")

# Set the figure size
plt.figure(figsize=(8, 8))

# grouped barplot
sns.barplot(x="Stock Symbol", y="Price USD", hue="smoker", data=tip:s, ci=None);
