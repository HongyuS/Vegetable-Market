# Return true if the card number is valid
def isValid(number):
    _sum = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
    if _sum % 10 == 0:
        return True
    else:
        return False

# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    _sum = 0
    for i in range(2, len(number)+1, 2):
        evenPlace = int(number[len(number) - i])
        if evenPlace < 5:
            _sum += evenPlace * 2
        else:
            _sum += getDigit(evenPlace * 2)
    return _sum

'''
Return this number if it is a single digit,
otherwise, return the sum of the two digits
'''
def getDigit(n):
    n = str(n)
    return int(n[0]) + int(n[1])

# Return sum of odd place digits in number
def sumOfOddPlace(number):
    _sum = 0
    for i in range(1, len(number), 2):
        _sum += int(number[len(number) - i])
    return _sum

def main():
    number = input('Please enter card number >')
    if number.isdigit() and isValid(number):
        print('The card number is valid.')
    else:
        print('The card number is invalid.')

if __name__ == "__main__":
    main()
