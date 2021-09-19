# Sending emails using python
# To create a python script that can send emails
# Topics: import packages, SMTP lib, sending a request to the server

import smtplib
import ssl
import getpass

smtp_server = "smtp.gmail.com"
port = 587    # for starttls
sender_email = "eddiebigdataengineer@gmail.com"
password = getpass.getpass(prompt="Type your password here and press enter: ", stream=None)    # input("Type your password here and press enter: ")
receiver_email = ["<CHANGE_ME>@gmail.com", "<CHANGE_ME>@hotmail.co.uk", "<CHANGE_ME>@hotmail.co.uk", "<CHANGE_ME>@gmail.com"]
message = """\nSubject: What's good bro? \n\nThis message is sent using Python."""

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send emails
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()    # can be omitted
    server.starttls(context=context)    # secure the connection
    server.ehlo()    # can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # print and error messages to stdout
    print(e)
finally:
    server.quit()
