from sys import argv

script, filename = argv

test_file = open(filename)

read_test = test_file.read()

print(read_test)