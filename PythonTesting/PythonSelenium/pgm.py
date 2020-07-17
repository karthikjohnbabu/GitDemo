## getting the input from the user
string = input("Enter a string: ")

## initializing a new string to apppend only alphabets
only_alpha = ""

## looping through the string to find out alphabets
for char in string:

## ord(chr) returns the ascii value
## CHECKING FOR UPPER CASE
    if ord(char) >= 65 and ord(char) <= 90:
        only_alpha += char
## checking for lower case
    elif ord(char) >= 97 and ord(char) <= 122:
        only_alpha += char

## printing the string which contains only alphabets
print(only_alpha)