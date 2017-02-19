"""
Title: Service Daemon
Author: Darius Strasel
Objective: Create a background thread that controls the execution of a Python package by
passing in user input for frequency, and start time.

i.e

python service_daemon.py

TODO: Change hour to optional argument
TODO: Connect 'package' to main()
TODO: Review use cases for required and optional cases
TODO: Check Python-Loop-Command-Script for frequency logic
TODO: Review argparser docs for cleaning up utility code.

"""

from sys import argv
import time
import datetime
from input_validator import *

FREQUENCY_VALUES = {'daily': 24, 'hourly': 1}


def sleep_until_hour(hour, minute):
    t = datetime.datetime.today()
    future = datetime.datetime(t.year,t.month,t.day,hour,minute)
    if t.hour >= hour:
        future += datetime.timedelta(days=1)
    time.sleep((future-t).seconds)


def main_module():
    while True:
        try:
            print("Stuff")
            time.sleep(5)
        except KeyboardInterrupt:
            print("Exiting program.")
            exit()


def main():
    module_arguments = argv
    if input_is_valid(module_arguments, FREQUENCY_VALUES):
        print('Input Success.')
    else:
        print("Input Failed.")

if __name__ == "__main__":
    main()
