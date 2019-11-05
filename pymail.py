# Omar Garcia
# Santa Clara University

import smtplib, poplib, ssl
import subprocess
import getpass
from os import system


def send(email_address):
    receiver_email = input("Please enter receiver's email address: ")
    smtp_server.sendmail(email_address, receiver_email, "SUBJECT: Test\nHi from me!\n")

def read():
    pass

_ = system("clear")

print("- * - * - * P y m a i l * - * - * -")
print("Welcome to the Python Gmail client!")

smtp_port = 465 # with SSL
pop3_port = 995 # with SSL

email_address = input("Please enter your email address: ") # converted raw_input to input
password = getpass.getpass("Please enter your password: ")


print('\nInitializing mail server...')
# STUDENT WORK
smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', smtp_port)
pop3_server = poplib.POP3_SSL('pop.gmail.com', pop3_port)
smtp_server.ehlo()

smtp_server.login(email_address, password)
print("smtp login successful!")
pop3_server.user(email_address)
pop3_server.pass_(password)
print("pop3 login successful!")

status = pop3_server.stat()
print(status)
print(pop3_server.list())

smtp_server.quit()
pop3_server.quit()