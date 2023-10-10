#ziyao chen, 10/27/2022, section 011, Problem 1: Simple Functions, Part 1c

def valid_date(a,b):
    if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
        if b < 1 or b > 31:
            return False
        else:
            return True
    elif a == 2:
        if b < 1 or b > 28:
            return False
        else:
            return True
    elif a == 4 or a == 6 or a == 9 or a == 11:
        if b < 1 or b > 30:
            return False
        else:
            return True
    else:
        return False

print (valid_date(99,1)) # False
print (valid_date(1,99)) # False
print (valid_date(99,99)) # False

print (valid_date(-99,1)) # False
print (valid_date(1,-99)) # False
print (valid_date(-99,-99)) # False

print (valid_date(9,25)) #True
print (valid_date(10,15)) # True
print (valid_date(11,31)) # False
print (valid_date(2,28)) # True
print (valid_date(2,29)) # False
