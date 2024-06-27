#Task 1: Your Mood Tracker
#Import the random package
import random

#Create a list of moods, days of the week, and times of day
moods = ["happy", "sad", "angry", "calm", "energetic", "tired", "irritated", "lonely", "confident"]
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time_of_day = ["morning", "afternoon", "evening", "night"]

#use a for loop to iterate the number of elements in days_of_the_week list, using the len() function for flexibility
for i in range(len(days_of_the_week)):
    #use another for loop to iterate through the number of elements in the time_of_day list, again using the len() function
    for j in range(len(time_of_day)):
        #the 'i' loop will stay on the first day_of_the_week element while the 'j' loop performs all iterations for time_of_day
        print("On " + days_of_the_week[i] + " " + time_of_day[j] + " you were " + random.choice(moods) + ".")