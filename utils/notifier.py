
import logging
import smtplib
import requests

class EmailNotifier:
    def __init__(self, sender, password, receiver):
        self.sender = sender
        self.password = password
        self.receiver = receiver
        logging.debug(f"Email notifier initialized with sender: {sender}, receiver: {receiver}, password: {password}")
        
    def send_email(self, subject, body):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(self.sender, self.password)
            msg = f'Subject: {subject}\n\n{body}'
            server.sendmail(self.sender, self.receiver, msg)
            server.quit()
            logging.info(f"Email sent to {self.receiver} with subject {subject} and body {body}")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")
            


class SlackNotifier:
    def __init__(self, webhook_url, channel, username):
        self.webhook_url = webhook_url
        self.channel = channel
        self.username = username

    def send_notification(self, message):
        payload = {
            "channel": self.channel,
            "username": self.username,
            "text": message
        }
        response = requests.post(self.webhook_url, json=payload)
        if response.status_code != 200:
            raise Exception(f"Failed to send notification to Slack: {response.text}")

    def send_cpu_usage_notification(self, cpu_usage):
        message = f"CPU usage is {cpu_usage}%"
        self.send_notification(message)