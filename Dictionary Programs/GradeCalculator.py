# Program to create grade calculator in Python
#       each student : name, assignments[], tests[], lab-works[]
#       10% marks : assignments
#       70% marks : tests
#       20% marks : lab works
#       90+ > A -- 80+> B -- 70+ > C -- 60+> D


class Student:
    def __init__(self, name, assignments, tests, lab):
        self.name = name
        self.assignments = assignments
        self.tests = tests
        self.lab = lab

    def calculate_total_average(self):
        self.assignment_total = sum(self.assignments)
        self.test_total = sum(self.tests)
        self.lab_total = sum(self.assignments)
        self.avg_assignment = self.assignment_total / len(self.assignments)
        self.avg_test = self.test_total / len(self.tests)
        self.avg_lab = self.lab_total / len(self.lab)

    def calculate_grade(self):
        self.calculate_total_average()
        self.grade_mark = self.avg_assignment * .10 +\
                          self.avg_test * .70 + \
                          self.avg_lab * .20
        if self.grade_mark >= 90:
            return f'marks :{self.grade_mark} grade :A'
        elif self.grade_mark >= 80:
            return f'marks :{self.grade_mark} grade :B'
        elif self.grade_mark >= 70:
            return f'marks :{self.grade_mark} grade :C'
        elif self.grade_mark >= 60:
            return f'marks :{self.grade_mark} grade :D'
        else:
            return f'marks :{self.grade_mark} grade :Failed'


sounak = Student('Sounak', [80, 50, 40, 20], [80, 80], [78.20, 77.20])
james = Student("James Potter", [82, 56, 44, 30], [80, 80], [67.90, 78.72])
dylan = Student("Dylan Rhodes", [82, 72, 23, 39], [78, 77], [80, 80])

print(f'Grade Mark  for {sounak.name} : {sounak.calculate_grade()}')
print(f'Grade Mark  for {james.name} : {james.calculate_grade()}')
print(f'Grade Mark  for {dylan.name} : {dylan.calculate_grade()}')