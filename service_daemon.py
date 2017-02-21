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
import argparse
from input_validator import *

FREQUENCY_VALUES = {'daily': 24, 'hourly': 1}


def sleep_until_hour(hour, minute):
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, t.day, hour, minute)
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

def argument_parser():
    parser = argparse.ArgumentParser(prog='service_daemon', description='Start a service instance.')
    parser.add_argument('frequency', metavar='frequency', type=str, choices=["daily", "hourly"],
                        help='Frequency that the %(prog)s service will cycle. [daily, or hourly]')
    parser.add_argument('-t', metavar='--time', type=int,required=False,
                        help='integer representing the start hour for the %(prog)s service-daemon lifecycle.')
    args = parser.parse_args()
    if args:
        return vars(args)
    # print(vars(args)["frequency"])

def main():
    valid_argument_values = argument_parser()
    if valid_argument_values:
        print("Success")
        print(valid_argument_values)
    else:
        print("False")


if __name__ == "__main__":
    main()
