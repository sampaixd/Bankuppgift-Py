import random
import hashlib
import os
import getpass
from time import sleep

class User:     #class for user
    def __init__(self, name, id, salt, password, partner):
        self.name = name
        self.id = id
        self.salt = salt
        self.password = password
        self.accounts = []      #list of accounts 
        self.partner = partner

    def Addpartner(self, nypartner):    #used when you get a new partner
        partner = nypartner

    def Removepartner(self):    #used when removing a partner
        partner = None

    def Addaccount(self):
        saldo = Parseint("Please enter your starting saldo: ")
        kontoid = self.id.Tostring + "-" + (1 + 1)
        self.konton.append(Konto(saldo, kontoid))
    
    def WriteaccountID(self):
        accountID = str(self.id) + '-' + str(1)
        print (accountID)
        print(self.partner)
    
    def CompareName(self, userinput):
        if userinput == self.name:
            return True
        return False

    def Login(self, userinput):
        encrypteduserinput = hashlib.pbkdf2_hmac("sha256", userinput.encode('utf-8'), self.salt, 156234)
        if (encrypteduserinput == (self.password)):
            return True
        return False
    
    def ViewPassword(self):
        print(self.password)

    def Name(self):
        return self.name

    
    def Info(self):
        print("Username: " + self.name)
        if (self.partner == None):
            print("Partner: None")
        else:
            print("Partner: ", end="")
            print(self.partner.Name())
        print("Encrypted password: " + str(self.password))

    

    
    


class Konto:
    def __init__(self, saldo, kontoid):
        self.saldo = saldo
        self.kontoid = kontoid

def Parseint(message):
    while True:
        try:
            userinput = int(input(message))
            break
        except ValueError:
            print("Incorrect input, please try again")


def Login(users):
    findingname = True
    while findingname:
        userinput = input("Please enter the name of your account: ")
        for i in range(len(users)):
            founduser = users[i].CompareName(userinput)
            if (founduser == True):
                attempts = 0
                while (attempts < 3):
                    userinput = getpass.getpass("Hello " + users[i].Name() + ", Please enter your password: ")
                    rightpassword = users[i].Login(userinput)
                    if (rightpassword == True):
                        print("Logging in as " + users[i].Name() + "...")
                        sleep(2)
                        attempts = 5
                        findingname = False
                    else:
                        print("Wrong password, please try again")
                        attempts += 1
                if (attempts == 3):
                    print("Failed to input the correct password, returning to main menu...")
                    sleep(2)
                    findingname = False

def Parsefloat(message):
    while True:
        try:
            userinput = float(input(message))
            break
        except ValueError:
            print("Incorrect input, please try again")

def Createaccount(users):
    foundpartner = False
    partner = None
    username = input("Please enter your name: ")
    userpartner = input("Do you have a partner? yes/no ")
    if (userpartner == "yes"):
        while (foundpartner == False):
            foundpartner = False
            userpartner = input("Please enter the name of your partner: ")
            foundpartner = False
            for i in range(0, len(users)):
                foundpartner = users[i].CompareName(userpartner)
                if foundpartner == True:
                    partner = users[i]
                    break
            if foundpartner == False:
                userpartner = input(print("Could not find your partner, do you wish to try again? y/n "))
                if userpartner == "y":
                    foundpartner = False
                elif userpartner == "n":
                    foundpartner = True
    password  = getpass.getpass("Please enter your password: ")
    salt = os.urandom(32)
    encryptedpassword = hashlib.pbkdf2_hmac("sha256", password.encode('utf-8'), salt, 156234)
    id = random.randint(100000, 999999)
    users.append(User(username, id, salt, encryptedpassword, partner))
    print("User added! returning to main menu...")
    sleep(2)
    

Clear = lambda: os.system('cls')

def Main():
    users = []
    programloop = True
    while programloop:
        Clear()
        print("Welcome to the bank app!")
        usercmd = input("Please write what you wish to do: ")
        Clear()
        match(usercmd):
            case "create account":
                 Createaccount(users)
            case"passwords":
                currentuser = 1
                for i in range(len(users)):
                    print(currentuser, ": ", end="")
                    users[i].ViewPassword()
                os.system('pause')
            case "info":
                for i in range(len(users)):
                    users[i].Info()
                os.system("pause")
            case "log in":
                Login(users)
             

Main()