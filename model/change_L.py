from dataclasses import dataclass
import json,requests
def base(user,lang):
        with open("config/data/userL.json","r+") as fp:
            data=json.load(fp)["user"]
            if user not in data:
                    d={user:lang}
                    data.update(d)
                    fp.seek(0)
                    json.dump(data, fp, indent=4)
                    fp.truncate()
class l_main():
    def  __init__(self,user,lang):
        base(user,lang)
        self.user = user
        self.lang = lang
        l_main(user,lang).change()
    def change(user,lang):
        with open("config/data/userL.json","r+") as fp:  
            data = json.load(fp)
            data["user"][user] = lang
            fp.seek(0)
            json.dump(data, fp, indent=4)
            fp.truncate()   
            
l_main("jacky","eng")

        

