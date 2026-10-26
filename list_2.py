restaurant_name = "Golden Restaurant"
daily_customers = 45
daily_income = 350000.0
is_open = True

menu = ["fried rice", "noodles", "soup", "salad"]
new_menu = ["coffee", "juice"]

print(type(restaurant_name))
print(type(daily_customers))
print(type(daily_income))
print(type(is_open))
print(type(menu))
print(type(new_menu))

if daily_customers >= 40:
    print("Good customer trafffic")
else:
    print("need more customers")

menu[2]="chicken soup"
print(menu)
menu.append("burger")
print(menu)
menu.insert(1,"pizza")
print(menu)
menu.extend(new_menu)
print(menu)
menu.pop()
print(menu)
# del menu
# print(menu)
