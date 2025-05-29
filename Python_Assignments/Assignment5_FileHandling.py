# Create a new file with name of sample.txt
# Write some content append some content and read separate execution
# Read content from begining
import os
with open('sample.txt','w') as file:
    file.write("Welcome to file handling\n")

with open("sample.txt", "a") as file:
    file.write("This is your first class\n")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

