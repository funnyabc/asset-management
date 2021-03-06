#!/usr/bin/env python3
"""
NUTNR Calibration Parser
Create the necessary CI calibration ingest information from a NUTNR
calibration file.
"""

__author__ = "Daniel Tran"
__version__ = "0.1.0"
__license__ = "MIT"

import csv
import datetime
import json
import os
import time
from common_code.cal_parser_template import Calibration


class NUTNRCalibration(Calibration):
    """Calibration class for NUTNR instruments.
    
    Attributes:
        cal_temp (float): Temperature at which calibrations were performed.
        wavelengths (list): Wavelengths used during calibration.
        eno3 (list): NO3 concentrations at different calibration wavelengths.
        eswa (list): Salt water bins at different calibration wavelengths.
        di (list): DI water bins at different calibrations.
        lower_limit (int): lower wavelength bound. Default of 217 nm
        upper_limit (int): upper wavelength bound. Default of 240 nm
        coefficients (dict): Dictionary containing all the relevant coefficients
                             associated with the instrument. These values will
                             be written to the appropriate CSV file.

    """

    def __init__(self, lower=217, upper=240):
        """Initializes the NUTNRACalibration Class.

        Args:
            lower (str): lower wavelength bound. Default of 217 nm
            upper (str): upper wavelength bound. Default of 240 nm
        """

        super(NUTNRCalibration, self).__init__('NUTNRA')
        self.cal_temp = 0.0
        self.wavelengths = []
        self.eno3 = []
        self.eswa = []
        self.di = []
        self.lower_limit = lower
        self.upper_limit = upper
        self.coefficients = {
            'CC_lower_wavelength_limit_for_spectra_fit': self.lower_limit,
            'CC_upper_wavelength_limit_for_spectra_fit': self.upper_limit
        }

    def read_cal(self, filename):
        """Reads cal file and scrapes it for calibration values.

        Arguments:
            filename (str) -- path to the calibration file.
        """

        with open(filename) as fh:
            for line in fh:
                parts = line.split(',')

                if len(parts) < 2:
                    continue  # skip anything that is not key value paired
                record_type = parts[0]

                if record_type == 'H':
                    key_value = parts[1].split()
                    if len(key_value) == 2:
                        name, value = key_value
                        if name == 'T_CAL' or (name == 'T_CAL_SWA' and 'CC_cal_temp' not in self.coefficients):
                            self.cal_temp = float(value)
                            self.coefficients['CC_cal_temp'] = self.cal_temp
                    elif 'creation' in key_value:
                        cal_date = datetime.datetime.strptime(
                            key_value[-2], '%d-%b-%Y')
                        if not self.date or self.date < cal_date:
                            self.date = cal_date
                    elif 'SUNA' in key_value:
                        self.serial = str(key_value[1]).lstrip('0')

                elif record_type == 'E':
                    _, wavelength, eno3, eswa, _, di = parts
                    self.wavelengths.append(float(wavelength))
                    self.eno3.append(float(eno3))
                    self.eswa.append(float(eswa))
                    self.di.append(float(di))
                    self.coefficients['CC_wl'] = json.dumps(self.wavelengths)
                    self.coefficients['CC_eno3'] = json.dumps(self.eno3)
                    self.coefficients['CC_eswa'] = json.dumps(self.eswa)
                    self.coefficients['CC_di'] = json.dumps(self.di)
            fh.close()


def main():
    """ Main entry point of the app """

    for path, _, files in os.walk('NUTNRA/manufacturer'):
        for file in files:
            # Skip hidden files
            if file[0] == '.':
                continue
            cal = NUTNRCalibration()
            if not file.startswith('SNA'):
                continue
            cal.read_cal(os.path.join(path, file))
            cal.write_cal_info(os.path.join(path, file))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('NUTNR: %s seconds' % (time.time() - start_time))
