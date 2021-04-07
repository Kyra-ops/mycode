#!/usr/bin/env python3
  
import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n********Details of Interface - ' + i + ' ************')
    try:    # This is a new line, you also need to indent the code below this line by 4 whitespaces
        print('MAC: ', end='')
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message
