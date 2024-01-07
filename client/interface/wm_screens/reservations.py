import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from client.interface.toolkits import headings
from client.settings import BACKGROUND_COLOR
from client.errors import InvalidCredentialsError
from server.sql.database import SQLReservations
import datetime
import random

class Reservations:
    def __init__(self, parent):
        self._parent = parent
        self.reservations = SQLReservations()

        # making and arranging GUI display
        self._title_frame = ttk.Frame(self._parent.content_frame, style="title_frame.TFrame", border=3, relief=tk.SOLID)
        self._input_frame = tk.Frame(self._parent.content_frame)
        self._reservation_frame = tk.Frame(self._parent.content_frame)

    def display_frames(self):
        self._create_title()
        self._create_input_fields()
        self._create_reservation_buttons()
        
        self._title_frame.grid(row=0, column=1, sticky=tk.NSEW)
        self._input_frame.grid(row=1, column=1, sticky=tk.NSEW)
        self._reservation_frame.grid(row=2, column=1, sticky=tk.NSEW)

    def _create_title(self):
        title = headings.Heading6(self._title_frame, text="Horizon Restaurants Make A Reservation")
        title.label.configure(background="#3498db", fg="#FFFFFF")  # blue bg
        title.label.grid(row=0, column=1, sticky=tk.NSEW)

    def _create_input_fields(self):
        # creating input boxes
        labels = ["Customer Name:", "First Name:", "Last Name:", "Allergen Info:", "Date:", "Time:", "Table Number:"]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(self._input_frame, text=label).grid(row=i, column=0, sticky=tk.E)
            entry = tk.Entry(self._input_frame)
            entry.grid(row=i, column=1, sticky=tk.W)
            entries.append(entry)

        self._input_entries = entries

    def _create_reservation_buttons(self):
        # make and delete reservation buttons
        tk.Button(self._input_frame, text="Make the Reservation", command=self.make_reservation).grid(row=7, column=0, columnspan=2)
        tk.Button(self._reservation_frame, text="Delete the Reservation", command=self.delete_reservation).grid(row=0, column=0, columnspan=2)

    def make_reservation(self):
        # get inputs from input fields
        customer_name = self._input_entries[0].get()
        first_name=self._input_entries[0].get()
        last_name=self._input_entries[1].get()
        
        #get allergen info for allergic cutomers
        allergen_info=self._input_entries[2].get()
        
        # Generate automatic Date and Time
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%H:%M")

        # Generate a random Table Number (assuming the range is from 1 to 20)
        table_number = str(random.randint(1, 35))
        
        # Generate automatic Date and Time
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%H:%M")

        # Generate a random Table Number (assuming the range is from 1 to 20)
        table_number = str(random.randint(1, 20))
        # validate non-empty inputs
        if not customer_name or not date or not time or not table_number:
            messagebox.showerror("Error", "Customer Name, Date, Time, and Table Number must be filled")
            return

        try:
            # Replace with actual method to make a reservation
            reservation_id = self.reservations.create_reservation(
                first_name=first_name,
                last_name=last_name,
                date=date,
                time=time,
                table_number=table_number,
                phone_number="",
                allergen_info= allergen_info
            )

            # If successful reservation is made
            messagebox.showinfo("Success", f"Reservation was made successfully! Reservation ID: {reservation_id}")

            # clear input boxes after successful reservation
            for entry in self._input_entries:
                entry.delete(0, tk.END)

        except InvalidCredentialsError as e:
            # Show an error message if there's a problem with the reservation operation
            messagebox.showerror("Error", f"Error in making the reservation: {str(e)}")

    def delete_reservation(self):
        # Get reservation ID from entry field
        reservation_id = simpledialog.askinteger("Delete Reservation", "Enter Reservation ID to delete:")

        # confirm reservation ID exists in database and not empty
        if not reservation_id:
            messagebox.showerror("Error", "Reservation ID must be filled")
            return

        try:
            # replace with actual method to delete a reservation
            self.reservations.delete_reservation(reservation_id)

            # When deleted successfully display 'deleted successfully'
            messagebox.showinfo("Success", f"Reservation {reservation_id} deleted successfully!")

        except InvalidCredentialsError as e:
            # show an error message if there's a problem with deleting reservation
            messagebox.showerror("Error", f"Error in deleting the reservation: {str(e)}")
            messagebox.showerror("Error", f"Error in deleting the reservation: {str(e)}")