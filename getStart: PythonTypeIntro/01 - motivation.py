def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe"))

# More Motivation
def get_name_with_age(name: str, age: int):
    name_with_age = name + "is old" + str(age)
    return name_with_age

print(get_name_with_age("ali", 10))
