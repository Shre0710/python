# Initialize a dictionary for the student records
student_records = {
    "John": {"age": 15, "grade": 90},
    "Emily": {"age": 16, "grade": 85},
    "Michael": {"age": 14, "grade": 92},
    "Sarah": {"age": 17, "grade": 88},
}

# Display the original student records
print("--- Student Records ---")
for name, details in student_records.items():
    print(f"{name}: Age = {details['age']}, Grade = {details['grade']}")

print("\n") 

print("Number of students in the records:", len(student_records))
print("\n")

student_name = "Emily"
student_details = student_records.get(student_name, "Student not found.")
print(f"Details for {student_name}: {student_details}")
print("\n")  


# 4. Remove a student from the records
removed_student = student_records.pop("Sarah", "Student not found.")
print(f"Removed student 'Sarah': {removed_student}")
print("\n") 

# 6. Clear the student records
student_records.clear()
print("Student records after clearing:", student_records)
print("\n") 

# 7. Reinitialize student records for further demonstration
student_records = {
    "John": {"age": 15, "grade": 90},
    "Emily": {"age": 16, "grade": 85},
    "Michael": {"age": 14, "grade": 92},
    "Sarah": {"age": 17, "grade": 88},
}

