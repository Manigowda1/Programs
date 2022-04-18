class Person:
    def __init__(self, name, idn):
        self.name = name
        self.idn = idn

    def display(self):
        print(self.name)
        print(self.idn)

    def details(self):
        print(f"My name is {self.name}")
        print(f"My id number is {self.idn}")


class Employee(Person):
    def __init__(self, name, idn, post, salary):
        self.post = post
        self.salary = salary
        Person.__init__(self, name, idn)

    def details(self):
        print(f"My name is {self.name}")
        print(f"My salary is {self.salary}")
        print(f"My post is {self.post}")
        print(f"My id number is {self.idn}")


a = Employee('Mani', 1585269, "SE", 25000)
a.display()
a.details()
