a1 = "Logical Python"
a2 = "Logical python"

print(id(a1) == id(a2))  # This will print False because they are different strings

a1 = "Logical"
a2 = "Logical"

print(id(a1) == id(a2))  # This will print True because they are the same string
# The id() function returns the identity of an object. This identity is unique and constant for this object during its lifetime.
# The id() function returns an integer (or long integer) representing the object's memory address.
# The id() function is useful for comparing the identity of two objects.

a1 = "Logical$"
a2 = "Logical$"
print(id(a1) == id(a2))  # This will print True because they are the same string