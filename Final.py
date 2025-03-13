class Characters: #Parent class Character that will be inherited by child classes Witches and Warlocks
    def __init__(self, name): #Creates name and health attributes
        self.name = name
        self.health = 10
    def health_report(self): #Reports the characters health if alive or checks if they are dead
        if self.health <= 0:
            print(self.name + " is dead!!!!!")
        else:
            print(self.name + " has " + str(self.health) + " health\n--------------------")

class Witches(Characters): #Child class of Characters
    def spell(self, target): #spell method that takes a target parameter, inflicts damage to target, and then calls health_report method
        target.health -= 1
        print(f"{self.name} uses Swoosh!")
        target.health_report()

class Warlocks(Characters): #Child class of Characters
    def spell(self, target): #spell method that takes a target parameter, inflicts damage to target, and then calls health_report method
        target.health -= 2
        print(f"{self.name} uses KABOOM!!")
        target.health_report()



glenda = Witches("Glenda") #Instantiates a Witches class
goliath = Warlocks("Goliath") #Instantiates a Warlock class


#Describes the scenario for the user
print("An overconfident witch by the name of Glenda picks a fight with a powerful warlock by the name of Goliath!!\nWho will win?!?!\n")

turn_counter = 0 #Variable to ensure each character takes turns, but to avoid the problem of a character attacking if they are already dead
while glenda.health > 0 and goliath.health > 0: #Checks to see if either character is dead by ensuring their health is greater than 0
    if turn_counter == 0 : #Checks if goliath's turn
        goliath.spell(glenda)
        turn_counter = 1 #Sets counter to 1 for glenda's turn
    else:
        glenda.spell(goliath)
        turn_counter = 0 #Sets counter to 0 for glenda's turn
