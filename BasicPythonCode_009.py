#########**************************************************************************************#########
import os
def CheckExist():
    print("Enter the file name you want to check exists or not")
    fd1=input()
    if os.path.exists(fd1):
        print("The file exists")
        exit()

def main():
    CheckExist()

if __name__=="__main__":
    main()
#########**************************************************************************************#########
def DisplayContents():
    print("Enter the file name you want to read")
    file=input()
    fd=open(file,"r")
    print("The contents of the file are displayed on next line........")
    print(fd.read())

def main():
    DisplayContents()

if __name__=="__main__":
    main()
#########**************************************************************************************#########
from sys import argv

def createCopy():
    print("Accepting the input from command line arguments to create file")

    file=argv[1]
    file1=open(file,"x")
    print("File created successfully")

    file2=open("Demo.txt", "r")
    for line in file2:
        file1.write(line)
    print("The contents has been copied from existing file to the newly created file")

def main():
    createCopy()

if __name__=="__main__":
    main()
#########**************************************************************************************#########
from sys import *
import os

def compare():
    file1=argv[1]
    if os.path.isfile(file1):
        print("File1 exists")
    file11=open(file1,"r")

    file2=argv[2]
    if os.path.isfile(file2):
        print("file2 exists")
    file22=open(file2, "r")

    for f1 in file11:
        for f2 in file22:
            if f1==f2:
                print("Success")
            else:
                print("Failure")

def main():
    compare()

if __name__=="__main__":
    main()
#########**************************************************************************************#########
from sys import argv

def StringInFile():
    count=0
    file=argv[1]
    file1=open(file,"r")

    String=argv[2]

    if String in file1:
        count=count+1
    print("The frequency of input string is :", count)

def main():
    StringInFile()

if __name__=="__main__":
    main()
#########**************************************************************************************#########
