import hashlib
import os
import getpass
import msvcrt
import sys
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



    def Addpartner(self, nypartner):    #used when you get a new partner
        self.partner = nypartner



    def Removepartner(self):    #used when removing a partner
        partner = None



    def Addaccount(self):   #when adding a account
        saldo = Parseint("Please enter your starting saldo: ")
        kontoid = self.id.Tostring + "-" + (1 + 1)  #writes the user id + "-(number of account)"
        self.konton.append(Account(saldo, kontoid))



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

        if (self.partner == None):
            print("Partner: None")

        else:
            print("Partner: ", end="")
            print(self.partner.Name())
        print("Encrypted password: " + str(self.password))

        if len(self.accounts) == 0:
            print("Accounts: None")

        else:
            for i in range(len(self.accounts)):
                print(self.accounts[i].AccountID())



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
