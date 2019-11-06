# Omar Garcia
# Santa Clara University

import smtplib, imaplib, ssl
import subprocess, tempfile
import email
import getpass
import os

def call_editor(msg):
    # linked to vi
    (f_desc, path) = tempfile.mkstemp()
    f = os.fdopen(f_desc, 'w')
    f.write(msg)
    f.close()

    editor = os.getenv('EDITOR', 'vi')
    subprocess.call('%s %s' % (editor, path), shell=True)

    with open(path, 'r') as fp:
        new_msg = fp.read().rstrip('\n')

    os.unlink(path)
    return new_msg

def user_choice(options):
    while True:
        print("Please select: ")
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
            

def main_menu(smtp, imap, email_addr):
    done = False
    
    while not done:
        make_visual("Main Menu")

        menu_options = ["read", "send", "quit"]
        cmd = user_choice(menu_options)

        if cmd == 1:
            print("entered read")
        elif cmd == 2:
            print("entered send")
            send_menu(email_addr)
        elif cmd == 3:
            print("quitting!")
            done = True
            continue

def edit_recipients(addrs):    
    done = False

    while not done:
        make_visual("Editing Recipients")
        
        cmd = user_choice(addrs)
       
        if cmd < len(addrs) - 1:
            prompt = input("delete %s? [y/n]: " % addrs[cmd - 1])
            if prompt == 'y' or prompt == 'Y':
                # delete this email address
                pass
            elif prompt == 'n' or prompt == 'N':
                print("Not doing anything...")
            else:
                print("Invalid option! Not doing anything...")
        elif cmd == len(addrs) - 1:
            prompt = input("enter new address: ") #TODO: check if email valid
            new_addr = addrs.insert(len(addrs) - 2, prompt)
        elif cmd == len(addrs):
            done = True # quit here            

    return addrs[:2] # strip the (new) and (quit)

def send_menu(email_addr):
    done = False
    to_addr = []
    cc_addr = []
    bcc_addr = []
    msg = ""

    while not done:
        make_visual("Sending Mail")

        menu_options = ['edit TO: ', 'edit CC: ', 'edit BCC:', 'edit message content', 'quit']
        cmd = user_choice(menu_options)

        if cmd == 1:
            to_addr = edit_recipients(to_addr + ['add new +'] + ['quit'])
        elif cmd == 2:
            cc_addr = edit_recipients(cc_addr + ['add new +'] + ['quit'])
        elif cmd == 3: 
            bcc_addr = edit_recipients(bcc_addr + ['add new +'] + ['quit'])
        elif cmd == 4:
            msg = call_editor(msg)
        elif cmd == 5:
            done = True


            

    #receiver_email = input("Please enter receiver's email address: ")
    #smtp_server.sendmail(email_address, receiver_email, "SUBJECT: Test\nHi from me!\n")

def read_menu():
    pass

def make_visual(title):
    _ = os.system("clear")

    bar_length = len('* ' + title + ' *')

    print('*' * bar_length)
    print('* ' + title + ' *')
    print('*' * bar_length)
    print('\n')

def main():
    _ = os.system("clear")
    print("- * - * - * P y m a i l * - * - * -")
    print("Welcome to the Python Gmail client!")

    smtp_port = 465 # with SSL
    imap_port = 993 # with SSL

    email_addr = input("Please enter your email address: ") # converted raw_input to input
    password = getpass.getpass("Please enter your password: ")


    print('\nInitializing mail servers...')
    # STUDENT WORK
    smtp = 0
    imap = 0
    #smtp = smtplib.SMTP_SSL('smtp.gmail.com', smtp_port)
    #imap = imaplib.IMAP4_SSL('imap.gmail.com', imap_port)
    #smtp.ehlo()

    #smtp.login(email_address, password)
    print("smtp login successful!")
    #imap.login(email_address, password)
    print("imap login successful!")

    #result, entries = imap.list()

    #for entry in entries:
    #    print(entry)


    #imap.select("inbox")

    main_menu(smtp, imap, email_addr)

    #smtp.quit()
    #imap.close(); imap.logout()

if __name__ == "__main__":
    main()
