import random
import hashlib
import os
import getpass
import msvcrt
import sys
from user import User
from admin import Admin
from time import sleep
from colors import Color



def Login(users):   #method for logging into a account

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
                        Clear()
                        users[i].Loggedin(users)
                        attempts = 5
                        findingname = False

                    else:
                        print("Wrong password, please try again")
                        attempts += 1

                if (attempts == 3):
                    print("Failed to input the correct password, returning to main menu...")
                    sleep(2)
                    findingname = False



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



def Createaccount(users):

    foundpartner = False    #used when looking for partner
    partner = None  #partner is set to none by default
    partnernumber = 0

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
                    partnernumber = i
                    print("Partner added!")
                    break

            if foundpartner == False:
                userpartner = input(print("Could not find your partner, do you wish to try again? y/n "))

                if userpartner == "y":
                    foundpartner = False

                else:
                    foundpartner = True
    password  = getpass.getpass("Please enter your password: ")

    salt = os.urandom(32)
    encryptedpassword = hashlib.pbkdf2_hmac("sha256", password.encode('utf-8'), salt, 156234)
    id = random.randint(100000, 999999)
    users.append(User(username, id, salt, encryptedpassword, partner))
    if partner != None:
        users[partnernumber].Addpartner(users[-1])
    print("User added! returning to main menu...")
    sleep(2)
    


Clear = lambda: os.system('cls')



def Main():
    users = []
    admin = Admin()
    currentoption = 0
    Clear()
    programloop = True

    while programloop:

        print("Welcome to the bank app!")
        print("What do you wish to do?\n") 

        if currentoption == 0:
            print(Color.selected, end="")   
        print("Create user" + Color.default)

        if currentoption == 1:
            print(Color.selected, end="")
        print("Log in" + Color.default)

        if currentoption == 2:
            print(Color.selected, end="")
        print("Admin login" + Color.default)

        if currentoption == 3:
            print(Color.selected, end="")
        print("View all users" + Color.default)

        if currentoption == 4:
            print(Color.selected, end="")
        print("Exit" + Color.default)
        print(Color.black)

        keypressed = str(msvcrt.getch())
        print(Color.default)
        #print("pressed " + str(keypressed))
        Clear()

        if keypressed == "b'q'":
            sys.exit()

        match(keypressed):

            case "b'w'" | "b'H'":
                if currentoption <= 0:
                    currentoption = 4

                else:
                    currentoption -= 1

            case "b's'" | "b'P'":

                if currentoption >= 4:
                    currentoption = 0

                else:
                    currentoption += 1

            case "b'\\r'":

                if currentoption == 0:
                    Createaccount(users)

                elif currentoption == 1:
                    Login(users)

                elif currentoption == 2:
                    admin.Login(users)

                elif currentoption == 3:
                    for i in range(len(users)):

                        users[i].Info()
                    os.system("pause")
                    
                else:
                    sys.exit()
                
                Clear()




if __name__ == "__main__":
    Main()