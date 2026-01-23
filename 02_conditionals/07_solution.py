coffee_size = input("Enter coffee size: ")
extra_shot = "Yes"

if extra_shot == "Yes":
    order = coffee_size +  " coffee with an extra shot."
else:
    order = coffee_size +  "Coffee"

print("Order: ", order)    