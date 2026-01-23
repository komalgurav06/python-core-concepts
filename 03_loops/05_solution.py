# Find the First Non-Repeated Character

input_str = "teetercbcdabcdm"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("First Non-Repeated character is: ", char)
        break



 # ek se jyada Non-Repeated Character Find karne ke liye 
'''
input = "teetercmk"
non_repeated = []
for char in input:
    if input.count(char) == 1:
        non_repeated.append(char)

print("Non-Repeated character: ",non_repeated)        
''' 

