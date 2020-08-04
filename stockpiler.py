import sqlite3
import sys
import colorama
from colorama import Fore, Back, Style, init
from tabulate import tabulate

init()
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

def main():
    menu()

def menu():
    print(Fore.GREEN + """
 _____ _             _          _ _           
/  ___| |           | |        (_) |          
\ `--.| |_ ___   ___| | ___ __  _| | ___ _ __ 
 `--. \ __/ _ \ / __| |/ / '_ \| | |/ _ \ '__|
/\__/ / || (_) | (__|   <| |_) | | |  __/ |   
\____/ \__\___/ \___|_|\_\ .__/|_|_|\___|_|   
                         | |                  
                         |_|                  
""" + Style.RESET_ALL)

    print("""
1. Create new stockpile (Please only do this once)\n
2. Add item to stockpile\n
3. Remove item from stockpile\n
4. Check stockpile\n
5. Close\n""")

    answer = input('Selection: ')

    if answer == "1":
        cursor.execute("CREATE TABLE stockpile(item_id INTEGER PRIMARY KEY, item_name char(50), item_size char(10), item_color char(10), item_price n(10));")
        print(Fore.GREEN + 'Successfully created stockpile.' + Style.RESET_ALL)
        menu()
    elif answer == "2":
        i_name = input('Item Name: ')
        i_size = input('Item Size: ')
        i_color = input('Item Color: ')
        i_price = input('Item Purchase Price: ')
        cursor.execute("""
        INSERT INTO stockpile(item_name, item_size, item_color, item_price)
        VALUES (?, ?, ?, ?)
        """, (i_name, i_size, i_color, i_price))
        conn.commit()
        print(Fore.GREEN + 'Data entered successfully.' + Style.RESET_ALL)
        menu()
    elif answer == "3":
        remove_answer = input('What item would you like removed? ')
        delete_query = """DELETE FROM stockpile WHERE item_id = ?"""
        cursor.execute(delete_query, remove_answer)
        conn.commit()
        print(Fore.GREEN + 'Record deleted successfully.' + Style.RESET_ALL)
        menu()
    elif answer == "4":
        cursor.execute("""
        SELECT item_id, item_name, item_size, item_color, item_price FROM stockpile;""")
        result = cursor.fetchall()
        print(tabulate(result, headers=['ID', 'Name', 'Size', 'Color', 'Price'], tablefmt='psql'))
        goBack = input('Press Y to go back to the main menu: ')
        if goBack == "Y" or "y":
            menu()
        else:
            pass
    elif answer == "5":
        if (conn):
            conn.close()
            sys.exit()

main()
