
start_num = int(input("Enter a starting number:")) #Asks user for a start and end number and assigns as int
end_num = int(input("Enter an ending number:"))

print(f"The even numbers between {start_num} and {end_num} are:") #fstring to print out message

for index in range(start_num, end_num + 1): #For loop to iterate between start and end number by assigning as range. end_num has 1 added to include end number in for loop
        if index % 2 == 0: #If index modulus by 2 is equal to zero, it means it is even
            print(index) #If even print out index

pos_int = int(input("\nEnter a positive integer:")) #Asks user for a positive integer
factor_var = 1 #Variable used to represent "factors" to check

print(f"The factors of {pos_int} are:") #fstring to print out statement

while factor_var <= pos_int: #While loop that checks if factor_var is less than or equal to user's input
    if pos_int % factor_var == 0: #Checks if User input modulus factor_var is equal to 0
        print(factor_var) #Prints out factor_var
        factor_var += 1 #Increases factor_var by 1 through each iteration
    else: #If modulus is not 0, increase by 1 without printing
        factor_var += 1

alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #list of letters in english language
name = "Osvaldo" #assigns my name to name variable
name_value = 0 #variable to keep track of the name value

for letter in name.lower(): #iterates through each letter in name. The .lower() used to make each letter case-insensitive
    name_value = name_value + alphabet_list.index(letter) #For each letter in name, grabs index from alphabet_list and adds it to name_value

print(f"\nThe numeric value of Osvaldo is: {name_value}") #Prints the value of name

x = int(input("\nEnter a positive integer: "))
int_num = 1

def squarer(num):
    """Function that takes a number and prints all the squares of integers that come before it

    Parameters
    ----------
    num : int
        Number that we will be counting to

    Returns
    -------
        Prints the square of each integer that comes before number
    """
    if num == 0: #Base condition of num = 0
        return
    else:
        squarer(num - 1) #Calls function recursively while subtracting 1 from num
        print(num ** 2) #print after squarer to print numbers in ascending order

squarer(x) #Calls squarer function with input of x


unsorted_list = [12, 43, 22, 34, 2, 21, 3, 33, 81] #Given unsorted list to teepee sort
unsorted_list.sort() #sorts list in order from lowest to highest
largest = unsorted_list[(len(unsorted_list) - 1)] #Stores largest number in the list to later append

even_list = [] #Creates list to store even numbers from unsorted list
odd_list = [] #Creates list to store odd numbers from unsorted list

for i in range(0 , len(unsorted_list) - 1): #Iterates through a range from first list item to second-largest list item
        if unsorted_list[i] % 2 == 0: #If int at list index 'i' is even, adds to even list
            even_list.append(unsorted_list[i])
        else: #Else, must be odd, add to odd list
            odd_list.append(unsorted_list[i])

even_list.reverse() #Reverses the order of even list for teepee sort

teepee_list = [] #Creates teepee list
teepee_list.extend(odd_list) #Adds contents of odd list to teepee list
teepee_list.append(largest) #Adds largest int to teepee list
teepee_list.extend(even_list) #Adds contents of even list to teepee list
print(teepee_list) #Prints teepee sorted list




#Finds the next largest number by rearranging the given numbers
sample_num = "45123876" #Test number, can be replaced with any set of numbers that does not repeat any number
num_list = list(sample_num) #Converts the sample number into a list of strings
indx = len(sample_num) - 2 #Identifies the second to last list position

while indx >= -1: #While loop that goes as long as indx is -1 or larger
    if indx == -1: #If indx ever reaches -1, prints that a larger number is not possible
        print("No larger arrangement is possible")
        break #Breaks out of the while loop

    elif sample_num[indx] < sample_num[indx + 1]: #ids first number, right to left, that is smaller than the number to its right
        front_list = num_list[0 : indx] #Creates a list of numbers found before the index
        back_list = num_list[indx + 1:] #Creates a list of numbers found after the index
        back_list.sort() #Sorts the list into ascending order

        for i in range(0, len(back_list)): #Iterates through entire back_list
            if back_list[i] > num_list[indx]: #Finds first number that is larger than our indx number
                larger = back_list[i] #Assigns the value of that larger number to "larger" variable
                break #breaks out of for loop as it is no longer needed

        #Swaps the places of the indx number and the smallest number to its right that is still larger than itself
        larger_index = num_list.index(larger) #Identifies the index where "larger" number is found in num_list
        left = num_list[indx] #Stores value found at indx
        right = num_list[larger_index] #Stores value found at larger index
        num_list.pop(indx) #Pop out number found at index indx
        num_list.insert(indx, right) #Inserts value of right at index indx
        num_list.pop(larger_index) #Pop out number found at larger index
        num_list.insert(larger_index, left) #Inserts value of left at larger index

        sorting_list = num_list[indx + 1:] #Creates a list of numbers found after the indx number
        sorting_list.sort() #Sorts the numbers in ascending order to later extend to list
        num_list[indx + 1:] = sorting_list #Replaces the numbers in the list after the index with our sorting_list
        next_highest = "".join(num_list) #Stores the list of strings as a single string
        print(next_highest) #Prints our next highest number
        break #Breaks out of the loop as it is no longer necessary

    else: #If number found at indx is larger than number to its right, shift indx to the left by 1
        indx -= 1



