#ziyao chen, 10/17/2022, section 011, Custom Number Range

while True:
    start_num = int(input("Start number: "))
    end_num = int(input("End number: "))
    if start_num <= 0 or end_num <= 0:
        print("Start and end must be positive")
        print()
    elif start_num >= end_num:
        print("End number must be greater than start number")
        print()
    else:
        print()
        break

for test_num in range(start_num, end_num + 1):
    if test_num > 2:
        for divisor in range(2,test_num):
            if test_num % divisor == 0:
                break
        if test_num % divisor != 0:
            print(test_num)
    elif test_num == 1:
        print("1")
    elif test_num == 2:
        print("2")
