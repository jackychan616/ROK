import json


import json

with open(r"C:\Users\jacky\Documents\discord\ROK\webhook\server.json", "r+") as fp:
    data = json.load(fp)
path = [data[i] for i in data if i != "1015223481643827221"]
print(path)