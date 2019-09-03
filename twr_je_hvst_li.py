#!/usr/bin/python3

import requests
import json
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--li_server", dest = "li_server", help="Loginsight Server Name")
parser.add_argument("-t", "--twr_server", dest = "twr_server", help="Tower Serer Name")
parser.add_argument("-a", "--li_agent_id",dest ="li_agent_id", default=str(0), help="LoginsightAgent")
parser.add_argument("-j", "--job_id",dest ="job_id", help="Tower Job ID")
parser.add_argument("-u", "--twr_user",dest = "twr_user", help="Tower User Name")
parser.add_argument("-p", "--twr_pass",dest = "twr_pass", help="Tower User Password")

args = parser.parse_args()

li_server = args.li_server
twr_server = args.twr_server
li_agent_id = args.li_agent_id
job_id = args.job_id
twr_user = args.twr_user
twr_pass = args.twr_pass

twr_api = "api/v2/jobs/" + job_id + "/job_events/"
twr_url = "https://" + twr_server + "/" + twr_api 
li_resturl = "http://" + li_server + ":9000/api/v1/messages/ingest/" + li_agent_id

headers = {"Accept":"application/json"}

response = requests.get(twr_url, auth=(twr_user, twr_pass), headers=headers, verify=False )

if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

results = response.json()['results']
twr_next = response.json()['next']

while twr_next:
    twr_url = "https://" + twr_server + twr_next
    response = requests.get(twr_url, auth=(twr_user, twr_pass), headers=headers, verify=False )
    twr_next = response.json()['next']
    results += response.json()['results']

for task in results:
    fields = []
    for r in task:
        my_dict =  { "name": str("twr_" + r),"content": str(task[r]) }
        fields.append(my_dict)
        if r == "modified":
            mod_time = (datetime.strptime(results[0][r], '%Y-%m-%dT%H:%M:%S.%fZ') - datetime(1970,1,1)).total_seconds()
    events = { "events": [{ "timestamp": mod_time, "fields": fields }] }
    events = json.dumps(events)
    print(events + "\n\n")
    # response = requests.post(li_resturl, events, verify=False )
    # print(response.text)
