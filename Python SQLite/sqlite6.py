import sqlite3


def main():
	#conn = sqlite3.connect('contacts.db')
	conn = sqlite3.connect("chocolate.db") # if you want to point to a different location 'conn = sqlite3.connect(r"C:\Databases\chocolate.db")'
	cur = conn.cursor()

	cur.execute('SELECT Description, RetailPrice FROM Products')

	row = cur.fetchone()

	while row != None:
		print(f'{row[0]:30} {row[1]:5}')
		row__ = cur.fetchone()

	conn.close()



if __name__ == '__main__':
	main()