
# List the prices for each shoe style.
# Calculate different scenerios for customers
# including the subtotal, the tax (.7%), and the
# total after subtotal and tax.
# Free Run : $75
# UltraBoost : $150
# Asics Gel Lyte : $120
# Vans Old Skool : $60
# Air Max 1 : $100
# Roshes : $70

item1 = float(input("Enter price of item1"))
item2 = float(input("Enter price of item2"))
item3 = float(input("Enter price of item3"))
item4 = float(input("Enter price of item4"))
item5 = float(input("Enter price of item5"))
item6 = float(input("Enter price of item6"))

subtotal = item1 + item2 + item3 + item4 + item5 + item6

tax = subtotal * 0.07

total = subtotal + tax

print subtotal
print tax
print total


item1 = float(input("Enter price of item1"))

item3 = float(input("Enter price of item3"))

item5 = float(input("Enter price of item5"))


""" Calculate subtotal, tax total, and total.
>>> item1 + item2
240.75
"""
subtotal = item1 + item3 + item5

tax = subtotal * 0.07

total = subtotal + tax

print subtotal
print tax
print total


