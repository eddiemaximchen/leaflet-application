import pandas as pd
import json
dfcity = pd.read_csv('uscities.csv',encoding='utf-8')
file = open('yelp_academic_dataset_business.json','r',encoding='utf-8')
lines = file.readlines()
file.close()

array1 = dfcity.groupby('city').size().index

dfcity.columns = ['city', 'city_ascii', 'state', 'state_name', 'county_fips',
       'county_name', 'lat', 'lng', 'population', 'density', 'source',
       'military', 'incorporated', 'timezone', 'ranking', 'zips', 'id']

dfsum = dfcity[['state','city','lat','lng']]
dfsum1=dfsum[dfsum["state"]=="CA"]
dfsum1.to_html('CA.html', index='')
