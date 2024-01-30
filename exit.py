import deff
import start 
def exit():
    trust=input("are you sure exit(y/n)? ")
    if trust=="y":
        print("good bye have good day........")
    elif trust=="n":
        deff.clear()
        start.start2()
    else:
        deff.correct()