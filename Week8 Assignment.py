phrase_1 = input("Enter a phrase:") #Asks user for a phrase
phrase_1_upper = input("\nEnter the same phrase but in all uppercase:") #Asks user to enter the same phrase but in all caps

if phrase_1.upper() == phrase_1_upper: #Checks if second phrase is equal to first phrase in all caps
    print("Stop shouting please!")
else: #If not equal, prints out message
    print("The phrase you entered doesn't match")

phrase_1 = input("Enter a phrase:") #Asks user to enter a phrase
count = 0 #Variable to keep count of vowels

for letter in phrase_1.lower(): #For loop through every letter in phrase_1.lower() to simplify coding
    if letter == "a": #If letter is equal to "a", increase count by 1
        count += 1
    elif letter == "e": #If letter is equal to "e", increase count by 1
        count += 1
    elif letter == "i": #If letter is equal to "i", increase count by 1
        count += 1
    elif letter == "o": #If letter is equal to "o", increase count by 1
        count += 1
    elif letter == "u": #If letter is equal to "u", increase count by 1
        count += 1
print(f"\nThe number of vowels in \"{phrase_1}\" is: {count}") #Prints out phrase and number of vowels found in it

phrase_1 = input("Enter a phrase: ") #First phrase to be compared
phrase_2 = input("Enter a second phrase: ") #Second phrase to be compared

if phrase_1 < phrase_2: #Checks if phrase_1 comes before phrase_2 alphabetically
    print(f"\"{phrase_1}\" comes before \"{phrase_2}\".")
else: #Otherwise, phrase_2 must come before phrase_1 alphabetically
    print(f"\"{phrase_2}\" comes before \"{phrase_1}\".")

email_1 = input("Enter your email address: ") #Asks user to enter email
email_2 = input("Re-enter your email address: ") #Asks user to re-enter the email

while email_1.lower() != email_2.lower(): #Checks if lower of both inputs don't match
    print("Inputs did not match") #Prints that the inputs didn't
    email_1 = input("Enter your email address: ") #Asks user to enter email again
    email_2 = input("Re-enter your email address: ") #Asks user to re-enter email again

print("Thank you!\n") #Once inputs match, print "Thank you"

import time #Import time module to measure speed of iteration vs recursion

factorial_3 = 3 #Variable with value of 3 we will find factorial of
factorial_10 = 10 #Variable with value of 10 we will find factorial of
factorial_25 = 25 #Variable with value of 25 we will find factorial of

product = 1 #Variable to keep count as we calculate the factorial
start = time.perf_counter_ns() #Time at start
while factorial_3 != 1: #Checks if variable is not equal to 1 and iterates until 1
    product *= factorial_3 #Multiplies product by current value of variable
    factorial_3 -= 1 #Subtracts 1 from variable until while condition is not met
stop = time.perf_counter_ns() #Time at stop
print(f"Factorial of 3 is {product}. It took {start-stop}ns to compute iteratively.") #Prints value of factorial and time in nanoseconds elapsed

product = 1 #Resets variable to 1 for next calculation
start = time.perf_counter_ns() #Time at start
while factorial_10 != 1: #Checks if variable is not equal to 1 and iterates until 1
    product *= factorial_10 #Multiplies product by current value of variable
    factorial_10 -= 1 #Subtracts 1 from variable until while condition is not met
stop = time.perf_counter_ns() #Time at stop
print(f"Factorial of 10 is {product}. It took {start-stop}ns to compute iteratively.") #Prints value of factorial and time in nanoseconds elapsed

product = 1 #Resets variable to 1 for next calculation
start = time.perf_counter_ns() #Time at start
while factorial_25 != 1: #Checks if variable is not equal to 1 and iterates until 1
    product *= factorial_25 #Multiplies product by current value of variable
    factorial_25 -= 1 #Subtracts 1 from variable until while condition is not met
stop = time.perf_counter_ns() #Time at stop
print(f"Factorial of 25 is {product}. It took {start-stop}ns to compute iteratively.\n") #Prints value of factorial and time in nanoseconds elapsed


def factorial_calc(num):
    """
    calculates the factorial of parameter passed

    :param num: (int) integer which we want the factorial calculated for
    :return: (int) the factorial of the number we passed the function
    """
    if num == 1: #Base function of num being equal to 1
        return 1 #return 1
    else: #If num is not 1
        return num * factorial_calc(num - 1) #returns the product of num times the function recursively called - 1

start = time.perf_counter_ns() #Time at start
product = factorial_calc(3) #Calls function with value and assigns to product
stop = time.perf_counter_ns() #Time at stop
print(f"Factorial of 3 is {product}. It took {start-stop}ns to compute recursively.") #Prints value of factorial and time in nanoseconds elapsed

start = time.perf_counter_ns() #Time at start
product = factorial_calc(10) #Calls function with value and assigns to product
stop = time.perf_counter_ns() #Time at stop
print(f"Factorial of 10 is {product}. It took {start-stop}ns to compute recursively.") #Prints value of factorial and time in nanoseconds elapsed

start = time.perf_counter_ns() #Time at start
product = factorial_calc(25) #Calls function with value and assigns to product
stop = time.perf_counter_ns() #Time at stop
print(f"Factorial of 25 is {product}. It took {start-stop}ns to compute recursively.") #Prints value of factorial and time in nanoseconds elapsed


"""
I'm not sure why the iteration and recursion of the small number, 3, took roughly the same amount of time
Anything above 3, the time elapsed for recursion was roughly half the time it took to calculate the factorial iteratively
From what I had understood, I expected the case to be the other way around so I am unsure why recursion was faster in this case
"""