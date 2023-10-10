#ziyao chen, 10/18/2022, section 011, Addition Table

while True:
    lowest_num = int(input("Start number: "))
    if lowest_num < 0:
        print("Lowest number must be 0 or greater")
    else:
        break
    
while True:
    highest_num = int(input("End number: "))
    if lowest_num > highest_num:
        print("Highest number must be larger than lowest number!")
    else:
        break
while True:
    command = input("Would you like to identify Prime numbers in your table? (y/n): ")
    if command == "y":
        t = len(str(highest_num*2))+2
        t_ = len(str(highest_num*2))
        t__= t*(highest_num - lowest_num + 2)
        print(format("+","^"+str(t)+"s"),end="")
        for c in range(lowest_num, highest_num + 1):
            print(format(c,">"+str(t)+"d"),end="")
        print("\n","-"*t__,sep="")
        for a in range(lowest_num, highest_num + 1):
            print(format(a, "<"+str(t_)+"d"),"|", end="")
            for b in range(lowest_num, highest_num + 1):
                if a + b > 1:
                    for i in range(2, a+b):
                        if ((a + b) % i) == 0:
                            print(format(a + b,">"+str(t)+"d"),end="")
                            break
                    else:
                        s = str(a+b)+"p"
                        print(format(s,">"+str(t)+"s"),end="")
                else:
                    print(format(a + b,">"+str(t)+"d"),end="")
            print()
        break
    elif command == "n":
        t = len(str(highest_num*2))+2
        t_ = len(str(highest_num*2))
        t__= t*(highest_num - lowest_num + 2)
        print(format("+","^"+str(t)+"s"),end="")
        for c in range(lowest_num, highest_num + 1):
            print(format(c,">"+str(t)+"d"),end="")
        print("\n","-"*t__,sep="")
        for a in range(lowest_num, highest_num + 1):
            print(format(a, "<"+str(t_)+"d"),"|", end="")
            for b in range(lowest_num, highest_num + 1):
                print(format(a + b,">"+str(t)+"d"),end="")
            print()
        break
    else:
        print("Invalid command, try again")
