print("Welcome to the Tip Calculator.")

bill = float(input("How much is the total amount ? \n"))

tip = int(input("What percentage would you like to give? ? 10 , 12 ,15 ? \n"))

people = int(input("How many people will share the bill? ? \n"))

bill_with_tip = bill + (bill/100) * tip

total_amount = bill_with_tip / people

print(f"Amount per person {total_amount}$")

