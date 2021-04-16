bill = int(input("bill: $"))
tip = int(input("tip: %"))
number_of_people = int(input("how many? "))

result = round((bill + round(bill*tip/100, 2))/number_of_people, 2)
print(f"each should pay: {result}")