fhand = open('mbox-shortedited.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) < 3 or words[0] != 'From' : continue #modified to match prev exercise
    print(words[2])
