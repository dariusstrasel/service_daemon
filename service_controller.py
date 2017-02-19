"""
Title: Service Watcher
Author: Darius Strasel
Objective: Control the execution of a Python package by
passing in user input for frequency, and start time.

i.e

start package

"""

from sys import argv
import re

def valid_date(input_time):
    time_regex = re.compile(r"^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$")
    return time_regex.match(input_time)

def input_is_valid(inputs):
    print("Inputs: %s, Length: %s" % (inputs, len(inputs)))
    frequency_values = ['daily', 'hourly']
    if len(inputs) == 3:
        if inputs[1].lower() in frequency_values:
            print(inputs[1])
            if valid_date(inputs[2]):
                print(inputs[2])
                return True
            print("Time input (%s) is not valid date. Please enter as: HH:MM" % inputs[2])
            return False
        print("Frequency value not accepted. Please pass one of the following: %s, %s" % (frequency_values[0], frequency_values[1]))
        return False
    print("Too few, or too many arguments. Must be three.")
    return False


def main():
    module_arguments = argv
    if input_is_valid(module_arguments):
        print('Input Success.')
    else:
        print("Input Failed.")

if __name__ == "__main__":
    main()