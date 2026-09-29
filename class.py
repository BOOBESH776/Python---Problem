class student:
    def __init__(self,name,age):
        self.name = name
        self.age= age
    def dis(self):
        print(f"I am {self.name} and {self.age} years old")
s = student("boobesh",19)
s.dis()