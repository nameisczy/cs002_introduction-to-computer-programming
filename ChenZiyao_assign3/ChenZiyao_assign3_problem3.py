#ziyao chen, 9/20/2022, section 011, Valid Date Checker

date = int(input("Enter a date (YYYYMMDD): "))
year = date // 10000
month = (date % 10000 - date % 100)// 100
day = date % 100
if year % 4 == 0:
    print(year,"is a leap year")
else:
    print(year,"is NOT a leap year")
if month == 1:
    if day > 31:
        print("This is not a valid date in",year)
    elif day == 1 or day == 21 or day == 31:
        print("January ",day,"st ",year," is a valid date",sep="")
    elif day == 2 or day == 22:
        print("January ",day,"nd ",year," is a valid date",sep="")
    elif day == 3 or day == 23:
        print("January ",day,"rd ",year," is a valid date",sep="")
    else:
        print("January ",day,"th ",year," is a valid date",sep="")
elif month == 2 and year % 4 == 0:
    if day > 29:
        print("This is not a valid date in",year)
    elif day == 1 or day == 21:
        print("February ",day,"st ",year," is a valid date",sep="")
    elif day == 2 or day == 22:
        print("February ",day,"nd ",year," is a valid date",sep="")
    elif day == 3 or day == 23:
        print("February ",day,"rd ",year," is a valid date",sep="")
    else:
        print("February ",day,"th ",year," is a valid date",sep="")
elif month == 2 and year % 4 != 0:
    if day > 28:
        print("This is not a valid date in",year)
    elif day == 1 or day == 21:
        print("February ",day,"st ",year," is a valid date",sep="")
    elif day == 2 or day == 22:
        print("February ",day,"nd ",year," is a valid date",sep="")
    elif day == 3 or day == 23:
        print("February ",day,"rd ",year," is a valid date",sep="")
    else:
        print("February ",day,"th ",year," is a valid date",sep="")
elif month == 3:
    if day > 31:
        print("This is not a valid date in",year)
    elif day == 1 or day == 21 or day == 31:
        print("March ",day,"st ",year," is a valid date",sep="")
    elif day == 2 or day == 22:
        print("March ",day,"nd ",year," is a valid date",sep="")
    elif day == 3 or day == 23:
        print("March ",day,"rd ",year," is a valid date",sep="")
    else:
        print("March ",day,"th ",year," is a valid date",sep="")
elif month == 4:
    if day > 30:
        print("This is not a valid date in",year)
    elif day == 1 or day == 21:
        print("April ",day,"st ",year," is a valid date",sep="")
    elif day == 2 or day == 22:
        print("April ",day,"nd ",year," is a valid date",sep="")
    elif day == 3 or day == 23:
        print("April ",day,"rd ",year," is a valid date",sep="")
    else:
        print("April ",day,"th ",year," is a valid date",sep="")
elif month == 5:
    if day > 31:
        print("This is not a valid date in",year)
    elif day == 1 or day == 21 or day == 31:
        print("May ",day,"st ",year," is a valid date",sep="")
    elif day == 2 or day == 22:
        print("May ",day,"nd ",year," is a valid date",sep="")
    elif day == 3 or day == 23:
        print("May ",day,"rd ",year," is a valid date",sep="")
    else:
        print("May ",day,"th ",year," is a valid date",sep="")
elif month == 6:
    if day > 30:
        print("This is not a valid date in",year)
    elif day == 1 or day == 21:
        print("June ",day,"st ",year," is a valid date",sep="")
    elif day == 2 or day == 22:
        print("June ",day,"nd ",year," is a valid date",sep="")
    elif day == 3 or day == 23:
        print("June ",day,"rd ",year," is a valid date",sep="")
    else:
        print("June ",day,"th ",year," is a valid date",sep="")
elif month == 7:
    if day > 31:
        print("This is not a valid date in",year)
    elif day == 1 or day == 21 or day == 31:
        print("July ",day,"st ",year," is a valid date",sep="")
    elif day == 2 or day == 22:
        print("July ",day,"nd ",year," is a valid date",sep="")
    elif day == 3 or day == 23:
        print("July ",day,"rd ",year," is a valid date",sep="")
    else:
        print("July ",day,"th ",year," is a valid date",sep="")
elif month == 8:
    if day > 31:
        print("This is not a valid date in",year)
    elif day == 1 or day == 21 or day == 31:
        print("August ",day,"st ",year," is a valid date",sep="")
    elif day == 2 or day == 22:
        print("August ",day,"nd ",year," is a valid date",sep="")
    elif day == 3 or day == 23:
        print("August ",day,"rd ",year," is a valid date",sep="")
    else:
        print("August ",day,"th ",year," is a valid date",sep="")
elif month == 9:
    if day > 30:
        print("This is not a valid date in",year)
    elif day == 1 or day == 21:
        print("September ",day,"st ",year," is a valid date",sep="")
    elif day == 2 or day == 22:
        print("September ",day,"nd ",year," is a valid date",sep="")
    elif day == 3 or day == 23:
        print("September ",day,"rd ",year," is a valid date",sep="")
    else:
        print("September ",day,"th ",year," is a valid date",sep="")
elif month == 10:
    if day > 31:
        print("This is not a valid date in",year)
    elif day == 1 or day == 21 or day == 31:
        print("October ",day,"st ",year," is a valid date",sep="")
    elif day == 2 or day == 22:
        print("October ",day,"nd ",year," is a valid date",sep="")
    elif day == 3 or day == 23:
        print("October ",day,"rd ",year," is a valid date",sep="")
    else:
        print("October ",day,"th ",year," is a valid date",sep="")
elif month == 11:
    if day > 3:
        print("This is not a valid date in",year)
    elif day == 1 or day == 21:
        print("November ",day,"st ",year," is a valid date",sep="")
    elif day == 2 or day == 22:
        print("November ",day,"nd ",year," is a valid date",sep="")
    elif day == 3 or day == 23:
        print("November ",day,"rd ",year," is a valid date",sep="")
    else:
        print("November ",day,"th ",year," is a valid date",sep="")
elif month == 12:
    if day > 31:
        print("This is not a valid date in",year)
    elif day == 1 or day == 21 or day == 31:
        print("December ",day,"st ",year," is a valid date",sep="")
    elif day == 2 or day == 22:
        print("December ",day,"nd ",year," is a valid date",sep="")
    elif day == 3 or day == 23:
        print("December ",day,"rd ",year," is a valid date",sep="")
    else:
        print("December ",day,"th ",year," is a valid date",sep="")
else:
    print("This is not a valid date in",year)
