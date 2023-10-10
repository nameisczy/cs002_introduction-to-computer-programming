#ziyao chen, 9/20/2022, section 011, Guess the Number Game with 3 Attempts

import random
print("I'm thinking of a number between 1 and 10!")
num = random.randint(1,10)
try1 = int(input("What's your guess? "))
if try1 == num:
    print("You got it!")
    print("The secret number was ",num,".",sep="")
    print("It took you 1 try to guess the number.")
elif try1 > num:
    print("Too high, try again.")
    try2 = int(input("What's your guess? "))
    if try2 == num:
      print("You got it!")
      print("The secret number was ",num,".",sep="")
      print("It took you 2 tries to guess the number.")
    elif try2 > num:
        print("Too high, try again.")
        try3 = int(input("What's your guess? "))
        if try3 == num:
            print("You got it!")
            print("The secret number was ",num,".",sep="")
            print("It took you 3 tries to guess the number.")
        else:
            print("The secret number was ",num,".",sep="")
            print("You didn't guess the number.")
    else:
        print("Too low, try again.")
        try3 = int(input("What's your guess? "))
        if try3 == num:
            print("You got it!")
            print("The secret number was ",num,".",sep="")
            print("It took you 3 tries to guess the number.")
        else:
            print("The secret number was ",num,".",sep="")
            print("You didn't guess the number.")
else:
    print("Too low, try again.")
    try2 = int(input("What's your guess? "))
    if try2 == num:
      print("You got it!")
      print("The secret number was ",num,".",sep="")
      print("It took you 2 tries to guess the number.")
    elif try2 > num:
        print("Too high, try again.")
        try3 = int(input("What's your guess? "))
        if try3 == num:
            print("You got it!")
            print("The secret number was ",num,".",sep="")
            print("It took you 3 tries to guess the number.")
        else:
            print("The secret number was ",num,".",sep="")
            print("You didn't guess the number.")
    else:
        print("Too low, try again.")
        try3 = int(input("What's your guess? "))
        if try3 == num:
            print("You got it!")
            print("The secret number was ",num,".",sep="")
            print("It took you 3 tries to guess the number.")
        else:
            print("The secret number was ",num,".",sep="")
            print("You didn't guess the number.")
