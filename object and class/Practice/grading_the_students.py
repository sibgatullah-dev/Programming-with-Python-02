class Student:
    def __init__(self,name,roll,grade):
        self.name = name
        self.roll = roll
        self.grade = grade
        
    def get_grade(self): # Passing the grade with a method so we can use the grade of this class to another class which isn't a child of this class
        return self.grade
    
class Course:
    def __init__(self,name,seats):
        self.name = name
        self.seats = seats
        self.students = []
    
    def add_student(self,student):
        if len(self.students) < self.seats and student.get_grade() > 70: # Since the student is an instance of the Student class so it has the method get_grade() in it which returns grade
            self.students.append(student)
            print("Student added in the course")
            return True
        else:
            print("The seats are filled.")
            return False
    
    def average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
    

s1 = Student('Tim',10,95)
s2 = Student('Jim',11,75)
s3 = Student('Lim',12,55)
s4 = Student('Him',13,69)
s5 = Student('Bim',14,80)

course = Course('Science',3)

course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
course.add_student(s4)
course.add_student(s5)

print("The average grade of the students in the course is: ",course.average_grade())