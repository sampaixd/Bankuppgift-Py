from collections import defaultdict
import hashlib
import os
import getpass
import msvcrt
from time import sleep
from typing import ValuesView
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
            gettingname = True

            while gettingname:
                name = getpass.getpass("Please enter username: ")
                if name == self.name: gettingname = False

                else:   print("Couldn't find the admin user, please try again")

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
        options = ["View all users", "View all transactions", "delete a user", "unlock a user", "give/remove money", "Exit"]
        loggedin = True

        while loggedin:
            selectedoption = OptionsList(question, options)
            
            match(selectedoption):

                case 0:
                    Admin.ViewAllUsers(self, users)

                case 1:
                    Admin.ViewTransactionHistory(self)

                case 2:
                    Admin.DeleteUser(self, users)

                case 3:
                    Admin.UnlockUser(self, users)

                case 4:
                    Admin.ChangeAccountMoney(self, users)

                case 5:
                    print("Logging out...")
                    sleep(1)
                    loggedin = False
                    Clear()



    def ViewAllUsers(self, users):

        if len(users) == 0:
            print("No users avalible")

        else:
            for i in range(len(users)):
            
                users[i].Info()
        os.system("pause")
        Clear()


    
    def ViewTransactionHistory(self):

        if len(User.transactionhistory) == 0:
            print("No transaction history avalible")

        else:
            for i in range(len(User.transactionhistory)):
                print(User.transactionhistory[i])

        os.system("pause")
        Clear()



    def DeleteUser(self, users):
        selectinguser = True
        
        if len(users) == 0:
            print("No users avalible")
            os.system("pause")

        else:

            usernames = []
            for i in range(len(users)):
                usernames.append(users[i].name)

            usernames.append("exit")
            chosenuser = OptionsList("Please choose a user to delete", usernames)
            
            try:
                print("Removed user " + users[chosenuser].name + ", returning to menu...")
                users.pop(chosenuser)

            
            except :
                print("Returning to main menu...")

        sleep(1)
        Clear()



    def UnlockUser(self, users):
        if len(users) == 0:
            print("No users avalible")
            os.system("pause")

        else:
            usernames = []
            usingmenu = True
            while usingmenu:
                for i in range(len(users)):
                    lockedstatus = ""

                    if users[i].locked == False:
                        lockedstatus = " Status: " + Color.green + " Unlocked" + Color.default

                    else:
                        lockedstatus = " Status: " + Color.error + " Locked" + Color.default

                    usernames.append(users[i].name + lockedstatus)
                usernames.append("unlock all users")
                usernames.append("exit")

                chosenuser = OptionsList("Please choose the user you wish to unlock", usernames)
                Clear()

                try:
                    users[chosenuser].UnlockAccount()
                
                except:
                    if chosenuser == len(users):
                        for i in range(len(users)):
                            users[i].UnlockAccount()
                        #print("Unlocked all accounts!")
                    else:
                        print("Exiting to menu...")
                        usingmenu = False
                
                usernames.clear()


            os.system("pause")
            Clear()



    def ChangeAccountMoney(self, users):
        question = "Please choose a user that you wish to give/remove money from"
        userinfo = []
        gotoaccounts = False

        if len(users) == 0:
            print("No users avalible")

        else:
            loop = True
            while loop:
                for i in range(len(users)):
                    userinfo.append(users[i].name)

                userinfo.append("exit")
                if gotoaccounts == False:    chosenuser = OptionsList(question, userinfo)

                else:    gotoaccounts = False

                if chosenuser == len(users):
                    break

                userinfo.clear()
                question = "Please select one of " + users[chosenuser].name + "s account"
                for i in range(len(users[chosenuser].accounts)):
                    userinfo.append(users[chosenuser].accounts[i].AccountID())

                userinfo.append("back")

                chosenaccount = OptionsList(question, userinfo)

                if chosenaccount == len(users[chosenuser].accounts):    
                    userinfo.clear()    
                    continue
                    
                question = "Would you like to add or remove money from account?"
                userinfo.clear()
                userinfo.append("Add")
                userinfo.append("Remove")
                userinfo.append("back")

                addremove = OptionsList(question, userinfo)

                addremovemsg = ""

                if addremove == 0:  addremovemsg = "add"

                elif addremove == 1: addremovemsg = "remove"
                
                else:
                    gotoaccounts = True    
                    continue
                ammount = 0

                selectingammount = True
                while selectingammount:

                    ammount = Parseint("Please enter how much you want to {} to the account: ".format(addremovemsg))
                    Clear()
                    if ammount > users[chosenuser].accounts[chosenaccount].Saldo(): 
                        print(Color.error + "ERROR!" + Color.default + "Cannot remove more than " + str(users[chosenuser].accounts[chosenaccount].Saldo()) + " usd from account!")
                    else:
                        selectingammount = False

                if addremovemsg == "add":   addremovemsg = "added"

                else: addremovemsg = "removed"
                users[chosenuser].AdminTransaction(chosenaccount, addremove, ammount)
                print("{money} usd {addremove}! Returning to menu...".format(money = ammount, addremove = addremovemsg))
                sleep(1)
                loop = False

                







                    


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



def Parseint(message):  #method for parsing a int
    while True:
        try:

            userinput = int(input(message))
            return userinput

        except ValueError:
            print(Color.error + "ERROR! " + Color.default + "Incorrect input, please try again")
