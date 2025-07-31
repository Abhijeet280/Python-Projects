import os
import pathlib as path

# Options to be displayed to the User
print("Press 1 to create a file")
print("Press 2 to read a file")
print("Press 3 to update a file")
print("Press 4 to delete a file")
print("Press 5 to see list of file")

# Function made to show the list of files that already exists


def showfiles():
    items = os.listdir()
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


# Function made to create a new file


def createfile():
    showfiles()
    name = input("Enter File Name : ")
    name = name + ".txt"
    if os.path.exists(name) and os.path.isfile(name):
        print("Your file already Exists")
    else:
        with open(name, "w") as f:
            data = input("What you want to write: ")
            f.write(data)
        print("Your file created successfully ")


# Function made to read the files


def readfiles():
    showfiles()
    name = input("Enter File Name To Be Readed : ")
    name = name + ".txt"
    if os.path.exists(name) and os.path.isfile(name):
        with open(name, "r") as f:
            print(f.read())
    else:
        print("File does not Exists")


# Function made to update the file


def updatefiles():
    name = input("Enter File Name To Be Updated : ")
    name = name + ".txt"
    if os.path.exists(name) and os.path.isfile(name):
        print("Press 1 to Overwrite a file : ")
        print("Press 2 to Append Text into a file : ")
        print("Press 3 to Rename a file : ")

        res = int(input("Enter Your Choice : "))
        if res == 1:
            with open(name, "w") as f:
                overwrite = input("Enter Text You Want To Overwrite: ")
                f.write(overwrite)
                print("Text Overwrited Successfully")
        elif res == 2:
            with open(name, "a") as ap:
                data = input("Enter Text You Want To Append : ")
                ap.write(data)
                print("Text Appended Successfully")
        else:
            new_name = input("Enter New Name For The File : ")
            new_name += ".txt"
            os.rename(name, new_name)
            print("Text Renamed Successfully")
    else:
        print("File does not Exists ")


# Function made to delete a file


def deletefiles():
    name = input("Enter file name to be Deleted : ")
    name = name + ".txt"
    if os.path.exists(name) and os.path.isfile(name):
        os.remove(name)
        print("File Deleted Successfully")
    else:
        print("File Does Not Exists")


# Getting response from the user

check = int(input("Enter Your Response : "))

if check == 1:
    createfile()

if check == 2:
    readfiles()

if check == 3:
    updatefiles()

if check == 4:
    deletefiles()

if check == 5:
    showfiles()
