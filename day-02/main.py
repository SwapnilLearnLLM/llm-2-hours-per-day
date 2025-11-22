# Tip Calculator
print("Welcome to the tip calculator !")
print("-----------------------------------")
bill = input("What was the total bill? $ ")
tip = input("What percentage tip would you like to give? 10, 12, 0r 15? ")
split = input("How many people to split the bill? ")
total_bill = float(bill)
tip_as_percent = float(tip) / 100
total_tip_amount = total_bill * tip_as_percent
bill_with_tip = float (total_bill + total_tip_amount)
paid_per_person = bill_with_tip / int(split)
final_amount = round(paid_per_person, 2)
print(f"Each person should pay: ${final_amount}")