"""
This is where we will call our automation to do stuff if
alerts.getAlertExists returns true
"""


import alerts
import requests
import time
import logging
import config
import json

logging.basicConfig(level=logging.INFO)

def doWork():
    """
    where we can put our work
    :return:
    """
    logging.info("looking for applicable alerts")
    settings = config.getSettings()
    saltStackMaster = settings["saltStackMaster"]
    saltStackUser = settings["saltStackUser"]
    saltStackPass = settings["saltStackPass"]
    saltStackStateToRun = settings["saltStackStateToRun"]
    alertsRaw = alerts.getAlertExists(True)
    if alertsRaw["alertExists"]:
        logging.info("Firing off Salt State since I see an alert")
        session = requests.Session()
        session.post('https://' + saltStackMaster + ':8000/login', verify=False, json={
            'username': saltStackUser,
            'password': saltStackUser,
            'eauth': 'auto',
        })
        resp = session.post('https://' + saltStackMaster + ':8000/login', verify=False, json=[{
            'client': 'local',
            'tgt': '*',
            'fun': 'state.orchestrate',
            'arg': [saltStackStateToRun],
        }])
        logging.info(resp.content)
        return resp
    else:
        return {"status": "nothing to do"}


while 1 > 0:
    settings = config.getSettings()
    cadence = settings["cadence"]
    results = doWork()
    logging.info("sleeping")
    time.sleep(cadence * 60)
