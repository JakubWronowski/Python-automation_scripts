''' Monitors and writes logs of the machine on which it's running '''

import psutil
import time
import logging


logging.basicConfig(filename='cpu_usage.log', level=logging.INFO, format='%(asctime)s: %(message)s')

def log_cpu_usage(interval=1):
    """Log CPU usage every interval seconds."""
    while True:
        cpu_usage = psutil.cpu_percent(interval)
        logging.info(f'CPU usage: {cpu_usage}%')
        time.sleep(interval)

if __name__ == "__main__":
    log_cpu_usage()


### Remeber it's not in the best practices to create infinite loop for logging because it will grow indefinitely. It's only for trainnig purposes :) ###
