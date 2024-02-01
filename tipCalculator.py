print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12 or 15? "))
peeps = int(input("How many people are splitting the bill? "))

total = (bill + (bill * tip / 100)) / peeps

rounded_total = "{:.2f}".format(total, 2)

print(f"Each person should pay {rounded_total}")
