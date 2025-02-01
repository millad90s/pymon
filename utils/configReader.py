import os 
import yaml

class ConfigReader:
    def __init__(self, config_file_path='config.yaml'):
        self.config_file_path = config_file_path
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    
    def get_config(self, path):
        keys = path.split('.')
        config = self.config
        for k in keys:
            config = config.get(k, {})
        return config