formatter = "{} {} {} {}"
# four empty sections

# first glimpse of object oriented programming!
print(formatter.format(1,2,3,4))
# Call its format function,
# similar to telling it to do a command line command named format.
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        "Lizzy",
        "learns",
        "Python",
        3
))
