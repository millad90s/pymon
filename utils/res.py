import psutil
import smtplib
import os 
import time
import logging
# import settings
from dotenv import load_dotenv
load_dotenv()

# env_reader = settings.EnvReader()

class RAMUsageMonitor:
    def __init__(self, warning, threshold):
        self.threshold = threshold
        self.warning = warning
        
    def check_ram_usage(self):
        ram_usage = psutil.virtual_memory().percent
        return ram_usage
    
    def is_thresould_exceeded(self):
        if self.check_ram_usage() > self.threshold:
            return True
        else:
            return False
        
    def is_warning_exceeded(self):
        if self.check_ram_usage() > self.warning:
            return True
        else:
            return False
    
    
class CPUUsageMonitor:
    def __init__(self,warning, threshold):
        self.threshold = threshold
        self.warning = warning
        self.cpu_usage = 0
        self.last_update = time.time()
        
    ### cpu usage func return a float between 0 and 100
    def check_cpu_usage(self, interval=1):
        """
        Check the current CPU usage percentage.

        Returns:
            float: The CPU usage as a percentage between WARNINGF and THRESHOLD.
        """
        current_time = time.time()
        if current_time - self.last_update >= interval:
            self.cpu_usage = psutil.cpu_percent(interval=1)
            self.last_update = current_time
            logging.info(f"CPU usage is {self.cpu_usage}%")
        return self.cpu_usage

    def is_thresould_exceeded(self):
        """
        Check if the current CPU usage exceeds the threshold.

        Returns:
            bool: True if the current CPU usage exceeds the threshold, False otherwise.
        """
        if self.cpu_usage > self.threshold:
            return True
        else:
            return False
            

    def is_warning_exceeded(self):
        """
        Check if the current CPU usage exceeds the warning threshold.

        Returns:
            bool: True if the current CPU usage exceeds the warning threshold, False otherwise.
        """
        if self.cpu_usage > self.warning:
            return True
        else:
            return False

if __name__ == '__main__':
    # send_email()
    pass

