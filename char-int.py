import operator
l1 = [('dave','R',13),('python','A',23),('hello','E',44),('mark','A',15),('world','E',66)]
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
student_objects = [Student('john', 'A', 15),Student('jane', 'B', 32),Student('dave', 'C', 20),]
print sorted(student_objects, key=lambda student: student.age)
print sorted(student_objects,key=operator.attrgetter('grade','age'))
print sorted(student_objects,key=operator.attrgetter('grade','age'),reverse=False)
print sorted(student_objects,key=operator.attrgetter('grade','age'),reverse=True)
print sorted(l1,key=operator.itemgetter(1,2))