# Omar Garcia
# Santa Clara University

import smtplib, poplib, ssl
import subprocess
from os import system

_ = system.("clear")

print("- * - * - * P y m a i l * - * - * -")
print("Welcome to the Python Gmail client!")



port = 465  # For SSL
email_address = input("Please enter your email address: ") # converted raw_input to input
password = input("Please enter your password: ", )
receiver_email = input("Please enter receiver's email address: ")


print '\nNow contacting the mail server...'
# STUDENT WORK
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.ehlo()

server.login(email_address, password)

print '\nSending email...'


# STUDENT WORK
server.sendmail(email_address, receiver_email, "SUBJECT: Test\nHi from me!\n%s" % ping_response)

server.quit()