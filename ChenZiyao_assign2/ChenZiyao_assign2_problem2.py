#ziyao chen, 9/20/2022, section 011, Compound Interest

print("This program will project how much you can earn by investing") #print text
print("money in a high-yield savings account over a 3 month period.") #print text
print() #print a blank line
print("To begin, enter how much money you would like") #print text
starting_balance = float(input("to initially invest (i.e. 500): ")) #let user define starting_balance and change it into float
print("Next, enter your projected annual interest rate.") #print text
annual_interest_rate = float(input("For example, enter 5 for 5%: ")) #let user define annual_interest_rate and change it into float
month_interest_rate = annual_interest_rate/1200 #calculate and define month_interest_rate
print() #print a blank line
print("------------------ Calculating ------------------") #print text
print() #print a blank line
print("Month","Starting Balance","Interest","Ending Balance",sep="  ") #print text

interest1 = starting_balance * month_interest_rate #calculate and define interest1
ending_balance1 = starting_balance + starting_balance * month_interest_rate #calculate and define ending_balance1
print("1      ",format(starting_balance,'<18.2f'),format(interest1,'<10.2f'),format(ending_balance1,'.2f'),sep="") #print text, using format function to add spaces to the right with a decimal place of 2
interest2 = ending_balance1 * month_interest_rate #calculate and define interest2
ending_balance2 = ending_balance1 + ending_balance1 * month_interest_rate #calculate and define ending_balance2
print("2      ",format(ending_balance1,'<18.2f'),format(interest2,'<10.2f'),format(ending_balance2,'.2f'),sep="") #print text, using format function to add spaces to the right with a decimal place of 2
interest3 = ending_balance2 * month_interest_rate *0.01 #calculate and define interest3
ending_balance3 = ending_balance2 +ending_balance2 * month_interest_rate #calculate and define ending_balance3
print("3      ",format(ending_balance2,'<18.2f'),format(interest3,'<10.2f'),format(ending_balance3,'.2f'),sep="") #print text, using format function to add spaces to the right with a decimal place of 2
