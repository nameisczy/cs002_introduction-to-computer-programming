#ziyao chen, 10/27/2022, section 011, Problem 1: Simple Functions, Part 1b

def maximum(a,b):
    if a > b:
        return a
    else:
        return b

def minimum(a,b):
    if a > b:
        return b
    else:
        return a
    
a = 5
b = 10
c = 15
d = 20

ans1 = maximum(a,b)
ans2 = maximum(a,c)
ans3 = maximum(a,d)
print (ans1,ans2,ans3) # 10 15 20

ans4 = minimum(d,c)
ans5 = minimum(d,b)
ans6 = minimum(d,a)
print (ans4,ans5,ans6) # 15 10 5

ans7 = maximum( maximum(a,b), maximum(c,d) )
print ("The biggest is:", ans7)

