import matplotlib.pyplot as plt  
import psycopg2

#create connection with DB
conn = psycopg2.connect(database="testdb", user = "postgres", password = "sonam", host = "127.0.0.1", port = "5432")

cur = conn.cursor()

#initializing the coordinate sets
area, bhk, price = [], [], []

#Fetching data from PostgreSql and storing in above created lists
cur.execute("SELECT AREA, BHK, PRICE FROM MAGICBRICK ORDER BY 1")
rows = cur.fetchall()
for row in rows:
	#print('\nArea: ', row[0])
	#print('BHk: ', row[1])
	#print('Price', row[2])
	area.append(row[0])
	bhk.append(row[1])
	price.append(row[2])
   
print ('area: ', area, '\nBHK: ', bhk, '\nPrice: ', price)

plt.title("Area-Price")
plt.plot(area, price)
plt.show() 

area.clear()
bhk.clear()
price.clear()

#Fetching data from PostgreSql and storing in above created lists
cur.execute("SELECT AREA, BHK, PRICE FROM MAGICBRICK ORDER BY 2")
rows = cur.fetchall()
for row in rows:
	#print('\nArea: ', row[0])
	#print('BHk: ', row[1])
	#print('Price', row[2])
	area.append(row[0])
	bhk.append(row[1])
	price.append(row[2])

plt.title("bhk-Price")
plt.plot(bhk, price)
plt.show() 

#Closing connection
conn.close()


'''
# Compute the x and y coordinates for points on a sine curve 
x = np.arange(0, 3 * np.pi, 0.1) 
y = np.sin(x) 


# Plot the points using matplotlib 
plt.plot(x, y) 
plt.show() '''
