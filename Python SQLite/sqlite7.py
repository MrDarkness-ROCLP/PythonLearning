import sqlite3


def main():
	#conn = sqlite3.connect('contacts.db')
	conn = sqlite3.connect("chocolate.db") # if you want to point to a different location 'conn = sqlite3.connect(r"C:\Databases\chocolate.db")'
	cur = conn.cursor()
	cur2 = conn.cursor()
	cur3 = conn.cursor()

	product_id = int(input('Enter a product ID: '))
	cur.execute('SELECT Description FROM Products WHERE ProductID = ?', (product_id,))
	cur2.execute('SELECT RetailPrice FROM Products WHERE ProductID = ?', (product_id,))
	print("The current price for", cur.fetchall(), 'is', cur2.fetchall())
	new_price = (input('Enter the new price: '))
	cur3.execute(''' UPDATE Products SET RetailPrice = ? WHERE ProductID = ? ''', (new_price, product_id))

	conn.commit()
	conn.close()



if __name__ == '__main__':
	main()