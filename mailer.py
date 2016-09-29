# Author: Aditya Inapurapu 
# Site: http://www.iaditya.com

import weather
import mailer

def get_emails():
    # Get list of all emails
    emails = {}

    try:
        email_file = open('emails.txt', 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
            
    except FileNotFoundError as err:
        print(err)
    return emails

def get_schedule():
    # Get the schedule
import smtplib

def send_emails(emails, schedule, forecast):
    # Connect to SMTP server
    server = smtplib.SMTP('smtp.gmail.com', '587');

    # Start TLS encryption
    server.starttls()

    # Login
    from_email = input("What's your gmail id?")
    password = input("What's your password?")
    server.login(from_email, password)

    # Send to entire email list
    for to_email, name in emails.items():
        message = 'Subject: Welcome to the weathermail app.\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += schedule + '\n\n'
        message += 'Have a good day!\n\n'
        
        server.sendmail(from_email, to_email, message)
    server.quit()
