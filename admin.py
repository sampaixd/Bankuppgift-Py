import hashlib
import os
import getpass
import msvcrt
from time import sleep
from user import User
from colors import Color

class Admin:
    def __init__(self):
        self.name = "admin1"
        self.salt = os.urandom(32)
        self.password = hashlib.pbkdf2_hmac("sha256", "pasword".encode("utf-8"), self.salt, 376583)
        self.locked = False



    def Login(self, users):

        if self.locked:
            print(Color.error + "ERROR! " + Color.default + "Admin user has been locked due to multiple failed logins. Please contact IT administrator to resolve the issue")
            os.system("pause")

        else:

            name = getpass.getpass("Please enter username: ")

            attempts = 0
            while attempts < 3:
                password = getpass.getpass("Please enter password: ")
                password = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), self.salt, 376583)
                
                if password != self.password:
                    print("Incorrect password, please try again")
                    attempts += 1

                else:
                    break

            if attempts >= 3:
                self.locked = True
                print("Account has been locked, please contact IT administrator to resolve the issue")
                os.system("pause") 
            
            else:
                print("Login successful, please wait...")
                sleep(1)
                Clear()
                Admin.Loggedin(self, users)
            Clear()
                


    def Loggedin(self, users):
        question = "Welcome " + self.name + "! What do you wish to do?"
        options = ["View all users", "View all transactions", "delete a user", "unlock a user", "give/remove money"]
        loggedin = True

        while loggedin:
            selectedoption = OptionsList(question, options)



    def Viewallusers(self, users):

        for i in range(len(users)):
        
            users[i].Info()
        os.system("pause")
        Clear()

Clear = lambda: os.system('cls')


def OptionsList(question, options):
    selectedoption = 0
    selecting = True
    
    while selecting:
        print (str(question + "\n"))
        for i in range(len(options)):
            if selectedoption == i:
                print(Color.selected, end="")
            print(options[i], Color.default)

        print(Color.black)
        pressedbutton = str(msvcrt.getch())
        print(Color.default)
        Clear()

        match(pressedbutton):
            case "b'w'" | "b'H'":
                if selectedoption <= 0:
                    selectedoption = len(options) - 1

                else:
                    selectedoption -= 1

            case "b's'" | "b'P'":

                if selectedoption >= len(options) - 1:
                        selectedoption = 0

                else:
                    selectedoption += 1

            case "b'\\r'":
                return selectedoption
