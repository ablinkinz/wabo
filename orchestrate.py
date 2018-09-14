"""
This is where we will call our automation to do stuff if
alerts.getAlertExists returns true
"""


import alerts


def doStuff():
    """
    where we can put our work
    :return:
    """
    alertsRaw = alerts.getAlertExists(True)
    if alertsRaw["alertExists"]:
        print("we need to do stuff")
