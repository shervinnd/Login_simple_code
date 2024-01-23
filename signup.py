import deff as d
import signin as si
import exit as e
import start as st



def signup():
    print("....sign up section....\nplease fil a all part to sign up:")
    signup_name()
    




def signup_name():
    while True: 
        f_name=input("enter your first name: ").lower()
        if len(f_name)>12 or type(f_name)==int or type(f_name)==float:
            d.correct()
        elif len(f_name)<3 :
            print("first name must be atleast 4 charcter!!")
        else:
            l_name=input("enter your last name: ").lower()
            if len(l_name)>12 or type(l_name)==int or type(l_name)==float:
                d.correct()
            elif len(l_name)<4:
                print("last name must be atleast 5 charcter!!")
            else:
                d.clear()
                signup_email(f_name,l_name)
                break


def signup_email(f_name,l_name):
    while True:
        email=input("plesase enter your email: ").lower()
        if len(email)<5 or len(email)>50 :
            print("email must be atlest 15 to 50 charecter!!!")
        elif email.endswith("@gmail.com") or email.endswith("@yahoo.com") or email.endswith("@tele.com"):
            d.clear()
            signup_phone(f_name,l_name,email)
            break
        else:
            d.correct()


def signup_phone(f_name,l_name,email):
    while True:
        phone=input("please enter your phone number: ")
        if not type(phone)==str:
            d.correct()
        elif len(phone)<11 or len(phone)>11:
            print("phone number must be 11 charcter!!")
        elif phone.startswith("0912") or phone.startswith("0910") or phone.startswith("0911") or phone.startswith("0903") or phone.startswith("0938") or phone.startswith("0990") or phone.startswith("0930") or phone.startswith("0919"):
            d.clear()
            signup_username(f_name,l_name,email,phone)
            break
        else:
            d.correct()

def signup_username(f_name,l_name,email,phone):
    while True:     
        username=input("please enter your username: ").lower()
        if type(username)==float:
            d.correct()
        elif len(username)>20 or len(username)<3 :
            print("username must be 4 to 10 charectar!!")
        else:
            with open("username.txt", "a") as f:
                f.write("\n")
                f.write(username)
                f.close()
            d.clear()
            signup_pass(f_name,l_name,email,phone,username)
            break

def signup_pass(f_name,l_name,email,phone,username):
    while True:    
        password=input("please enter your password: ")
        if type(password)==float:
            d.correct()
        elif len(password)>20 or len(password)<8:
            print("password must be 5 to 10 charecter")
        else:
            with open("password.txt", "a") as f:
                f.write("\n")
                f.write(password)
                f.close()
            d.clear()
            signup_info(f_name,l_name,email,phone,username,password)
            break

def signup_info(f_name,l_name,email,phone,username,password):
    print(" ..your account is created thanks for join..")
    print(f"firstname:{f_name} \nlastname:{l_name}\nemail:{email}\nphone number:{phone}\nusername:{username}\npassword:{password}")

