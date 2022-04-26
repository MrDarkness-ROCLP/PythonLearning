import sqlite3


def main():
	#conn = sqlite3.connect('contacts.db')
	conn = sqlite3.connect("chocolate.db") # if you want to point to a different location 'conn = sqlite3.connect(r"C:\Databases\chocolate.db")'
	cur = conn.cursor()

	product_id = int(input('Enter a product ID: '))
	cur.execute('''SELECT Description, RetailPrice FROM Products
		           WHERE ProductID = ? ''', (product_id,))
	
	results = cur.fetchone()

	if results != None:
		print(f"The current price for {results[0]} is ${results[1]:.2f}")
		new_price = float(input('Enter the new price: '))
		cur.execute('''UPDATE Products SET RetailPrice = ?
		               WHERE ProductID == ?''', (new_price, product_id))
		conn.commit()
		print('The price successfully changed')
	else:
		print(f"Product ID '{pid}' not found")

	conn.close()



if __name__ == '__main__':
	main()