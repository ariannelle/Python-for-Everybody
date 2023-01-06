#this programme stores the words in text as keys in a dictionary
book = dict()
fhand = open('words.txt')
for line in fhand:
    words = line.split() #split lines into words
    for word in words:
        book[word] = book.get(word, 0) + 1 #add each word to dictionary and establish count


for k,v in book.items(): # k and v correspond to key and value respectively
    print(k, v)

#check if a word is in the dictionary
#check_word = input('Enter a word: ')
#present = check_word in book
#print(present)
