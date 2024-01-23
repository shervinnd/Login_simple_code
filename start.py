import deff as d
import signin as si
import signup as su 
import exit as e

def start():
   while True:
        d.menu1()
        any=input("enter: ")
        if any != "s":
            d.correct()
        else:
            d.menu2()
            entery=input("enter: ")
            if entery == "1":
                su.signup()
                break
            elif entery =="2":
                si.signin()
                break
            elif entery =="e":
                e.exit()
                break
            else:
                d.correct()