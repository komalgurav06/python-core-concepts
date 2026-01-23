# Multiplication Table Printer

table_num = int(input("Enter Table Nuber: "))

for i in range(1, 11):
    if i == 5:
        continue
    print(table_num, 'x', i, '=', table_num * i)



# Multiple iteration skip karne ke liye
''' if i in (5, 6, 7):
      continue

    if i == 5 or i == 6 or i == 7:
      continue
'''    