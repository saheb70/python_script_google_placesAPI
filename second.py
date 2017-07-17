import urllib2
import json
import csv
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf8')


API_key=''#insert your google places api key here
f=open('Details.csv','w')
writer=csv.writer(f,delimiter='|')

with open('Plcace_ID.csv')as f:
	rows=csv.reader(f)
	for x in rows:
		s=x[1]	
		re=urllib2.urlopen('https://maps.googleapis.com/maps/api/place/details/json?placeid='+str(s)+'&key='API_key'')
		ht=re.read()
		s1=ht
		s2=json.loads(s1)
		s3=s2.get("result")
		s4=s3.get("name")
		s5=s3.get("formatted_phone_number")
		s6=s3.get("formatted_address")
		s8=s3.get("website")
		s9=s3.get("rating")
		print s4,s8
		writer.writerow([s4,s9,s5,s6,s8])
