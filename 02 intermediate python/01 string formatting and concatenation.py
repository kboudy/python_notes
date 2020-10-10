from os import path

# string formatting in most cases
name = "Keith"
print(f"Hello, {name}")
print("Hello, {}".format(name))

# concat lists with join
names = ["Jeff", "Gary", "Jill", "Samantha"]
print(",".join(names))

# os.path.join for file names
print(path.join("/mnt/some", "file.txt"))
