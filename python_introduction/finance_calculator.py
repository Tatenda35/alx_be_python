income = int(input("Enter your monthly income:"))
expense = int(input("Enter your total monthly expenses:"))
savings = income - expense
projected  = (savings * 12) + (savings * 12 * 0.05)
print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${projected}.")
