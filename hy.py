
class Teacher:
    def __init__(self, name, courseName):
        self.name = name
        self.courses = courseName

    def setName(self, name):
        self.name = name

    def setcoursesName(self, courseName:list):
        self.courses = courseName

    def getName(self):
        return self.name
    
    def getcourses(self):
        return self.courses
    
class Parent:
    def __init__(self, name, child, contactInfo):
        self.name = name
        self.child = child
        self.contactInfo = contactInfo

    def setName(self, name):
        self.name = name

    def setChild(self, child):
        self.child = child 

    def setContactInfo(self, contactInfo):
        self.contactInfo = contactInfo 

    def getName(self):
        return self.name

    def getChild(self):
        return self.child
    
    def getContactInfo(self):
        return self.contactInfo

class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setSex(self, sex):
        self.sex = sex

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getSex(self):
        return self.sex
    


s1 = Student("HY", 18, "F")
s2 = Student("SY", 19, "F")
s3 = Student("YS", 20, "M")
s4 = Student("DV", 20, "F")

p1 = Parent("HJ", "HY", "01020199599")
p2 = Parent("HJ", "SY", "01087289599")
p3 = Parent("YSM", "YS", "01011112222")
p4 = Parent("DVM", "DV", "01022223333")

t1 = Teacher("Adam", "Computerscience")
t2 = Teacher("Mel", "advanced ELA")
t3 = Teacher("SE", "spanish")

students = [s1,s2,s3,s4]
for eachS in students:
    print(eachS.getName())
