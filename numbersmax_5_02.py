smallest = None
largest = None
#test for integer or done
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        flinp = float(inp)
    except:
        print('Invalid number')
        continue

#deciding largest and smallest
    if largest is None or flinp > largest:
        largest = flinp
    if smallest is None or flinp < smallest:
        smallest = flinp

print('largest:', largest, 'smallest:', smallest)
