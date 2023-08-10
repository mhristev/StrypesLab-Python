class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = {}
    
    def getSalary(self):
        return self.salary
    
    def addCourse(self, signiture, name):
        self.courses[signiture] = name
        
    def getCourses(self):
        for key, value in self.courses.items():
            print(f'{key} {value}')

class Student(SchoolMember):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = {}
        # self.enroll_year = 
        # self.grades = 
        
    def attentCourse(self, signature, year):
        pass


A = Teacher('Andonov',30,3000)
A.addCourse('PHS', 'Physics')
A.addCourse('MTH', 'Math')
A.getCourses()

B = Student('Petrov',21)