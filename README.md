# scheduleAppiePy
quick little python testfile for logging in and obtaining the schedule of AH employees. Meant to give insight to the AH login and schedule requests, will be used in a React Native app later.

## Usage
example: 
`python3 main.py  --username "pnlxxxxx" --password "qwerty123456" `

### required parameters:
parameter name    | explaination
-------------     | -------------
username          | the full username. Usually something along the lines of pnlxxxxx
password          | The password (case and space sensitive!).


### optional parameters:
parameter name  | explaination
------------- | -------------
verbose       | getting a verbose output. Default is false
logFile       | the path to the log file. If not declared, no log file will be created
scheduleJsonFile  | the output for the json schedule data output. If not declared, the default id `output.json`
