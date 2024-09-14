import os

with open('Intro.txt', 'w') as file:
    file.write("Hello, I'm Sam")
    file.write("I study in Grade 11 and love coding")
file.close()

with open('Intro.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
file.close()

if os.path.exists("My_File.txt"):
    os.remove("My_File.txt")
else:
    print('File is inexistant')

#Creating a file if the given file does not exist

my_file = open("My_File.txt", 'w')
my_file.write("This is my new file, now it exists!")
my_file.close()

#Deleting a file

os.remove('fl.txt')

#Deleting a folder

os.rmdir('folder')