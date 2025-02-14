x = int(input("Enter an integer:")) #Assign user input to x

while x > 0: #While loop to check if x is greater than 0
    print(x)
    x = x - 1 #Subtracts 1 from x until while condition is not met
print ("Blastoff!")

x = int(input("Enter an integer:")) #Assign user input to x
while x > 0: #While loop to check if x is greater than 0
    if x % 2 == 0: #Determines if x is divisible by 2
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")
    x = x - 1 #Subtracts 1 from x until while condition is not met
print ("Blastoff!")

x = int(input("Enter an integer:")) #Assign user input to x
decrease_amount = int(input("Enter an amount to decrease by:"))
while x > 0: #While loop to check if x is greater than 0
    if x % 2 == 0: #Determines if x is divisible by 2
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")
    x = x - decrease_amount #Subtracts user decrease amount from x until while condition is not met
print ("Blastoff!")

user_word = input("Enter a word:") #Asks for user work input and assigns
while len(user_word) > 0: #While loop that checks if there is at least 1 character in the string
    if len(user_word) >= 5: #Checks if length of word is at least 5
        print(f"{user_word} has {len(user_word)} letters")
        user_word = input("Enter a word:") #Asks for another string
    else: #When length of string is less than 5, prints goodbye and breaks the while loop
        print("Goodbye!")
        break

user_word = input("Enter a word:") #Asks for user work input and assigns
try_limit = 5
while len(user_word) > 0:
    if len(user_word) >= 5 and try_limit > 0: # Checks if length is at least 5 and that try limit is greater than 1
        print(f"{user_word} has {len(user_word)} letters")
        try_limit -= 1 #Subtracts 1 from try_limit after each word with length of at least 5
        user_word = input("Enter a word:")  # Asks for another string
    elif len(user_word) < 5 and try_limit > 0: #If the length is less than 5 and there are still tries remaining
        print("Goodbye")
        break
    else: #Only met when tries have been depleted
        print("Loser")
        break

num = 10
while num <= 100: #Checks if num is less than or equal to 100
    print(f"{num}  {bin(num)}  {hex(num)}") #Prints num as int, binary, and hex
    num += 1 #Adds 1 to num each pass


def star_iteration(num):
    """ Uses iteration to take an input and print out the amount of * minus 1 each time

    Parameters
    ----------
    num : int
        Starting number for stars to be printed

    Returns
    -------
    none
    """
    while num > 0: #Only runs as long as num is greater than 0
        print ("*" * num) #Prints "*" equal to the value of num
        num -= 1 #Reduces num by 1 each pass

x = int(input("Enter a number:")) #Asks user for a number input

star_iteration(x) #Calls star_iteration function based on user input

def star_recursion(num):
    """ Uses recursion to take an input and print out the amount of * minus 1 each time

    Parameters
    ----------
    num : int
        Starting number for stars to be printed

    Returns
    -------
    none
    """
    if num == 0: #Checks to see if num is equal to 0
        return
    else:
        print("*" * num)  # Prints "*" equal to the value of num
        star_recursion(num - 1) #Calls on itself with input of num - 1

x = int(input("Enter a number:")) #Asks user for a number input

star_recursion(x) #Calls star_recursion function based on user input