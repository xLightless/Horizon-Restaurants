import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from client.interface.toolkits import headings
from client.settings import BACKGROUND_COLOR
from client.errors import InvalidCredentialsError
from server.sql.database import database

class ReservationBox:
    def __init__(self, parent, staff_id):
        self._parent = parent 
        self._staff_id = staff_id

        # making and arranging GUI display
        self._title_frame = ttk.Frame(self._parent.content_frame, style="title_frame.TFrame", border=3, relief=tk.SOLID)
        self._input_frame = tk.Frame(self._parent.content_frame)
        self._reservation_frame = tk.Frame(self._parent.content_frame)

        self._title_frame.grid(row=0, column=1, sticky=tk.NSEW)
        self._input_frame.grid(row=1, column=1, sticky=tk.NSEW)
        self._reservation_frame.grid(row=2, column=1, sticky=tk.NSEW)

        self._create_title()
        self._create_input_fields()
        self._create_reservation_buttons()

    def _create_title(self):
        title = headings.Heading6(self._title_frame, text="Horizon Restaurants Make A Reservation")
        title.label.configure(background="#3498db", fg="#FFFFFF")  # blue bg
        title.label.grid(row=0, column=1, sticky=tk.NSEW)

    def _create_input_fields(self):
        # creating input boxes
        labels = ["Customer Name:", "Date:", "Time:", "Table Number:"]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(self._input_frame, text=label).grid(row=i, column=0, sticky=tk.E)
            entry = tk.Entry(self._input_frame)
            entry.grid(row=i, column=1, sticky=tk.W)
            entries.append(entry)

        self._input_entries = entries

    def _create_reservation_buttons(self):
        # make and delete reservation buttons
        tk.Button(self._input_frame, text="Make the Reservation", command=self.make_reservation).grid(row=4, column=0, columnspan=2)
        tk.Button(self._reservation_frame, text="Delete the Reservation", command=self.delete_reservation).grid(row=0, column=0, columnspan=2)

    def make_reservation(self):
        # get inputs from input fields
        customer_name, date, time, table_number = [entry.get() for entry in self._input_entries]

        # validate non empty inputs
        if not all([customer_name, date, time, table_number]):
            messagebox.showerror("Error", "All fields must be filled")
            return

        try:
            # Replace with actual method to make a reservation
            reservation_id = database.make_reservation(customer_name, date, time, table_number)

            # If successful reservation is made
            messagebox.showinfo("Success", f"Reservation was  made successfully! Reservation ID: {reservation_id}")

            # Clear entry boxes after successful reservation
            for entry in self._input_entries:
                entry.delete(0, tk.END)

        except InvalidCredentialsError as e:
            # Show an error message if there's a problem with the reservation operation
            messagebox.showerror("Error", f"Error in making the reservation: {str(e)}")

    def delete_reservation(self):
        # Get reservation ID from entry field
        reservation_id = simpledialog.askinteger("Delete Reservation", "Enter Reservation ID to delete:")

        # Confirm reservation ID exists and not empty
        if not reservation_id:
            messagebox.showerror("Error", "Reservation ID must be filled")
            return

        try:
            # Replace with actual method to delete a reservation
            database.delete_reservation_by_id(reservation_id)

            # When deleted successfully display 'deleted successfully'
            messagebox.showinfo("Success", f"Reservation {reservation_id} deleted successfully!")

        except InvalidCredentialsError as e:
            # Show error message if there's a problem with deleting the reservation
            messagebox.showerror("Error", f"Error in deleting the reservation: {str(e)}")


if __name__ == "__main__":
    # Connect to database
    database.connect_to_database()

    # create GUI window
    root = tk.Tk()

    
    staff_id = "123456"

    # create  instance of the ReservationBox class
    reservation_box = ReservationBox(root, staff_id)

    # Start the Tkinter main loop
    root.mainloop()
