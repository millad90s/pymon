import os
from dotenv import load_dotenv

class EnvReader:
    def __init__(self, env_file_path='.env'):
        self.env_file_path = env_file_path
        load_dotenv(self.env_file_path)
        self.sender = os.getenv('sender')
        self.password = os.getenv('password')
        self.receiver = os.getenv('receiver')
        
    def get_var(self, var_name):
        return os.getenv(var_name)
    