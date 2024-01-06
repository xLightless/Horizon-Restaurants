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

        # Create and arrange GUI components
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
        title = headings.Heading6(self._title_frame, text="Reservations System Page")
        title.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
        title.label.grid(row=0, column=1, sticky=tk.NSEW)

    def _create_input_fields(self):
        # Create and arrange input fields
        labels = ["Reservation ID:", "Date:", "Time:", "Table Number:", "Branch ID:", "Customer ID:"]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(self._input_frame, text=label).grid(row=i, column=0, sticky=tk.E)
            entry = tk.Entry(self._input_frame)
            entry.grid(row=i, column=1, sticky=tk.W)
            entries.append(entry)

        self._input_entries = entries

    def _create_reservation_buttons(self):
        # Create and arrange reservation buttons
        tk.Button(self._input_frame, text="Make Reservation", command=self.make_reservation).grid(row=6, column=0, columnspan=2)
        tk.Button(self._reservation_frame, text="Delete Reservation", command=self.delete_reservation).grid(row=0, column=0, columnspan=2)

    def make_reservation(self):
        # Get values from input fields
        reservation_id, date, time, table_number, branch_id, customer_id = [entry.get() for entry in self._input_entries]

        # Validate non-empty entries
        if not all([reservation_id, date, time, table_number, branch_id, customer_id]):
            messagebox.showerror("Error", "All fields must be filled")
            return

        try:
            # Insert data into the 'reservations' table in the database
            database.insert_into_reservations(reservation_id, date, time, table_number, branch_id, customer_id)

            # If successful reservation is made
            messagebox.showinfo("Success", "Reservation made successfully!")

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
            # Remove the reservation from the 'reservations' table in the database
            database.delete_reservation_by_id(reservation_id)

            # When deleted successfully display 'deleted successfully'
            messagebox.showinfo("Success", f"Reservation {reservation_id} deleted successfully!")

        except InvalidCredentialsError as e:
            # Show error message if there's a problem with deleting the reservation
            messagebox.showerror("Error", f"Error in deleting the reservation: {str(e)}")


if __name__ == "__main__":
    # Connect to dtb
    database.connect_to_database()

    # creeate GUI window
    root = tk.Tk()

    # Assume staff_id is available after successful login (replace with actual staff_id logic)
    staff_id = "123456"

    # Create an instance of the ReservationBox class
    reservation_box = ReservationBox(root, staff_id)

    # Start the Tkinter main loop
    root.mainloop()
