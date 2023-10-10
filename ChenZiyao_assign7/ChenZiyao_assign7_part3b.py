#ziyao chen, 11/10/2022, section 011

def ascii_shift(string,integer):
    new_string = ''
    for i in string:
        new_string = new_string + chr(ord(i)+integer)
    return new_string

def shift_right(string):
    new_string = string[len(string)-1]+string[0:len(string)-1]
    return new_string

def shift_left(string):
    new_string = string[1:len(string)]+string[0]
    return new_string

def flip(string):
    if len(string) % 2 == 0:
        new_string = string[len(string)//2:] + string[0:len(string)//2]
    else:
        new_string = string[len(string)//2+1:]+string[len(string)//2]+string[0:len(string)//2]
    return new_string

def add_letters(string,integer):
    import random
    new_string = ''
    for i in string:
        new_string = new_string + i
        for c in range(0,integer):
            s = chr(random.randint(65,90))
            num = random.randint(0,1)
            if num == 0:
                new_string = new_string + s
            else:
                new_string = new_string + s.lower()
    return new_string

def delete_characters(string,integer):
    new_string = string[::integer+1]
    return new_string

while True:
    pattern = input("Enter an encoding pattern, 'end' to end: ")
    if pattern == 'end':
        break
    word = input("Enter a word to encode/decode: ")
    for i in pattern:
        if i == 'A':
            word = add_letters(word,1)
            print("Added 1 character:",word)
        elif i == 'X':
            word = delete_characters(word,1)
            print("Deleted 1 character:",word)
        elif i == 'F':
            word = flip(word)
            print("Flipped:",word)
        elif i == 'U':
            word = ascii_shift(word,1)
            print("ASCII shifted up:",word)
        elif i == 'D':
            word = ascii_shift(word,-1)
            print("ASCII shifted down:",word)
        elif i == 'L':
            word = shift_left(word)
            print("Shifted left:",word)
        elif i == 'R':
            word = shift_right(word)
            print("Shifted right:",word)
        else:
            continue
