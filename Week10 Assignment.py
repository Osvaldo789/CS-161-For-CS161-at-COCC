import math #import math to utilize the math.ceil function to round up the population potential

class SolarObject: #Creates SolarObject class as the Parent class for Planet and Comet
    def __init__(self, dist, spin, orbit_time, name): #Initializes attributes to later be inherited by child classes
        self.dist = dist #Distance from sun in au
        self.spin = spin #Type of spin, placeholder for now
        self.orbit_time = orbit_time #Time it takes to orbit the sun in either days or years as appropriate
        self.name = name #Name of the solar object
    def colonization(self): #Calculates the colonization potential using 6 billion as a reference at 1 au
        print(f"{math.ceil(6 / self.dist)} billion")
    def spin_type(self): #Creates method for use later
        pass

class Planet(SolarObject): #Creates Planet as a child class of SolarObject
    def __init__(self, dist, spin, orbit_time, name): #Inherits attributes from parent class
        super().__init__(dist, spin, orbit_time, name)
        self.spin = "slightly elliptical" #Changes spin attribute to specific for a Planet class
    def colonization(self): #Prints out the details and colonization potential for a planet
        print(f"{self.name} is {str(self.dist)} au from the Sun. It spins {self.spin} and has an orbit taking {self.orbit_time} days.")
        print(f"It can support a population of {math.ceil(6 / self.dist)} billion")

class Comet(SolarObject): #Creates Comet as a child class of SolarObject
    def __init__(self, dist, spin, orbit_time, name): #Inherits attributes from parent class
        super().__init__(dist, spin, orbit_time, name)
        self.spin = "like crazy" #Changes spin attribute to specific for a Comet class
    def colonization(self): #Prints out the details and colonization potential for a comet
        print(f"{self.name} is {str(self.dist)} au from the Sun. It spins {self.spin} and has an orbit taking {self.orbit_time} years.")
        print(f"It can support a population of {math.ceil(6 / self.dist)} billion")

Earth = Planet(1, "...", 365, "Earth") #Creates Earth as an instance of Planet with according attributes
Mars = Planet(1.4, "...", 687, "Mars") #Creates Mars as an instance of Planet with according attributes

Halley = Comet(35, "...", 76.95, "Halley") #Creates Halley as an instance of Comet with according attributes
HaleBopp = Comet(354, "...", 2397.29, "HaleBopp") #Creates HaleBopp as an instance of Comet with according attributes

#Calls colonization method for all 4 instances created
Earth.colonization()
Mars.colonization()
Halley.colonization()
HaleBopp.colonization()