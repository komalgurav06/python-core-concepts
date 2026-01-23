# Sum of even numbers.

n = int(input("Enter the number(e.g.,10,20,30): "))
sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += 1

print("Sum of even number is: ", sum_even)        