from utils.cpu import check_cpu_usage
import utils.mem
import yaml
print(check_cpu_usage())
print(utils.mem.check_ram_usage())

## TODO:
## 1- monitor cpu usage and send alert to email if it is higher than threshould
## 2- monitor memory usage and send alert to email if it is higher than threshould




def read_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

# # Example usage
config = read_config('config.yaml')
monitor_config = config['monitor']

for resource, settings in monitor_config.items():
    print(f"Monitoring {resource}:")
    print(f"  Threshold: {settings['threshold']}")
    print(f"  Alert: {settings['alert']}")
    print(f"  Warning: {settings['warning']}")
    print("  Notification:")
    print(f"    Email: {settings['notification']['email']}")
    print(f"    Slack: {settings['notification']['slack']}")