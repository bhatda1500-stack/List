hotel_name = "Crown Hotel"
total_rooms = 30
room_price = 50000.0
is_open = True

room_types = ["standard", "deluxe", "family", "suite"]
new_room_types = ["premium", "executive"]

print(type(hotel_name))
print(type(total_rooms))
print(type(room_price))
print(type(is_open))
print(type(room_types))
print(type(new_room_types))

if total_rooms>=20:
    print("enough room available")
else:
    print("limited room available")
print(room_types)
room_types[1]="deluxe twin"
print(room_types)
room_types.extend(new_room_types)
print(room_types)
room_types.remove("family")
print(room_types)
room_types.pop()
print(room_types)