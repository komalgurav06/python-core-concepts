fruit = input("Enter Fruit name: ")
color = input("Enter fruit color: ")

if fruit == "Banana":
    if color == "Green":
        print("Banana is Unripe.")

    elif color == "Yellow":
        print("Banana is Ripe.") 

    elif color == "Brown":
        print("Banana is Overripe.")

    else:
        print("Invalid Fruit Color.")

else:
    print("Fruit is NOT avilable.")                   