distance = float(input("Enter distance in km: "))

if distance < 3:
    recommended = "Go for a walk."

elif distance < 15:
    recommended = "Go for a bike."

else:
    recommended = "Go for a car."    

print(recommended)