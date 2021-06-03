import json

with open('ressources/conf.json') as j:
    data = json.load(j)

access_token = data["access_token"]
access_token_secret = data["access_token_secret"]
consumer_key = data["consumer_key"]
consumer_secret = data["consumer_secret"]

zk_idr = data["zookeeper_idr"]
zk_prt = data["zookeeper_prt"]
zk_url = zk_idr+":"+zk_prt

track_workds = data["track_workds"]
