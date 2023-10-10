#ziyao chen, 3/10/2022, section 011, Decimal to Binary

while True:
    num = int(input("Enter a number greater than or equal to 0: "))
    if num < 0:
        print("Invalid, try again")
    else:
        break
num_=num
num_num=""
while True:
    num_num = str(num%2)+num_num
    print(num,"% 2 =",num%2,"---",num_num)
    print(num,"/ 2 =",num//2)
    if num//2 == 0:
        break
    num = num//2
print("\n")
print(num_,"in binary is",num_num)
    
    
