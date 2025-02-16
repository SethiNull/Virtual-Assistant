import datetime
import pyfiglet
from colorama import Fore, Back, Style, init 
import os
import webbrowser
import psutil
import subprocess
import requests
import json
import pyjokes

init(autoreset=True)

def execute_command(command):
    if 'help' in command:
        print(Fore.YELLOW+"""
    -------------------------------------------
    1) help : Show Possible Commands.
    2) time : Show Current Time.
    3) open notepad : Open the notepad.
    4) open calc : Open calculator.
    5) open google : Open Google.com in browser.
    6) oopen youtube : Open YouTube in browser.
    7) open gmail : Open Gmail in browser.   
    8) search google <query> : Search Directly in web. 
    9) system info : Show the system info like CPU, Memory Usage, etc.      
    10) open whatsapp : Start WhatsApp application.
    11) show public ip : Show your public IP.
    12) ip info <public ip> : Show information about a Public IP.
    -------------------------------------------
    """)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M:%p")
        print(Fore.GREEN+"Current Time is", current_time)
    
    elif 'open notepad' in command:
        print(Fore.CYAN+"Opening Notepad...")
        os.system("notepad")
    
    elif 'open calc' in command:
        print(Fore.CYAN+"Opening Calculator...")
        os.system("calc")
    elif 'open google' in command:
        print(Fore.CYAN+"Opening Google....")
        webbrowser.open('https://google.com')

    elif 'open youtube' in command:
        print(Fore.CYAN+"Opening YouTube...")
        webbrowser.open('https://youtube.com')
    
    elif 'open gmail' in command:
        print(Fore.CYAN+"Opening Gmail...")
        webbrowser.open('https://gmail.com')
    elif 'search google' in command:
        query = command.replace('search google',"")
        if query.strip():
            print(Fore.CYAN+"Searching google for:",query)
            webbrowser.open("https://www.google.com/search?q="+query)
        else:
            print(Fore.RED+"Please provide a search query")
    
    elif 'system info' in command:
        print(Fore.GREEN+"Getting System Info....")
        print(Fore.YELLOW+"CPU usage:",psutil.cpu_percent(),"%")
        print(Fore.YELLOW+"Memory usage:",psutil.virtual_memory().percent,"%")
        print(Fore.YELLOW+"Disk usage:",psutil.disk_usage('/').percent,"%\n")

    elif 'open whatsapp' in command:
        print(Fore.CYAN + "Opening WhatsApp...")
        subprocess.run([
        r"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2506.4.0_x64__cv1g1gvanyjgm\WhatsApp.exe"
    ], shell=True)   

    elif 'show public ip' in command:
        response = requests.get("https://api.ipify.org?format=text")
        if response.status_code == 200:
            print(Fore.GREEN+"Your Public IP:",response.text.strip())
        else:
            print(Fore.RED+"Failed to get public IP, Check Internet Connection!!")    

    elif 'ip info' in command:
        ip = command.replace('ip info',"").strip()
        if ip:
            response = requests.get("https://ipinfo.io/"+ip.strip()+"/json")
            if response.status_code == 200:
                data = response.json()
                print(Fore.GREEN+"\nInformation for IP:",ip.strip(),"\n")
                print(Fore.YELLOW+"IP          :",data.get('ip'))
                print(Fore.YELLOW+"Hostname    :",data.get('hostname','N/A'))
                print(Fore.YELLOW+"Region      :",data.get('region','N/A'))
                print(Fore.YELLOW+"City        :",data.get('city','N/A'))
                print(Fore.YELLOW+"Country     :",data.get('country','N/A'))
                print(Fore.YELLOW+"Organisation:",data.get('org','N/A'))
            else:
                print(Fore.RED+"Failed to fetch information for IP",ip.strip())
    
    elif 'tell me a joke' in command:
        print(Fore.YELLOW+pyjokes.get_joke())
    
    elif 'exit' in command:
        print(Fore.MAGENTA+"\nGoodBye Sir!!")
        return False
    else:
        print(Fore.RED+"Sorry, I don't understand that command yet!!")
    
    return True



def greet():
    hour = datetime.datetime.now().hour
    if hour<12:
        print(Fore.GREEN+"Good Morning!")
    elif hour<18:
        print(Fore.MAGENTA+"Good Afternoon!")
    else:
        print(Fore.LIGHTBLUE_EX+"Good Evening!")

    print(Fore.BLUE+"Welcome Aditya-sama, How can I help you?")

ascii_art = pyfiglet.figlet_format("S.O.L.I.S",font="slant")
print(Fore.WHITE+"Created by Aditya")
print(Fore.RED+ascii_art)

greet()

try:
    while True:
        command = input(Fore.CYAN+"Enter your Command: ").lower()
        if not execute_command(command):
            break
except KeyboardInterrupt:
    print(Fore.LIGHTMAGENTA_EX+"\nGoodbye Sir!")
