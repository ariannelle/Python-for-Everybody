# check if input is integer or 'done'
count = 0
sum = 0.0

while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        flinp = float(inp)
    except:
        print('Invalid input')
        continue
    # tested for integer, done or other value
    count = count + 1
    sum = sum + flinp

print(sum, count, sum/count)
