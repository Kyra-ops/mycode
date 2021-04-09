#!/usr/bin/python3
"""Kyra | spacex upcoming launch data"""

import requests

def main():
    url = "https://api.spacexdata.com/v3/launches/upcoming"

    response = requests.get(url)

    # capture attached JSON from the returned 200 response
    launches = response.json()

    # show a single launch within the many launches
    for launch in launches:
        print(launch)


if __name__ == "__main__":
    main()
