#Task 1: Random Choice Game
#Create a game where a player has a list of items, they have to guess which item was selected.
#Use random.choice() to select the item and take the user's guess with input.
#Provide feedback on whether they guessed correctly or not.

#Import the random package
import random

#Create a list of items the user has to select from
fruits = ["apple", "banana", "orange", "cherry", "grape", "strawberry", "pineapple"]

#Provide the user with options to choose from
print("Welcome to my guessing game!")
print("Please guess which fruit I'm going to select.")
#use end statement to print different print functions on the same line
print("Your options are", end = " ")
#use a for loop to iterate through the list, leaving out the last element so we don't add an unnecessary comma
for i in range(len(fruits) - 1):
    print(fruits[i], end = ", ")
#finish the output of options with the last item in the list we previously left out
print ("or " + fruits[-1])

#Ask the user to guess which item will be selected
users_guess = input("Which fruit will you pick? ")

#Randomly select an item from the fruits list
right_answer = random.choice(fruits)
#Use a while loop to give the user multiple attempts if they don't guess it right, force the users input to all lowercase for flexibility
while users_guess.lower() != right_answer:
    #reroll the right answer
    right_answer = random.choice(fruits)
    #Tell the user they didn't guess correctly
    print("I'm sorry, that wasn't correct.")
    #Prompt the user for another guess
    users_guess = input("Which fruit do you think it is now? ")
else:
    print("That was right! You win!")


