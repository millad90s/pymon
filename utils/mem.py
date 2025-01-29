### lets monitor memory usage and send alert to email if it is higher than threshould 

import psutil
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

sender = os.getenv('sender')
password = os.getenv('password')
receiver = os.getenv('receiver')

RAM_THRESHOLD = 40

def check_ram_usage():
    ram_usage = psutil.virtual_memory().percent
    return ram_usage

def send_email(ram_usage, RAM_THRESHOLD):
    if ram_usage > RAM_THRESHOLD:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        subject = 'RAM usage is high'
        body = f'RAM usage is {ram_usage}%'
        msg = f'Subject: {subject}\n\n{body}'
        server.sendmail(sender, receiver, msg)
        server.quit()
        debug = f'Email sent to {receiver} with subject {subject} and body {body}'
        print(debug)

def slack_notification():
    pass

if __name__ == '__main__':
    send_email(check_ram_usage())