genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
genre_sublist = []

#Task 1: The Selective DJ
#Create a new list by slicing the genres list from the second to fourth tracks
#iterate through the entire genre list
for i in range(len(genres)):
    #Check if the element exists within the sliced portion of the list
    if genres[i] in genres[1:4]:
        #If the element is is the correct portion, add it to the new list
        genre_sublist.append(genres[i])
        print(genres[i])

#Add a space before the next set of output
print()

#Task 2: The One-Liner Band with List Comprehensions
#Create the new list to add appended elements to
type_of_music = []

#iterate through each element of the genre list
for j in range(len(genres)):
    #Add the current genre, plus the word 'Music' to the new list
    type_of_music.append(genres[j] + " Music")

#Output the new list
print(type_of_music)

#Add a space before the next set of output
print()

#Task 3: Numerical Beats with range()
#Create a variable used count down from 10
count_down = 10

#Loop for the number of times we want to count down from
for k in range(10):
    print(str(count_down) + "...")
    
    #reduce the iterator
    count_down -= 1

#Print the final output after the count down has finished
print("The beat drops now!")