import json
import pandas as pd
cities= pd.read_csv('uscities.csv',encoding='utf-8')
states=pd.read_json("states.json")
city=cities[['city','state_id','state_name','lat','lng']]
city=cities[['city','state_id','lat', 'lng']]
state="VA"
city=city[city['state_id']=='VA']
city.drop(columns='state_id')
cities=[]
for i in range(len(city)):
    cities.append({
        "city":city.values[i][0],
        "state_id":city.values[i][1],
        "lat":city.values[i][2],
        "lng":city.values[i][3]
    })
UT=[]
UT.append({
    "state_name":states['state_name'][42],
    "state":states['state'][42],
    "lat":states["latitude"][42],
    "lng":states["longitude"][42],
    'cities':cities
    })
with open(f"map/{state}.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(UT, ensure_ascii=False, indent=4))

