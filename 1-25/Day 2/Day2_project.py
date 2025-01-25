print("Welcome to our tip calculator!")
bill_amount= float(input("What was the total bill amount?\n$"))
tip_amount = float(input("How muc tip would you like to give?\n%")) / 100
split_count = int(input("How many people are going to split the bill?\n"))

total_bill = bill_amount + (bill_amount * tip_amount)
calculator = round((total_bill / split_count),2)

print(f"Each Person should pay: ${calculator}")
