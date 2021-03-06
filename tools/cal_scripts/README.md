# OOI Instrument Parsers

 The following scripts extract calibration information from various manufacturer calibration sheets. These calibration sheets define the values that various instruments use to calibrate themselves for data acquisition.
 These scripts automatically creates of calibration files in the format requested by ooi-integration.
 Serial numbers and asset tracking numbers can be found in the [sensor bulk file](
https://github.com/funnyabc/asset-management/blob/master/bulk/sensor_bulk_load-AssetRecord.csv) in the root repository.

The scripts currently support the creation of the following instrument types:

* CTD
* DOFSTA
* FLCDRA
* FLNTUA
* FLOR
* NUTNR
* OPTAA
* SPKIR

There is potential to create more scripts for more instruments, so feel free to contribute to this page.

These scripts are based on those written by Dan Mergens, who developed the original scripts which can still be found in the [ooi-tools](https://github.com/oceanobservatories/ooi-tools/tree/master/instrument/calibration) repository.

## Getting Started

Clone the repository into your local machine. In the repository, there are a set of directories of each of the supported instrument types. Navigate to the repository in your preferred terminal or a file explorer system. There are a series of folders which contain the parsers and subdirectories containing manufacturer calibration files and completed csv files. Put the manufacturer calibration files in the "manufacturer" directory. The parsers will search for the files in this folder while it is running.

## File Structure

    .
    ├── common_code             # Common code shared among all parsers
    # This section is where instrument calibration sheets from manufacturers
    should be placed so the script knows where to look for sheets. Place them
    in the appropriate calibration directory.
    ├── CTD                       
    |   ├── manufacturer        # Place manufaturer calibration files here to be scripted   
    ├── FLCDRA                    
    |   ├── manufacturer        # Place manufaturer calibration files here to be scripted   
    ├── FLNTUA                    
    |   ├── manufacturer        # Place manufaturer calibration files here to be scripted   
    ├── FLOR                      
    |   ├── manufacturer        # Place manufaturer calibration files here to be scripted   
    ├── NUTNRA
    |   ├── manufacturer        # Place manufaturer calibration files here to be scripted   
    ├── OPTAA
    |   ├── manufacturer        # Place manufaturer calibration files here to be scripted   
    ├── PARADA
    |   ├── manufacturer        # Place manufaturer calibration files here to be scripted   
    ├── SPKIRA
    |   ├── manufacturer        # Place manufaturer calibration files here to be scripted   
    ├── ctd_cal_parser.py       # Script that parses CTD calibration files
    ├── dofsta_cal_parser.py    # Script that parses DOFSTA calibration files
    ├── flcdra_cal_parser.py    # Script that parses FLCDRA calibration files
    ├── flntua_cal_parser.py    # Script that parses FLNTUA calibration files
    ├── flor_cal_parser.py      # Script that parses FLOR calibrations files
    ├── nutnr_cal_parser.py     # Script that parses NUTNR calibration files
    ├── optaa_cal_parser.py     # Script that parses OPTAA calibration files
    ├── parada_cal_parser.py    # Script that parses PARADA calibrations files
    ├── spkira_cal_parser.py    # Script that parses SPKIRA calibrations files
    ├── instrumentLookUp.db     # Lookup table in db mapping serial numbers to ASSET_UIDs
    └── README.md

### Prerequisites

* Python 3.x
* Linux terminal emulator

If you do not already have Python installed on your computer, you will need to install it to make this program work.
On Linux, run the following command.

```bash
sudo apt-get install python3.x
```

On MacOS, if you have Homebrew, call this command

```bash
brew install python3.x
```

On Windows, install Cygwin or preferred terminal emulator. Make sure to select Python as part of the installation process.
Another method is to use the Linux Subsystem available on Windows 10.

If you need any packages needed in these files, you can use pip to help you install them.

On Linux, run the following command.

```bash
sudo apt-get install python-pip
```

On MacOS, if you have Homebrew, call this command

```bash
brew install pip
```

Otherwise, use this command in your terminal:

```bash
sudo easy_install pip
```

To install a package, simply call the command in this format:

```bash
pip install <package>
```

## Running the code
First place the calibration files in their designated directories under the manufacturer directory. You may need to create a new manufacturer folder to hold it. After performing this step, you can run the script by simply calling it.

To run the script, call it in this format.

```bash
python3 script_name.py
```

If there are multiple versions of Python on your system, such as Python 2, you may have to invoke the name of that version when calling the script.

```bash
python3 script_name.py
```

You can run each of the scripts individually by calling the corresponding parser.

``` bash
python3 ctd_cal_parser.py
python3 dofsta_cal_parser.py
python3 flcdra_cal_parser.py
python3 flntua_cal_parser.py
python3 flor_cal_parser.py
python3 nutnr_cal_parser.py
python3 optaa_cal_parser.py
python3 spkir_cal_parser.py
```

The parsers will go through each file and add the completed files into their respective calibration files in asset-management.

<!-- To run all scripts, call the script run_all_parsers.py:

```bash
python run_all_parsers.py
``` -->

## Authors

* **Dan Mergens** - *Initial work of writing the scripts* - [danmergens](https://github.com/danmergens)
* **Daniel Tran** - *Modifications of scripts and setup of the parser system* - [funnyabc](https://github.com/funnyabc)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Dan Mergens for starting the calibration scripts

Last updated 27th January 2019
