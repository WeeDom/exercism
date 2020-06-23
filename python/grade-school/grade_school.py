from collections import namedtuple
from operator import attrgetter


class School:
    def __init__(self):
        self.Student = namedtuple('Student', 'name grade')
        self.students = []

    def add_student(self, name, grade):
        self.students.append(self.Student(name, grade))

    def roster(self):
        return list(n.name
                    for n in sorted(
                        self.students, key=attrgetter('grade', 'name')
                        ))

    def grade(self, grade_number):
        return list(n.name
                    for n in sorted(
                        self.students, key=attrgetter('grade', 'name'))
                    if n.grade == grade_number)
