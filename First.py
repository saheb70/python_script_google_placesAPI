#to find places on google maps,firstly place id is needed.
# in this First.py it will fetch place id's of locations and store it in Place_ID.csv
import urllib2
import json
import csv
import urllib
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
f=open('Plcace_ID.csv','w')
writer=csv.writer(f)

query=''   #it takes search input eg. 'cafe+in+delhi'
API_key='' #Insert your google places key here


url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' +query+ '&region=in&key='+API_key+''
response = urllib2.urlopen(url)

while True:
    html=response.read()
    re=html	
    json_1 = json.loads(re)
    results = json_1.get("results",None)
    page_token = json_1.get("next_page_token",None)
    for i in results:
        placeid = i.get("place_id")
        name = i.get("name")
	#print placeid, name
        writer.writerow([name,placeid])
    time.sleep(2)
    response = urllib2.urlopen('https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + query + '&region=in&key='+API_key+'&pagetoken=' + str(page_token) + '')	
    if page_token==None:# google only gives 20 output per page and max pages can be 3. to get next page page_token is given on each page
	    break#if we do not get page_token so it means we are at the last page and code will break.
    
