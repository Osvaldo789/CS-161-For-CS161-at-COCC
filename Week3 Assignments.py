####1st Assignment####

user_name = input("What is your name?\n") #Assign user's name to x
print("Hello " + user_name + "!") #Concatenate a sentence


####2nd Assignment####

user_age = input("What's your age?\n") #Assign user's age to x
print(f"Your age plus 5 is {int(user_age) + 5}") #Error trying to concatenate a string with an integer, need to convert str to int

####3rd Assignment####

age_add = input("Pick a number to add to your age:\n") #Asks for user's desired age to add
print(f"Your age plus {age_add} is equal to {int(age_add) + int(user_age)}.") #fstring to simplify concatenation

####4th Assignment####

hours_worked = float(input("How many hours did you work last week? Please include decimals i.e. 10.0, 15.2, 25.7: \n")) #Assigns user float to a variable
hourly_wage = float(input("Without using the '$' sign, what is your hourly wage in decimal format?\n")) #Assigns user float to different variable

####5th Assignment

print(f"Your gross pay this week is: ${hours_worked * hourly_wage}\nYour estimated annual gross pay will be: ${(hours_worked * hourly_wage) * 50}")
#Single string concatenation using an fstring to perform math and print out the result

annual_gross = hours_worked * hourly_wage * 50
print(annual_gross) #Used to verify correct computation was done

#If-Else statement to determine tax bracket and compute approx pay after taxes
if annual_gross >= 0 and annual_gross <= 11600:
    print(f"Your estimated pay after taxes is: ${annual_gross * 0.9}")
elif annual_gross > 11600 and annual_gross <= 47150:
    print(f"Your estimated pay after taxes is: ${annual_gross * 0.88}")
elif annual_gross > 47150 and annual_gross <= 100525:
    print(f"Your estimated pay after taxes is: ${annual_gross * 0.78}")
elif annual_gross > 100525 and annual_gross <= 191950:
    print(f"Your estimated pay after taxes is: ${annual_gross * 0.76}")
elif annual_gross > 191950 and annual_gross <= 243725:
    print(f"Your estimated pay after taxes is: ${annual_gross * 0.68}")
elif annual_gross > 243725 and annual_gross <= 609350:
    print(f"Your estimated pay after taxes is: ${annual_gross * 0.65}")
elif annual_gross > 609350:
    print(f"Your estimated pay after taxes is: ${annual_gross * 0.63}")