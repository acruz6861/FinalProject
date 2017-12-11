
# List the prices for each shoe style.
# Christmas/Holiday sale is going on
# Everything is 30% off
# Calculate different scenerios for customers
# including the subtotal, the tax (.7%), and the
# total after subtotal and tax.

item1 = float(input("Enter price of item1"))
item2 = float(input("Enter price of item2"))
item3 = float(input("Enter price of item3"))
item4 = float(input("Enter price of item4"))
item5 = float(input("Enter price of item5"))
item6 = float(input("Enter price of item6"))

subtotal = item1 + item2 + item3 + item4 + item5 + item6

tax = subtotal * 0.07

total = subtotal + tax

print total




