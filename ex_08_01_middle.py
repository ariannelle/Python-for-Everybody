# middle function contains everything except the first and last element from a list
def middle(stuff):
    return stuff[1:len(stuff)-1] # return middle of list without first and last elements

things = list()   #user enters list elements
while True:
    inp = input('Enter an input: ')
    if inp == 'done': break
    things.append(inp)

ends = middle(things)
print(ends)
