brackets = [
    # Single
    [(0.10, 0, 8350), (0.15, 8350, 33950), (0.25, 33950, 82250), (0.28, 82250, 171550), (0.33, 171550, 372950), (0.35, 372950, 999999999)],
    # Married Filing Jointly
    [(0.10, 0, 16700), (0.15, 16700, 67900), (0.25, 67900, 137050), (0.28, 137050, 208850), (0.33, 208850, 372950), (0.35, 372950, 999999999)],
    # Married Filing Separately
    [(0.10, 0, 8350), (0.15, 8350, 33950), (0.25, 33950, 68525), (0.28, 68525, 104425), (0.33, 104425, 186475), (0.35, 186475, 999999999)],
    # Head of Household
    [(0.10, 0, 11950), (0.15, 11950, 45500), (0.25, 45500, 117450), (0.28, 117450, 190200), (0.33, 190200, 372950), (0.35, 372950, 999999999)]
]

income = float(input("Enter taxable income: "))

print("\nFiling Status:")
print("0 Single")
print("1 Married Filing Jointly")
print("2 Married Filing Separately")
print("3 Head of Household")

status = int(input("Enter your choice (0-3): "))

tax = 0
money_left = income

for rate, start, end in brackets[status]:
    if money_left <= 0:
        break
    width = end - start
    in_this_bracket = min(money_left, width)
    tax += in_this_bracket * rate
    money_left -= in_this_bracket

names = ["Single", "Married Filing Jointly", "Married Filing Separately", "Head of Household"]

print("\n----- Results -----")
print("Income:       $", format(income, ",.2f"))
print("Status:       ", names[status])
print("Tax owed:     $", format(tax, ",.2f"))
