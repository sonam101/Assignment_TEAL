from bs4 import BeautifulSoup
import pandas as pd
import requests
import psycopg2


#create connection with DB
conn = psycopg2.connect(database="testdb", user = "postgres", password = "sonam", host = "127.0.0.1", port = "5432")

cur = conn.cursor()

#fetching details from the site
content = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&Locality=Safdarjung-Enclave&cityName=New-Delhi")
i =1
soup = BeautifulSoup(content.text)

for a in soup.findAll('div', attrs={'class':'m-srp-card SRCard'}):
	price = a.find('div', attrs={'class' : "m-srp-card__price"}).text.strip()
	pr = price.split(' ')
	if pr[2]=='Lac': pr[1] = float(pr[1])/100 
	bhks = a.findAll('span', attrs={'class' : "m-srp-card__title__bhk"})
	bhks1 = bhks[0].text.strip().split(' ')

	area = a.find('div', attrs={'class' : 'm-srp-card__summary__info'}).text.strip()
	ar = area.split('\xa0')
	if ar[1]=='sqyrd': ar[0] = int(ar[0]) * 9

	bhk = a.findAll('div', attrs={'class' : "m-srp-card__summary__info"})
	status = bhk[1].text

	flr = bhk[2].text.split(' ')
	no_of_floor = flr[3]
	if no_of_floor=='Ground': no_of_floor = 0
	floor_avl = flr[0]
	if floor_avl=='Ground': floor_avl = 0

	property_type = bhk[3].text
	furnishing = bhk[4].text

	#inserting data in PostgreSql
	sql = ("INSERT INTO MagicBrick (Area, Bhk, Status, Total_Floor, Floor_Available, Transaction, Furnishing, Price) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)");
	val = (int(ar[0]), int(bhks1[0]), status, int(no_of_floor), int(floor_avl), property_type, furnishing, float(pr[1]))
	cur.execute(sql,val)


'''	print('\n Property', i)
	i+=1
	print('area', area, ar[0] , '\n bhks',bhks1[0], '\n status', status, '\n no of floor', no_of_floor, '\n floor ava', floor_avl, '\n property type', property_type, '\n furnishing', furnishing, '\n price', price ,pr[1])'''

#Committing connection and closing
conn.commit()
conn.close()
