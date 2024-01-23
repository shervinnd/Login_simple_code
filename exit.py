import deff as d
import start as st
def exit():
    trust=input("are you sure exit(y/n)? ")
    if trust=="y":
        print("good bye have good day........")
    elif trust=="n":
        st.start()
    else:
        d.correct()