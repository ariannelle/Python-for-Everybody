#track unique words in text and produce list

things = list() #create empty list
fhand = open('romeo.txt')

for line in fhand:
    words = line.split() #splits line into words
    for word in words: # look at each word in line
        if word in things: #is word in the new list
            continue
        things.append(word) #add new word to list
things.sort() #sort in alphabetical order
print(things)
