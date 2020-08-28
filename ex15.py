#importing the argv
from sys import argv
#setting how much parameters
script, filename = argv
#txt is now set to the file in the second parameter
txt = open(filename)
#we read the file(print it)
print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
