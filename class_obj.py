class Student:
    Type = 'Student'

    def __init__(self, id, dept):
        self.id = id
        self.dept = dept

S1= Student(104, "CSE") 
S2 = Student(205, "IT")

print('Student 1 details:') 
print('Type is :', S1.Type) 
print('ID: ', S1.id)
print('Dept: ', S1.dept)

print('Student 2 details:') 
print('Type is:', S2.Type) 
print('ID: ', S2.id)
print('Dept: ', S2.dept)
 
print("\nAccessing class variable using class name") 
print(Student .Type)

print("Done by Vishal")