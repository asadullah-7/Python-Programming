class Person:
    def __init__(self,name,CNIC,gender,address):
        self.name = name
        self.CNIC = CNIC
        self.gender = gender
        self.address = address

    def display(self):
        print(f"Name: {self.name}")
        print(f"CNIC = {self.CNIC}")
        print(f"Gender = {self.gender}")
        print(f"Address: {self.address}")


man = Person("Asad",35,'m',"H#43/9")
man.display()

