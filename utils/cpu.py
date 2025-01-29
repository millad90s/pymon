import psutil
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

sender = os.getenv('sender')
password = os.getenv('password')
receiver = os.getenv('receiver')

CPU_THRESHOLD = 4

## check cpu usage
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage


## send email
def send_email():
    cpu_usage = check_cpu_usage()
    if cpu_usage > CPU_THRESHOLD:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        subject = 'CPU usage is high'
        body = f'CPU usage is {cpu_usage}%'
        msg = f'Subject: {subject}\n\n{body}'
        server.sendmail(sender, receiver, msg)
        server.quit()
        debug = f'Email sent to {receiver} with subject {subject} and body {body}'
        print(debug)
        

if __name__ == '__main__':
    send_email()