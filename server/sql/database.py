import mysql.connector
import warnings
import pandas as pd
import random

# Disables pandas sql warning
warnings.simplefilter(action='ignore', category=UserWarning)

class Database(object):
    def __init__(
        self,
        host:str = "localhost",
        user:str = "root",
        password:str = "Password1",
        database:str = ""
    ):
        """ Establish a mysql connection 

        Args:
            host (str, optional): Name or IP address of the server host - and TCP/IP port.
            user (str, optional): Name of the user to connect with. Defaults to "root".
            password (str, optional): The user's password.
            database (str, optional): The name of the database.

        """
    
        self.__db = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        
        self.cursor = self.__db.cursor()
            
    def get_table(self, table:str, dataframe:bool = False):
        """ Gets the raw table of a database. Can be used in polymorphism

        Args:
            table (str): Name of the table to display.
            dataframe (bool, optional): Display a Pandas DataFrame of 'table'. Defaults to False.

        """
        
        query = "SELECT * FROM %s;" % table
        if dataframe == False:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.__db.commit()
            return result

        dataframe = pd.read_sql_query(query, self.__db)
        df = pd.DataFrame(dataframe)
        return df
    
    def get_table_header_x(self, table:str, column_name:str):
        """ Returns the integer position and name of a table column name

        Args:
            table (str): Name of the table.
            column_name (str): Column name of 'table'

        Returns:
            tuple: (column_name, column_x)
        """
        
        # Fetches a new table result
        self.get_table(table)
        try:
            col_int = 0
            for item in self.cursor.column_names:
                col_int += 1
                if item == column_name:
                    # Set parent table header and header position int
                    head_id = item
                    head_id_int = col_int
                    return head_id,head_id_int
        except IndexError:
            pass
    
    def get_table_record(self, table:str, row:int, dataframe: bool = False):
        """ Gets a single row from a table via row number

        Args:
            table (str): Name of the table.
            row (int): The row or record index of a tuple in a table.
            dataframe (bool, optional): Display a Pandas DataFrame of 'table'. Defaults to False.

        Returns:
            tuple | DataFrame: Returns record of table.
        """
        
        query = "SELECT * FROM %s;" % table
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.__db.commit()
        if dataframe == False:
            try:
                return (result[row] if row <= len(result) else IndexError)
            except IndexError:
                return f"Invalid row/record in {table}."
        
        dataframe = pd.read_sql_query(query, self.__db)
        df = pd.DataFrame(dataframe)
        return "%s" %  df.iloc[[row]]
    
    def get_table_value_record(self, table:str, column_name:str, value:str):
        """ Gets a table record by value rather than row number

        Args:
            table (str): Name of the table.
            column_name (str): The column name in 'table'.
            value (str): The value in 'column_name' to get a record.

        Returns:
            tuple: Returns record of table.
        """
        
        try:
            query = "SELECT * FROM %s WHERE %s = '%s'" % (table, column_name, value)
            self.cursor.execute(query)
            return self.cursor.fetchall()[0]
        except IndexError:
            return f"Invalid row/record in {table}."
    
    def get_table_column(self, table:str, column_name:str) -> tuple:
        """ Gets the column header and values from a table

        Args:
            table (str): Name of the table.
            column_name|key (str): FK or PK or column name of table

        Returns:
            tuple: (column_name, column_y)
        """
        
        query = "SELECT %s FROM %s;" % (column_name, table)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if self.cursor.column_names[0] == column_name:
            return (self.cursor.column_names[0], result)
        
    def get_table_cell(self, table:str, column_name:str, row:int):
        """ Gets the unknown cell data of a column in a table

        Args:
            table (str): Name of the table.
            column_name (str): The column name in 'table'.
            row (int): The iterable row of the record.
        """
        
        query = "SELECT * FROM %s WHERE %s = %s;" % (table, column_name, row)
        self.cursor.execute(query)
        self.cursor.fetchall()
        
        # Passes stubhead into function to return column_name position as integer
        column_int = int(self.get_table_header_x(table, column_name)[1])
        
        try:
            # Gets a record from a table using the row given by the user
            record = self.get_table_record(table, row)
            
            # Uses column_int to go across the record row to find the value of a cell
            for x in range(len(record)):
                if x == column_int-1:
                    return record[x]
        except IndexError:
            pass
        
    def count_table_rows(self, table:str) -> int:
        """ Returns the total record rows in a table

        Args:
            table (str): Name of the table.

        Returns:
            int: Total number of rows in 'table'.
        """
        
        query = "SELECT * FROM %s" % table
        self.cursor.execute(query)
        self.cursor.fetchall()
        rows = int(self.cursor.rowcount)
        return rows
        
    def set_table_record(self, table:str, pk_id:int, values:tuple):
        """ Insert a new record of tuple values into a database table

        Args:
            table (str): Name of the table.
            pk_id (int): Primary key value to enter into 'table'.
            values (tuple): Tuple of values to insert into 'table'.
        """
        
        record_values = "', '".join((values))
        query = f"INSERT INTO {table} VALUES ({pk_id}, '{record_values}')"
        self.cursor.execute(query)
        self.__db.commit()
        
    def is_value_in_table(self, table:str, column_name:str, value:str) -> bool:
        """ Checks if value is in a table already """
        
        # Probably an inefficient method on a large scale of table data
        # Checks if table is empty and returns False if so        
        table_column = self.get_table_column(table, column_name=column_name)[1]
        for column in table_column:
            for row in column:
                if row == value:
                    return True if row == value else False
    
    def get_table_record_y(self, table:str, column_name:str, value:str) -> tuple:
        """ Returns the integer value of a tuple row

        Args:
            table (str): Name of the table.
            column_name (str): The column name in 'table'.
            value (str): The value in 'column_name' to return integer position

        Returns:
            tuple: (record, record_y)
        """
        
        tbl = self.get_table_column(table, column_name)[1]
        row_int = 0
        for column in tbl:
            for row in column:
                row_int += 1
                if row == value:
                    return (row, row_int)
        
    def truncate_table_data(self, table:str) -> list:
        """ Removes all records from a table """
        
        query = "TRUNCATE TABLE %s" % table
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_primary_key_record(self, table:str, pk_id):
        """ Similar to get_table_record() except uses the primary key instead of row number """
        
        query = "SHOW COLUMNS FROM %s" % table
        self.cursor.execute(query)
        pk_column_name = str(self.cursor.fetchall()[0][0])
        
        query = "SELECT * FROM %s WHERE %s = '%s'" % (table, pk_column_name, pk_id)
        
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()[0]
        except IndexError:
            return "Primary key '%s' not found in '%s'." % (pk_id, table)
    
    def update_table_record_value(self, table:str, column_name:str, value, pk_column_name:str, pk_id):
        """ Update a table record by setting a new value in a single row

        Args:
            table (str): Name of the table.
            column_name (str): The column name in 'table'.
            set_value (_type_): Updates the current value to a new value.
            pk_column_name (str): Primary key column name.
            pk_id (int): Primary key column name ID.
        """
        
        #UPDATE TABLE SET COLUMN = VALUE WHERE PRIMARY_KEY = VALUE
        query = "UPDATE %s SET %s = '%s' WHERE %s = %s" % (table, column_name, value, pk_column_name, pk_id)
        self.cursor.execute(query)
        self.__db.commit()
        
    def update_table_record_values(self, table:str, column_names:tuple, values:tuple, pk_column_name:str, pk_id:int):
        """ Update the entire row of a record obtained by primary key id
        
        Args:
            table (str): Name of the table.
            column_name (str): The column name in 'table'.
            set_value (_type_): Updates the current value to a new value.
            pk_column_name (str): Primary key column name.
            pk_id (int): Primary key column name ID.
        """
        
        build_values = ""
        build_list = list(values)
        build_columns = list(column_names)
        
        for i in range(len(build_columns)):
            if i != len(build_columns)-1:
              build_values = build_values + build_columns[i] + ' = ' + "'" + build_list[i] + "'" + ', '
            else:
                build_values = build_values + build_columns[i] + ' = ' + "'" + build_list[i] + "'"

        query = "UPDATE %s SET %s WHERE %s = '%s'" % (table, build_values, pk_column_name, pk_id)
        self.cursor.execute(query)
        self.__db.commit()
        
    def get_table_records_of_key(self, table:str, key_column_name:str, key:int, dataframe:bool = False):
        """ Obtains multiple records of the same column_name value e.g. if KEY = 25000 then return all records of 25000."""
        
        self.cursor.close() # Close cursor without buffer
        cursor_buffer = self.__db.cursor(buffered=True) # Open new connection
        query = "SELECT * FROM %s WHERE %s = '%s';" % (table, key_column_name, key)
        cursor_buffer.execute(query)
        self.__db.commit()
        
        if dataframe == False:
            result = cursor_buffer.fetchall()
            cursor_buffer.close()
            self.cursor = self.__db.cursor()
            return result
        
        # Produce a dataframe of sql query
        dataframe = pd.read_sql_query(query, self.__db)
        df = pd.DataFrame(dataframe)
        
        # Close old cursor and open original connection
        cursor_buffer.close()
        self.cursor = self.__db.cursor()
        return df
    
    def get_table_records_of_value(self, table:str, column_name:str, value, dataframe:bool = False):
        """ Obtains multiple records of the same column_name value e.g. if KEY = 25000 then return all records of 25000."""
        
        self.cursor.close() # Close cursor without buffer
        cursor_buffer = self.__db.cursor(buffered=True) # Open new connection
        query = "SELECT * FROM %s WHERE %s = '%s'" % (table, column_name, value)
        cursor_buffer.execute(query)
        self.__db.commit()
        
        if dataframe == False:
            result = cursor_buffer.fetchall()
            cursor_buffer.close()
            self.cursor = self.__db.cursor()
            return result
        
        # Produce a dataframe of sql query
        dataframe = pd.read_sql_query(query, self.__db)
        df = pd.DataFrame(dataframe)
        
        # Close old cursor and open original connection
        cursor_buffer.close()
        self.cursor = self.__db.cursor()
        return df

    def del_table_record(self, table:str, column_name:str, value):
        """ Delete a table row from the database """
        
        query = "DELETE FROM %s WHERE %s = '%s'" % (table, column_name, value)
        self.cursor.execute(query)
        self.__db.commit()
         
    def count_permissible_rows(self, table:str, column_name:str, value):
        """ Counts rows from an sql where clause
        
        Args:
            table (str): Name of the table.
            column_name (str): The column name in 'table'.
            value (str): The value in 'column_name' to return integer position.

        Returns:
            tuple (int, int): x and y of 'table'.
        
        """
        
        query = "SELECT * FROM %s WHERE %s = '%s'" % (table, column_name, value)
        self.cursor.execute(query)
        self.cursor.fetchall()
        rows = int(self.cursor.rowcount)
        return rows
    
    def insert_table_null_record(self, table:str, pk_id:int, values:tuple, null_column:int):
        """ Insert a new record into the database including a null record. This works by inserting the NULL value between values.

        Args:
            table (str): Name of the table.
            pk_id (int): Primary key value to enter into 'table'.
            values (tuple): Tuple of values to insert into 'table'.
            null_column (int): The column to insert NULL.
        """
        
        values_list = list(values)
        sub_list = []
        
        # -1 would be the primary key
        for col in range(0, len(values_list)):
            # Place NULL item between list items
            if col == null_column:
                
                # Make a sub list and clear entries past null
                sub_list = values_list[col::]
                del values_list[col::]
                
                # Append NULL and add the old values back
                values_list.append('NULL')
                for item in sub_list:
                    values_list.append(item)
                
        
        # Append null value to value list if not found null_column
        list_length = len(values_list)
        if null_column >= list_length:
            values_list.append('NULL')
            
        values = tuple(values_list)
        str_values = str(values)
        
        # Remove quotes from NULL
        if 'NULL' in str_values:
            prefix = str_values.find('NULL') - 1
            suffix = str_values.find('NULL') + 4
            build_values = ""
            startswith = str_values.find('(')
            endswith = str_values.find(')')
            for char in range(len(str_values)):
                if (char != prefix) and (char != suffix) and (char != startswith) and (char != endswith):
                    build_values = build_values + str_values[char]
        values = build_values
        
        # Build NULL query
        query = "INSERT INTO %s VALUES (%s, %s)" % (table, pk_id, values)
        self.cursor.execute(query)
        self.__db.commit()
        
        
        
database = Database(database="horizon_restaurants2")

class SQLMenu(object):
    def get_menu_table(self):
        """Returns the whole menus table from the database. """
        return database.get_table("menu_items", True)
    
    def get_menu(self):
        """Gets a limited menu dataframe consisting of [item name, description, price]. """
        
        data = self.get_menu_table()
        columns = ["item_name", "description", "price"]
        data = data.loc[:, columns]
        return data

    def get_menu_allergen(self, item_name):
        try:
            
            menu_item_record = database.get_table_value_record("menu_items", "item_name", item_name)
            menu_item_id = menu_item_record[0] if menu_item_record else None

            if menu_item_id:
                
                allergen_record = database.get_table_value_record("menu_allergens", "menu_item_idx", menu_item_id)
                allergen_id = allergen_record[0] if allergen_record else None

                if allergen_id:
                   
                    allergen_name_record = database.get_table_value_record("allergens", "allergen_id", allergen_id)
                    allergen_name = allergen_name_record[1] if allergen_name_record else None

                    if allergen_name:
                        return {
                            'menu_item_id': menu_item_id,
                            'allergen_id': allergen_id,
                            'allergen_name': allergen_name
                        }
        except Exception as e:
            print(f"Error in get_additional_items: {str(e)}")
        return None
    def count_menu_table_rows(self):

        total_items = database.count_table_rows("menu_items")
        return total_items

    def get_menu_item_record(self, row:int, dataframe: bool = False):
        return database.get_table_record("menu_items", row, dataframe)

    def get_all_menu_items(self):
        """ Fetch all menu items at once """
        return database.get_table("menu_items")

    def insert_new_order(self, order_date, order_time, order_price, order_discount, menu_item_id, order_status):
        current_max_order_id = database.count_table_rows("orders")
        new_order_id = current_max_order_id + 1
        print("Attempting to insert order with menu_item_id:", menu_item_id)

        values = (order_date, order_time, order_price, order_discount, order_status, str(menu_item_id))

        database.set_table_record("orders", new_order_id, values)

        return new_order_id
        
        
class SQLKitchenOrders(object):
    def get_displayed_orders(self):
        # If this number is set then the reservation has no table.
        NO_TABLE_NUMBER = 999

        # Get data from the database and filter the data for relevant columns.
        orders = self.get_paid_orders().loc[:, ["order_id", "order_status", "menu_item_id"]]
        menu = SQLMenu().get_menu_table().loc[:, ["menu_item_id", "item_name"]]
        res = SQLReservations().get_reservations()
        
        # Merge the data into a table
        merged_data = pd.merge(pd.merge(orders, menu, on='menu_item_id', how='left'), res, left_on='order_id', right_on='reservation_id', how='left')
        
        # Filter out menu_item_id, reservation_id, date, and time.
        merged_data = merged_data[['order_id', 'order_status', 'item_name', 'table_number']]
        
        # If the person did not set a reservation table, assume its for delivery or staff food.
        merged_data['table_number'] = merged_data['table_number'].fillna(NO_TABLE_NUMBER)
        
        return merged_data
    
    def get_orders(self, dataframe=True):
        """Return orders table. """
        
        orders = database.get_table("orders", dataframe)
        return orders
    
    def get_paid_orders(self):
        """Returns only orders that have been paid for by customers but not plated. """
        
        orders = database.get_table_records_of_value("orders", "order_status", "PAID", True)
        return orders      
     
    def cancel_kitchen_order(self, order_id_pk):
        """Updates an order to cancelled due to it being removed by kitchen staff. """
        
        # Updates the order to cancelled.
        database.update_table_record_value("orders", "order_status", "CANCELLED", "order_id", order_id_pk)
     
    def get_bulk_orders(self):
        return
    
    def mark_order_as_ready(self, order_primary_key, serve_date, serve_time):
        """Updates an order to 'mark as ready' by kitchen staff. """
        
        # Get the order id via kitchen table
        kitchen_order = database.get_table_value_record("kitchen", "order_id", order_primary_key)
        record_primary_key = kitchen_order[0]
        
        # If a kitchen/order record exists, update the order as completed along with a serve datetime.
        if type(record_primary_key) == int:
            database.update_table_record_value("kitchen", "serve_date", value=serve_date, pk_column_name="kitchen_id", pk_id=record_primary_key)
            database.update_table_record_value("kitchen", "serve_time", value=serve_time, pk_column_name="kitchen_id", pk_id=record_primary_key)
            database.update_table_record_value("orders", "order_status", "COMPLETED", "order_id", order_primary_key)
    
    def get_sequential_orders(self, table_number:int):
        return
    
    def check_category_item_availability(self, category_name:str) -> dict:
        return
    
    def get_item(self, item_name:int) -> dict:
        return
    

class SQLReservations(object):
    def get_customers(self):
        return database.get_table("customer", True)
    
    def get_reservations(self):
        return database.get_table("reservations", True)
    
    # def create_reservation(self, date, time, table_number, first_name, last_name, phone_number, allergen_id):
    #     """ Creates a reservation for a customer along with their allergens and info.

    #     Args:
    #         date (_type_): YYYY-MM-DD
    #         time (_type_): HH:MM:SS
    #         table_number (_type_): the table number.
    #         first_name (_type_): customer first name.
    #         last_name (_type_): customer last name.
    #         phone_number (_type_): customer phone number.
    #         allergen_id (_type_): allergen id.
    #     """
        
    #     reservations = self.get_reservations()
    #     len_reservations = len(reservations['reservation_id'])
    #     reservation_id = len_reservations + 1
    #     database.set_table_record("reservations", reservation_id, values=(date, time, table_number))
        
    #     customers = self.get_customers()
    #     len_customers = len(customers['customer_id'])
    #     customer_id = len_customers + 1
    #     database.set_table_record("customers", customer_id, values=(first_name, last_name, phone_number, allergen_id))
    
    def create_reservation(self, date, time, table_number, first_name, last_name, phone_number, allergen_name):
        """ Creates a reservation for a customer along with their allergens and info.

        Args:
            date (_type_): YYYY-MM-DD
            time (_type_): HH:MM:SS
            table_number (_type_): the table number.
            first_name (_type_): customer first name.
            last_name (_type_): customer last name.
            phone_number (_type_): customer phone number.
            allergen_name (_type_): allergen name.
        """
        
        reservations = self.get_reservations()
        len_reservations = len(reservations['reservation_id'])
        reservation_id = len_reservations + 1
        database.set_table_record("reservations", reservation_id, values=(date, time, table_number))
        
        #get row number and 
        customers = self.get_customers()
        len_customers = len(customers['customer_id'])
        customer_id = random.randint(1, 1000000)
        # database.set_table_record("customer", customer_id, values=(first_name, last_name, phone_number, allergen_name))
        
        # corelate allergen name to allergen ID from 1 to 15
        allergen_id = self.get_allergen_id(allergen_name)
        
        # insert customer table with information
        database.set_table_record("customer", customer_id, values=(first_name, last_name, str(phone_number), str(allergen_id)))
        
        #insert kitchen id and reservation id into kitchen table
        # kitchen = SQLKitchenOrders()
        # kitchen_id = len(kitchen.get_orders()['order_id']) + 1
        # database.set_table_record("kitchen", kitchen_id, values=(date, time, str(customer_id), str(reservation_id), "0", "0"))
        
    def get_allergen_id(self, allergen_name):
        #Gets the allergen ID based on the allergen name. """
        menu_allergens = database.get_table("allergens", True)
        allergen_id = menu_allergens[menu_allergens['allergen_name'] == allergen_name]['allergen_id'].values[0]
        return allergen_id
    
    def delete_reservation(self, reservation_id):
        """ This function deletes a row in reservations of the given parameter. """
        
        database.del_table_record("reservations", "reservation_id", value=str(reservation_id))

class SQLBranch(object):
    def get_branch_cities(self):
        return database.get_table("branch_cities", True)
    
    def get_branch_locations(self):
        return database.get_table("branch_locations", True)
    
    def get_branch_locations_of_id(self, city_id):
        return database.get_table_records_of_value("branch_locations", "city_id", city_id)
    
    def get_branch_city_id(self, city_name):
        record = database.get_table_value_record("branch_cities", "city_name", city_name.get())
        city_id = record[0]
        return city_id
        
class SQLStaff(object):
    def create_staff_user(self, first_name, last_name, staff_id_number, password, phone, branch_role, branch_id):
        pk_id = database.count_table_rows("staff")
        pk_id = pk_id + 1
        database.set_table_record("staff", pk_id=pk_id, values=(first_name, last_name, str(staff_id_number), password, str(phone), "NONE",str(branch_role), str(branch_id)))
        
    def del_staff_user(self, staff_id_number):
        database.del_table_record("staff", "staff_id_number", staff_id_number)
    
    # def get_branches_of_city_id(self, city_id):
    #     return database.get_table_records_of_value("branch_locations", "city_id", city_id, True)