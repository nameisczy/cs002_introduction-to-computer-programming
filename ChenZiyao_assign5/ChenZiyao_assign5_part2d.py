#ziyao chen, 10/17/2022, section 011, Tabular Formatting

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
        break
a = 0
t = len(str(end_num))+1
for test_num in range(start_num, end_num + 1):
    if test_num > 1:
        for i in range(2,test_num):
            if (test_num % i) == 0:
                break
        else:
            a = a + 1
            print(format(test_num,">"+str(t)+"d"), end="")
            if a % 10 == 0:
                print()
        
            
