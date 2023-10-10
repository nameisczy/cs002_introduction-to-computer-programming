#Part 3f
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_nums = [10, 5, 20]
while True:
    flag = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
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
    elif flag == 'u':
        update_name = input("Enter a product name: ")
        if update_name in product_names:
            z = product_names.index(update_name)
            print("What would you like to update?")
            update = input("(n)ame, (c)ost or (q)uantity: ")
            if update == 'n':
                while True:
                    newname = input("Enter a new name: ")
                    if newname in product_names:
                        print("Duplicate name!")
                    else:
                        product_names[z] = newname
                        print("Product name has been updated")
                        break
            elif update == 'c':
                while True:
                    newcost = float(input("Enter a new cost: "))
                    if newcost > 0:
                        product_costs[z] = format(newcost,'.2f')
                        print("Product cost has been updated")
                        break
                    else:
                        print("Invalid cost!")
            elif update == 'q':
                while True:
                    newquantity = int(input("Enter a new quantity: "))
                    if newquantity > 0:
                        product_nums[z] = newquantity
                        print("Product quantity has been updated")
                        break
                    else:
                        print("Invalid quantity!")
            else:
                print("Invalid option")
        else:
            print("Product doesn't exist. Can't update.")
    elif flag == 'e':
        highest_cost = max(product_costs)
        lowest_cost = min(product_costs)
        x = product_costs.index(highest_cost)
        y = product_costs.index(lowest_cost)
        total = 0
        for ii in range(len(product_names)):
            total = total + product_costs[ii] * product_nums[ii]
        print("Most expensive product:     ",highest_cost,"(" + product_names[x] + ")")
        print("Least expensive product:    ",lowest_cost,"(" + product_names[y] + ")")
        print("Total value of all products:",format(total,'.2f'))
    else:
        print("Invalid option, try again")
    print()
print("See you soon!")
