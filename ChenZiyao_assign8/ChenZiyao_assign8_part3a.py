#Part 3a: Fast Food Restaurant
# product lists
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
while True:
    flag = input("(s)earch for product or (q)uit: ")
    if flag == 'q':
        break
    elif flag == 's':
        name = input("Enter a product name: ")
        if name in product_names:
            i = product_names.index(name)
            print('We sell "' + name + '" at', product_costs[i], "per unit")
        else:
            print('''Sorry, we don't sell "''' + name + '"')
    else:
        print("Invalid option, try again")
    print()
print("See you soon!")
