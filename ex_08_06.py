# enter numbers into a list and find maximum and minimum

things = list() #create empty list
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    try: # check if integer is entered
        flinp = float(inp)
    except:
        print('Invalid input')
        continue
    things.append(flinp) # add number to list

print('Maximum:', max(things))
print('Minimum:', min(things))
