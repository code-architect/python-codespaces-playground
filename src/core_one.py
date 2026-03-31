# a = 10
# y = 10

# if a is y:
#     print("a and y are the same object in memory.")
# else:    
#     print("a and y are different objects in memory.")


# x = 10
# y = 20

# if x is not y:
#     print("x and y are different objects in memory.")
# else:
#     print("x and y are the same object in memory.") 


name = "Alice"
year = 2024
print(f"My name is {name} and the year is {year}.")
print("My name is {} and the year is {}.".format(name, year))
print("My name is %s and the year is %d." % (name, year))
print("My name is " + name + " and the year is " + str(year) + ".")
# print("My name is", name, "and the year is", year + ".")
print("My name is {0} and the year is {1}.".format(name, year))
print("My name is {name} and the year is {year}.".format(name=name, year=year))
print(f"My name is {name.upper()} and the year is {year + 1}.")
print("My name is {0} and the year is {1}.".format(name.lower(), year - 1))
print("My name is {name} and the year is {year}.".format(name=name.capitalize(), year=year * 2))
print("My name is %s and the year is %d." % (name.swapcase(), year // 2))
print("My name is " + name.title() + " and the year is " + str(year ** 2) + ".")
print("My name is {}, and the year is {}.".format(name.center(20), year))
print(f"My name is {name.ljust(20)} and the year is {year}.")
print("My name is {0} and the year is {1}.".format(name.rjust(20), year))
print("My name is {name} and the year is {year}.".format(name=name.center(20), year=year))
print("My name is %s and the year is %d." % (name.lstrip(), year))
print("My name is " + name.rstrip() + " and the year is " + str(year) + ".")
print("My name is {0} and the year is {1}.".format(name.strip(), year))
print(f"My name is {name.strip()} and the year is {year}.")
print("My name is {name} and the year is {year}.".format(name=name.strip(), year=year))
print("My name is %s and the year is %d." % (name.strip(), year))
print("My name is " + name.strip() + " and the year is " + str(year) + ".")
print("My name is {0} and the year is {1}.".format(name.strip(), year))