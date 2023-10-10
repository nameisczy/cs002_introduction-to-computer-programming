try:
    filename = input("Enter an image filename:  ")
    import urllib.request
    url = "https://cs.nyu.edu/~kapp/python/"+filename+".txt"
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    split_data = data.split(",")  
except:
    print("Sorry, '"+filename+".txt' doesn't exist.")
else:
    print("Success!  I was able to find '"+filename+".txt'")
    import turtle
    turtle.setup(int(split_data[0]),int(split_data[1]))
    turtle.tracer(0)
    turtle.penup()
    turtle.goto(-int(split_data[0])/2,int(split_data[1])/2)
    greyscale = float(split_data[2])
    turtle.fillcolor(greyscale, greyscale, greyscale)
    turtle.begin_fill()
    turtle.forward(int(split_data[0]))
    turtle.right(90)
    turtle.forward(int(split_data[1]))
    turtle.right(90)
    turtle.forward(int(split_data[0]))
    turtle.right(90)
    turtle.forward(int(split_data[1]))
    turtle.right(90)
    turtle.end_fill()
    count = 1
    if split_data[4] == 'true':
        num = 5
        while num < len(split_data):
            countt = 0
            for i in range(num,len(split_data),3):
                if split_data[i] == 'b' or split_data[i] == 'b\n':
                    turtle.goto(-int(split_data[0])/2,int(split_data[1])/2-count*int(split_data[3]))
                    num = num + countt + 1
                    count = count + 1
                    break
                turtle.fillcolor(float(split_data[i]), float(split_data[i+1]), float(split_data[i+2]))
                turtle.begin_fill()
                turtle.forward(int(split_data[3]))
                turtle.right(90)
                turtle.forward(int(split_data[3]))
                turtle.right(90)
                turtle.forward(int(split_data[3]))
                turtle.right(90)
                turtle.forward(int(split_data[3]))
                turtle.right(90)
                turtle.end_fill()
                turtle.forward(int(split_data[3]))
                countt = countt + 3
    else:
        for i in range(4,len(split_data)):
            if split_data[i] == 'b' or split_data[i] == 'b\n':
                turtle.goto(-int(split_data[0])/2,int(split_data[1])/2-count*int(split_data[3]))
                count = count + 1
                continue
            greyscale1 = float(split_data[i])
            turtle.fillcolor(greyscale1, greyscale1, greyscale1)
            turtle.begin_fill()
            turtle.forward(int(split_data[3]))
            turtle.right(90)
            turtle.forward(int(split_data[3]))
            turtle.right(90)
            turtle.forward(int(split_data[3]))
            turtle.right(90)
            turtle.forward(int(split_data[3]))
            turtle.right(90)
            turtle.end_fill()
            turtle.forward(int(split_data[3]))
    turtle.update()
