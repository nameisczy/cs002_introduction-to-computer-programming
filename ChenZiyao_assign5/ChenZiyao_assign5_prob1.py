#ziyao chen, 10/3/2022, section 011, Pizza Party

budget = int(input("Enter budget for your party: "))
slice_cost = float(input("Cost per slice of pizza: "))
pie_cost = float(input("Cost per whole pizza pie (8 slices): "))
end = int(input("How many people will be attending your party? "))
slice_num_total = 0
for num in range(1,end+1):
    while True:
        slice_num = int(input("Enter number of slices for person #"+str(num)+": "))
        if slice_num < 0:
            print("Not a valid entry, try again!")
            print("\n")
        else:
            break
    slice_num_total =  slice_num_total + slice_num
pie_num_total = slice_num_total // 8
slice_num_left = slice_num_total % 8
total_cost = pie_cost * pie_num_total + slice_cost * slice_num_left
left = budget - total_cost
if left >= 0:
    print("You should purchase",pie_num_total,"pies and",slice_num_left,"slices")
    print("Your total cost will be:",format(total_cost,".2f"))
    if left > 0:
        print("You will still have",format(left,".2f"),"left after your order")
    else:
        print("You will have no money left after your order.")
else:
    print("Your order cannot be completed.")
    print("You would need to purchase",pie_num_total,"pies and",slice_num_left,"slices")
    print("This would put you over budget by",format(total_cost - budget,".2f"))
