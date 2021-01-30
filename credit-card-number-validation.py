''' Credit card number validation

Credit card numbers follow certain patterns: It must have between 13 and 16 digits, 
and the number must start with:
■ 4 for Visa cards
■ 5 for MasterCard credit cards
■ 37 for American Express cards
■ 6 for Discover cards

In 1954, Hans Luhn of IBM proposed an algorithm for validating credit card numbers. The
algorithm is useful to determine whether a card number is entered correctly or whether
a credit card is scanned correctly by a scanner. The validation steps are as the following:
1. Double every second digit from right to left. If doubling of a digit results in a
twodigit number, add up the two digits to get a single-digit number. 
2. Add all single-digit numbers from Step 1
3. Add all digits in the odd places from right to left in the card number.
4. Sum the results from Steps 2 and 3. 
5. If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is
invalid.'''

# Prompt Card Number to be verified
cardNumber = str(input("Enter card number: "))

#Return this number if it is a single digit, otherwise,
#return the sum of the two digits
def getDigit (digit):
    if digit // 5 == 0:
        return digit * 2
    elif digit // 5 == 1:
        firstDoubledDigit = digit * 2 // 10
        lastDoubledDigit = digit * 2 % 10
        return firstDoubledDigit + lastDoubledDigit

#Get the result from Step 2
def sumOfDoubleEvenPlace(cardNumber):
    sum = 0
    position = len(cardNumber) - 2
    while position >= 0:
        doubleValue = getDigit(int(cardNumber[position]))
        sum += doubleValue
        position -= 2
    return sum

#Return sum of odd place digits in number
def sumOfOddPlace(cardNumber):
    sum = 0
    position = len(cardNumber) - 1
    while position >= 0:
        sum += int(cardNumber[position])
        position -= 2
    return sum

#Return true if the card number is valid
def isValid(cardNumber):
    sum = sumOfDoubleEvenPlace(cardNumber) + sumOfOddPlace(cardNumber)
    if sum % 10 == 0:
        return True
    else:
        return False

#checking card type
if cardNumber[0] == '4':
    cardType = 'Visa'
elif cardNumber[0] == '5':
    cardType = 'Master'
elif cardNumber[0:1] == '37':
    cardType == 'American Express'
elif cardNumber [0] == '6':
    cardType = ' Discover'
else:
    cardType = 'not identified'

# Output
if isValid(cardNumber):
    print ("This is a valid", cardType, "card")
else:
    print("This is a invalid", cardType, "card")
