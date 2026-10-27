campus_name = "NuraDev"
student_count = 35
course_fee = 150000
is_registration_open = True

courses = ["Python", "Web Development", "Flutter", "Computer Basic"]
new_courses = ["AI for Life and Work", "Rust Programming"]

print(type(campus_name))
print(type(student_count))
print(type(course_fee))
print(type(is_registration_open))
print(type(courses))
print(type(new_courses))

if student_count>=30:
    print("enrollment target achieved")
else:
    print("need more students")

print(courses)
courses[2]= "mobile app development"
print(courses)
courses.append("UI/UX design")
print(courses)
courses.insert(1, "Scratch coding")
print(courses)
courses.extend(new_courses)
print(courses)
courses.remove("Computer Basic")
print(courses)
courses.pop()
print(courses)
