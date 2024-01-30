import deff 
import exit


def signin():
   deff.clear()
   print("....sign in section....")
   signin_username()




def signin_username():
   while True:   
      username=input("please enter your username: ")
      with open("username.txt", "r") as f:
         file_content = f.read().splitlines()
         if username in file_content:
            deff.clear()
            print(True)
            signin_password(username)
            break

         elif username=="exit":
            exit.exit()

         else:
            deff.clear()
            print("your username is not saved or wrong!!")
            


def signin_password(username):
   while True:   
      password=input("plese enter your password: ")
      with open("password.txt", "r") as f:
         file_content = f.read().splitlines()
         if password in file_content:
            print(True)
            deff.clear()
            signin_info(username)
            break
         elif username=="exit":
            exit.exit()

         else:
            deff.clear()
            print("your password is not saved or wrong!!")


def signin_info(username):
   print(f"...welcome {username} thanks for comeback...")
