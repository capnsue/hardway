from sys import argv

script, filename, = argv

print(f"We're gonna erase {filename}.")
print("if you don't want that, hit control-c")
print("if you do want that press return")

input("?")

print("opening file...")
target = open(filename, 'w')

print("truncating file, bye")
target.truncate()

print("now i'm gonna ask you for 3 lines")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("i am going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally we close it.")
target.close()
