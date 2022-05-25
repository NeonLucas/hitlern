import mysql.connector as ms

#initializing variables for host user passwd and database
hst = ""
usr = ""
pswd = ""
dbase = ""

# might need a show table function

def create_database(hst, usr, pswd, dbase):
	mydb = ms.connect(host = hst, user = usr, passwd = pswd)

	cur = mydb.cursor()

	query = "create database %s;" % (dbase)

	cur.execute(query)

	cur.close()
	mydb.close()

def init_connection(host, user, passwd, database):
	global hst, usr, pswd, dbase
	hst = host
	usr = user
	pswd = passwd
	dbase = database

def create_table(tablename, table_values):
	mydb = ms.connect(host = hst, user = usr, passwd = pswd, database = dbase)

	cur = mydb.cursor()

	query = "create table %s%s;" % (tablename, table_values)

	cur.execute(query)
	mydb.commit()

	cur.close()
	mydb.close()

def descript(tablename):
	mydb = ms.connect(host = hst, user = usr, passwd = pswd, database = dbase)

	cur = mydb.cursor()

	query = "desc %s;" % (tablename)

	cur.execute(query)

	res = cur.fetchall()
	
	for i in res:
		print(i)

	cur.close()
	mydb.close()

def insert_val(table, columns, values):
	mydb = ms.connect(host = hst, user = usr, passwd = pswd, database = dbase)

	cur = mydb.cursor()

	query = "insert into %s %s values%s;" % (table, columns, values)

	cur.execute(query)
	mydb.commit()

	cur.close()
	mydb.close()

def select_dat(table, columns, conditions = "nothing", order ="nothing"):
	mydb = ms.connect(host = hst, user = usr, passwd = pswd, database = dbase)

	cur = mydb.cursor()

	contd = ""
	order_str = ""

	if conditions != "nothing":
		contd = "WHERE %s" % (conditions)
	else:
		pass

	if order != "nothing":
		order_str = "ORDER BY %s" % (order)
	else:
		pass

	query = "select %s from %s %s %s;" % (columns, table, contd, order_str)

	cur.execute(query)

	res = cur.fetchall()

	return res
	
	cur.close()
	mydb.close()

def alter_table(tablename, type, column):
	mydb = ms.connect(host = hst, user = usr, passwd = pswd, database = dbase)

	cur = mydb.cursor()

	query = "alter table %s %s %s;" % (tablename, type, column)

	cur.execute(query)

	cur.close()
	mydb.close()

def update_table(tablename, set_statement, conditions = "nothing"):
	mydb = ms.connect(host = hst, user = usr, passwd = pswd, database = dbase)

	cur = mydb.cursor()

	contd = ""

	if conditions != "nothing":
		contd = "where %s" % (conditions)
	else:
		pass

	query = "update %s set %s %s;" % (tablename, set_statement, contd)

	cur.execute(query)
	mydb.commit()

	cur.close()
	mydb.close()

def delete_row(tablename, conditions):
	mydb = ms.connect(host = hst, user = usr, passwd = pswd, database = dbase)

	cur = mydb.cursor()

	query = "delete from %s where %s" %(tablename, conditions)

	cur.execute(query)
	mydb.commit()

	cur.close()
	mydb.close()


def drop_table(tablename):
	mydb = ms.connect(host = hst, user = usr, passwd = pswd, database = dbase)

	cur = mydb.cursor()

	query = "drop table %s" % (tablename)

	cur.execute(query)
	mydb.commit()

	cur.close()
	mydb.close()

def custom_query(query): #EXPERIMENTAL
	mydb = ms.connect(host = hst, user = usr, passwd = pswd, database = dbase)

	cur = mydb.cursor()

	cur.execute(query)
	mydb.commit()

	cur.close()
	mydb.close()










