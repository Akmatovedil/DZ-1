class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'fullname{self.fullname}\n age {self.age}\n is_married{self.is_married}')

    def __str__(self):
        return f'fullname {self.fullname}'

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        Person.__init__(self, fullname, age, is_married)
        self.marks = marks

    def average_marks(self):
        print(sum(self.marks)/5)


class Teacher (Person):
    salary = 10000
    def __init__(self, fullname, age, is_married,experience):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience

    def Calculate_salary(self):
        if self.experience > 3:
            new_salary = self.salary + ((self.experience - 3)*(self.salary//100*5))
            return new_salary

    def introduce_myself(self):
        print(f'fullname{self.fullname}\n age {self.age}\n is_married{self.is_married}\n experience{self.experience}\n '
              f'salary{self.salary}')

teacher1 = Teacher('Суран Асанович', 57, 'Yes', 7  )
print(f'name: {teacher1.fullname}\nage: {teacher1.age}\nis_married:{teacher1.is_married}\nexperience:{teacher1.experience}')
print(f'Salary: {teacher1.Calculate_salary()}')
def create_students ():
    student1 = Student(fullname='Айбек', age=23, is_married='No', marks={
        'Математика': 5,
        'Русский': 4,
        'География': 4,
        'Английский': 3})

    student2 = Student(fullname='Шамиль', age=24, is_married='No', marks={
        'Математика': 5,
        'Русский': 5,
        'География': 5,
        'Английский': 5})

    student3 = Student(fullname='Чынгыз', age=23, is_married='No', marks={
        'Математика': 4,
        'Русский': 5,
        'География': 3,
        'Английский': 4})

    result = [student1, student2, student3]
    return result

students = create_students()
for i in students:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f"Name: {i.fullname}\n"
          f"Age: {i.age}\n"
          f"Maried: {i.is_married}\n"
          f"Average marks: {sum(list)/len(list)}\n")






