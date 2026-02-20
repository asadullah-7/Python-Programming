class Person:
    def __init__(self,name,CNIC,gender):
        self.name = name
        self.CNIC = CNIC
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}")
        print(f"CNIC = {self.CNIC}")
        print(f"Gender = {self.gender}")


man = Person("Asad",35,'m')
man.display()

