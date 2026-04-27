# Placeholders in Strings

# 1. Concatenation
name = "jake"
print(name + " is 15 years old")

print("-----")

# 2. Placeholders using %
name = "jake"
sentence = "%s is 15 years old"
print(sentence % name)

print("-----")

# Multiple placeholders
sentence = "%s %s was the president of the United States"
print(sentence % ("Barack", "Obama"))

print("-----")

# Different data types
sentence = "%s is %d years old"
print(sentence % ("rio", 24))

print("-----")

# 3. f-strings (recommended)
name = "rio"
print(f"Hello, {name}")

print("-----")

x = 10
y = 20
print(f"The sum of x and y is {x + y}")
