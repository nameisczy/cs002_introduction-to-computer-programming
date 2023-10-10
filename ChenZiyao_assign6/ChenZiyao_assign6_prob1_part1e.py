#ziyao chen, 10/27/2022, section 011, Problem 1: Simple Functions, Part 1e

def simple_sort_version2(a, b, c):
    if a > b > c:
        return c, b, a
    elif a > c > b:
        return b, c, a
    elif b > a > c:
        return c, a, b
    elif b > c > a:
        return a, c, b
    elif c > a > b:
        return b, a, c
    else:
        return a, b, c

# next, write a new function called 'simple_sort_version2' that accepts three values.  you can assume
# that your three values will always be the same data type (all ints, all floats or all strings).
# sort these values in ascending order and return them. 
# you may use any function that you've written so far in this assignment if you'd like to (simple_sort_version1, maximum, minimum, etc)

# your function should work perfectly with the following lines of code
a,b,c = simple_sort_version2(10,20,30)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(10,30,20)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,10)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,20)
print (a,b,c) # 20 20 30
