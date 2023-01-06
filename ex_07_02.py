sum = 0.0
count = 0

inp = input('Enter a file name: ')
try:
    fhand = open(inp)
except:
    print('File cannot be opened:', inp)
    exit()
for line in fhand:
    line = line.rstrip() #remove extra space
    if line.startswith('X-DSPAM-Confidence:'):
        colpos = line.find(':') #find colon position
        value = line[colpos+2:] #extract confidence string value
        fl_value = float(value) #convert to float
        count = count + 1
        sum = sum + fl_value

print('The average spam confidence is:', sum/count)
