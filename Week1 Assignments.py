####1st assignment####

pet_type = "Cat"
pet_name = "GatoCat"
#Variables for use in print function
print(f"I have a {pet_type} and her name is {pet_name}")

####2nd assignment####

print("\nEnter your First Name:")
user_name = input()
#Assign user's name
print("Enter your current age:")
user_age = int(input())
#Assign user's age
user_savings = int(input(print("Enter your yearly savings:")))
print(user_savings)
#Different way to assign variable, unsure how to get rid of the "none" on the terminal

print(f"\nHello {user_name}! You are currently {user_age} years old.\nIn 10 years, you will be {user_age + 10}.")
print(f"If you save ${user_savings} each year, in 5 years you will have saved ${user_savings * 5}!")
print(f"Your average monthly savings is ${user_savings//12}!")
#Takes inputs and performs calculations. Needed to specify which variables were integers as I was having an error
#stating I could not concatenate a string with an integer. Also needed to do floor division "//" to have a whole number.
#Unsure if there's a better way to do that

####3rd assignment####

print("\nEnter current month:") #Adds new line and asks for user to enter current month, hopefully January
month = str(input())

def second_calc(month) :
     if month.lower() == "january" : #checks if input was january without being case-sensitive
         month = 31
         print(f"The number of seconds in January is {month * 24 * 60 * 60}.")
     else :
         print("I'm sorry, I only know how to calculate the number of seconds in January.")
second_calc(month)


####4th assignment####

print("\nHow many eggs do you have?")
egg_number = int(input()) #Assigns input to variable

print(f"This makes {egg_number // 12} dozen egg carton(s) with {egg_number % 12} egg(s) left over")
    #Calculates amount of dozen egg cartons able to be made and returns the value