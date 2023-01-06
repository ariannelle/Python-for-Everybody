# this program reads a mailbox file and categorises each mail message by which day of the week it was sent 
inp = input('Enter a file name: ')
try:
    fhand = open(inp)
except:
    print('File cannot be opened:', inp)
    exit()

book = dict()
for line in fhand:
    line = line.rstrip() #remove extra space
    if line.startswith('From '): # only selects lines starting with From
        words = line.split() #split target lines into words
        #print(words[2])
        day = words[2] # selects the day from the string
        book[day] = book.get(day, 0) + 1
print(book) # prints days and the count
