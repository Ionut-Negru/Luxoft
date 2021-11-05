# Reader.py
"""This file containts the functions used to read the json files"""
import json
import datetime
from CloudCtx import CloudCtx
from HealthInst import HealthInst
def read_json(file_name=""):
    result = []
    try:
        data = open(file_name,)
        data = json.load(data)
    except FileNotFoundError:
        print("There is no file inside the project folder,try using the full path ")
    else:
        for x in data['imdata']:
            cloudData = x['hcloudCtx']['attributes']
            health = x['hcloudCtx']['children']
            lastModified = cloudData['modTs']
            if(lastModified.split("T")[1].find('+')):
                lastModified = [lastModified.split("T")[0]] + lastModified.split("T")[1].split("+")
                timezone = datetime.timedelta(hours=int(lastModified[2].split(':')[0]), minutes=int(lastModified[2].split(':')[1]))
                lastModified = datetime.datetime(int(lastModified[0].split("-")[0]), int(lastModified[0].split("-")[1]),
                                                 int(lastModified[0].split("-")[2]), int(lastModified[1].split(':')[0]),
                                                 int(lastModified[1].split(':')[1]), int(float(lastModified[1].split(':')[2])))
                lastModified = lastModified + timezone
            else:
                lastModified = [lastModified.split("T")[0]] + lastModified.split("T")[1].split("+")
                timezone = datetime.timedelta(hours=int(lastModified[2].split(':')[0]), minutes=int(lastModified[2].split(':')[1]))
                lastModified = datetime.datetime(int(lastModified[0].split("-")[0]), int(lastModified[0].split("-")[1]),
                                                 int(lastModified[0].split("-")[2]), int(lastModified[1].split(':')[0]),
                                                 int(lastModified[1].split(':')[1]), int(float(lastModified[1].split(':')[2])))
                lastModified = lastModified - timezone


            if len(health) > 0:
                health =  health[0]['healthInst']['attributes']
                result.append(CloudCtx(cloudData['name'],
                                       cloudData['tenantName'],
                                       cloudData['description'],
                                       cloudData['nameAlias'],
                                       cloudData['ctxProfileName'],
                                       HealthInst(health['cur'],health['maxSev']),
                                       lastModified))
            else:
                result.append(CloudCtx(cloudData['name'],
                                       cloudData['tenantName'],
                                       cloudData['description'],
                                       cloudData['nameAlias'],
                                       cloudData['ctxProfileName'],
                                       HealthInst(current_health=0),
                                       lastModified))

    return result