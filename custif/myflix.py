#!/usr/bin/env python3

print('Your workout plan is being generated')

# wrap connection in a float() to accept decimals as numbers
weight = float(input("How much weight are you trying to lose in pounds? "))

wrklist = ["25 pushups", "20 burpees", "30 squats"]
wrklist2 = ["15 pushups", "20 burpees", "25 squats"]
wrklist3 = ["15 pushups", "15  burpees", "20 squats"]

# if input value was higher or equal to 10
if weight > 15:
    message =  wrklist
elif weight > 10 and weight <= 15:
    message = wrklist2
else:    #elif weight <= 10:
    message = wrklist3
print(message)

