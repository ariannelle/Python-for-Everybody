
count = 0
inp = input('Enter a file name: ')
try:
    fhand = open(inp)
except:
    print('File cannot be opened:', inp)
    exit()

for line in fhand:
    line = line.rstrip() #remove extra space
    if line.startswith('From '):
        count = count + 1
        words = line.split() #split target lines into words
        print(words[1])

print('There were', count, 'lines in the file with From as the first word')
