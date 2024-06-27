# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

#Task 1: Use a For Loop
#Have the For loop iterate for the number of elements in the list
for i in range(4):
    print("Track " + str(i + 1) + ": " + genres[i],  end = ", ")

    #Check the number of iterations and add a message for each
    if i == 0:
        print("the sound of the soul.")
    elif i == 1:
        print("release your inner rebel.")
    elif i == 2:
        print("powerful messages and sick beats.")
    elif i == 3:
        print("soothes and relaxes the mind.")
    #Add output in case the loop iterates outside the expected amount of times
    else:
        print("ERROR") 

print() #Add space before the next set of output

#Task 2: Use a While Loop
#Create a variable to be the iterator
j = 0

#using the iterator, print out each element and its message, then increase the value of the iterator to continue the loop
while j != 4:
    print("Track " + str(j + 1) + ": " + genres[j],  end = ", ")

    #Check the number of iterations and add a message for each
    if j == 0:
        print("the sound of the soul.")
    elif j == 1:
        print("release your inner rebel.")
    elif j == 2:
        print("powerful messages and sick beats.")
    elif j == 3:
        print("soothes and relaxes the mind.")
    #Add output in case the loop iterates outside the expected amount of times
    else:
        print("ERROR") 

    j += 1

print() #Add space before the next set of output

#Task 3: Use the range() Function in a loop
#Use the length of the list to iterate though all elements
for k in range(len(genres)):
    #Determine if the genre has a light show
    #Genres with light shows
    if k == 1 or k == 2:
        print("Track " + str(k + 1) + ": " + genres[k] + ", the light show is ready.")
    #Genres without light shows get skipped
    else:
        pass