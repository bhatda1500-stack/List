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
print(type(room_type))
print(type(new_room_types))

if total_rooms>=20:
    print("enough room available")