def average(num1, num2, num3):
    """Takes average of three numbers and returns

    Parameters
    ----------
    num1 : int
        1st number
    num2 : int
        2nd number
    num3 : int
        3rd number

    Returns
    -------
    int
        Average of 3 numbers
    """
    return (num1 + num2 + num3)/3

print(average(7, 5, 9)) #Will not run if print is placed before function as python reads from top down
print(average(6, 6,7))
#Will not run as num1 is defined only within the function and not as a global variable ---print(num1)

def dog_to_human(dog_age):
    """Takes dog age and converts to human years

    Parameters
    ----------
    dog_age : int
        Age of dog to be converted

    Returns
    -------
    int
        Dog's age in equivalent human years
    """
    human_years = 24 + (dog_age - 2) * 4 #Equation to convert dog to human years
    return human_years

dog_age = 11
print(f"{dog_age} dog years is equivalent to {dog_to_human(dog_age)} human years.")

def car_value(price, car_age, type):
    """Calculates the value of a particular car after certain amount of years

    Parameters
    ----------
    price : int
        Price car was purchased for
    car_age : int
        How old the car is
    type : str
        Type of car i.e. German, Japanese, or Italian

    Returns
    -------
    int
        The value of the car after x amount of years
    """
    if type.lower() == "german":
        return price - ((price * 0.05) * car_age) #Calculates depreciation
    elif type.lower() == "japanese":
        return price - ((price * 0.07) * car_age) #Calculates depreciation
    elif type.lower() == "italian":
        return price + ((price * 0.05) * car_age) #Calculates appreciation

#Various questions to gather information for variables
car_price = int(input("What was your car's purchase price?\n"))
car_age = int(input("How old is your car?\n"))
car_type = input("Is you car German, Japanese, or Italian?\n")

#Fstring to call function and concatenate variables and strings
print(f"The value of a(n) {car_type.capitalize()} car will be ${car_value(car_price, car_age, car_type)} after {car_age} years.")

dog_name = input("Welcome to Dog Age Calculator!!\nWhat is your dog's name?\n") #Assigns name to variable
dog_age = int(input("What is your dog's age?\n")) #Overwrites previous variable

#Calls on previously written function dog_to_human
print(f"Your dog, {dog_name.capitalize()}, is {dog_to_human(dog_age)} human years old!\n")

def icecream_price(scoops):
    """Calculates price of an icecream depending on the amount of scoops desired

    Parameters
    ----------
    scoops : int
        Number of scoops desired

    Returns
    -------
    int
        Price of the icecream
    """
    return (scoops * 1.15) + 2.25
scoop_number = int(input(f"Welcome to OZ's ice cream shop!\nAn ice cream costs $2.25 plus $1.15 per scoop\nHow many scoops would you like?\n"))
print(f"A {scoop_number}-scoop ice cream cone will cost ${icecream_price(scoop_number)}!")