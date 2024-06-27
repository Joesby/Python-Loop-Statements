#Task 1: Loop Condition Exploration
#Create a variable to keep track of iterations
iterator = 0

#Write a while loop with a condition that will never be false, creating an infinite loop
while(2 != 1):
    #count up with out iterator to make the following if statement true after 5 loops
    iterator += 1
    if iterator == 5:
        break

#Provide output so we know we actually broke out of the loop
print("The loop has been broken.")

#Task 2: Conditional Exit
#Modify the infinite loop from Task 1 to include a confition that will eventually be true and remove the break statement
#reset our iterator variable
iterator = 0

#Use a version of the previous if statment to become the new while condition
while(iterator != 5):
    iterator += 1

#Provide output so we know the loop broke
print("Our iterator hit level " + str(iterator) + "!")