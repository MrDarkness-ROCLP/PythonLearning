import sqlite3


def main():
	#conn = sqlite3.connect('contacts.db')
	conn = sqlite3.connect("inventory.db") # if you want to point to a different location 'conn = sqlite3.connect(r"C:\Databases\inventory.db")'
	cur = conn.cursor()

	cur.execute('''CREATE TABLE Inventory (ItemID INTEGER PRIMARY KEY NOT NULL,
		                                   ItemName TEXT,
		                                   Price REAL)''')

	conn.commit()
	conn.close()



if __name__ == '__main__':
	main()