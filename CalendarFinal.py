def month_details(month, year):
    if month == 0:
        return ("January - {}".format(year), 31)
    if month == 1:
        if (year%100!=0 and year%4==0) or year%400==0:
            return ("Febuary - {}".format(year), 29)
        return ("Febuary - {}".format(year), 28)
    if month == 2:
        return ("March - {}".format(year), 31)
    if month == 3:
        return ("April - {}".format(year), 30)
    if month == 4:
        return ("May - {}".format(year), 31)
    if month == 5:
        return ("June - {}".format(year), 30)
    if month == 6:
        return ("July - {}".format(year), 31)
    if month == 7:
        return ("August - {}".format(year), 31)
    if month == 8:
        return ("September - {}".format(year), 30)
    if month == 9:
        return ("October - {}".format(year), 31)
    if month == 10:
        return ("November - {}".format(year), 30)
    if month == 11:
        return ("December - {}".format(year), 31)
year = int(input("Enter a year: "))
dayOfWeek=98
while(dayOfWeek>6 or dayOfWeek<0):
    dayOfWeek = int(input("Enter the first day of the year, (ex. Sunday = 0, Monday = 1, Tuesday = 2, etc.): "))

for i in range(0,12):
    temp1, temp2 = month_details(i, year)
    print("{month:^29}".format(month=temp1))
    print("-"*29)
    print(" Sun Mon Tue Wed Thu Fri Sat ")
    j=0
    for i in range(1, temp2+1):
        while dayOfWeek!=j:
            print("    ",end="")
            j+=1
        print("{num:>4}".format(num=i),end="")
        dayOfWeek+=1
        dayOfWeek%=7
        j=dayOfWeek
        if dayOfWeek==0:
            print()
    print("\n")
