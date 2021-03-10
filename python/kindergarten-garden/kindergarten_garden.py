PLANT_NAMES = {
    'R': 'Radishes',
    'C': 'Clover',
    'G': 'Grass',
    'V': 'Violets'
}
STUDENT_NAMES = {
    'Alice',
    'Bob',
    'Charlie',
    'David',
    'Eve',
    'Fred',
    'Ginny',
    'Harriet',
    'Ileana',
    'Joseph',
    'Kincaid',
    'Larry'
}


class Garden:
    def __init__(self, diagram, students=None):
        self.students_plants = {}

        if not students:
            students = STUDENT_NAMES

        start, end = 0, 2
        cups = diagram.splitlines()
        for name in sorted(students):
            self.students_plants[name] = [
                PLANT_NAMES[i] for i in cups[0][slice(start, end)]
            ]
            self.students_plants[name] += [
                PLANT_NAMES[i] for i in cups[1][slice(start, end)]
            ]
            start = start + 2
            end = end + 2

    def plants(self, student):
        return self.students_plants[student]
