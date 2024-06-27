#Task 1: Your Mood Today
#Import the random package
import random
#Create a list of moods and days of the week
moods = ["Happy", "Sad", "Angry", "Calm", "Energetic"]
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Using a for loop, iterate a number of times using the range function, and use the len() function for flexibility
for i in range(len(days_of_the_week)):
    #On each loop use the iteration to select the day of week, and the random.choice function to select a random mood from that list
    print("On " + days_of_the_week[i] + ", you were feeling " + random.choice(moods) + ".")