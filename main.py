import utils.res
import utils.notifier
import time
from utils.configReader import ConfigReader
from utils.settings import EnvReader
import yaml
import logging


if __name__ == "__main__":
    
    ### enable debug mode
    logging.basicConfig(level=logging.DEBUG)
    
    
    # Load configuration and environment variables
    config_reader = ConfigReader()
    env_reader = EnvReader()
    
    # Get environment variables
    sender = env_reader.get_var('sender')
    password = env_reader.get_var('password')
    receiver = env_reader.get_var('receiver')
    print(sender)
    print(receiver)
    print(password)
    print(type(password))
    
    # Get configuration and environment variables
    cpu_alert = config_reader.get_config('monitor.cpu.alert')
    cpu_interval = config_reader.get_config('monitor.cpu.INTERVAL')
    cpu_warning = config_reader.get_config('monitor.cpu.warning')
    cpu_theshold = config_reader.get_config('monitor.cpu.threshold')
    cpu_notification = config_reader.get_config('monitor.cpu.notification')
    
    print(cpu_alert)
    print(cpu_interval)
    print(cpu_warning)    
    print(cpu_theshold)
    print(cpu_notification)
    
    cpu = utils.res.CPUUsageMonitor(cpu_warning, cpu_theshold)
    while(True):
        logging.info("Checking CPU usage...")
        cpu.check_cpu_usage(cpu_interval)
        if cpu.is_warning_exceeded() and cpu_notification['email']:
            email_notifier = utils.notifier.EmailNotifier(sender, password, receiver)
            email_notifier.send_email("Warning: CPU usage is high", f"CPU usage is {cpu.cpu_usage}%")
        # if cpu.is_thresould_exceeded() and cpu_notification['slack']:
        #     slack_notifier = utils.res.SlackNotifier()
        #     slack_notifier.send_cpu_usage_notification(cpu.cpu_usage)
        time.sleep(2)