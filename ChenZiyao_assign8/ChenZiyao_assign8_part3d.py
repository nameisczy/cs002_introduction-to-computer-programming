#Part 3d
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_nums = [10, 5, 20]
while True:
    flag = input("(s)earch, (l)ist, (a)dd, (r)emove or (q)uit: ")
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
        print("Product                   Price  Quantity")
        for c in range(len(product_names)):
            print(format(product_names[c],'<26s'),product_costs[c],format(product_nums[c],'>9d'))
    elif flag == 'a':
        while True:
            new_name = input("Enter a new product name: ")
            if new_name in product_names:
                print("Sorry, we already sell that product. Try again.")
            else:
                product_names.append(new_name)
                break
        while True:
            new_cost = float(input("Enter a product cost: "))
            if new_cost > 0:
                product_costs.append(new_cost)
                break
            else:
                print("Invalid cost. Try again.")
        while True:
            new_num = int(input("How many of these products do we have? "))
            if new_num > 0:
                product_nums.append(new_num)
                print("Product added!")
                break
            else:
                print("Invalid quantitiy. Try again.")
    elif flag == 'r':
        remove_name = input("Enter a product name: ")
        if remove_name in product_names:
            a = product_names.index(remove_name)
            product_names.remove(remove_name)
            product_costs.remove(product_costs[a])
            product_nums.remove(product_nums[a])
            print("Product removed!")
        else:
            print("Product doesn't exist. Can't remove.")
    else:
        print("Invalid option, try again")
    print()
print("See you soon!")
