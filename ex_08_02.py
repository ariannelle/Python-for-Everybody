# break and fix code in pg 105

hand = open('mbox-shortedited.txt')
count = 0
for line in hand:
    words = line.split()
    #print('Debug:', words)
    if len(words) < 3 : continue #modified from len == 0 since theres lines w/ < 3 words so no index of 2
    if words[0] != 'From' : continue # skips lines that do not start with 'From'
    print (words[2])
