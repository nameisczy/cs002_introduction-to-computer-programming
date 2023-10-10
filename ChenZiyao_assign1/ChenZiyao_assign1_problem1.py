#ziyao chen, 9/12/2022, section 011, Variables & Print Statemnets

score1 = 100 #define variable score1, score1 is an integer
score2 = 94 #define variable score2, score2 is an integer
score3 = 88 #define variable score3, score3 is an integer
first_name = "Ada" #define variable first_name, first_name is a string
last_name = "Lovelace" #define variable last_name, last_name is a string
class_curve = 1.5 #define variable class_curve, score1 is a floating point number

print("Grade report for:",first_name,last_name) #print Grade report for: Ada Lovelace
print("Individual scores:",end=" ") #print Individual scores:
print(score1,score2,score3,sep=", ",end="\n")  #print 100, 94, 88 
Average_Score = (score1+score2+score3)//3 #calculate the average score
print("Average Score:",Average_Score) #print the result
averagescore_with_classcurve = Average_Score + class_curve #calculate the average score with class curve
print("Average Score with Class Curve:",averagescore_with_classcurve) #print the result
