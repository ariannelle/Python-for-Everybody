def computegrade(score):
    if score > 1: #score is out of range
        return 'Bad score'

    elif score >= 0.9:
        return 'A'

    elif score >= 0.8:
        return 'B'

    elif score >= 0.7:
        return 'C'

    elif score >= 0.6:
        return 'D'

    elif score < 0.6:
        return 'F'


inp = input('Please enter score: ')
try: # score is not an integer
    score = float(inp)
except:
    print('Bad score')
    quit()


grade = computegrade(score)
print(grade)
