from sys import argv
# get the argv function from the sys package

script, filename = argv
# assign the two args to separate objects

txt = open(filename)
# open the file

print(f"Here's your file {filename}:")
print(txt.read())
# read the text from the file and print it

# print("Type the filename again:")
# file_again = input("> ")
# # have the user write the file name again

# txt_again = open(file_again)
# # open the file again

# print(txt_again.read())
# read the text from the file again and print again

txt.close()
txt_again.close()