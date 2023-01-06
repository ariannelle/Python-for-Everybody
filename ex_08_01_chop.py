# chop function removes the first and last element from a list
def chop(stuff):
    del stuff[len(stuff) - 1]    #remove last element
    del stuff[0]                 #remove first element


things = list()
while True:
    inp = input('Enter an input: ')
    if inp == 'done': break
    things.append(inp)


less_things  = chop(things)
print(things)        #modified list
print(less_things)   #None
