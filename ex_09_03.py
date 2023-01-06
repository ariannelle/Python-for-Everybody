# this programme checks for amount of mail messages from each sender in a maibox file
inp = input('Enter a file name: ')
try:
    fhand = open(inp)
except:
    print('File cannot be opened:', inp)
    exit()

mailbox = dict()
for line in fhand:
    line = line.rstrip() #remove extra space
    if line.startswith('From '): # only selects lines starting with From
        words = line.split() #split target lines into words
        #print(words[1])
        sender = words[1] # selects the senders email address from the string
        mailbox[sender] = mailbox.get(sender, 0) + 1
print(mailbox) # prints senders email address and the count
