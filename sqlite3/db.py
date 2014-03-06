import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

sql = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, user VARCHAR(15), pass VARCHAR(15))"
cursor.execute(sql)
conn.commit()

def create():
	user = input('User: ')
	pasw = input('Pass: ')
	sql = "INSERT INTO users VALUES(NULL, '%s','%s')" % (user,pasw)
	cursor.execute(sql)
	conn.commit()
	menu()
def read():
	sql = "SELECT * FROM `users`"
	for row in cursor.execute(sql):
		print(row)
	menu()
def delete():
	id = input('Delete from ID: ')
	sql = "DELETE FROM users WHERE id = '%s'" % id
	cursor.execute(sql)
	conn.commit()
	menu()
def menu():	
	print('\nSelect an option:\n[1] Add [2] Search [3] Update [4] Delete\n')
	op = int(input('Option: '))
	if(op == 1):
		create()
	if(op == 2):
		read()
	if(op == 2):
		update()
	if(op == 4):
		delete()
	if(op == 0):
		exit()
menu()