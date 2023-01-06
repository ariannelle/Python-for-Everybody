# this programme records domain name where message was sent from

inp = input('Enter a file name: ')
try:
    fhand = open(inp)
except:
    print('File cannot be opened:', inp)
    exit()

mailbox = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '): # only selects lines starting with "From"
        words = line.split()
        sender = words[1] # selects only the senders email address from the string
        #atpos = sender.find('@') #find at position
        address= sender.split('@') #split at @
        domain = address[1] # selects only the domain position
        #print(domain)
        mailbox[domain] = mailbox.get(domain, 0) + 1
print(mailbox)
