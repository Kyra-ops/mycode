#!/usr/bin/env python3
# create a list of strings
stores = [{"name": "Target", "retail": ["food", "clothes", "furniture", "alcohol", "pharmacy"]},
         {"name": "Walmart", "retail": ["clothes", "furniture", "alcohol", "pharmacy"]},
         {"name": "Publix", "retail": ["food", "pharmacy", "alcohol"]}]
# loop across the list called stores
for x in stores:
    print("The store is:" + x.get("name"))   # newline, print current store, and end without newline
print("\nOur loop has ended.") # print when loop has finished

