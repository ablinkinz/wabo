"""
This is where we will call our automation to do stuff if
alerts.getAlertExists returns true
"""


import alerts
import requests
import config


def doWork():
    """
    where we can put our work
    :return:
    """
    settings = config.getSettings()
    saltStacMaster = settings["saltStackMaster"]
    saltStackUser = settings["saltStackUser"]
    saltStackPass = settings["saltStackPass"]
    saltStackStateToRun = settings["saltStackStateToRun"]
    alertsRaw = alerts.getAlertExists(True)
    if alertsRaw["alertExists"]:
        print("Firing off Salt State: ", saltStackStateToRun)
        session = requests.Session()
        session.post('http://' + saltStacMaster + ':8000/login', json={
            'username': saltStackUser,
            'password': saltStackUser,
            'eauth': 'auto',
        })
        resp = session.post('http://' + saltStacMaster + ':8000/login', json=[{
            'client': 'local',
            'tgt': '*',
            'fun': 'state.orchestrate',
            'arg': [saltStackStateToRun],
        }])
        return resp
    else:
        return {"status": "nothing to do"}