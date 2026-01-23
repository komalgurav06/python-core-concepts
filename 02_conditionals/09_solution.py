year = int(input("Enter the year: "))

if year % 4 == 0:
    print(year, "is Leap year.")

elif year % 400 == 0:
    print(year, "is Leap year.")    

elif year % 100 != 0:
    print(year, "is NOT Leap year.")    