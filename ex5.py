my_name = "Lizzy"
my_age = 32
my_height = 64 # inches
my_weight = 125
my_eyes = "green"
my_teeth = "white"
my_hair = "blond"

my_height_cm = my_height * 2.54
my_weight_kg = my_weight / 2.205

print(f"Let's talk about {my_name}.")
print(f"She's {my_height} inches tall ({round(my_height_cm)} cm).")

print(f"She's {my_weight} pounds ({round(my_weight_kg)} kg).")
print(f"She's got {my_eyes} eyes and {my_hair} hair.")
print(f"Her teeth are usually {my_teeth}.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight}, I get {total}.")
