#VIETNAM SỜ CU RI TY#
import socket
import os
import requests
import random
import getpass
import time
import sys

from rich_gradient import Gradient
grad = Gradient()

name = input("UserName:")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ascii_vro():
    clear()
    print(f'''   
   ''')
    clear()

def banners():
    clear()    
    print(f"""
METHODS
CLEAR 
""")

def meth():        
    print(f'''
\x1b[38;5;55mHTTP-\x1b[1;37mBROWSER    \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mHTTP-\x1b[1;37mSPAM       \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mHTTP-\x1b[1;37mKILLER     \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mHTTP-\x1b[1;37mGET        \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mHTTP-\x1b[1;37mMERIS      \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mCLOUD\x1b[1;37mFLARE      \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mHTTP-\x1b[1;37mBYPASS     \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
\x1b[38;5;55mHTTP-\x1b[1;37mFLOOD      \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]
''')

def menu():
    os.system("clear")
    print("""          
                        \x1b[1;37m╔╦╗ ╦ \x1b[38;5;55m╦╔═ ╦ ╦
                        \x1b[1;37m║║║ ║ \x1b[38;5;55m╠╩╗ ║ ║
                        \x1b[1;37m╩ ╩ ╩ \x1b[38;5;55m╩ ╚═╚═╝
                  \x1b[1;37m-Best C2 In\x1b[38;5;55m the Year 2024-
             \x1b[1;37m╚═╦══════════════\x1b[38;5;55m═══════════════╦═╝       
          \x1b[1;37m╚╦═══╩══════════════\x1b[38;5;55m═══════════════╩═══╦╝
    \x1b[1;37m╚╦═════╩══════════════════\x1b[38;5;55m═══════════════════╩══════╦╝
     \x1b[1;37m║        -Welcome To Miku\x1b[38;5;55mC2 Made By VanDuc-        ║
     \x1b[1;37m║             -Powerful L\x1b[38;5;55mayer7 Bypasser-           ║        
    \x1b[1;37m╔╩═╦══════════════════════\x1b[38;5;55m════════════════════════╦═╩╗
       \x1b[1;37m║            -PhuVanDuc\x1b[38;5;55m X Miku C2-             ║
      \x1b[1;37m╔╩══════════════════════\x1b[38;5;55m════════════════════════╩╗
      \x1b[1;37m║  _Copyright © 2024 Mik\x1b[38;5;55mu C2 All Right Reserved_ ║
     \x1b[1;37m╔╩═══════════════════════\x1b[38;5;55m═════════════════════════╩╗
      
    """)

# ============================================================
#        🔥🔥 UPGRADE LAYER 7 MENU USING rich_gradient 🔥🔥
# ============================================================

def layer7_menu():
    clear()

    print(grad.text("╔══════════════════════════════════╗", colors=["#00FFFF","#FF00FF"]))
    print(grad.text("        LAYER 7  METHODS           ", colors=["#FF00FF","#00FFFF"]))
    print(grad.text("╚══════════════════════════════════╝", colors=["#00FFFF","#FF00FF"]))
    print()

    print(grad.text("[1] TLS", colors=["#00FFFF", "#FF00FF"]))
    print(grad.text("[2] BYPASS", colors=["#00FFFF", "#FF00FF"]))
    print(grad.text("[3] TLS1", colors=["#00FFFF", "#FF00FF"]))
    print(grad.text("[4] KILL", colors=["#00FFFF", "#FF00FF"]))
    print(grad.text("[5] HIGH", colors=["#00FFFF", "#FF00FF"]))
    print(grad.text("[0] BACK", colors=["#FF0000", "#FF9900"]))

    print()

    choice = input(grad.text(f"{name}@Layer7:~# ", colors=["#00FFFF","#FF00FF"]))

    methods_dict = {
        "1": "tls",
        "2": "bypass",
        "3": "tls1",
        "4": "kill",
        "5": "high"
    }

    if choice in methods_dict:
        method = methods_dict[choice]
        os.system(f"node {method}.js")
    elif choice == "0":
        main()
    else:
        print(grad.text("Invalid choice! Try again...", colors=["#FF0000", "#FF6600"]))
        time.sleep(1)
        layer7_menu()

# ============================================================

def main():
    menu()
    while True:
        cnc = input(f"\x1b[1;37m{name}@\x1b[38;5;55mAdmin\x1b[1;37m:~# ")
        if cnc.lower() in ["methods", "method"]:
            layer7_menu()                
        elif cnc.lower() in ["clear", "cls"]:
            main()
        elif cnc.lower() == "help":
            help()
        else:
            try:
                cmmnd = cnc.split()[0]
                os.system("clear")
                menu()
            except IndexError:
                pass

def login():
    clear()
    user = "PhuVanDuc"
    passwd = "MikuC2"
    username = input("Username: ")
    password = getpass.getpass(prompt='Password: ')
    if username != user or password != passwd:
        print("\nFail")
        sys.exit(1)
    elif username == user and password == passwd:
        print("Welcome To MikuC2")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
