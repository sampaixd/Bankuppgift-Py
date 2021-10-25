import hashlib
import os
import getpass
import msvcrt
import sys
from time import sleep
from account import Account
from colors import Color


class User:     #class for user
    def __init__(self, name, id, salt, password, partner):
        self.name = name
        self.id = id
        self.salt = salt
        self.password = password
        self.accounts = []      #list of accounts 
        self.partner = partner



    def Changeuserinfo(self):
        changinginfo = True
        selectedoption = 0
        while changinginfo:
            print("What do you wish to change?")

            if selectedoption == 0:
                print(Color.selected, end="")
            print("Name" + Color.default)

            if selectedoption == 1:
                print(Color.selected, end="")
            
            if self.partner == None:
                print("Add partner" + Color.default)

            else:
                print("Remove partner" + Color.default)

            if selectedoption == 2:
                print(Color.selected, end="")
            print("Change password")

            if selectedoption == 3:
                print(Color.selected, end="")
            print("Exit" + Color.default)


            pressedkey = str(msvcrt.getch())
            Clear()

            match(pressedkey):

                case "b'w'" | "b'H'":
                    if currentoption <= 0:
                        currentoption = 3

                    else:
                        currentoption -= 1

                case "b's'" | "b'P'":

                    if currentoption >= 3:
                        currentoption = 0

                    else:
                        currentoption += 1

                case "b'\\r'":

                    if currentoption == 0:
                        print("temp")


    def Addpartner(self):    #used when you get a new partner
        newpartner = input("Please enter the name of your new partner")
        for i in range(len(self.accounts)):
            foundpartner = User.CompareName(newpartner)
            if foundpartner == True:
                print("Partner found, adding " + newpartner + "as your new partner")
                self.partner = newpartner



    def Removepartner(self):    #used when removing a partner
        partner = None


    def ChangeName(self):
        newname = input("Please enter your new name: ")
        self.name = newname
        print("Name changed to " + self.name + "!, returning to prevoius menu...")
        sleep(2)        



    def Addaccount(self):   #when adding a account
        saldo = Parseint("Please enter your starting saldo: ")
        kontoid = str(self.id) + "-" + str((len(self.accounts) + 1))  #writes the user id + "-(number of account)"
        self.accounts.append(Account(saldo, kontoid))



    def WriteaccountID(self):   #used for testing
        accountID = str(self.id) + '-' + str(1)
        print (accountID)
        print(self.partner)
    



    def CompareName(self, userinput):   #used to compare different names, used to find users when logging in or adding partners
        if userinput == self.name:
            return True
        return False



    def Login(self, userinput):
        encrypteduserinput = hashlib.pbkdf2_hmac("sha256", userinput.encode('utf-8'), self.salt, 156234)    #encrypts input
        if (encrypteduserinput == (self.password)):     #compares the encrypted input with the encrypted password
            return True     #returns true if they are the same
        return False
    


    def ViewPassword(self):     #used for testing
        print(self.password)



    def Name(self):     #used for returning the name of the user
        return self.name


    
    def Info(self):     #used for testing, will be accessible when logged in sometime later
        print("Username: " + self.name)
        print("User ID: " + str(self.id))

        if (self.partner == None):
            print("Partner: None")

        else:
            print("Partner: ", end="")
            print(self.partner.Name())
        print("Encrypted password: " + str(self.password))

        if len(self.accounts) == 0:
            print("Accounts: None")

        else:
            print("Accounts:")
            for i in range(len(self.accounts)):
                print(self.accounts[i].AccountID() + "   money in account: " + str(self.accounts[i].Saldo()) + " usd")



    def Loggedin(self):
        loggedin = True
        selectedoption = 0
        while loggedin:

            print("Welcome " + self.name + "! what do you wish to do?")
            print()

            if selectedoption == 0:
                print(Color.selected, end="")
            print("View user information" + Color.default)

            if selectedoption == 1:
                print(Color.selected, end="")
            print("Change user information" + Color.default)  

            if selectedoption == 2:
                print(Color.selected, end="")
            print("Add account" + Color.default) 

            if selectedoption == 3:
                print(Color.selected, end="")
            print("perform transaction with account" + Color.default)

            if selectedoption == 4:
                print(Color.selected, end="")
            print("Log out" + Color.default)

            pressedkey = str(msvcrt.getch())
            Clear()
            match(pressedkey):

                case "b'w'" | "b'H'":
                    if selectedoption <= 0:
                        selectedoption = 4

                    else:
                        selectedoption -= 1

                case "b's'" | "b'P'":

                    if selectedoption >= 4:
                        selectedoption = 0

                    else:
                        selectedoption += 1

                case "b'\\r'":
                    if selectedoption == 0:
                        User.Info(self)
                        os.system("pause")

                    elif selectedoption == 1:
                        print("temp")

                    elif selectedoption == 2:
                        User.Addaccount(self)

                    elif selectedoption == 3:
                        print("temp")

                    else:
                        loggedin = False
                        print("Logging out, please wait...")
                        sleep(2)

                case "b'q'":
                    sys.exit()
        
            Clear()




Clear = lambda: os.system('cls')



def Parseint(message):  #method for parsing a int
    while True:
        try:
            userinput = int(input(message))
            return userinput
        except ValueError:
            print("Incorrect input, please try again")



def Parsefloat(message):    #method to parse float
    while True:
        try:
            userinput = float(input(message))
            return userinput
        except ValueError:
            print("Incorrect input, please try again")
