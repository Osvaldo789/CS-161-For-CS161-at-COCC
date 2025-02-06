
user_num = float(input("Enter a number:")) #Assigns user input to a variable

if (user_num % 5) == 0: #Gives remainder when dividing user_num by 5. If it is 0, prints that number is divisible by 5
    print("Your number is divisible by 5.")
else:
    print("Your number is not divisible by 5.")

user_state = input("Enter a US State and I'll tell you the Capital:\n") #Asks user for a state name
user_state = user_state.strip().capitalize() #Formats the string to better catch entry error

#If/elif/else chain to check for state name and print capital
if user_state == "California":
    print("The capital is Sacramento")
elif user_state == "Texas":
    print("The capital is Austin")
elif user_state == "Arizona":
    print("The capital is Phoenix")
elif user_state == "Colorado":
    print("The capital is Denver")
elif user_state == "Hawaii":
    print("The capital is Honolulu")
elif user_state == "Idaho":
    print("The capital is Boise")
else:
    print("I don't know that one")

user_state = input("Enter a US State and I'll tell you the Capital using a dictionary and .get():\n") #Asks user for a state name
user_state = user_state.strip().capitalize() #Formats the string to better catch entry error

#dictionary with collection of states and capitals for later lookup
states = {
    "California" : "Sacramento",
    "Texas" : "Austin" ,
    "Arizona" : "Phoenix",
    "Colorado" : "Denver",
    "Hawaii" : "Honolulu",
    "Idaho" : "Boise",
}

capital = states.get(user_state, "I don't know that one") #Creates capital variable and utilizes get() to lookup the value in the dictionary
#Assigns "I don't know that one" if value not found in dictionary
print(capital)

user_state = input("Enter a US State and I'll tell you the Capital using match case:\n") #Asks user for a state name
user_state = user_state.strip().lower().capitalize() #Formats the string to better catch entry error

match user_state: #match using user_state
    case "California" | "Texas" | "Arizona" | "Colorado" | "Hawaii" | "Idaho": #Checks if user_state is equal to any of listed states
        capital = states.get(user_state)  # Creates capital variable and utilizes get() to lookup the value in the dictionary
        print(capital)
    case other: #To catch if other case is not met
        print("I don't know that one")



#Tells user the price of the pool according to age and then asks for user age and assigns to variable
user_age = int(input("Welcome to the pool! Prices are as follows!\nUnder 2 years old: Free\n2-11: $3\n12-60: $6\nOver 60: $4\nHow old are you?"))

def pool_admission(age):
    """Takes age input and returns a price depending on where it falls

    Parameters
    ----------
    age : int
        Age to be examined

    Returns
    -------
    int
        Price of pool ticket as determined by age

    """
    if age < 2 :
        return 0
    elif age < 12 :
        return 3
    elif age < 61 :
        return 6
    else:
        return 4

print(f"Your age is {user_age}. Your pool ticket will be: ${pool_admission(user_age)}\n")

import requests #imported requests method for use

x = requests.get("http://coccbobcat.com/") #Grabs HTML code from URL and assigns to x

print(x.text) #prints contents of x

x_160 = x.text.count("160") #Counts the amount of times the number 160 appears

#f string to print out in a sentence the amount of times the number 160 appears
print(f"The substring \"160\" appears {x_160} times in the HTML source of http://coccbobcat.com.\n")

import psutil #imported psutil method for use

p = psutil.pids() #calls on psutil to list the processes currently running

print(p) #print p to verify proper function

print(f"Number of running processes: {len(p)}.") #Counts the number of items in the list p