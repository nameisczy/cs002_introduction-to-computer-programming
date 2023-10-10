#

file1 = open('class_data.txt','r')
file2 = open('enrollment_data.txt','r')
data1 = file1.read()
data2 = file2.read()
ID = input("Enter a course ID (i.e. CS0002, CS0004): ")
split_data1 = data1.split("\n")
flag = False
for i in range(len(split_data1)):
    if ID in split_data1[i]:
        flag = True
        split_data11 = split_data1[i].split(",")
        print("The title of this class is:",split_data11[1])
        split_data2 = data2.split("\n")
        count = 0
        for ii in range(len(split_data2)):
            if ID in split_data2[ii]:
                count = count + 1
        print("The course has",count,"students enrolled")
        for iii in range(len(split_data2)):
            if ID in split_data2[iii]:
                split_data22 = split_data2[iii].split(",")
                print("*",split_data22[1]+","+split_data22[2])
if flag == False:
    print("Cannot find this course")
file1.close()
file2.close()
