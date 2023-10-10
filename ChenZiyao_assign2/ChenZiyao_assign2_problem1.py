#ziyao chen, 9/20/2022, section 011, Grade Calculator

assignments = float(input("Enter overall assignments grade: ")) #let user define variable assignments and change it into float
quizzes = float(input("Enter overall quiz grade: ")) #let user define variable quizzes and change it into float
midterm = float(input("Enter midterm grade: ")) #let user define variable midterm and change it into float
final_grade = float(input("What would you like your final grade to be?: ")) #let user define variable final_grade, the desired grade
final = format(((final_grade-0.3*assignments-0.1*quizzes-0.3*midterm)/0.3),'.2f') #calculate the score user need to receive on the final exam to receive the inputting desired grade
print("You need to receive a ",final,"% on your final to get a ",final_grade," in the class.", sep = "") #print the result
