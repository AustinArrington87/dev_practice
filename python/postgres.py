import psycopg2 as pg
import datetime

conn = pg.connect(database="teralytic_dev_db", user="teralytic_admin", password="t3ralyt1c", host="teralytic-prod-cluster.cluster-ctbamupmugqj.us-east-1.rds.amazonaws.com", port="5432")

print("Teralytic DB Connected")

cur = conn.cursor()

# enter board_id 
serial_code = '0004a30b002125f9'

###GRABBING DATA#############

#coords
SQL = "SELECT last_known_latlng from probes WHERE serial_code="+"'"+str(serial_code)+"'"
cur.execute(SQL)
coords = cur.fetchall()
coords = [item for items in coords for item in items]
coords =  coords[0]
print("Coords: " + str(coords)) 

SQL = "SELECT last_known_latlng from probes WHERE serial_code= %s;"
cur.execute(SQL,[serial_code,])
coords = cur.fetchall()
coords = [item for items in coords for item in items]
coords =  coords[0]
print("Coords: " + str(coords)) 


#import datetime as dt
#cur.execute("""SELECT * 
#               FROM people_counter 
#               WHERE time_stamp BETWEEN %s and %s;""", 
#            (dt.date(2015,6,1), dt.date(2015,6,30)))

