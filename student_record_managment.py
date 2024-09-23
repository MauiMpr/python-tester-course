student1 = ("John Doe", 18, "Grade 12")
student2 = ("Jane Smith", 17, "Grade 11")
student3 = ("Mike Johnson", 16, "Grade 10")

students = (student1, student2, student3)

print(f"Number of students: {len(students)}")
print(f"Index of Jane Smith: {students.index(student1)}")

students_ids = {1001, 1002, 1003}
students_courses = {"Math", "English", "Science"}

print(f"Student courses: {students_courses}")
print(f"The students IDS are: {students_ids}")

combined_data = students_ids.union(students_courses)
print(combined_data)

new_students_id = {1004, 1005, 1006}
new_students_id.update(students_ids)
print(f"new student ids are: {new_students_id}")

frozen_courses = frozenset(["P.E", "Geography", "Art"])
print(frozen_courses)

frozen_student_data = frozenset(students)
print(f"Frozen Student Data: {frozen_student_data}")