#!/usr/bin/env python3
# you should chmod this file before using run.py --> chmod +x Cron_job.py
# this file is created to create a log file to track the cron job progress
# to do the cron job to run every 5 minutes
# 1- type in terminal --> crontab -e
# 2- choose the editor you prefer
# 3- type --> */5 * * * * python3 /home/ubuntu/RCP-Corum/src/run.py
# 4- save and exit
import logging
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, 'Cron_job.log')
# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

def do_logging():
    logger.info("Web Scraping and Data Cleaning is Done")


if __name__ == '__main__':
    do_logging()