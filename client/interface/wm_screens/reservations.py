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
        #calling methods for creation and configuration inpute fields reservation buttons and title
        self._create_title()
        self._create_input_fields()
        self._create_reservation_buttons()
        
        self._title_frame.grid(row=0, column=1, sticky=tk.NSEW)
        self._input_frame.grid(row=1, column=1, sticky=tk.NSEW)
        self._reservation_frame.grid(row=2, column=1, sticky=tk.NSEW)
        
        self._parent.configure(bg="black")
        #background color for input fraame
        self._input_frame.configure(bg="black")
        # reservation frame background color
        self._reservation_frame.configure(bg="black")
        #set title frme background color
        self._title_frame.configure(style="Black.TFrame")
        
        text_color="white"
        #set text color throughout gui windown
        for widget in self._reservation_frame.winfo_children():
            widget.configure(fg=text_color)
        
        for widget in self._title_frame.winfo_children():
            widget.configure(fg=text_color)

        for widget in self._input_frame.winfo_children():
            widget.configure(fg=text_color)


    def _create_title(self):
        title = headings.Heading6(self._title_frame, text="Horizon Restaurants Make A Reservation")
        title.label.configure(background="#3498db", fg="white")  # blue bg
        title.label.grid(row=0, column=1, sticky=tk.NSEW)

   
   
    def _create_input_fields(self):
        # creating input boxes
        labels = ["First Name: ", "Last Name: ", "Phone Number: ", "Table Number: "]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(self._input_frame, text=label).grid(row=i, column=0, sticky=tk.E)
            entry = tk.Entry(self._input_frame)
            entry.grid(row=i, column=1, sticky=tk.W)
            entries.append(entry)

        # create a drop down with allergen names.
        tk.Label(self._input_frame, text="Allergen Name:").grid(row=4, column=0, sticky=tk.E)
        allergen_names = ["Gluten", "Lupin", "Celery", "Crustaceans", "Milk", "Sulphur Dioxide", "Sesame", "Molluscs", "Mustard", "Nuts", "Eggs", "Fish", "Soybeans", "Peanuts", "None"]
        allergen_dropdown = ttk.Combobox(self._input_frame, values=allergen_names)
        allergen_dropdown.grid(row=4, column=1, sticky=tk.W)
        entries.append(allergen_dropdown)
        
        self._input_entries = entries

    
    
    def _create_reservation_buttons(self):
        # make and delete reservation buttons
        tk.Button(self._input_frame, text="Make the Reservation", command=self.make_reservation).grid(row=6, column=0, columnspan=2)
        tk.Button(self._reservation_frame, text="Delete the Reservation", command=self.delete_reservation).grid(row=0, column=0, columnspan=2)

    
    
    def make_reservation(self):
        # get inputs from input fields
       # customer_name = self._input_entries[0].get()
        first_name = self._input_entries[0].get()
        last_name = self._input_entries[1].get()
        phone_number = self._input_entries[2].get()
        table_number = self._input_entries[3].get()
        allergen_name = self._input_entries[4].get()  # get allergen_name from the dropdown
        
        # validate non-empty inputs
        if not first_name or not last_name or not table_number:
            messagebox.showerror("Error", "Customer Name, Table Number must be filled")
            return

        try:
            # replace with actual method to make a reservation
            current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            reservation_id = self.reservations.create_reservation(
                first_name=first_name,
                last_name=last_name,
                date=current_date_time.split(" ")[0],
                time=current_date_time.split(" ")[1],
                table_number=table_number,
                phone_number=phone_number,
                allergen_name=allergen_name  # use allergen_name selected from dropdown
            )

            # once a successful reservation is made display
            messagebox.showinfo("Success", f"Reservation was made successfully! Reservation ID: {reservation_id}")

            # clear input boxes after a successful reservation
            for entry in self._input_entries:
                entry.delete(0, tk.END)

        except InvalidCredentialsError as e:
            # Show an error message if there's a problem with the reservation operation
            messagebox.showerror("Error", f"Error in making the reservation: {str(e)}")



    def delete_reservation(self):
        # get reservation ID from entry field
        reservation_id = simpledialog.askinteger("Delete Reservation", "Enter Reservation ID to delete:")

        # confirm reservation ID exists in database and not empty
        if not reservation_id:
            messagebox.showerror("Error", "Reservation ID must be filled")
            return

        try:
            # replace with actual method to delete a reservation
            self.reservations.delete_reservation(reservation_id)

            # when reservation deleeted output 'deleted successfully'
            messagebox.showinfo("Success", f"Reservation {reservation_id} deleted successfully!")

        except InvalidCredentialsError as e:
            # show an error message if there's a problem with deleting reservation
            messagebox.showerror("Error", f"Error in deleting the reservation: {str(e)}")
