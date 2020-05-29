import numpy as np
import matplotlib.pyplot as plt
import psycopg2

#create connection with DB
conn = psycopg2.connect(database="testdb", user = "postgres", password = "sonam", host = "127.0.0.1", port = "5432")
cur = conn.cursor()

#initializing the coordinate sets
bhk, floor, price = [], [], []

#Fetching data from PostgreSql and storing in above created lists
cur.execute("SELECT BHK, Floor_Available, MAX(PRICE) FROM MAGICBRICK GROUP BY BHK, FLOOR_AVAILABLE ORDER BY 1,2,3")
rows = cur.fetchall()
for row in rows:
	#print('\nArea: ', row[0])
	#print('BHk: ', row[1])
	#print('Price', row[2])
	bhk.append(row[0])
	floor.append(row[1])
	price.append(row[2])



N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

'''       MAX DATA     '''

yvals = [-0.1, -0.1, 0.65]      #2bhk 1st floor 2nd floor 3rd floor cost
rects1 = ax.bar(ind, yvals, width, color='r')
zvals = [3.90, 3.25, 3.99]		#3bhk 1st floor 2nd floor 3rd floor cost
rects2 = ax.bar(ind+width, zvals, width, color='g')
kvals = [5.5, 7, 5.5]	#4bhk 1st floor 2nd floor 3rd floor cost
rects3 = ax.bar(ind+width*2, kvals, width, color='b')

ax.set_title('Maximum Price Chart')
ax.set_ylabel('Price')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('1st Floor', '2nd Floor', '3rd Floor') )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('2bhk', '3bhk', '4bhk') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()


N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

'''       MIN DATA     '''

yvals = [-0.1, -0.1, 0.65]      #2bhk 1st floor 2nd floor 3rd floor cost
rects1 = ax.bar(ind, yvals, width, color='r')
zvals = [3.2, 2.6, 2.5]		#3bhk 1st floor 2nd floor 3rd floor cost
rects2 = ax.bar(ind+width, zvals, width, color='g')
kvals = [4.75, 4.4, 5.5]	#4bhk 1st floor 2nd floor 3rd floor cost
rects3 = ax.bar(ind+width*2, kvals, width, color='b')

ax.set_title('Minimum Price Chart')
ax.set_ylabel('Price')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('1st Floor', '2nd Floor', '3rd Floor') )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('2bhk', '3bhk', '4bhk') )

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()

autolabel(rects2)
autolabel(rects3)

plt.show()
