import sqlite3


def main():
	#conn = sqlite3.connect('contacts.db')
	conn = sqlite3.connect("inventory.db") # if you want to point to a different location 'conn = sqlite3.connect(r"C:\Databases\inventory.db")'
	cur = conn.cursor()
	again = 'y'

	while again == 'y':
		item_name = input('What is your item name: ')
		price = float(input('Price: '))

		cur.execute(''' INSERT INTO Inventory (ItemName, Price)
			            VALUES (?, ?)''',
			            (item_name, price))

		again = input('Add another item? (y/n): ')

	conn.commit()
	conn.close()



if __name__ == '__main__':
	main()