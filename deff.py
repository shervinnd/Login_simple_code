import os 

menu_items = {
    "sign up": {
        "name": "Sign up",
        "description": "enter your info and save your account",
        "order": 1,
    }, 
    "sign in": {
        "name": "Sign in",
        "description": "enter your username and passsword after you logged in your account",
        "order": 2,
    }
}

def menu1():
    print(".....hi welcome to loggin app.....\nplese enter s to continue or e for exit .....")

def menu2():
    index = 1
    for key in menu_items:
            print(f"\t{index}. ", menu_items[key]['name'])
            print(f"\t\tHelp text: {menu_items[key]['description']}\n")
            index += 1
    print("\te. Exit\n")


def correct():
    print("please enter correct option!!")

def menu_signup():
    print()

def clear():
    if os.name == 'nt':
        os.system('cls')

def sort_menu(menu2: dict):
    func = lambda x: x[1]['order']
    return dict(sorted(menu2.items(), key=func))