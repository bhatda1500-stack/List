shop_name = "Tech World"
staff_name = "Aye Aye"
monthly_sales = 1200000
is_registered = True

products = ["laptop", "mouse", "keyboard", "monitor"]
new_products = ["webcam", "headphones"]

print(type(shop_name))
print(type(staff_name))
print(type(monthly_sales))
print(type(is_registered))
print(type(products))
print(type(new_products))

if monthly_sales>=1000000:
    print("Moonthly target achieved")
else:
    print("Monthly target not achieved")

print(products)
products[1]="wireless mouse"
print(products)
products.append("printer")
print(products)
products.insert(1, "USB cable")
print(products)
products.extend(new_products)
print(products)
products.remove("keyboard")
print(products)
products.pop()
print(products)