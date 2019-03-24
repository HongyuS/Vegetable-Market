def sqrt(n):    # function to calculate square root
    lastGuess = 1
    while True:
        nextGuess = (lastGuess + (n/lastGuess)) / 2
        if nextGuess - lastGuess <= 0.0001\
                and lastGuess - nextGuess <= 0.0001:
            return nextGuess
        else:
            lastGuess = nextGuess

while True:     # an example of using the function
    try:
        n = float(input('Enter a positive number >'))
    except:
        print('Invalid input.\nPlease try again!')
    else:
        if n > 0:
            break
        else:
            print('Please input a positive number.')
print('The square root of', n, 'is:', sqrt(n))
