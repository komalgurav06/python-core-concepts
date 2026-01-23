pet = input("Enter Pet name: ")
age = int(input("Enter pet age: "))

if pet == "dog":
    if age < 2:
        print("Recommended food: Puppy Food")
    else:
        print("Recommended food: Adult Food")    

if pet == "cat":
    if age > 5:
        print("Recommended food: Senior Food")
    else:
        print("Recommended food: Adult Food")  










