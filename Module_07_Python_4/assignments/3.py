class Student:
    def __init__(self, name, rollNo, marks):
        self.__name = name
        self.__rollNo = rollNo
        self.__marks = marks
    
    # GETTER METHODS
    @property
    def name(self):
        return self.__name
    @property
    def rollNo(self):
        return self.__rollNo
    @property
    def marks(self):
        return self.__marks
    
    # SETTER METHODS
    @name.setter
    def name(self, name):
        self.__name = name
    @rollNo.setter
    def rollNo(self, rollNo):
        if rollNo <= 0:
            return "Roll Number can't be negative !"
        else:
            self.__rollNo = rollNo
    @marks.setter
    def marks(self, marks):
        if marks < 0 and marks > 100:
            return "Invalid Marks !"
        else:
            self.__marks = marks
            
sonu = Student("Sourakanti", 18, 91)
print(sonu.name, sonu.rollNo, sonu.marks) # Triggers getter method for name
sonu.name = "Sourakanti Mandal" # Triggers setter method with name = "Sourakanti Mandal"
sonu.rollNo = 23
sonu.marks = 50
print(sonu.name, sonu.rollNo, sonu.marks)