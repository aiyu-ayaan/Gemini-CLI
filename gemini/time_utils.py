import time
from datetime import datetime


def get_time_in_millis():
    return int(time.time() * 1000)


def get_formatted_time():
    return datetime.now().strftime('%d %B %Y %I:%M:%S %p')
