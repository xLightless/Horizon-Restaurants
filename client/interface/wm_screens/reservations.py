import tkinter as tk
from tkinter import messagebox
import pymysql

class ReservationBox:
    def __init__(self, root):
        # Initialize the Tkinter application
        self.root = root
        self.root.title("Reservations System Page")

        # connect to the MySQL database
        self.conn = pymysql.connect(
            host='localhost',
            user='   ',  # MySQL username
            password='   ',  #  MySQL password
            database='horizon_restaurants',  # Change to your database name
            charset='utf8mb4', #character set, to take in diverse text inputs..
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

        # Create and arrange GUI components
        tk.Label(root, text="Date:").grid(row=0, column=0)
        tk.Label(root, text="Time:").grid(row=1, column=0)
        tk.Label(root, text="Table Number:").grid(row=2, column=0)
        tk.Label(root, text="Branch ID:").grid(row=3, column=0)
        tk.Label(root, text="Customer ID:").grid(row=4, column=0)

        self.date_entry = tk.Entry(root)
        self.time_entry = tk.Entry(root)
        self.table_number_entry = tk.Entry(root)
        self.branch_id_entry = tk.Entry(root)
        self.customer_id_entry = tk.Entry(root)

        self.date_entry.grid(row=0, column=1)
        self.time_entry.grid(row=1, column=1)
        self.table_number_entry.grid(row=2, column=1)
        self.branch_id_entry.grid(row=3, column=1)
        self.customer_id_entry.grid(row=4, column=1)

        # Button to initiate reservation creation
        tk.Button(root, text="Make Reservation", command=self.make_reservation).grid(row=5, column=0, columnspan=2)

    def make_reservation(self):
        # Get values from entry fields
        date = self.date_entry.get()
        time = self.time_entry.get()
        table_number = self.table_number_entry.get()
        branch_id = self.branch_id_entry.get()
        customer_id = self.customer_id_entry.get()

        # Validate non-empty entries
        if not date or not time or not table_number or not branch_id or not customer_id:
            messagebox.showerror("Error", "All fields must be filled")
            return

        try:
            # Insert data into the 'reservations' table in the database
            self.cursor.execute('''
                INSERT INTO reservations (date, time, table_number, branch_id, customer_id)
                VALUES (%s, %s, %s, %s, %s)
            ''', (date, time, table_number, branch_id, customer_id))

            # Make the changes to the database
            self.conn.commit()

            # If succesful reservation is made
            messagebox.showinfo("Success", "Reservation made successfully!")

            # Clear entry boxes after successful reservation
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.table_number_entry.delete(0, tk.END)
            self.branch_id_entry.delete(0, tk.END)
            self.customer_id_entry.delete(0, tk.END)

        except pymysql.Error as e:
            # Show an error message if there's an problem with the database operation
            messagebox.showerror("Error", f"Error in making the reservation: {str(e)}")


if __name__ == "__main__":
    # Create Tkinter root gui window and start the application
    root = tk.Tk()
    app = ReservationBox(root)
    root.mainloop()
