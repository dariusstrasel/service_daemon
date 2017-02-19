"""
This module contains utility functions for validating user input to the service daemon.
"""

import re


def valid_date(input_time):
    time_regex = re.compile(r"^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$")
    if time_regex.match(str(input_time)):
        return True
    return False


def input_is_valid(inputs, frequency_values):
    print("Inputs: %s, Length: %s" % (inputs, len(inputs)))
    if len(inputs) == 3:
        if inputs[1].lower() in frequency_values.keys():
            print(inputs[1])
            if valid_date(inputs[2]):
                print(inputs[2])
                return True
            print("Time input (%s) is not valid date. Please enter as: HH:MM" % inputs[2])
            return False
        print("Frequency value not accepted. Please pass one of the following: %s" % ([key for key in frequency_values.keys()]))
        return False
    print("Too few, or too many arguments. Must be three.")
    return False

if __name__ == "__name__":
    pass
