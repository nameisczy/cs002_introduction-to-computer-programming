#ziyao chen, 9/12/2022, section 011, Using the print function

name1 = input("Please enter name #1: ") #define variable name1
name2 = input("Please enter name #2: ") #define variable name2
name3 = input("Please enter name #3: ") #define variable name3
print() #print a blank line
print("Here are your names in every possible order:") #print text
print("-"*44) #print text
print() #print a blank line
print("1.",end=" ") 
print(name1,name2,name3,sep=", ",end="\n") #print one of the possible orders
print() #print a blank line
print("2. **",end="")
print(name1,name3,name2,sep="** **",end="") #print one of the possible orders
print("**")
print() #print a blank line
print("3. ",end="")
print(name2,name1,name3,sep="-",end="\n") #print one of the possible orders
print() #print a blank line
print("4. ",end="")
print(name2)
print("  ",name3) #print one of the possible orders
print("  ",name1)
print() #print a blank line
print("5. ",end="")
print(name3)
print("   ",name2,"!",sep="") #print one of the possible orders
print("  ",name1)
print() #print a blank line
print("6.",end=" ")
print("---",name3,sep="")
print("   ------",name1,sep="") #print one of the possible orders
print("   ","-"*9,name2,sep="")
