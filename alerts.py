"""
Get the alerts and trigger some orchestration
"""
import forecast
import config
import operator


def getAlerts():
    """
    get our alerts from the forecast class
    >>> alerts = forecast.GetWeatherDotGovAlerts()
    >>> True if alerts else False
    True
    """
    alerts = forecast.GetWeatherDotGovAlerts()
    results = alerts.results()
    if results["features"]:
        eventResult = {}
        counter = 0
        for feature in results["features"]:
            scounter = str(counter)
            eventResult[scounter] = {}
            eventResult[scounter]["eventType"] = feature["properties"]["event"]
            eventResult[scounter]["eventStart"] = feature["properties"]["effective"]
            eventResult[scounter]["eventEnd"] = feature["properties"]["ends"]
            eventResult[scounter]["eventUrgency"] = feature["properties"]["urgency"]
            eventResult[scounter]["eventHeadline"] = feature["properties"]["headline"]
            eventResult[scounter]["eventDescription"] = feature["properties"]["description"]
            eventResult[scounter]["eventInstruction"] = feature["properties"]["instruction"]
            counter = counter + 1
        return eventResult


def getAlertExists(verbose=False):
    """
    lets see if our alerts have any of the keywords we are looking for
    """
    settings = config.getSettings()
    keyWords = settings["alertEventTypeKeyWords"]
    alerts = getAlerts()
    flag = False
    for word in keyWords:
        if alerts:
            for alert in alerts:
                alertType = alerts[alert]["eventType"]
                if operator.contains(alertType, word):
                    flag = True
    if verbose:
        return {"alertExists": flag, "Raw Message": alerts}
    else:
        return {"alertExists": flag}
