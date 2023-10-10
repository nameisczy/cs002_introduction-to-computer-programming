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

if total > 9:
    while True:
        total_ = 0
        for c in str(total):
            total_ = total_ + int(c)
        print("Further reduction:",total_)
        total = total_
        if total <= 9:
            break
if total == 0:
    meaning = 'Emptiness'
elif total == 1:
    meaning = 'Independence'
elif total == 2:
    meaning = 'Quiet'
elif total == 3:
    meaning = 'Charming'
elif total == 4:
    meaning = 'Harmony'
elif total == 5:
    meaning = 'New directions'
elif total == 6:
    meaning = 'Love'
elif total == 7:
    meaning = 'Spirituality'
elif total == 8:
    meaning = 'Organization'
elif total == 9:
    meaning = 'Romatic'
print("This name means ...",meaning,sep='')
