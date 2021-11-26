"""
Logging passed information to csv files format.

Author: Nicoline Louise Thomsen
"""

import csv
import datetime
import numpy as np

class Logger():

    def __init__(self):
        
        time = str(datetime.datetime.now())[11:19]
        dateid = time.replace(':', '')

        file_name = 'logs/data_' + dateid +'.csv'
        log = open(file_name, 'w+', newline='')  # w+ mode truncates (clears) the file (new file for every test)   
        
        self.logger = csv.writer(log, dialect = 'excel')

        self.logger.writerow('Time', 'Latitude', 'Longitude')


    def log_to_file(self, *data):

        row = [data]
        
        self.logger.writerow(row)
