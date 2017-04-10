"""
Title: Service Daemon
Author: Darius Strasel
Objective: Create a background thread that controls the execution of a Python package by
passing in user input for frequency, and start time.

i.e

python service_daemon.py hourly

python service_daemon.py -time 1:00 daily


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


def days_hours_minutes(td):
    return_data = [td.days, td.seconds//3600, (td.seconds//60) % 60]
    escaped_data = tuple([0 if item == -1 else item for item in return_data])
    return escaped_data


def sleep_until_hour(hour=None, minute=None, time_scope="hourly"):
    print("Hour: %s, Minute: %s, Time Scope: %s" % (hour, minute, time_scope))
    now = datetime.datetime.today()
    if not hour and not minute:
        print("No sleep time specified: defaulting to %s, plus frequency (%s)" % (now, time_scope))
        if time_scope == 'hourly':
            future = datetime.datetime(now.year, now.month, now.day, now.hour + 1, now.minute)
        elif time_scope == 'daily':
            future = datetime.datetime(now.year, now.month, now.day + 1, now.hour, now.minute)
        time_remaining = days_hours_minutes(future - now)
        print("Sleeping for %s days, %s hours, %s minutes." % (time_remaining[0], time_remaining[1], time_remaining[2]))
        time.sleep((future - now).seconds)

    future = datetime.datetime(now.year, now.month, now.day, hour, minute)
    delta = (future - now)
    time_remaining = days_hours_minutes(delta)
    if now.hour >= hour and time_scope == 'daily':
        future += datetime.timedelta(days=1)
    elif now.hour >= hour and time_scope == 'hourly':
        future += datetime.timedelta(days=1)
        delta = (future - now)
        print("Time scope is hourly, but time is not in the future.")
    print("Sleeping for %s days, %s hours, %s minutes." % (time_remaining[0],time_remaining[1], time_remaining[2]))
    time.sleep(delta.seconds)


def argument_parser():
    parser = argparse.ArgumentParser(prog='service_daemon', description='Start a service instance.')
    parser.add_argument('frequency', metavar='frequency', type=str, choices=["daily", "hourly"],
                        help='Frequency that the %(prog)s service will cycle. [daily, or hourly]')
    parser.add_argument('-time', metavar='--time', type=lambda d: datetime.datetime.strptime(d, '%H:%M'), required=False,
                        help='integer representing the start hour for the %(prog)s service-daemon lifecycle.')
    args = parser.parse_args()
    if args:
        return vars(args)

def main():
    valid_argument_values = argument_parser()
    if valid_argument_values:
        print("Success")
        print(valid_argument_values)
        if not valid_argument_values["time"]:
            sleep_until_hour(time_scope=valid_argument_values["frequency"])
        else:
            sleep_until_hour(valid_argument_values["time"].hour, valid_argument_values["time"].minute,
                             valid_argument_values["frequency"])
    else:
        print("False")


if __name__ == "__main__":
    main()
