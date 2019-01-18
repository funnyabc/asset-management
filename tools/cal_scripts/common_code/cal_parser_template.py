#!/usr/bin/env python3
'''
Common code shared between the different parsers in this file. Includes a
Calibration object that defines some default fields and functions.
Also includes a function to parse through a csv that shows the link
between serial numbers and UIDs.
'''
import csv
import datetime
import os
import sqlite3
import time


class Calibration(object):
    """Template for a calibration object that can be used as a base for


    Attributes:
        asset_tracking_number (str): Asset UID
        serial (str): Serial number associated with the instrument
        date (datetime): Date when the calibration was performed
        coefficients (dict): Dictionary containing all the relevant coefficients
                             associated with the instrument. These values will
                             be written to the appropriate CSV file.
        type (str): the type of instrument the calibration file is for.

    """
    def __init__(self):
        """Initializes the Calibration Class."""
        self.asset_tracking_number = None
        self.serial = None
        self.date = None
        self.coefficients = {}
        self.type = None

    def write_cal_info(self):
        """Writes data to a CSV file in the format defined by OOI integration"""
        if not self.get_uid():
            return
        complete_path = os.path.join(os.path.realpath('../..'), 'calibration',
                                     self.type)
        file_name = self.asset_tracking_number + '__' + self.date
        with open(os.path.join(complete_path, '%s.csv' % file_name),
                  'w') as info:
            writer = csv.writer(info)
            writer.writerow(['serial','name', 'value', 'notes'])
            for each in sorted(self.coefficients.items()):
                row = [self.serial] + list(each)
                row.append('')
                writer.writerow(row)

    def move_to_archive(self, inst_type, file):
        """Moves parsed calibration file to the manufacturer_ARCHIVE
           directory.

        Args:
            inst_type (str): type of instrument that indicates which folder to
                             move in the calibration directory.
            file (str): name of the file to move

        """
        os.rename(os.path.join(os.getcwd(), inst_type, 'manufacturer', file), \
                    os.path.join(os.getcwd(), inst_type,
                                 'manufacturer_ARCHIVE', file))

    def get_uid(self):
        sql = sqlite3.connect('instrumentLookUp.db')
        uid_query_result = sql.execute('select uid from instrument_lookup'
                                       'where serial=:sn',\
                                       {'sn':self.serial}).fetchone()
        if len(uid_query_result) != 1:
            return False
        self.asset_tracking_number = uid_query_result[0]
        return True

def get_uid_serial_mapping(csv_name):
    lookup = {}
    with open(csv_name, 'rb') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            lookup[row['serial']] = row['uid']
    return lookup
