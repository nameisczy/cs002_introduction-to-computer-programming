#ziyao chen, 9/20/2022, section 011, Sum of Place Values

number1 = int(input("Enter a number between 0 and 999: ")) #let user define variable number1 and convert it into integer
number2 = int(input("Enter another number between 0 and 999: ")) #let user define variable number2 and convert it into integer
print("sum of ones     =",number1%10,"+",number2%10,"=",number1%10+number2%10) #calculate, add and print ones digit
print("sum of tens     =",number1//10-number1//100*10,"+",number2//10-number2//100*10,"=",number1//10-number1//100*10+number2//10-number2//100*10) #calculate, add and print tens digit
print("sum of hundreds =",number1//100,"+",number2//100,"=",number1//100+number2//100) #calculate, add and print hundreds digit
