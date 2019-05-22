# imports the argv module so we can get args from the command line.
from sys import argv

# puts the 2 command line arguments into variables.  arg 1 is called scripts, arg 2 is called filename
script, filename = argv

# creates a file object called txt which points to the file named filename
txt = open(filename)

print(f"Here's your file {filename}:")

# prints the stuff in the txt variable to the screen
print(txt.read())

# ask the user to type the filename again, store answer in file_again
print("type the filename again:")
file_again = input("> ")

# put contents of file_again into variable txt_again
txt_again = open(file_again)

# print contents of txt_again to the screen
print(txt_again.read())
