import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

# function = operations["+"]
# print(function(2, 3))

num1 = int(input("First number: "))

for operation in operations:
    print(operation)

desired_operation = input("Insert desired operation: ")
num2 = int(input("Second number: "))

answer = operations[desired_operation](num1, num2)
print(f"{num1} {desired_operation} {num2} = {answer}")

while True:
    option = input(f"type y to make further calcs with {answer} and no to quit: ")
    if option == "y":
        desired_operation = input("Insert another desired operation: ")
        num3 = int(input("Next number: "))

        answer2 = operations[desired_operation](answer, num3)
        print(f"{answer} {desired_operation} {num3} = {answer2}")
        answer = answer2
    else:
        print("k tnx bye")
        break
