#ziyao chen, 10/3/2022, section 011, Roll the Dice

sides = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
while sides != 4 and sides != 6 and sides != 8 and sides != 10 and sides != 12 and sides != 20:
    print("Invalid size, try again.")
    sides = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
print("\n")
print("Thanks, here we go!")

num1 = 1
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
num7 = 0
die1_sum = 0
die2_sum = 0

while True:
    import random
    die1 = random.randint(1,sides)
    die2 = random.randint(1,sides)
    die1_sum = die1_sum + die1
    die2_sum = die2_sum + die2
    print("\n",num1,". ","die #1 is *",die1, "* and die #2 is *",die2,"* ",sep="",end="")
    if (die1 == 2 or die1 == 4 or die1 == 6 or die1 == 8 or die1 == 10 or die1 == 12 or die1 == 14 or die1 == 16 or die1 == 18 or die1 == 20) and (die2 == 2 or die2 == 4 or die2 == 6 or die2 == 8 or die2 == 10 or die2 == 12 or die2 == 14 or die2 == 16 or die2 == 18 or die2 == 20):
        print("Evens!",end="")
        num3 = num4 + 1
    if (die1 == 1 or die1 == 3 or die1 == 5 or die1 == 7 or die1 == 9 or die1 == 11 or die1 == 13 or die1 == 15 or die1 == 17 or die1 == 19) and (die2 == 1 or die2 == 3 or die2 == 5 or die2 == 7 or die2 == 9 or die2 == 11 or die2 == 13 or die2 == 15 or die2 == 17 or die2 == 19):
        print("Odds!",end="")
        num4 = num5 + 1
    if die1 == die2:
        print("Doubles!",end="")
        num2 = num2 + 1
    if die1 + die2 == sides:
        print("Sum value is size value!",end="")
        num7 = num7 + 1
    if die1 == sides and die2 == sides:
        print("High!",end="")
        num3 = num3 + 1
    if (die1 == sides and die2 == 1) or (die1 == 1 and die2 == sides):
        print("High / Low!",end="")
        num6 = num6 + 1
    if die1 == 1 and die2 == 1:
        print("Snake Eyes!")
        print("\n")
        print("You finally got snake eyes on roll #",num1)
        print("Along the way you rolled DOUBLES ",num2," times. (",format(num2/num1/100,'.2f'),"% of all rolls were doubles)",sep="")
        print("Along the way you rolled TWO HIGH VALUES ",num3," times. (",format(num3/num1/100,'.2f'),"% of all rolls were two high values)",sep="")
        print("Along the way you rolled TWO EVENs ",num4," times. (", format(num4/num1/100,'.2f'),"% of all rolls were two evens)",sep="")
        print("Along the way you rolled TWO ODDS ",num5," times. (",format(num5/num1/100,'.2f'),"% of all rolls were two odds)",sep="")
        print("Along the way you rolled HIGH / LOW ",num6," times. (", format(num6/num1/100,'.2f'),"% of all rolls were high/low)",sep="")
        print("Along the way you rolled A SUM VALUE ",num7," times. (", format(num7/num1/100,'.2f'),"% of all rolls were a sum value",sep="")
        print("Average roll for die #1:",die1_sum)
        print("Average roll for die #2:",die2_sum)
        break
    num1 = num1 + 1
