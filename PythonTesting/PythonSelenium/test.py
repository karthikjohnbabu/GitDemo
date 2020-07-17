## get the input from the user
string = input("Enter a string: ")

## initializing a new string to append only alphabets
only_alpha = ""

## looping through the string to find out alphabets
for char in string:

## checking whether the char is an alphabet or not using chr.isalpha() method
    if char.isalpha():
        only_alpha += char

## printing the string which contains only alphabets
print(only_alpha)