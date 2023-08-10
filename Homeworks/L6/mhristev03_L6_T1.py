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
        
    def attendCourse(self, signature, year):
        self.courses[signature] = {'grades': [], 'year': year }
        
    def addGrade(self, signature, grade):
        if signature in self.courses:
            self.courses[signature]['grades'].append(grade)
    
    def getCourses(self):
        for key, value in self.courses.items():
            print(f'{key} {value}')

    def getAvgGrade(self, signature):
        if signature in self.courses:
            return sum(self.courses[signature]['grades']) / len(self.courses[signature]['grades'])
        