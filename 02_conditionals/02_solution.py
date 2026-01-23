age = int(input("Enter your age: "))
day = "wednesday"

price = 12 if age >= 18 else 8

if day == "wednesday":
    price -= 2

print("Your ticket price is $: ", price)    