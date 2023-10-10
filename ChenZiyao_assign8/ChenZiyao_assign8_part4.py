#Part 4: List Functions
def listlen(l):
    c = 0
    for i in l:
        c = c + 1
    return c

def listmax(l):
    if listlen(l) == 0:
        return None
    else:
        max_ = l[0]
        for i in range(listlen(l)):
            if l[i] > max_:
                max_ = l[i]
        return max_

mylist = [10, 20, 30, 5, 3]
x = listmax(mylist)
print (x)
print (mylist)

def listcopy(l):
    l_ = [] + l
    return l_

def listappend(l, e):
    l_ = [] + l + [e]
    return l_

def listinsert(l, ll, e):
    l_ = []
    for i in l:
        if i == l[ll]:
            l_ = l_ + [e] + [i]
        else:
            l_ = l_ + [i]
    return l_

def listremove(l, e):
    l_ = []
    for i in l:
        if i == e:
            continue
        else:
            l_ = l_ + [i]
    return l_

def listreverse(l):
    l_ = []
    for i in range(1, listlen(l) + 1):
        l_ = l_ + [l[-i]]
    return l_
