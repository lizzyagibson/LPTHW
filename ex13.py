from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print("What comes after the third variable?")
fourth = input()
print("Yes,", fourth, "comes after the third variable,", third)