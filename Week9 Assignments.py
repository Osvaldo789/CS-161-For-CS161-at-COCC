class Students: #creates a class for students
    def __init__(self, name, age, grade): #Initizalizes attributes such as name, age, and grade
        self.name = name
        self.age = age
        self.grade = grade
    def details(self): #Method to print out the details for a student
            print(self.name + " is " + self.age + " and is in " + self.grade + " grade.")

raj = Students("Raj", "16", "11th") #Creates raj as a Students object and assigns attributes
joe = Students("Joe", "17", "11th") #Creates joe as a Students object and assigns attributes

raj.details() #Calls on details method for raj
joe.details() #Calls on details method for joe

class Staff: #Creates class for Staff
    def __init__(self, name, dep, role, salary): #Initializes name, dep, role, salary
        self.name = name
        self.dep = dep
        self.role = role
        self.salary = salary

class Teacher(Staff): #Creates child class from Staff
    def __init__(self, name, dep, role, salary, age): #Initializes all attributes from Staff plus an age attribute
        super().__init__(name, dep, role, salary) #Super init to inherit attributes from Staff
        self.age = age #Assigns age attribute
    def details(self): #Method to print out the details for a teacher
        print(f"{self.name} is  a {self.age} year old {self.role} in the {self.dep} department. Their salary is ${self.salary}.")

raj = Teacher("Raj", "Science", "Teacher", "50,000", "20") #Creates raj as a Teacher object and assigns attributes
joe = Teacher("Joe", "Science", "Teacher", "59,000", "58") #Creates joe as a Teacher object and assigns attributes

raj.details() #Calls on details method for raj
joe.details() #Calls on details method for joe

class Square: #Creates Square class
    def __init__(self, len, name): #Initializes length and name attributes
        self.len = len
        self.name = name
    def calculations(self): #Method that calculates area and perimeter of a square
        #Area calculates by taking the length and raising to power of 2. Perimeter calculated by taking the length and multiplying by 4
        print(f"The area of {self.name} is {self.len ** 2}. The perimeter of {self.name} is {self.len * 4}")

square1 = Square(10, "Square1") #Creates square1 as a Square object and assigns attributes
square2 = Square(20, "Square2") #Creates square2 as a Square object and assigns attributes

square1.calculations() #Calls on Calculations method for square1
square2.calculations() #Calls on Calculations method for square2