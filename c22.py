# VIETNAM SỜ CU RI TY
import socket
import os
import requests
import random
import getpass
import time
import sys

# Hàm neon màu cầu vồng
def neon(text):
    colors = [31, 32, 33, 34, 35, 36, 91, 92, 93, 94, 95, 96]  # ANSI colors
    result = ""
    for char in text:
        if char.strip() == "":
            result += char
        else:
            result += f"\x1b[1;{random.choice(colors)}m{char}\x1b[0m"
    return result

name = input(neon("UserName:"))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ascii_vro():
    clear()
    print(neon('''
   '''))
    clear()

def banners():
    clear()
    print(neon("""
METHODS
CLEAR 
"""))

def meth():
    print(neon('''
HTTP-BROWSER    [URL]    [PORT]    [TIME]
HTTP-SPAM       [URL]    [PORT]    [TIME]
HTTP-KILLER     [URL]    [PORT]    [TIME]
HTTP-GET        [URL]    [PORT]    [TIME]
HTTP-MERIS      [URL]    [PORT]    [TIME]
CLOUDFLARE      [URL]    [PORT]    [TIME]
HTTP-BYPASS     [URL]    [PORT]    [TIME]
HTTP-FLOOD      [URL]    [PORT]    [TIME]
'''))

def menu():
    os.system("clear")
    print(neon("""
                        ╔╦╗ ╦ ╦╔═ ╦ ╦
                        ║║║ ║ ╠╩╗ ║ ║
                        ╩ ╩ ╩ ╩ ╚═╚═╝
                  -Best C2 In the Year 2024-
             ╚═╦═══════════════════╦═╝       
          ╚╦═══╩═══════════════════╩═══╦╝
    ╚╦═════╩══════════════════════════╩══════╦╝
     ║        -Welcome To MikuC2 Made By VanDuc-        ║
     ║             -Powerful Layer7 Bypasser-           ║        
    ╔╩═╦══════════════════════════════════════╦═╩╗
       ║            -PhuVanDuc X Miku C2-             ║
      ╔╩══════════════════════════════════════╩╗
      ║  _Copyright © 2024 Miku C2 All Right Reserved_ ║
     ╔╩══════════════════════════════════════╩╗
"""))

def main():
    menu()
    while True:
        cnc = input(neon(f"{name}@Admin:~# "))
        if cnc.lower() in ["methods", "method"]:
            meth()
        elif cnc.lower() in ["clear", "cls"]:
            main()
        elif cnc.lower() == "help":
            help()
        
        # LAYER 7 METHODS
        elif "HTTP-BROWSER" in cnc.upper():
            try:
                url, port, duration = cnc.split()[1:4]
                clear()
                print(neon(f"""
Target      × [{url}]
Port        × [{port}]
Duration    × [{duration}]
Method      × [HTTP-BROWSER]
User        × [{name}]
Vip         × [TRUE]
ADMIN       × [PhuVanDuc]
Plan        × [SLIVER X VIP]
"""))
            except IndexError:
                menu()
        
        elif "HTTP-KILLER" in cnc.upper():
            try:
                url, port, duration = cnc.split()[1:4]
                clear()
                print(neon(f"""
Target      × [{url}]
Port        × [{port}]
Duration    × [{duration}]
Method      × [HTTP-KILLER]
User        × [{name}]
Vip         × [TRUE]
ADMIN       × [PhuVanDuc]
Plan        × [SLIVER X VIP]
"""))
            except IndexError:
                menu()
        
        elif "HTTP-SPAM" in cnc.upper():
            try:
                url, port, duration = cnc.split()[1:4]
                clear()
                print(neon(f"""
Target      × [{url}]
Port        × [{port}]
Duration    × [{duration}]
Method      × [HTTP-SPAM]
User        × [{name}]
Vip         × [TRUE]
ADMIN       × [PhuVanDuc]
Plan        × [SLIVER X VIP]
"""))
            except IndexError:
                menu()
        
        elif "HTTP-GET" in cnc.upper():
            try:
                url, port, duration = cnc.split()[1:4]
                clear()
                print(neon(f"""
Target      × [{url}]
Port        × [{port}]
Duration    × [{duration}]
Method      × [HTTP-GET]
User        × [{name}]
Vip         × [TRUE]
ADMIN       × [PhuVanDuc]
Plan        × [SLIVER X VIP]
"""))
            except IndexError:
                menu()
        
        elif "CLOUDFLARE" in cnc.upper():
            try:
                url, port, duration = cnc.split()[1:4]
                clear()
                print(neon(f"""
Target      × [{url}]
Port        × [{port}]
Duration    × [{duration}]
Method      × [CLOUDFLARE]
User        × [{name}]
Vip         × [TRUE]
ADMIN       × [PhuVanDuc]
Plan        × [SLIVER X VIP]
"""))
            except IndexError:
                menu()
        
        elif "HTTP-MERIS" in cnc.upper():
            try:
                url, port, duration = cnc.split()[1:4]
                clear()
                print(neon(f"""
Target      × [{url}]
Port        × [{port}]
Duration    × [{duration}]
Method      × [HTTP-MERIS]
User        × [{name}]
Vip         × [TRUE]
ADMIN       × [PhuVanDuc]
Plan        × [SLIVER X VIP]
"""))
            except IndexError:
                menu()
        
        elif "HTTP-FLOOD" in cnc.upper():
            try:
                url, port, duration = cnc.split()[1:4]
                clear()
                print(neon(f"""
Target      × [{url}]
Port        × [{port}]
Duration    × [{duration}]
Method      × [HTTP-FLOOD]
User        × [{name}]
Vip         × [TRUE]
ADMIN       × [PhuVanDuc]
Plan        × [SLIVER X VIP]
"""))
            except IndexError:
                menu()
        
        elif "HTTP-BYPASS" in cnc.upper():
            try:
                url, port, duration = cnc.split()[1:4]
                clear()
                print(neon(f"""
Target      × [{url}]
Port        × [{port}]
Duration    × [{duration}]
Method      × [HTTP-BYPASS]
User        × [{name}]
Vip         × [TRUE]
ADMIN       × [PhuVanDuc]
Plan        × [SLIVER X VIP]
"""))
            except IndexError:
                menu()
        
        else:
            try:
                _ = cnc.split()[0]
                clear()
                menu()
            except IndexError:
                pass

def login():
    clear()
    user = "PhuVanDuc"
    passwd = "MikuC2"
    username = input(neon("Username: "))
    password = getpass.getpass(prompt=neon('Password: '))
    if username != user or password != passwd:
        print(neon("\nFail"))
        sys.exit(1)
    elif username == user and password == passwd:
        print(neon("Welcome To MikuC2"))
        time.sleep(0.3)
        ascii_vro()
        main()

login()
