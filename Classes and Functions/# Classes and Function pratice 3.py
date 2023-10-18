# Student Information
student_name = "Alice"
student_age = "16"
student_grade = [85, 90, 74, 92, 83]
# Oganizing class for student
class Student:
    def __init__(self, name, age, marks):
        self.student_name = name
        self.student_age = age
        self.student_grade = marks 
    
    def get_average(self):
        average = sum(self.student_grade) / len(self.student_grade)
        return average
    
    def is_eligble(self):
        requirement = 60
        average_grade = self.get_average()
        
        if average_grade >= requirement:
            return True
        else:
            return False
# Define class into a variable
stu = Student(student_name, student_age, student_grade)
# Check if student is eligble or not
if stu.is_eligble():
    print(f"{student_name} is eligble for the class")
else:
    print(f"{student_name} is not eligble for the class")
