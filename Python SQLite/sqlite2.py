import sqlite3


def main():
	#conn = sqlite3.connect('contacts.db')
	conn = sqlite3.connect("inventory.db") # if you want to point to a different location 'conn = sqlite3.connect(r"C:\Databases\inventory.db")'
	cur = conn.cursor()

	cur.execute('''INSERT INTO Inventory (ItemName, Price)
		           VALUES ("Screwdriver", 4.99)''')

	cur.execute('''INSERT INTO Inventory (ItemName, Price)
		           VALUES ("Computer", 2000)''')

	conn.commit()
	conn.close()



if __name__ == '__main__':
	main()