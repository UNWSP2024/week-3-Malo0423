hotdog = 3.50
chilidog = 4.50
cheese = 0.50
peppers = 0.75
grilled_onions = 1.00
tax = 0.07




hotdogOrder = (input('Do you want a hotdog or a chilidog? '))
if "hotdog" in hotdogOrder:
    hotdogOrder = 3.50
else:
    if "chilidog" in hotdogOrder:
        hotdogOrder = 4.50
cheeseOrder = (input('Do you want cheese? '))
if "yes" in cheeseOrder:
    cheeseOrder = 0.50
else:
    if "no" in cheeseOrder:
        cheeseOrder = 0.00
pepperOrder = (input('Do you want peppers? '))
if "yes" in pepperOrder:
    pepperOrder = 0.75
else:
    if "no" in pepperOrder:
        pepperOrder = 0.00
onionOrder = (input('Do you want grilled onions? '))
if "yes" in onionOrder:
    onionOrder = 1.00
else:
    if "no" in onionOrder:
        onionOrder = 0.00


subtotal = hotdogOrder + cheeseOrder + pepperOrder + onionOrder
sales_tax = subtotal * tax
total = subtotal + sales_tax
print('Your subtotal is $', format(subtotal, ',.2f'),)
print('Your tax is $', format(sales_tax, ',.2f'),)
print('\n\nYour total is $', format(total, ',.2f'),)