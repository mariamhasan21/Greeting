# Create a Python program capable of greeting you with Good Morning, Good Afternoon and Good Evening.
import time
print("---------------Welcome to the console---------------")
user_time = int(input("Enter the time (24 Hour Clock): ")) #takes the input
#used execpt handling in case if the user inputs anything rather than time
try:
    if (user_time >= 0 and user_time < 12):
            print("Good morning, sir!")
    elif (user_time >= 12 and user_time < 17):
            print("Good afternoon, sir!")
    elif (user_time >= 17 and user_time <= 24):
            print("Good evening, sir")
    else:
            print("Please enter time within 0-24 Hour")
except ValueError:
    print("Invalid time")
