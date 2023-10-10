#ziyao chen, 9/20/2022, section 011, Valid Triangle Tester

print("Valid Triangle Tester") #print text
print("\n") #print a blank line

x1 = float(input("Enter point #1 - x position: ")) #let user define variable x1 and convert it into float
y1 = float(input("Enter point #1 - y position: ")) #let user define variable y1 and convert it into float
x2 = float(input("Enter point #2 - x position: ")) #let user define variable x2 and convert it into float
y2 = float(input("Enter point #2 - y position: ")) #let user define variable y2 and convert it into float
x3 = float(input("Enter point #3 - x position: ")) #let user define variable x3 and convert it into float
y3 = float(input("Enter point #3 - y position: ")) #let user define variable y3 and convert it into float

print("\n") #print a blank line
print("The length of each side of your test shape is:") #print text
print("\n") #print a blank line

import math 
side1 = round(math.sqrt(((x1-x2)**2+(y1-y2)**2)),2) #calculate and define side1
side2 = round(math.sqrt(((x1-x3)**2+(y1-y3)**2)),2) #calculate and define side2
side3 = round(math.sqrt(((x2-x3)**2+(y2-y3)**2)),2) #calculate and define side3

print("Side 1:",side1) #print text
print("Side 2:",side2) #print text
print("Side 3:",side3) #print text

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1: #evaluate if three sides can form a triangle or not.
    print("This is a valid triangle!") #print result
    if side1 == side2 == side3: #evaluate if the triangle a equilateral triangle or not
        print("This is an equilateral triangle") #print result
    elif side1 == side2 or side1 == side3 or side2 == side3: #evaluate if the triangle a isosceles triangle or not
        print("This is an isosceles triangle") #print the result
    else: #if the condition above evalutes to False then execute the block associated with the "else" statement
        print("This is a scalene triangle") #print text 
    if round(side1**2)+round(side2**2)==round(side3**2) or round(side1**2)+round(side3**2)==round(side2**2) or round(side2**2)+round(side3**2)==round(side1**2): #evaluate if the triangle a right triangle
        print("This is also a right triangle") #print text
else: #if the condition above evaluates to False then execute the block associated with the "else" statement
    print("This is not a valid triangle") #print text


    
