store_name = "Fashion House"
staff_count = 5
monthly_income = 850000.0
is_open = True

clothes = ["shirt", "jeans", "jacket", "dress"]
new_clothes = ["skirt", "hoodie"]

print(type(store_name))
print(type(staff_count))
print(type(monthly_income))
print(type(is_open))
print(type(clothes))
print(type(new_clothes))

if monthly_income>=800000:
    print("income target achieved ")
else:
    print("income target not achieved")

print(clothes)
clothes[1]="black jeans"
print(clothes)
clothes.append("sweater")
print(clothes)
clothes.insert(1, "T-shirt")
print(clothes)
clothes.extend(new_clothes)
print(clothes)
clothes.remove("jacket")
print(clothes)
clothes.pop()
print(clothes)