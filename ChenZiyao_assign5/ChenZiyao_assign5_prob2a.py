#ziyao chen, 10/3/2022, section 011, Prime Number Finder

while True:
    test_num = int(input("Enter a positive number to test: "))
    if test_num > 2:
        print("\n")
        for divisor in range(2,test_num):
            if test_num % divisor == 0:
                print(divisor,"is a divisor of",test_num,"... stopping")
                break
            else:
                print(divisor,"is NOT a divisor of",test_num,"... continuing")
        print("\n")
        if test_num % divisor != 0:
            print(test_num,"is a prime number!")
        else:
            print(test_num,"is not a prime number.")
        break
    elif test_num == 1:
        print("\n")
        print("1 is technically not a prime number.")
        break
    elif test_num == 2:
        print("\n")
        print("2 is a prime number!")
        break
    else:
        print("Need a positive number! Try again!")
