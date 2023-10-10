#ziyao chen, 10/27/2022, section 011, Problem 2, Part 2b:Number Analyzer

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

def is_odd(a):
    if a % 2 != 0:
        return True
    else:
        return False

def is_prime(a):
    if a == 1:
        return False
    else:
        for i in range(2,a):
            if a % i == 0:
                return False
        else:
            return True

def is_perfect(a):
    b = 0
    for i in range(1,a):
        if a % i == 0:
            b = b + i
    if a == b:
        return True
    else:
        return False

def is_abundant(a):
    b = 0
    for i in range(1,a):
        if a % i == 0:
            b = b + i
    if a < b:
        return True
    else:
        return False
    
while True:
    print("Main Menu")
    print()
    print("1 - Find all prime numbers within a given range")
    print("2 - Find all perfect numbers within a given range")
    print("3 - Find all abundant numbers within a given range")
    print("4 - Chart all even, odd, prime, perfect and abundant numbers within a given range")
    print("5 - Quit")
    print()
    choice = input("Your choice: ")
    if choice == "1":
        while True:
            start_num = int(input("Enter starting number: "))
            if start_num <= 0:
                print("Invalid, try again")
            else:
                break

        while True:
            end_num = int(input("Enter ending number: "))
            if end_num < start_num:
                print("Invalid, try again")
            else:
                break
        print()
        print("All prime numbers between",start_num,"and",end_num)
        print("##############")
        for ii in range(start_num, end_num + 1):
            d3 = is_prime(ii)
            if d3 == True:
                print(ii)
        print("##############")
        print()

    elif choice == "2":
        while True:
            start_num = int(input("Enter starting number: "))
            if start_num <= 0:
                print("Invalid, try again")
            else:
                break

        while True:
            end_num = int(input("Enter ending number: "))
            if end_num < start_num:
                print("Invalid, try again")
            else:
                break
        print()
        print("All perfect numbers between",start_num,"and",end_num)
        print("##############")
        for ii in range(start_num, end_num + 1):
            d4 = is_perfect(ii)
            if d4 == True:
                print(ii)
        print("##############")
        print()

    elif choice == "3":
        while True:
            start_num = int(input("Enter starting number: "))
            if start_num <= 0:
                print("Invalid, try again")
            else:
                break

        while True:
            end_num = int(input("Enter ending number: "))
            if end_num < start_num:
                print("Invalid, try again")
            else:
                break
        print()
        print("All abundant numbers between",start_num,"and",end_num)
        print("##############")
        for ii in range(start_num, end_num + 1):
            d5 = is_abundant(ii)
            if d5 == True:
                print(ii)
        print("##############")
        print()

    elif choice == "4":
        while True:
            start_num = int(input("Enter starting number: "))
            if start_num <= 0:
                print("Invalid, try again")
            else:
                break

        while True:
            end_num = int(input("Enter ending number: "))
            if end_num < start_num:
                print("Invalid, try again")
            else:
                break
        print()
        print("Number    Even      Odd       Prime     Perfect   Abundant",end="")
        for ii in range(start_num, end_num + 1):
            d1 = is_even(ii)
            d2 = is_odd(ii)
            d3 = is_prime(ii)
            d4 = is_perfect(ii)
            d5 = is_abundant(ii)
            print("\n",format(ii,"<9"),end="")
            if d1 == True:
                print("x        ",end=" ")
            else:
                print("         ",end=" ")
            if d2 == True:
                print("x        ",end=" ")
            else:
                print("         ",end=" ")
            if d3 == True:
                print("x        ",end=" ")
            else:
                print("         ",end=" ")
            if d4 == True:
                print("x        ",end=" ")
            else:
                print("         ",end=" ")
            if d5 == True:
                print("x        ",end=" ")
            else:
                print("         ",end=" ")
        print()
        print()
        
    elif choice == "5":
        print()
        print("Goodbye!")
        break

    else:
        print("I don't understand that ...")
        print()
        print()
