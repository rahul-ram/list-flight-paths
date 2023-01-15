## Graph based implementation to find paths between nodes.

## setup 

Tested on Windows Subsystem for Linux (`Ubuntu version 2`) with python 3.10.6

`sudo apt-get install python-virtualenv`
### To install pip
1. `sudo apt update`
2. `sudo apt install python3-pip`

### Clone repository

1) `git clone https://github.com/rahul-ram/list-flight-paths.git`
2) `cd list-flight-paths`
3) `virtualenv venv`
4) `. venv/bin/activate`
5) `pip install click`
6) `pip install --editable .` or `pip install --editable .`

### To run 
1) `cd venv`
2) `./bin/list-flight-paths "Castle Black" "Riverrun"`

    ### or
    run `./venv/bin/list-flight-paths "Castle Black" "Riverrun"` from project root folder

## To test for different costs matrix
Edit `data.json` and update `costs` and `nodes`

### Run unittests
`cd list-flight-paths`

`python -m unittest discover tests/`

