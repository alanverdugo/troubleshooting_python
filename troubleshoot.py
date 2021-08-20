#!/usr/bin/python
"""It is hard to fail, but it is worse never to have tried to succeed."""

# OS stuff
import os

# Log stuff
import logging

# Our utilities
from utilities import generic

# Data wrangling
import pandas as pd

# HTTP requests
import requests

# Missing requirement (ModuleNotFound error)
import xyz


def first():
    """Fail miserably doing several things."""
    # Fail by trying to use a missing object (NameError).
    LOGGER.info("This is a very mysterious object: {:s}".format(str(mystery)))

    # Let's read some long stack trace (by failing to connect to a server).
    # (requests.exceptions.ConnectionError)
    _ = requests.get('https://fail.host', auth=('user', 'pass'))

    # Execute the "second" function.
    second()

    # If we are here, it means it all works.
    LOGGER.info("The program finished succesfully!")


def second():
    """Fail miserably trying to do other things."""
    failed_dict = {"A": 1,
                   "B": 2,
                   "C": 3}

    # Let's try to access a un-existing key (KeyError).
    LOGGER.info("This is the D key: {:d}".format(failed_dict["D"]))

    # Let's access data that does not exist in a list or tuple (IndexError)
    rip_list = ("Ivan", "Rogelio", "Alan")
    LOGGER.info("This is the fourth Ex-IBMer: {:s}".format(rip_list[3]))

    # Let's try to use an un-existing attribute (AttributeError)
    weird_dataframe = {"source_system_interaction_key": "",
                       "customer_name": ""}
    LOGGER.info("These are the dataframe's columns: {:s}".format(
        str(", ".join(weird_dataframe.columns))))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    LOGGER = logging.getLogger("Troubleshooting!")
    # Execute the first function.
    first()
