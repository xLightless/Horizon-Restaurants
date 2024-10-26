# --------------------------------------------------------------------------------------- #
# 
#   This is the USER Management page window manager screen module.
#   Any functions related to this particular interface should
#   specifically be programmed in this environment.
# 
# --------------------------------------------------------------------------------------- #

from client.interface.toolkits import headings, inputs
from client.settings import BACKGROUND_COLOR
from client.errors import InvalidCredentialsError, AccountCreationError, AccountDeletionError
from server.sql.database import SQLBranch, SQLStaff
from tkinter import messagebox, simpledialog

import tkinter.ttk as ttk
import tkinter as tk
import random

class UserManagement(object):
    def __init__(self, parent):
        self._parent = parent
        self.style = ttk.Style()
        self.branch = SQLBranch()
        self.sqlstaff = SQLStaff()
        
        # print(self.branch.get_branch_cities())
        
        # Title frame
        self._title_frame = ttk.Frame(self._parent.content_frame, style="um_title_frame.TFrame", name="um_title_frame", border=3, relief=tk.SOLID)
        self.title = headings.Heading6(self._title_frame, text="User Management")
        
        # User management content frame
        self.user_management_frame = ttk.Frame(self._parent.content_frame, style="user_management_frame.TFrame")

        # Personal frame
        self.top_frame = ttk.Frame(self.user_management_frame, style="um_top_frame.TFrame", name="um_top_frame")
        self.personal_lbl_frame = ttk.LabelFrame(self.top_frame, text="Personal Information", style="um_personal_label_frame.TLabelframe", name="um_personal_label_frame")
        self.first_name = inputs.InputBox(self.personal_lbl_frame, label_text="First Name: ")
        self.last_name = inputs.InputBox(self.personal_lbl_frame, label_text="Last Name: ")
        # self.email_address = inputs.InputBox(self.personal_lbl_frame, label_text="Email Address: ")
        self.phone_number = inputs.InputBox(self.personal_lbl_frame, label_text="Phone Number: ")
        
        # Staff frame
        self.middle_frame = ttk.Frame(self.user_management_frame, style="um_middle_frame.TFrame")
        self.staff_lbl_frame = ttk.LabelFrame(self.middle_frame, text="Staff Information", style="um_staff_label_frame.TLabelframe", name="um_staff_label_frame")


        # Generated staff id frame
        self.staff_id_generate_frame = ttk.Frame(self.staff_lbl_frame, style="staff_id_generate_frame.TFrame", padding=12)
        self.staff_id_prefix_label = ttk.Label(self.staff_id_generate_frame, style="staff_id_prefix_label.TLabel", text="Staff ID: ")
        self.staff_id_generate_label = ttk.Label(self.staff_id_generate_frame, style="staff_id_prefix_label.TLabel", text=random.randrange(1280128, 9999999))

        # Password creation
        self.password_frame = ttk.Frame(self.staff_lbl_frame, style="password_frame.TFrame", padding=12)
        self.password_prefix_label = ttk.Label(self.password_frame, style="password_prefix_label.TLabel", text="Set a Password: ")
        self.password_entry = ttk.Entry(self.password_frame)
        
        # Branch role drop down
        self.branch_role_items = ["Staff", "Chef", "Manager", "Admin", "HR Director"]
        self.branch_role_frame = ttk.Frame(self.staff_lbl_frame, style="branch_role_frame.TFrame", padding=12)
        self.branch_role_prefix_label = ttk.Label(self.branch_role_frame, style="branch_role_prefix_label.TLabel", text="Staff Role: ")
        self.branch_role_combobox = ttk.Combobox(self.branch_role_frame, style="branch_role_combobox.TCombobox", values=self.branch_role_items, state='readonly')

        # Branch locations
        self.branch_locations_items = self.branch.get_branch_cities()
        self.city_names = [i for i in self.branch_locations_items["city_name"]]
        # self.city_names_ids = [i for i in self.branch_locations_items['city_id']]
        
        # self.branch_locations_cities = self.branch_locations_items.loc[:, ['city_name']]
        self.branch_locations_frame = ttk.Frame(self.staff_lbl_frame, style="branch_locations_frame.TFrame", padding=12)
        self.branch_locations_prefix_label = ttk.Label(self.branch_locations_frame, style="branch_locations_prefix_label.TLabel", text="Select Location: ")
        self.branch_selection_input = ttk.Combobox(self.branch_locations_frame, style="branch_selection_input.TCombobox")
        self.branch_selection_input2 = ttk.Combobox(self.branch_locations_frame, style="branch_selection_input2.TCombobox", values=self.city_names, state='readonly')
        # self.branch_selection_input2.bind("<<ComboboxSelected>>", func=lambda _: messagebox.showerror("asdas", "asdasd"))
        
        # Submit to database frame
        self.bottom_frame = ttk.LabelFrame(self.user_management_frame, text="Account Operations", style="um_bottom_frame.TLabelframe", name="um_bottom_frame")
        self.button_frame = ttk.Frame(self.bottom_frame, style="um_button_frame.TFrame")
        
        # CRUD buttons
        self.btn_create_account = tk.Button(self.button_frame, text="Create Account")
        self.btn_update_account = tk.Button(self.button_frame, text="Update Account")
        self.btn_delete_account = tk.Button(self.button_frame, text="Delete Account")
        
    def update_select_branch_button(self, city_name):
        """Update the selection of branches from user management screen. """
        
        city_id = self.branch.get_branch_city_id(city_name)
        branches = self.branch.get_branch_locations_of_id(city_id=city_id)
        branches = [f"ID: {branches[i][0]}, POSTCODE: {branches[i][1]}" for i in range(len(branches))]
        print(branches)
        self.branch_selection_input.configure(values=(branches))

    def create_account_button(self):
        """Create a users account from user management screen. """
        
        phone_number = self.phone_number.input_box.get()
        
        if len(phone_number) != 0:
            for char in phone_number:
                if not char.isdigit():
                    print("bad char " + char)
                    messagebox.showerror("Account Creation Error!", AccountCreationError())
                    return
                
            branch_id, branch_postcode = self.branch_selection_input.get().split(',')
            branch_id = branch_id.split("ID: ")[1]
            branch_postcode = branch_postcode.split(" ")[2] + branch_postcode.split(" ")[3]    
            
            branch_role = {
                1: "Staff",
                2: "Chef",
                3: "Manager",
                4: "Admin",
                5: "HR Director"
            }
            branch_role_ = 0
            for key, value in branch_role.items():
                if value == self.branch_role_combobox.get():
                    branch_role_ = key
                    break
            
            data = [
                self.first_name.input_box.get(),
                self.last_name.input_box.get(),
                self.staff_id_generate_label.cget('text'),
                self.password_entry.get(),
                phone_number,
                int(branch_role_),
                int(branch_id)
            ]
            
            try:
                self.sqlstaff.create_staff_user(
                    *data
                )
                messagebox.showinfo("Success!", f"Account with staff id {data[2]} has been created!")
                self.first_name.input_box.selection_clear()
                return
            except:
                messagebox.showerror("Account Creation Error!", AccountCreationError())
                return
                
        messagebox.showerror("Account Creation Error!", AccountCreationError())
        return
        
    def delete_account_button(self):
        """Deletes a users account via staff id in the user management screen."""
        
        staff_id_input = simpledialog.askinteger("Delete an account!", "Enter the staff id of the person to delete:\n")
        
        try:
            self.sqlstaff.del_staff_user(staff_id_number=staff_id_input)
            messagebox.showinfo("Success!", f"You have deleted the user: {staff_id_input}.")
        except:
            messagebox.showerror("Account Deletion Error", AccountDeletionError())
            return
        return

    def display_frames(self):
        """Display user management frames to the top level window. """
        
        # Title Frame
        self._title_frame.grid_rowconfigure(0, weight=0)
        self._title_frame.grid_columnconfigure(0, weight=1)
        self._title_frame.grid_columnconfigure(1, weight=1)
        self._title_frame.grid_columnconfigure(2, weight=1)
        
        # Title
        self.title.label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
        
        # User Management Frame
        self.user_management_frame.grid_rowconfigure(0, weight=1)
        self.user_management_frame.grid_rowconfigure(1, weight=1)
        self.user_management_frame.grid_rowconfigure(2, weight=1) # Button frame
        self.user_management_frame.grid_columnconfigure(0, weight=1)
        
        # Personal info
        # Account operations 1
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_rowconfigure(1, weight=1)
        self.top_frame.grid_rowconfigure(2, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)
        
        # Staff info
        # Account operations 1
        self.middle_frame.grid_rowconfigure(0, weight=1)
        self.middle_frame.grid_rowconfigure(1, weight=1)
        self.middle_frame.grid_rowconfigure(2, weight=1)
        self.middle_frame.grid_columnconfigure(0, weight=1)
        
        # Staff label frame
        self.staff_lbl_frame.grid_rowconfigure(0, weight=1)
        self.staff_lbl_frame.grid_rowconfigure(1, weight=1)
        self.staff_lbl_frame.grid_columnconfigure(0, weight=1)
        self.staff_lbl_frame.grid_columnconfigure(1, weight=1)
        self.staff_lbl_frame.grid(row=0, column=0, sticky=tk.NSEW)

        # Staff generated ID
        self.staff_id_generate_frame.grid_rowconfigure(0, weight=1)
        self.staff_id_generate_frame.grid_columnconfigure(0, weight=1)
        self.staff_id_generate_frame.grid_columnconfigure(1, weight=1)
        self.staff_id_generate_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.staff_id_prefix_label.grid(row=0, column=0, sticky=tk.NSEW)
        self.staff_id_generate_label.grid(row=0, column=1, sticky=tk.NSEW)
        
        # Staff password
        self.password_frame.grid_rowconfigure(0, weight=1)
        self.password_frame.grid_columnconfigure(0, weight=1)
        self.password_frame.grid_columnconfigure(1, weight=1)
        self.password_frame.grid(row=1, column=0, sticky=tk.NSEW)
        self.password_prefix_label.grid(row=0, column=0, sticky=tk.NSEW)
        self.password_entry.grid(row=0, column=1, sticky=tk.NSEW, padx=3)
        
        self.branch_role_frame.grid_rowconfigure(0, weight=1)
        self.branch_role_frame.grid_columnconfigure(0, weight=1)
        self.branch_role_frame.grid_columnconfigure(1, weight=1)
        self.branch_role_frame.grid(row=0, column=1, sticky=tk.NSEW)
        self.branch_role_prefix_label.grid(row=0, column=0, sticky=tk.NSEW)
        self.branch_role_combobox.grid(row=0, column=1, sticky=tk.NSEW, padx=3)
        
        # Branch locations
        self.branch_locations_frame.grid_rowconfigure(0, weight=1)
        self.branch_locations_frame.grid_columnconfigure(0, weight=1)
        self.branch_locations_frame.grid_columnconfigure(1, weight=1)
        self.branch_locations_frame.grid_columnconfigure(2, weight=1)
        self.branch_locations_frame.grid(row=1, column=1, sticky=tk.NSEW)
        self.branch_locations_prefix_label.grid(row=0, column=0, sticky=tk.NSEW)
        self.branch_selection_input.grid(row=0, column=1, sticky=tk.NSEW, padx=3)
        self.branch_selection_input2.grid(row=0, column=2, sticky=tk.NSEW, padx=3)
        
        
        # CRUD Operations
        # Account operations 3
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_rowconfigure(1, weight=1)
        self.bottom_frame.grid_rowconfigure(2, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        
        # Button Frame
        self.button_frame.grid_rowconfigure(0, weight=1)
        self.button_frame.grid_rowconfigure(1, weight=1)
        self.button_frame.grid_rowconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        
        # Styling
        self.style.configure("um_title_frame.TFrame", background=BACKGROUND_COLOR)
        self.style.configure("user_management_frame.TFrame", background=BACKGROUND_COLOR)
        self.style.configure("um_top_frame.TFrame", background=BACKGROUND_COLOR)
        self.style.configure("um_personal_label_frame.TLabelframe", background=BACKGROUND_COLOR)
        self.style.configure("um_personal_label_frame.TLabelframe.Label", background=BACKGROUND_COLOR, foreground='#FFFFFF', font=('Arial', 12, 'bold'))
        self.style.configure("staff_id_generate_frame.TFrame", border=1, relief=tk.SOLID, background=BACKGROUND_COLOR)
        self.style.configure("staff_id_prefix_label.TLabel", background=BACKGROUND_COLOR, foreground="#FFFFFF", font=('Arial', 12, 'bold'))
        self.style.configure("staff_id_generate_label.TLabel", background=BACKGROUND_COLOR, foreground="#FFFFFF", font=('Arial', 12, 'bold'))
        self.style.configure("password_frame.TFrame", border=1, relief=tk.SOLID, background=BACKGROUND_COLOR)
        self.style.configure("password_prefix_label.TLabel", background=BACKGROUND_COLOR, foreground="#FFFFFF", font=('Arial', 12, 'bold'))
        self.style.configure("branch_role_frame.TFrame", border=1, relief=tk.SOLID, background=BACKGROUND_COLOR)
        self.style.configure("branch_role_prefix_label.TLabel", background=BACKGROUND_COLOR, foreground="#FFFFFF", font=('Arial', 12, 'bold'))
        self.style.configure("branch_locations_frame.TFrame", border=1, relief=tk.SOLID, background=BACKGROUND_COLOR)
        self.style.configure("branch_locations_prefix_label.TLabel", background=BACKGROUND_COLOR, foreground="#FFFFFF", font=('Arial', 12, 'bold'))
        self.style.configure("branch_selection_input.TCombobox", state='readonly')
        self.style.configure("branch_selection_input2.TCombobox", state='readonly')
        
        # First name
        self.first_name.get_frame().configure(background=BACKGROUND_COLOR, padx=12, pady=12)
        self.first_name.input_box_label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
        
        # Last name
        self.last_name.get_frame().configure(background=BACKGROUND_COLOR, padx=12, pady=12)
        self.last_name.input_box_label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
        
        # Email address
        # self.email_address.get_frame().configure(background=BACKGROUND_COLOR, padx=12, pady=12)
        # self.email_address.input_box_label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
        
        # Phone number
        self.phone_number.get_frame().configure(background=BACKGROUND_COLOR, padx=12, pady=12)
        self.phone_number.input_box_label.configure(background=BACKGROUND_COLOR, fg="#FFFFFF")
        
        
        # Staff info
        self.style.configure("um_middle_frame.TFrame",  background=BACKGROUND_COLOR)
        self.style.configure("um_staff_label_frame.TLabelframe", background=BACKGROUND_COLOR)
        self.style.configure("um_staff_label_frame.TLabelframe.Label", background=BACKGROUND_COLOR, foreground='#FFFFFF', font=('Arial', 12, 'bold'))
        
        # Generated staff ID label
        # self.style.configure("staff_id_generate_frame.TFrame", background='red')
        
        
        
        
        
        
        
        self.style.configure("um_bottom_frame.TLabelframe", background=BACKGROUND_COLOR)
        self.style.configure("um_bottom_frame.TLabelframe.Label", background=BACKGROUND_COLOR, foreground='#FFFFFF', font=('Arial', 12, 'bold'))
        self.style.configure("um_button_frame.TFrame", background=BACKGROUND_COLOR, border=1, relief=tk.SOLID)
        
        
        # Content frame
        self._title_frame.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
        self.title.label.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)
        
        # User management frame
        self.user_management_frame.grid(row=1, column=0, rowspan=2, columnspan=3, sticky=tk.NSEW)   # Container Frame
        self.top_frame.grid(row=0, column=0, columnspan=3,sticky=tk.NSEW, padx=12, pady=12)         # Personal frame
        self.middle_frame.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW, padx=12, pady=12)     # Staff frame
        self.bottom_frame.grid(row=2, column=0, columnspan=3, sticky=tk.NSEW, padx=12, pady=12)     # CRUD frame
        
        
        
        # Personal frames
        self.personal_lbl_frame.grid(row=0, column=0, sticky=tk.NSEW)
        
        # Personal Inputs
        self.first_name.display(grid=[0, 0], sticky=tk.NSEW)
        self.last_name.display(grid=[1, 0], sticky=tk.NSEW)
        # self.email_address.display(grid=[0, 1], sticky=tk.NSEW)
        self.phone_number.display(grid=[1, 1], sticky=tk.NSEW)
        
        # Account operations frame
        self.button_frame.grid(row=1, column=0, sticky=tk.NSEW, padx=12, pady=12)
        self.btn_create_account.grid(row=0, column=0, rowspan=3, sticky=tk.NSEW)
        self.btn_update_account.grid(row=0, column=1, rowspan=3, sticky=tk.NSEW)
        self.btn_delete_account.grid(row=0, column=2, rowspan=3, sticky=tk.NSEW)
        
        self.branch_selection_input2.bind("<<ComboboxSelected>>", func=lambda _: self.update_select_branch_button(city_name = self.branch_selection_input2))
        self.branch_selection_input.configure(state='readonly')
        
        self.btn_create_account.bind("<ButtonRelease>", func=lambda _: self.create_account_button())
        self.btn_delete_account.bind("<ButtonRelease>", func=lambda _: self.delete_account_button())