# W.A.B.O
Weather Alert Based Orchestration
<img src="./img/ablinkin.png" align="right"
     title="Ablinkin logo" width="125" height="125">

WABO is a tool designed to be a starting point for creating complex orchestrations
that are based on weather alerts. I started this project as a POC for my home lab.
The idea was to move my workload to the cloud when there are hurricane alerts in my area.

As time goes on I will add some orchestration examples and some location self awareness logic.


<p align="center">
  <img src="./img/getAlertExists.png" alt="WABO Example"
       width="700" height="350">
</p>

## Requirements:
* python 3.x
* requests
* urllib
* json

## How do I use it:
First, download `wabo`:

```sh
$ git clone https://github.com/ablinkinz/wabo.git
```
cd to the `wabo` directory:

```sh
$ cd wabo
```

open the python3 repl:
```sh
$ python3
```

import wabos alert module
```python
>>> import alerts
```

let's check to see if we have any current alerts in our area, in verbose mode
(make sure your .config/settings.json file is update for your state and zip)
```python
>>> alerts.getAlertExists(True)
```
<p align="center">
  <img src="./img/getAlertExistsVerbose.png" alt="WABO Example"
       width="700" height="350">
</p>

to fire off as a "process" and loop based on cadence:
```bash
python orchestrate.py
```
[ablinkin]:                         ./img/ablinkin.png

## Settings Explained:
* "openWeatherMapAPIKey": "PLACE KEY HERE"
    * Currently this is not used. Later it will allow grabbing weather forecasts
* "saltStackMaster": ""
    * The salt master api to connect to
* "saltStackUser": ""
    * The salt master api username
* "saltStackPass": ""
    * The salt master api password
* "saltStackStateToRun": ""
    * The salt state to execute to do the "work"
* "zipCode": "29483"
    * Will be required for openweather
* "state": ""
    * if you set the two letter state code (South Carolina would be SC) it will get the
    alerts for the entire state. If left blank will default to the coordinates
* "coords": "33.0975,-80.1753"
    * This will narrow down the alerts to your area. If left blank they will be acquired 
    from your IP
* "units": "imperial"
    * Imperial or Metric
* "alertEventTypeKeyWords": ["Hurricane", "Tropical", "Rip", "Flood"]
    * A list of key words you want to trigger on
* "cadence":
    * The frequency to check for new alerts (in minutes)

## Who Uses WABO:
Just me I suppose
