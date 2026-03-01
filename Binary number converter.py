Number = input("Enter a number: ") 
base = int(input("enter the base between 2 and 16:"))
integer = int(Number, base)
binary = bin(integer)

print(f"{Number} in base {base} is: {integer} in base 10 and {binary[2:]} in base 2")
#everything on the left is the title of a variable, everything on the right is its code
