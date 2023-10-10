#ziyao chen, 10/17/2022, section 011, Find all Prime Numbers between 1 and 1000

for test_num in range(1,1001):
    if test_num > 2:
        for divisor in range(2,test_num):
            if test_num % divisor == 0:
                break
        if test_num % divisor != 0:
            print(test_num,"is a prime number!")
    elif test_num == 1:
        print("1 is technically not a prime number.")
    elif test_num == 2:
        print("2 is a prime number!")
