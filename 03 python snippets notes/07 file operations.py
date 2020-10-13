import os

# create a file if it doesn't exist
# use "x" instead of "w" if you want a FileExistsError
with open("demofile.txt", "w") as writer:
    # write a line
    # the following two are equivalent.  print() will insert the \n automatically
    # writer.write("First line\n")
    print("First line", file=writer)

# append a line
with open("demofile.txt", "a") as writer:
    print("second line", file=writer)

print("Read the entire file as a string: ")
with open("demofile.txt", "r") as reader:
    print(reader.read())

print("Read the entire file's lines into a List:")
with open("demofile.txt", "r") as reader:
    print(reader.readlines())

print()
print("Read the file line by line:")
with open("demofile.txt", "r") as reader:
    for line in reader:
        print(line, end="")

# delete it
os.remove("demofile.txt")
