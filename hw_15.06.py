from datetime import datetime, timedelta
import logging
from argparse import ArgumentParser
import os


logging.basicConfig(filename="errors.log", filemode="r+",
                    format="[%(asctime)s] - (%(message)s)",
                    datefmt="%d/%m/%y | %I:%M | %p")


# #2nd task
now = datetime.now()
birth_date = input("Enter friends birthday(format DD-MM-YYYY):")
comp_time = datetime.strptime(birth_date, "%d-%m-%Y")
# print(comp_time)
if now < comp_time < now + timedelta(weeks=1):
    print("Your friends birthday will be in a week")
else:
    print("Relax, dont worry about friends birtday")

# 3rd task [10/03/17 | 11:00 | AM] - (Some message here)
logging.critical("Critical error")
logging.info("Info message")
logging.warning("Warning message")

# 4th task
parser = ArgumentParser()
log_values = ["info", "warning", "debug", "error", "critical"]
parser.add_argument("-l", "-level", dest="level", help="Logging level.example:{}".format(log_values))
args = parser.parse_args()
log_level = args.level
if log_level not in log_values:
    print("Incorrect debug level!")
else:
    print("Chosen debug level is:", log_level.upper())

# numeric_level = getattr("logging", str(log_level), None)
# print(numeric_level)
# logging.basicConfig(level=numeric_level)

# Bonus #1
# "2017 06 16" to datetime.datetime and return 06/16/17
date_to_convert = input("Enter date(format YYYY MM DD:)")
date_converted = datetime.strptime(date_to_convert, "%Y %m %d")
print("Converted date is:", date_converted)
date_back_converted = date_converted.strftime("%m/%d/%y")
print("Back converted date is:", date_back_converted)

