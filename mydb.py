import json

class Database:
    def add_data(self,name,email,password):
        with open('db.json','r') as f:
            temp=json.load(f)
        if email in temp:
            return 0
        else:
            temp[email]=[name,password]
            with open("db.json",'w') as t:
                json.dump(temp,t)
            return 1
        
    def search(self,email,password):
        with open('db.json','r') as f:
            temp=json.load(f)
            if email in temp:
                if temp[email][1]==password:
                    return 1
                else:
                    return 0
            else :
                return 0