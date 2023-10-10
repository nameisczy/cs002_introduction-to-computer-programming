#ziyao chen, 10/27/2022, section 011, Problem 3, Part 3

while True:
    times = int(input("How many problems would you like to attempt? "))
    if times <= 0:
        print("Invalid number, try again")
        print()
    else:
        break

while True:
    width = int(input("How wide do you want your digits to be? 5-10: "))
    if width > 10 or width < 5:
        print("Invalid width, try again")
    else:
        break
    print()
print()
while True:
    character = input("What character would you like to use? ")
    if len(character) == 1:
        print()
        break
    else:
        print("String too long, try again")

print("Here we go!")
print()
count = 0
import random
import digitalclock
for i in range(1,times+1):
    print("What is .....")
    print()
    number1 = random.randint(0,9)
    digitalclock.print_number(number1, width, character)
    print()
    operator = random.randint(1,2)
    if operator == 1:
        print(digitalclock.plus(width, character))
        operator = "+"
    else:
        print(digitalclock.minus(width, character))
        operator = "-"
    print()
    number2 = random.randint(0,9)
    digitalclock.print_number(number2,width,character)
    answer = int(input("= "))
    if digitalclock.check_answer(number1, number2, answer, operator) == True:
        print("Correct!")
        count = count + 1
    else:
        print("Sorry, that's not correct.")
    print()
print("You got", count, "out of", times, "correct!")
