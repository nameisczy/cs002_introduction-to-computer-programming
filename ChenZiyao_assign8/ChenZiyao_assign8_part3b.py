#Part 3b
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_nums = [10, 5, 20]
while True:
    flag = input("(s)earch, (l)ist or (q)uit: ")
    if flag == 'q':
        break
    elif flag == 's':
        name = input("Enter a product name: ")
        if name in product_names:
            i = product_names.index(name)
            print('We sell "' + name + '" at', product_costs[i], "per unit")
            print("We currently have", product_nums[i], "in stock")
        else:
            print('''Sorry, we don't sell "''' + name + '"')
    elif flag == 'l':
        print("Product         Price  Quantity")
        print("soft drink       0.99   10")
        print("onion rings      1.29   5")
        print("small fries      1.49   20")
    else:
        print("Invalid option, try again")
    print()
print("See you soon!")
