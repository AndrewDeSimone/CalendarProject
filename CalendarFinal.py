year = int(input("Enter a year: "))
dayOfWeek=98
while(dayOfWeek>6 or dayOfWeek<0): dayOfWeek = int(input("Enter the first day of the year, (ex. Sunday = 0, Monday = 1, Tuesday = 2, etc.): "))
for i in range(0,12):
    temp1, temp2 = [["January - {}".format(year), 31], ["Febuary - {}".format(year), 28 + (year%100!=0 and year%4==0) or year%400==0], ["March - {}".format(year), 31], ["April - {}".format(year), 30], ["May - {}".format(year), 31], ["June - {}".format(year), 30], ["July - {}".format(year), 31], ["August - {}".format(year), 31], ["September - {}".format(year), 30], ["October - {}".format(year), 31], ["November - {}".format(year), 30], ["December - {}".format(year), 31]][i]
    print(f"{temp1:^29}\n{'-'*29}\n Sun Mon Tue Wed Thu Fri Sat ")
    j=0
    for i in range(1, temp2+1):
        while dayOfWeek!=j:
            print("    ",end="")
            j+=1
        print("{num:>4}".format(num=i),end="")
        dayOfWeek=(dayOfWeek+1)%7
        j=dayOfWeek
        if dayOfWeek==0: print()
    print("\n")
    