#ziyao chen, 3/10/2022, section 011, Pick Up Sticks

stick_num = int(input("How many sticks (10-100)? "))
while True:
    if stick_num > 100:
        print("Sorry, that's too many sticks. Try again")
        stick_num = int(input("How many sticks (10-100)? "))
    elif stick_num < 10:
        print("Sorry, that's too few sticks. Try again")
        stick_num = int(input("How many sticks (10-100)? "))
    else:
        print("Great Let's play ...")
        break
left_num = stick_num
while True:
    print("\n")
    print("Turn: Player 1")
    print("There are",left_num,"sticks on the table.")
    take_num = int(input("How many sticks do you want to take (1, 2 or 3)? "))
    if take_num != 1 and take_num != 2 and take_num != 3:
        print("Sorry, that's not a valid number.")
        continue
    else:
        left_num = left_num - take_num
        if left_num < 0:
            print("Sorry, that would bring the total # of sticks below 0. Try again.")
            left_num = left_num+take_num
        if left_num == 0:
            print("\n")
            print("There are no sticks left on the table! Game over.")
            print("Player 2 wins!")
            break
    print("\n")
    print("Turn: Player 2")
    print("There are",left_num,"sticks on the table.")
    take_num = int(input("How many sticks do you want to take (1, 2 or 3)? "))
    left_num = left_num - take_num
    if left_num < 0:
        print("Sorry, that would bring the total # of sticks below 0. Try again.")
        left_num = left_num+take_num
    if left_num == 0:
        print("\n")
        print("There are no sticks left on the table! Game over.")
        print("Player 1 wins!")
        break
