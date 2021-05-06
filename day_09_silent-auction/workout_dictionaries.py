{"key1": "value1", "key2": "value2"}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."}

print(programming_dictionary["Function"])

programming_dictionary["Loop2"] = "Def for the loop again"

print(programming_dictionary)

empty_dictionary = {}

# programming_dictionary = {}
# print(programming_dictionary)

programming_dictionary["Function"] = "Different value"
print(programming_dictionary["Function"])
print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
