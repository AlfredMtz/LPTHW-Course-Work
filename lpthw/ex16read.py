from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here is the content of your file {filename}:")
print(txt.read())
txt.close()

print(f"The file {filename} was also closed")
