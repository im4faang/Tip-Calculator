print("Welcome to The Tip Calculator.")

total_bill = float(input("What was the total bill?: $"))
tip = int(input("How much tip would you like to give? "))
people = int(input("How many people to split the bill? "))

result = (total_bill / people) * (1 + tip / 100)
format_result = "{:.2f}".format(result)

print(f"Each person should pay: ${format_result}")
