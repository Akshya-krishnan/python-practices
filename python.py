# String Functions

# Capitalize

m="hello".capitalize()
print(m)

# upper

m="hello".upper()
print(m)

# Lower

m="hello".lower()
print(m)

# Swap

m="hello".swapcase()
print(m)

m="HELLO".swapcase()
print(m)

# len

m="hello".__len__()
print(m)

# startswith

prod_name="Men's T shirts"
m=prod_name.startswith("Men")
print(m)

prod_name="Men's T shirts"
m=prod_name.startswith("Girl")
print(m)

# endswith

prod_name="Men's T shirts"
m=prod_name.endswith("shirts")
print(m)

# count

prod_name="Men's T shirts"
m=prod_name.count("Men")
print(m)

# find

prod_name="Men's T shirts"
m=prod_name.find("T")
print(m)

# Split

prod_name="Men's T shirts"
m=prod_name.split(" ")
print(m)

# isnumeric

phone="1256833"
m=phone.isnumeric()
print(m)

# isalpha

name='Akshaya'
m=name.isalpha()
print(m)

# isalnum

password="Upcode123"
m=password.isalnum()
print(m)