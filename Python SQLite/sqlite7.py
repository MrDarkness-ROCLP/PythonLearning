import sqlite3


def main():
	#conn = sqlite3.connect('contacts.db')
	conn = sqlite3.connect("chocolate.db") # if you want to point to a different location 'conn = sqlite3.connect(r"C:\Databases\chocolate.db")'
	cur = conn.cursor()

	product_id = int(input('Enter a product ID: '))
	cur.execute('SELECT Description, RetailPrice FROM Products WHERE ProductID = ?', (product_id,))
	result = cur.fetchone()

	if result != None:
		print(f"The current price for {result[0]} is ${result[1]:.2f}")
		new_price = (input('Enter the new price: '))
		cur.execute('''UPDATE Products SET RetailPrice = ?
			           WHERE ProductID == ?''',
			           (new_price, product_id))
		conn.commit()
		print(f"The price for {result[0]} has been updated.")
	else:
		print(f"The Product ID '{product_id}' is not found.")
	conn.close()



if __name__ == '__main__':
	main()