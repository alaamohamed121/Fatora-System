import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import sqlite3
from tkinter import *
from datetime import datetime





class InventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Fatora - Inventory Management Program")
        
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.pack()
        

        # Add a list to store usernames and passwords
        self.credentials = [["alaa", "pass"], ["username2", "password2"]]

    def submit(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        for user, password in self.credentials:
            if entered_username == user and entered_password == password:
                self.login_message = tk.Label(self, text="Logging in...")
                self.login_message.pack()
                self.after(2000, self.login)
                return
        self.login_message = tk.Label(self, text="Access denied")
        self.login_message.pack()



    def login(self):
        self.login_message.destroy()
        self.destroy()
        new_app = NewApp()



class NewApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome to our program")
        self.label = tk.Label(self, text="welcome sir")
        self.label.pack()

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.pack()
        

        # Create the buttons
        self.add_item_button = tk.Button(self.button_frame, text="Add Item", command=self.add_item)
        self.remove_item_button = tk.Button(self.button_frame, text="Remove Item", command=self.remove_item)
        self.search_button = tk.Button(self.button_frame, text="show & search", command=self.show_data_window)
        self.edit_button = tk.Button(self.button_frame, text="edit item", command=self.edit_item)
        self.sale_process_button = tk.Button(self.button_frame, text="sale process", command=self.sell_now)
        self.report_button = tk.Button(self.button_frame, text="report", command=self.report)


  

        # Pack the buttons
        self.add_item_button.pack(side="left")
        self.remove_item_button.pack(side="left")
        self.search_button.pack(side="left")
        self.edit_button.pack(side="left")
        self.sale_process_button.pack(side="left")
        self.report_button.pack(side="left")



        


        
    def add_item(self):
            # Create a new window
            self.new_window = tk.Toplevel(self)
    
            self.tree = ttk.Treeview(self.new_window, columns=("name", "quantity", "price", "Manufacturer company", "country"))
            self.tree.heading("#0", text="ID")
            self.tree.heading("name", text="Name")
            self.tree.heading("quantity", text="Quantity")
            self.tree.heading("price", text="Price")
            self.tree.heading("Manufacturer company", text="Manufacturer company")
            self.tree.heading("country", text="country")

            self.tree.column("#0", width=30, minwidth=30, stretch=tk.NO)
            self.tree.column("name", width=150, minwidth=150, stretch=tk.NO)
            self.tree.column("quantity", width=100, minwidth=100, stretch=tk.NO)
            self.tree.column("price", width=100, minwidth=100, stretch=tk.NO)
            self.tree.column("Manufacturer company", width=150, minwidth=150, stretch=tk.NO)
            self.tree.column("country", width=150, minwidth=150, stretch=tk.NO)

            self.tree.pack()

            self.name_label = tk.Label(self.new_window, text="Name:")
            self.name_label.pack()

            self.name_entry = tk.Entry(self.new_window)
            self.name_entry.pack()

            self.quantity_label = tk.Label(self.new_window, text="Quantity:")
            self.quantity_label.pack()

            self.quantity_entry = tk.Entry(self.new_window)
            self.quantity_entry.pack()

            self.price_label = tk.Label(self.new_window, text="Price:")
            self.price_label.pack()

            self.price_entry = tk.Entry(self.new_window)
            self.price_entry.pack()

            self.manufacturer_label = tk.Label(self.new_window, text="Manufacturer company:")
            self.manufacturer_label.pack()

            self.manufacturer_entry = tk.Entry(self.new_window)
            self.manufacturer_entry.pack()
            
            self.country_label = tk.Label(self.new_window, text="country:")
            self.country_label.pack()

            self.country_entry = tk.Entry(self.new_window)
            self.country_entry.pack()
            
            self.submit_button = tk.Button(self.new_window, text="Submit", command=self.add_to_tree)
            self.submit_button.pack()
            self.id = 1
    def add_to_tree(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        company = self.manufacturer_entry.get()
        country = self.country_entry.get()
        

        self.tree.insert("", tk.END, text=self.id, values=(name, quantity, price, company, country))
        self.id += 1
        

        conn = sqlite3.connect('fatora_database.db')
        c = conn.cursor()
        # Insert a new row of data into the table
        insert_stmt = "INSERT INTO products (name, quantity, price, company, country) VALUES ('{}', '{}', '{}', '{}', '{}')".format(name, quantity, price, company, country)
        c.execute(insert_stmt)
        # Commit the changes and close the connection
        conn.commit()
        c.close()
        conn.close()


    def remove_item(self):
        # Create a new window
        self.remove_window = tk.Toplevel(self)
        self.remove_window.title("Remove Item")

        # Create a ttk Treeview widget to display the data
        self.tree = ttk.Treeview(self.remove_window, columns=("name", "quantity", "price", "manufacturer", "country"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("quantity", text="Quantity")
        self.tree.heading("price", text="Price")
        self.tree.heading("manufacturer", text="Manufacturer")
        self.tree.heading("country", text="Country")

        self.tree.column("#0", width=30, minwidth=30, stretch=tk.NO)
        self.tree.column("name", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column("quantity", width=50, minwidth=50, stretch=tk.NO)
        self.tree.column("price", width=50, minwidth=50, stretch=tk.NO)
        self.tree.column("manufacturer", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column("country", width=50, minwidth=50, stretch=tk.NO)
        
        self.tree.pack()
        self.delete_button = tk.Button(self.remove_window, text="delete", command=self.confirm_remove)
        self.delete_button.pack()

    # Read data from main file
        conn = sqlite3.connect('fatora_database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM products")
        rows = c.fetchall()

        for row in rows:
            self.tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
        

    def confirm_remove(self):
        # Get the selected item
        selected_item = self.tree.selection()

        # If an item is selected, ask for confirmation
        if selected_item:
            result = messagebox.askyesno("Remove Item", "Are you sure you want to remove this item?")
            if result:
                # Get the item's values
                item_id = self.tree.item(selected_item)['text']
                item_values = self.tree.item(selected_item)['values']

                # Remove the item from the Treeview
                self.tree.delete(selected_item)

                # Remove the item from the CSV file
                conn = sqlite3.connect('fatora_database.db')
                c = conn.cursor()
                delete_stmt = 'DELETE FROM products WHERE id = ?'
                c.execute(delete_stmt, (item_id,))
                conn.commit()
                conn.close()
            else:
                print("No item selected.")

    def show_data_window(self):
        # Create a new window
        self.data_window = tk.Toplevel(self)
        self.data_window.title("Inventory Data")
        
        # Create a search bar
        self.search_bar = tk.Entry(self.data_window) 
        self.search_bar.pack()
        
        # Create a search button
        self.search_button = tk.Button(self.data_window, text="Search", command=self.search)
        self.search_button.pack()
        
        # Create a ttk Treeview widget to display the data
        self.tree = ttk.Treeview(self.data_window, columns=("name", "quantity", "price", "manufacturer", "country"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("quantity", text="Quantity")
        self.tree.heading("price", text="Price")
        self.tree.heading("manufacturer", text="Manufacturer")
        self.tree.heading("country", text="Country")

        self.tree.column("#0", width=30, minwidth=30, stretch=tk.NO)
        self.tree.column("name", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column("quantity", width=50, minwidth=50, stretch=tk.NO)
        self.tree.column("price", width=50, minwidth=50, stretch=tk.NO)
        self.tree.column("manufacturer", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column("country", width=50, minwidth=50, stretch=tk.NO)
        
        self.tree.pack()

        # Read data from main file
        conn = sqlite3.connect('fatora_database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM products")
        rows = c.fetchall()

        for row in rows:
            self.tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))

    def search(self):
        search_string = self.search_bar.get()
        self.tree.delete(*self.tree.get_children()) # remove any existing items from the Treeview widget
        conn = sqlite3.connect('fatora_database.db')
        c = conn.cursor()
        search_stmt = 'SELECT * FROM products WHERE id = ? or name LIKE ?'
        c.execute(search_stmt, (search_string, '%'+search_string+'%'))

        rows = c.fetchall()

        for row in rows:
                if search_string in row[1] or search_string in row[0]:
                    self.tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
                else:
                    pass
        conn.commit()
        conn.close()


    def edit_item(self):
        # Create a new window
        self.data_window = tk.Toplevel(self)
        self.data_window.title("edit data")
    
        
        # Create a edit button
        self.edit_button = tk.Button(self.data_window, text="edit", command=self.on_edit)
        self.edit_button.pack()
        
        # Create a ttk Treeview widget to display the data
        self.tree = ttk.Treeview(self.data_window, columns=("name", "quantity", "price", "manufacturer", "country"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("quantity", text="Quantity")
        self.tree.heading("price", text="Price")
        self.tree.heading("manufacturer", text="Manufacturer")
        self.tree.heading("country", text="Country")

        self.tree.column("#0", width=30, minwidth=30, stretch=tk.NO)
        self.tree.column("name", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column("quantity", width=50, minwidth=50, stretch=tk.NO)
        self.tree.column("price", width=50, minwidth=50, stretch=tk.NO)
        self.tree.column("manufacturer", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column("country", width=50, minwidth=50, stretch=tk.NO)
        
        self.tree.pack()

        # Read data from main file
        conn = sqlite3.connect('fatora_database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM products")
        rows = c.fetchall()

        for row in rows:
            self.tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))


    def on_edit(self):
        self.selected_item = self.tree.selection()

        if hasattr(self, 'selected_item'):
            # Open a new window
            self.data_window = tk.Toplevel(self)
            self.data_window.title("edit data")

            # Read data from main file
            conn = sqlite3.connect('fatora_database.db')
            c = conn.cursor()
            c.execute("SELECT * FROM products where id = ?", (self.tree.item(self.selected_item)['text'],))
            data = c.fetchone()
            conn.close()

            # Create entry widgets and populate them with the data
            self.name_label = Label(self.data_window, text="Name:")
            self.name_label.grid(row=0, column=0)
            self.name_entry = Entry(self.data_window)
            self.name_entry.insert(0, data[1])
            self.name_entry.grid(row=0, column=1)

            self.quantity_label = Label(self.data_window, text="Quantity:")
            self.quantity_label.grid(row=1, column=0)
            self.quantity_entry = Entry(self.data_window)
            self.quantity_entry.insert(0, data[2])
            self.quantity_entry.grid(row=1, column=1)

            self.price_label = Label(self.data_window, text="Price:")
            self.price_label.grid(row=2, column=0)
            self.price_entry = Entry(self.data_window)
            self.price_entry.insert(0, data[3])
            self.price_entry.grid(row=2, column=1)

            self.company_label = Label(self.data_window, text="company:")
            self.company_label.grid(row=3, column=0)
            self.company_entry = Entry(self.data_window)
            self.company_entry.insert(0, data[4])
            self.company_entry.grid(row=3, column=1)

            self.country_label = Label(self.data_window, text="Country:")
            self.country_label.grid(row=4, column=0)
            self.country_entry = Entry(self.data_window)
            self.country_entry.insert(0, data[5])
            self.country_entry.grid(row=4, column=1)

            self.save_button = Button(self.data_window, text="Save", command=self.save_changes)
            self.save_button.grid(row=5, column=1)

    def save_changes(self):
        conn = sqlite3.connect('fatora_database.db')
        c = conn.cursor()
        c.execute("UPDATE products SET name = ?, quantity = ?, price = ?, company = ?, country = ? WHERE id = ?", (self.name_entry.get(), self.quantity_entry.get(), self.price_entry.get(), self.company_entry.get(), self.country_entry.get(), self.tree.item(self.selected_item)['text']))
        conn.commit()
        conn.close()
        self.data_window.destroy()
        self.tree.item(self.selected_item, values=(self.name_entry.get(), self.quantity_entry.get(), self.price_entry.get(), self.company_entry.get(), self.country_entry.get()))
        messagebox.showinfo("Done","The action is done!")
   


    def sell_now(self):
         # Create a new window
            self.new_window = tk.Toplevel(self)


            self.name_label = tk.Label(self.new_window, text="product name:")
            self.name_label.pack()
           

            self.name_entry = tk.Entry(self.new_window)
            self.name_entry.pack()

            self.quantity_label = tk.Label(self.new_window, text="Quantity:")
            self.quantity_label.pack()

            self.quantity_entry = tk.Entry(self.new_window)
            self.quantity_entry.pack()

            self.name_of_buyer_label = tk.Label(self.new_window, text="name of buyer:")
            self.name_of_buyer_label.pack()

            self.name_of_buyer_entry = tk.Entry(self.new_window)
            self.name_of_buyer_entry.pack()

            self.calculate_button = tk.Button(self.new_window, text="calculate", command=self.sale_on)
            self.calculate_button.pack()

            self.total_cost_label = tk.Label(self.new_window, text="total cost:")
            self.total_cost_label.pack()

  
            
            self.time_label = tk.Label(self.new_window, text="time:")
            self.time_label.pack()
            current_time = datetime.now().strftime("%H:%M:%S")
            self.time_label.config(text=current_time)

            self.date_label = tk.Label(self.new_window, text="date:")
            self.date_label.pack()
            current_date = datetime.now().strftime("%Y-%m-%d")
            self.date_label.config(text=current_date)

            

            self.submit_button = tk.Button(self.new_window, text="Submit", command=self.decrease_quantity)
            self.submit_button.pack()

    
    def sale_on(self):
        product_name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())
        # Make sure the inputs are valid
        if product_name and isinstance(quantity, int):
            # Connect to the database
            conn = sqlite3.connect('fatora_database.db')
            c = conn.cursor()
            c.execute("SELECT price FROM products WHERE name=?", (product_name,))
            result = c.fetchone()
            # Make sure the result is valid
            if result:
                re = result[0]
                total_price = quantity * re
                self.total_cost_label.configure(text=f"Total: {total_price}")
        else:
            total_price = 0

  
    def decrease_quantity(self):
        
        # Connect to the database
        conn = sqlite3.connect('fatora_database.db')
        c = conn.cursor()

        # Get the product name and quantity from the entry fields
        product_name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())

        # Decrease the quantity of the product in the database
        c.execute("UPDATE products SET quantity = quantity - ? WHERE name = ?", (quantity, product_name))
        conn.commit()

        # Close the connection to the database
        conn.close()
        messagebox.showinfo("Done","The action is done!")
                

    def report(self):
        report_new_window = tk.Toplevel(self)
        button = tk.Button(report_new_window, text='Make Report Now', command=self.make_pdf)
        button.pack()



    def make_pdf(self):
        # Connect to the database
        conn = sqlite3.connect('fatora_database.db')
        cursor = conn.cursor()

        # Execute a query
        cursor.execute("SELECT * FROM products")

        # Fetch the results
        results = cursor.fetchall()
        results_1 = str(results)
        # Write the results to file
        with open("report.csv", 'w') as f:

            f.write(results_1)
        



        # Close the connection
        conn.close()
        messagebox.showinfo("Done","The action is done!")

        
        


if __name__ == '__main__':
    app = InventoryApp()
    app.mainloop()

