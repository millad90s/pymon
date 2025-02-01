import utils.res
from utils.configReader import ConfigReader
from utils.settings import EnvReader
import yaml


if __name__ == "__main__":
    # Load configuration and environment variables
    config_reader = ConfigReader()
    env_reader = EnvReader()
    
    # Get environment variables
    sender = env_reader.get_var('sender')
    password = env_reader.get_var('password')
    receiver = env_reader.get_var('receiver')
    print(sender)
    print(receiver)
    
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
    