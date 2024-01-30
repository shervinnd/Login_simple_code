import deff 
import signin 
import exit 
import start 
import time


def signup():
    deff.clear()
    print("....sign up section....\nplease fil a all part to sign up:")
    signup_name()
    




def signup_name():
    while True: 
        f_name=input("enter your first name: ").lower()
        if len(f_name)>12 or type(f_name)==int or type(f_name)==float:
            deff.correct()
        elif len(f_name)<3 :
            print("first name must be atleast 4 charcter!!")
        elif f_name=="exit":
            exit.exit()
        else:
            l_name=input("enter your last name: ").lower()
            if len(l_name)>12 or type(l_name)==int or type(l_name)==float:
                deff.correct()
            elif len(l_name)<4:
                print("last name must be atleast 5 charcter!!")
            elif l_name=="exit":
                exit.exit()
            else:
                deff.clear()
                signup_email(f_name,l_name)
                break


def signup_email(f_name,l_name):
    while True:
        email=input("plesase enter your email: ").lower()
        if len(email)<5 or len(email)>50 :
            print("email must be atlest 15 to 50 charecter!!!")
        elif email.endswith("@gmail.com") or email.endswith("@yahoo.com") or email.endswith("@tele.com"):
            deff.clear()
            signup_phone(f_name,l_name,email)
            break
        elif email  =="exit":
            exit.exit()
        else:
            deff.correct()


def signup_phone(f_name,l_name,email):
    while True:
        phone=input("please enter your phone number: ")
        if not type(phone)==str:
            deff.correct()
        elif len(phone)<11 or len(phone)>11:
            print("phone number must be 11 charcter!!")
        elif phone.startswith("0912") or phone.startswith("0910") or phone.startswith("0911") or phone.startswith("0903") or phone.startswith("0938") or phone.startswith("0990") or phone.startswith("0930") or phone.startswith("0919"):
            deff.clear()
            signup_username(f_name,l_name,email,phone)
            break
        elif phone=="exit":
            exit.exit()
        else:
            deff.correct()

def signup_username(f_name,l_name,email,phone):
    while True:     
        username=input("please enter your username: ").lower()
        if type(username)==float:
            deff.correct()
        elif len(username)>20 or len(username)<3 :
            print("username must be 4 to 10 charectar!!")
        
        elif username=="exit":
            exit.exit()
        
        else:
            with open("username.txt", "a") as f:
                f.write("\n")
                f.write(username)
                f.close()
            deff.clear()
            signup_pass(f_name,l_name,email,phone,username)
            break

def signup_pass(f_name,l_name,email,phone,username):
    while True:    
        password=input("please enter your password: ")
        if type(password)==float:
            deff.correct()
        elif len(password)>20 or len(password)<8:
            print("password must be 5 to 10 charecter")
        
        elif password=="exit":
            exit.exit()
        
        else:
            with open("password.txt", "a") as f:
                f.write("\n")
                f.write(password)
                f.close()
            deff.clear()
            signup_info(f_name,l_name,email,phone,username,password)
            break

def signup_info(f_name,l_name,email,phone,username,password):
    print(" ..your account is created thanks for join..")
    print(f"firstname:{f_name} \nlastname:{l_name}\nemail:{email}\nphone number:{phone}\nusername:{username}\npassword:{password}")
    time.sleep(7)
    deff.clear()
    start.start2()
