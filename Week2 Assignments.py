####1st Assignment####

x = 11

print(x, bin(x), hex(x)) #Prints x as decimal, binary, and hex

####2nd Assignment####

X = 11

print(X, bin(X), hex(X))

X = int(1.825)

print(X, bin(X), hex(X)) #X was assigned a float and the bin and hex functions are unable to interpret the float so it needs to be converted into an integer

####3rd Assignment####

y = 0b1011 #assigned binary
z = 0xA3 #assigned hex

print(y,z)

####4th Assignment####

a = 18      #int
b = 0b1011  #bin
c = 0xA3    #hex
d = a + b + c

print (f"The sum is {d}") #f string to concatenate a string with an integer

####5th Assignment####  

original_size = 3451
dictionary_size = 958
compressed_text_size = 1020
compression_value = 1 - ((compressed_text_size + dictionary_size) / original_size) # calculates compression value given variables

print(f"Compressed text size: {compressed_text_size} characters\n     Dictionary size: {dictionary_size} characters"
      f"\n               Total: {compressed_text_size + dictionary_size} characters\n  Original text size: {original_size}"
      f" characters\n         Compression: " + format(compression_value, ".2%")) #format to only use 2 decimal places
