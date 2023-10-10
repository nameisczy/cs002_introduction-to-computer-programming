#ziyao chen, 11/10/2022, section 011

name = input("Name: ")
new_name = ''
for i in name:
    if i.isalpha():
        new_name = new_name + i.lower()
print("Your 'cleaned up' name is:",new_name)
print("Your 'cleaned up' name reduces to:")
total = ord(new_name[0])-96
print(total,end=' ')
for c in range(1,len(new_name)):
    print('+',ord(new_name[c])-96,end=' ')
    total = total + ord(new_name[c]) -96
print("=",total)
