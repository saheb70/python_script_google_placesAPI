import urllib2
import json
import csv
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf8')
f=open('Plcace_ID.csv','w')
writer=csv.writer(f)

query=''#it takes search input eg. 'cafe+in+delhi'



url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' +query+ '&region=in&key=AIzaSyATA5BmRaFHFIOR2_OYEo-AlkwK1RwmHek'
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
        #remove '#' to see current search while runnig 
	#print placeid, name
        writer.writerow([name,placeid])
    time.sleep(2)
    response = urllib2.urlopen('https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + query + '&region=in&key=AIzaSyATA5BmRaFHFIOR2_OYEo-AlkwK1RwmHek&pagetoken=' + str(page_token) + '')	
    if page_token==None:
	    break
    
