#ziyao chen, 11/10/2022, section 011

while True:
    flag = True
    name = input("Enter a username: ")
    print("* Length of username:",len(name))
    print("* All characters are alpha-numeric:",name.isalnum())
    if name[0].isdigit() or name[len(name)-1].isdigit():
        flag = False
    print("* First & last characters are not digits:",flag)
    up = 0
    lower = 0
    digit = 0
    for i in name:
        if i.isupper():
            up = up + 1
        elif i.islower():
            lower = lower + 1
        elif i.isdigit():
            digit = digit + 1
    print("* # of uppercase characters in the username:",up)
    print("* # of lowercase characters in the username:",lower)
    print("* # of digits in the username:",digit)
    if len(name) < 8 or len(name) > 15:
        flag = False
    elif name.isalnum() == False:
        flag = False
    elif up < 1 or lower < 1 or digit < 1:
        flag = False
    if flag == True:
        break
    print("Username is invalid, please try again")
    print()
print("Username is valid!")
