# Omar Garcia
# Santa Clara University

import smtplib, imaplib, ssl
import subprocess
import email
import getpass
from os import system

def user_choice(options):
    while True:
        print("Please select an option: ")
        for index, elem in enumerate(options):
            print("(%d) %s" % (index + 1, elem))

        try:
            choice = int(input())
        except ValueError:
            print("Invalid option!")
            continue

        if 0 < choice <= len(options):
            return choice
        else:
            print("Invalid option!")
            continue
            

def main_menu(smtp, imap):
    quit = False
    
    while not quit:
        menu_options = ["read", "write", "quit"]
        cmd = user_choice(menu_options)

        if cmd == 1:
            print("entered read")
        elif cmd == 2:
            print("entered write")
        elif cmd == 3:
            print("quitting!")
            quit = True
            continue



def send_menu(email_address):
    back = False

    while not back:
        menu_options = ['']
    receiver_email = input("Please enter receiver's email address: ")
    smtp_server.sendmail(email_address, receiver_email, "SUBJECT: Test\nHi from me!\n")

def read_menu():
    pass

def main():
    _ = system("clear")

    print("- * - * - * P y m a i l * - * - * -")
    print("Welcome to the Python Gmail client!")

    smtp_port = 465 # with SSL
    imap_port = 993 # with SSL

    email_address = input("Please enter your email address: ") # converted raw_input to input
    password = getpass.getpass("Please enter your password: ")


    print('\nInitializing mail servers...')
    # STUDENT WORK
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', smtp_port)
    imap = imaplib.IMAP4_SSL('imap.gmail.com', imap_port)
    #smtp.ehlo()

    #smtp.login(email_address, password)
    print("smtp login successful!")
    #imap.login(email_address, password)
    print("imap login successful!")

    #result, entries = imap.list()

    #for entry in entries:
    #    print(entry)


    #imap.select("inbox")

    main_menu(smtp, imap)

    #smtp.quit()
    #imap.close(); imap.logout()

if __name__ == "__main__":
    main()
