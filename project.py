import sqlite3
from bokeh.io import output_file, show
from bokeh.plotting import figure

def main():
    print("(Use 1-20 for testing)")
    current_user = input("Enter your user ID: ")
    connection = sqlite3.connect('database.db')
    while (True):
        print("////////////////////////////////")
        print("\nWhat do you want to do?")
        print("1) View my orders")
        print("2) View my shopping cart")
        print("3) View my information")
        print("4) Edit my information")
        print("5) View products")
        print("6) Create new shopping cart")
        print("7) Create BOKEH bar chart")
        print("0) Exit")
        choise = int(input("Your choise: "))
        if choise == 0:
            print("Thank you!")
            connection.commit()
            connection.close()
            break
        elif choise == 1:
            vieworders(connection, current_user)
        elif choise == 2:
            viewshoppingcart(connection, current_user)
        elif choise == 3:
            viewmyinfo(connection, current_user)
        elif choise == 4:
            editinformation(connection, current_user)
        elif choise == 5:
            viewproducts(connection)
        elif choise == 6:
            createnewsc(connection, current_user)
        elif choise == 7:
            createbokeh(connection)
        else:
            print("Unkown selection. Try again.\n")
    
    return 0


def vieworders(connection, customer):
    cursor = connection.cursor()
    cursor.execute("""SELECT ShoppingCart.ID_SC FROM ShoppingCart
                    INNER JOIN Orders
                    ON ShoppingCart.ID_SC=Orders.ID_SC
                    WHERE ShoppingCart.ID_Customer=?""",(customer,))
    orders = cursor.fetchall()
    print("\n////////////////////////////////")
    if len(orders) == 0:
        print("You haven't ordered anything yet!\n")
    else:
        print("Your order history (order numbers):")
        for order in orders:
            print(order)

    
    

def viewshoppingcart(connection, customer):
    """This function allow you view shopping cart"""
    cursor = connection.cursor()
    print("\n////////////////////////////////")
    print("Your latest shopping cart:")
    cursor.execute('SELECT MAX(ID_SC) FROM ShoppingCart WHERE ID_Customer=?',(customer,))
    latest_sc = cursor.fetchall()[0][0]

    cursor.execute("""SELECT Product.Manufacturer, Product.Model, Product.Memory 
                    FROM ShoppingCart
                    INNER JOIN ProductsInShoppingCart
                    ON ShoppingCart.ID_SC=ProductsInShoppingCart.ShoppingCart
                    INNER JOIN Product
                    ON Product.ID_Product=ProductsInShoppingCart.Product
                    WHERE ShoppingCart.ID_SC=?""",(latest_sc,))
    rows = cursor.fetchall()
    cursor.execute('SELECT Total_Price FROM ShoppingCart WHERE ID_SC=?',(latest_sc,))
    total_price = cursor.fetchall()[0][0]
    item = 1
    for row in rows:
        print("\nItem "+str(item)+":")
        print("Name:",row[0],row[1])
        print("Memory:",row[2])
        item=item+1
    print("\nTotal price:",total_price,)

def viewmyinfo(connection, customer):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Customer WHERE ID_Customer=?',(customer,))
    rows = cursor.fetchall()
    print("\n////////////////////////////////")
    print("Your information:\n")
    for row in rows:
        print("Customer ID:",row[0])
        print("Name:",row[2])
        print("SSN:",row[1])
        print("Address:",row[3],)

def editinformation(connection, customer):
    cursor = connection.cursor()
    while True:
        print("\n////////////////////////////////")
        print("What would you like to edit?")
        print("1) Name")
        print("2) SSN")
        print("3) Address")
        print("0) Exit")
        editable = int(input("Choise: "))
        if editable == 1:
            name = input("New name: ")
            cursor.execute('UPDATE Customer SET Name=? WHERE ID_Customer=?',(name, customer,))
            connection.commit()
            break
        elif editable == 2:
            ssn = input("New social security number: ")
            cursor.execute('UPDATE Customer SET Social_Number=? WHERE ID_Customer=?',(ssn, customer,))
            connection.commit()
            break
        elif editable == 3:
            address = input("New address: ")
            cursor.execute('UPDATE Customer SET Address=? WHERE ID_Customer=?',(address, customer,))
            connection.commit()
            break
        elif editable == 0:
            break
        else:
            print("Choose 1-3. Try again.")

def viewproducts(connection):
    cursor = connection.cursor()
    while True:
        print("\n////////////////////////////////")
        print("What would you like to view?")
        print("1) Phones")
        print("2) Tablets")
        print("3) The most expensive product")
        print("4) The least expensive product")
        print("0) Exit")
        selection = int(input("Choise: "))
        print("\n")
        if selection == 1:
            pattern_phone = "22%"
            cursor.execute("SELECT Manufacturer, Model, Memory, Release_Year FROM Product WHERE ID_Product LIKE ?",(pattern_phone,))
            rows = cursor.fetchall()
            for row in rows:
                print("{} {}, Memory: {}, Release year: {}".format(row[0],row[1],row[2],row[3]))
            break
        elif selection == 2:
            pattern_tablet = "11%"
            cursor.execute("SELECT Manufacturer, Model, Memory, Release_Year FROM Product WHERE ID_Product LIKE ?",(pattern_tablet,))
            rows = cursor.fetchall()
            for row in rows:
                print("{} {}, Memory: {}, Release year: {}".format(row[0],row[1],row[2],row[3]))
            break
        elif selection == 3:
            cursor.execute("SELECT Manufacturer, Model, Memory, Release_Year, Price FROM Product WHERE Price=(SELECT MAX(Price) FROM Product)")
            product = cursor.fetchall()[0]
            print("The most expensive product is:")
            print("\nName: {} {}\nMemory: {}\nRelease year: {}\nPrice: {}".format(product[0],product[1],product[2],product[3],product[4]))
        elif selection == 4:
            cursor.execute("SELECT Manufacturer, Model, Memory, Release_Year, Price FROM Product WHERE Price=(SELECT MIN(Price) FROM Product)")
            product = cursor.fetchall()[0]
            print("The least expensive product is:")
            print("\nName: {} {}\nMemory: {}\nRelease year: {}\nPrice: {}".format(product[0],product[1],product[2],product[3],product[4]))
        elif selection == 0:
            break
        else:
            print("Unkown selection. Try again")

def createnewsc(connection, customer):
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(ID_SC) FROM ShoppingCart")
    latest_sc=cursor.fetchall()[0][0]
    latest_sc+=1
    product_list=[]
    while True:
        print("\n////////////////////////////////")
        print("What would you like to add?")
        print("1) Phone")
        print("2) Tablet")
        print("3) Add selected")
        print("0) Exit")
        selection = int(input("Your choise: "))
        if selection == 0:
            break
        elif selection == 1:
            phone_pattern="22%"
            cursor.execute("""SELECT * FROM Product WHERE ID_Product LIKE ?""",(phone_pattern,))
            phone_list=cursor.fetchall()
            print("Available products:")
            for i in phone_list:
                print(i)
            id=int(input("Enter product id or 0 to exit: "))
            if id == 0:
                break
            else:
                product_list.append(id)
        elif selection == 2:
            tablet_pattern="11%"
            cursor.execute("""SELECT *
                            FROM Product
                            WHERE ID_Product LIKE ?""",(tablet_pattern,))
            phone_list=cursor.fetchall()
            print("Available products:")
            for i in phone_list:
                print(i)
            id=int(input("Enter product id or 0 to exit: "))
            if id == 0:
                break
            else:
                product_list.append(id)
        elif selection == 3:
            total_price=0
            for id in product_list:
                cursor.execute("""INSERT INTO ProductsInShoppingCart (Shoppingcart, Product)
                                VALUES (?,?)""",(latest_sc, id,))
                connection.commit()
                cursor.execute("""SELECT Price FROM Product WHERE ID_Product=?""",(id,))
                total_price = total_price + int(cursor.fetchone()[0])
            cursor.execute("""INSERT INTO ShoppingCart (ID_SC, ID_Customer, Total_Price)
                            VALUES (?,?,?)""",(latest_sc, customer, total_price,))
            connection.commit()
            print("Products added to shopping cart!")
            


def createbokeh(connection):
    output_file("barchart.html")
    cursor = connection.cursor()

    cursor.execute("""SELECT Model FROM Product""")
    names = []
    for i in cursor.fetchall():
        names.append(i[0])

    cursor.execute("""SELECT Price FROM Product""")
    prices = []
    for i in cursor.fetchall():
        prices.append(i[0])
    

    p = figure(x_range=names, height=500, width=750, title="Product Prices",
           toolbar_location=None, tools="")

    p.vbar(x=names, top=prices, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.major_label_orientation = "vertical"

    show(p)


main()