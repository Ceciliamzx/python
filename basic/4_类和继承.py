

class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Name: {self.name}, Age: {self.age}")


class student(people):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        super().introduce()
        print(f"Student ID: {self.student_id}")


class teacher(people):
    def __init__(self, name, age, subject, icon="https://www.baidu.com/img/flexible/logo/pc/result.png"):
        super().__init__(name, age)
        self.subject = subject
        self.icon = icon

    def introduce(self):
        super().introduce()
        print(f"Subject: {self.subject}")
        print(f"icon: {self.icon}")



if __name__ == "__main__":
    p = people("Alice", 30)
    s = student("Bob", 20, "S12345")
    t = teacher("Charlie", 40, "Math")

    s.student_id = ""
    s.introduce()

    lst = [ p, s, t ]
    for person in lst:
        person.introduce()
        print("-----")