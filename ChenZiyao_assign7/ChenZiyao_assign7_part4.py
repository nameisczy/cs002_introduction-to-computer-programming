def string_length(string):
    count = 0
    for i in string:
        count = count + 1
    return count

def string_isalpha(string):
    flag = True
    if string == '':
        flag = False
    else:
        for i in string:
            if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
                continue
            else:
                flag = False
                break
    return flag

def string_adjustcase(string1,string2):
    new_string = ''
    if string2 == 'upper':
        for i in string1:
            if 97 <= ord(i) <= 122:
                new_string = new_string + chr(ord(i)-32)
            else:
                new_string = new_string + i
    elif string2 == 'lower':
        for i in string1:
            if 65 <= ord(i) <= 90:
                new_string = new_string + chr(ord(i)+32)
            else:
                new_string = new_string + i
    else:
        new_string = string1
    return new_string

def string_capitalize(string):
    new_string = ''
    flag = True
    for i in string:
        if flag == True:
            if 97 <= ord(i) <= 122:
                new_string = new_string + chr(ord(i)-32)
            else:
                new_string = new_string + i
            flag = False
        elif flag == False:
            if 65 <= ord(i) <= 90:
                new_string = new_string + chr(ord(i)+32)
            else:
                new_string = new_string + i
                if i == ' ':
                    flag = True
    return new_string
