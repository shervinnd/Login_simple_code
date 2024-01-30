import deff
import signin 
import signup 
import exit 

def start1():
    while True:
        deff.menu1()
        any=input("enter: ")
        if any == "s":
            start2()
            break
        elif any=="e":
            exit.exit()
            break
        else:
            deff.correct()


def start2():
    while True:
        deff.menu2()
        entery=input("enter: ")
        if entery == "1":
            signup.signup()
            break
        elif entery =="2":
            signin.signin()
            break
        elif entery =="e":
            exit.exit()
            break
        else:
            deff.correct()