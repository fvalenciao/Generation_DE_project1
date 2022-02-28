import csv
from prettytable import PrettyTable
from funcs import wipe, get_prods, get_courier, select_key
from db import execute_query

class Queries():
    
    def __init__(self,table_name):
        self.name = 'Queries' # override for each dependent class
        self.table_name = table_name
        self.props = execute_query(f"SHOW columns FROM {self.table_name}")
        
        # get list of strings with column names
        props_values = []
        for i in self.props:
            props_values.append(i['Field'])
        
        self.props = props_values

    def renumber_ids(self):
        #ID has to be the first column of table
        rows = execute_query(f'SELECT {self.props[1]} FROM {self.table_name}')
        counter = 1
        
        for row in rows:
            row_content = row[self.props[1]]
            execute_query(f'UPDATE {self.table_name} SET {self.props[0]} = {counter} WHERE {self.props[1]} = "{row_content}"')
            counter += 1
            
    def show_contents(self):
        contents = execute_query(f'SELECT * FROM {self.table_name}')

        t = PrettyTable(self.props)
        
        for elem in contents:
            elem_values = list(elem.values())
            t.add_row(elem_values)
            
        print(t)
        return(contents)
        
    def add_elem(self,products,couriers):
        new_elem = []
        cols = []
        counter = 0
        
        for prop in self.props[1:len(self.props)]:
            cols.append(prop)
            
            while True:
                try:
                    if prop == 'items':
                        new_prop = get_prods(products)
                    elif prop == 'courier':
                        new_prop = get_courier(couriers)
                    elif prop == 'status':
                        new_prop = 'Preparing'
                    else:
                        new_prop = input(f'Please enter the {prop} for the new {self.name} or press 0 to return to the menu: \n')
                        wipe()
                        
                    if new_prop == '0':
                        return
                    else:
                        if prop != 'status':
                            user_inp = input(f'Press 1 to CONFIRM "{new_prop}" as the {prop} for the new {self.name} \nPress 0 to return to the menu \n')
                            wipe()
                            
                            if int(user_inp) == 1:
                                new_elem.append(f'"{new_prop}"')
                                counter += 1
                                break
                            
                            elif int(user_inp) == 0:
                                return
                            
                            else:
                                wipe()
                                print('Incorrect input. Please try again \n')
                        else:
                            new_elem.append(f'"{new_prop}"')
                            counter += 1
                            break
                    
                except:
                    wipe()
                    print('Incorrect input. Please try again \n')
        
        if counter == len(self.props)-1:
            props_str = ', '.join(cols)
            values_str = ', '.join(new_elem)
            try:
                execute_query(f'INSERT INTO {self.table_name} ({props_str}) VALUES ({values_str})')
                self.renumber_ids()
                print(f'The new {self.name} has been successfully created. \n')
            except:
                wipe()
                print(f'An error has occurred: The new {self.name} could not be created. Please try again')
    
    def list_prop(self, prop):
        contents = execute_query(f'SELECT * FROM {self.table_name}')
        prop_list = []
        for elem in contents:
            prop_list.append(elem[prop])
        return(prop_list)
    
    def update_elem(self,products,couriers):
        while True:
            contents = self.show_contents()
            try:
                elem_num = int(input(f'\n Please enter ID of {self.name} to be updated or press 0 to return to the menu: \n'))
                
                if elem_num == 0:
                    break
                
                elif elem_num > 0:
                    if elem_num <= len(contents):
                        user_inp = int(input(f'Press 1 to confirm you wish to update {self.name} n. "{elem_num}" \nPress 0 to return to the menu \n'))
                        wipe()
                    
                        if user_inp == 1:
                            
                            elem_col = select_key(self.props)
                            curr_value_dict = execute_query(f'SELECT {elem_col} FROM {self.table_name} WHERE {self.props[0]} = {elem_num}')
                            curr_value = curr_value_dict[0][elem_col]
                            print(f'The current {elem_col} for this {self.name} is "{curr_value}".')
                            
                            if elem_col == 'items' or elem_col == 'courier':
                                
                                user_inp2 = int(input(f'Press 1 to confirm you wish to update the "{elem_col}" in this {self.name}\nPress 0 to return to the menu \n'))
                                wipe()
                                
                                if user_inp2 == 1:
                                    if elem_col == 'items':
                                        new_val = get_prods(products)
                                    elif elem_col == 'courier':
                                        new_val = get_courier(couriers)
                                        
                                    user_inp3 = int(input(f'Press 1 to confirm "{new_val}" as the "{elem_col}" for this {self.name}\nPress 0 to return to the menu \n'))
                                    wipe()
                                    
                                    if user_inp3 == 1:
                                        try:
                                            execute_query(f'UPDATE {self.table_name} SET {elem_col} = "{new_val}" WHERE {self.props[0]} = {elem_num}')
                                            print(f'{elem_col} in {self.name} n. {elem_num} has been successfully updated')
                                            self.renumber_ids()
                                            break
                                        except:
                                            wipe()
                                            print(f'An error has occurred: The {self.name} could not be updated. Please try again')
                                    
                                    elif user_inp3 == 0:
                                        break
                                    else:
                                        wipe()
                                        print('Incorrect input. Please try again \n')
                                
                                elif user_inp2 == 0:
                                    break
                                else:
                                    wipe()
                                    print('Incorrect input. Please try again \n')
                            else:
                                new_val = input(f'Please enter new {elem_col} or press 0 to cancel.\n')
                            
                                if new_val == '0':
                                    break
                                else:
                                    user_inp2 = int(input(f'Press 1 to confirm "{new_val}" as the {elem_col} for this {self.name}\nPress 0 to return to the menu \n'))
                                    wipe()
                                    
                                    if user_inp2 == 1:
                                        try:
                                            execute_query(f'UPDATE {self.table_name} SET {elem_col} = "{new_val}" WHERE {self.props[0]} = {elem_num}')
                                            print(f'{elem_col} in {self.name} n. {elem_num} has been successfully updated')
                                            self.renumber_ids()
                                            break
                                        except:
                                            wipe()
                                            print(f'An error has occurred: The {self.name} could not be updated. Please try again')
                                    
                                    elif user_inp2 == 0:
                                        break
                                    else:
                                        wipe()
                                        print('Incorrect input. Please try again \n')
                            
                        elif user_inp == 0:
                            break
                        
                        else:
                            wipe()
                            print('Incorrect input. Please try again \n')
                    else:
                        wipe()
                        print(f'Incorrect input. Please enter the ID of an existing {self.name} \n')
                else:
                    wipe()
                    print('Incorrect input. Please try again \n')
            except:
                wipe()
                print('Incorrect input. Please try again. \n')
    
    def delete_elem(self):
        while True:
            contents = self.show_contents()
        
            try:
                elem_num = int(input(f'\n Please enter index of {self.name} to be deleted or press 0 to return to the menu: \n'))
                
                if elem_num == 0:
                    break
                
                elif elem_num > 0:
                    if elem_num <= len(contents):
                        user_inp = int(input(f'Press 1 to confirm you wish to delete {self.name} n. {elem_num} \nPress 0 to return to the menu \n'))
                        wipe()
                    
                        if user_inp == 1:
                            execute_query(f'DELETE FROM {self.table_name} WHERE {self.props[0]} = {elem_num}')
                            print(f'{self.name} n. {elem_num} has been successfully deleted')
                            self.renumber_ids()
                            break
                        
                        elif user_inp == 0:
                            break
                        
                        else:
                            wipe()
                            print('Incorrect input. Please try again \n')
                    else:
                        wipe()
                        print(f'Incorrect input. Please enter the ID of an existing {self.name} \n')    
                else:
                    wipe()
                    print('Incorrect input. Please try again. \n')
                    
            except:
                wipe()
                print('Incorrect input. Please try again. \n')

    def save_csv(self,file_path):
        contents = execute_query(f'SELECT * FROM {self.table_name}')
        
        with open(file_path, 'w',1,'utf-8') as f:
            fieldnames = self.props
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in contents:
                writer.writerow(row)

class ProductQueries(Queries):
    
    def __init__(self, table_name):
        super().__init__(table_name)
        
        self.name = 'Product'
        self.menu = """ PRODUCT OPTIONS:
    Press 0 to return to MAIN MENU.
    Press 1 to SEE FULL LIST of existing products
    Press 2 to add a NEW PRODUCT
    Press 3 to UPDATE existing PRODUCT
    Press 4 to DELETE existing PRODUCT
    """

class CourierQueries(Queries):
    
    def __init__(self, table_name):
        super().__init__(table_name)
        
        self.name = 'Courier'
        self.menu = """ COURIER LIST OPTIONS:
    Press 0 to return to MAIN MENU.
    Press 1 to SEE FULL LIST of couriers
    Press 2 to add a NEW COURIER
    Press 3 to UPDATE existing COURIER
    Press 4 to DELETE existing COURIER
    """

class OrderQueries(Queries):
    def __init__(self, table_name):
        super().__init__(table_name)
        
        self.name = 'Order'
        self.menu = """ ORDER OPTIONS:
    Press 0 to return to MAIN MENU.
    Press 1 to SEE FULL LIST of existing orders
    Press 2 to ADD a new order
    Press 3 to UPDATE STATUS of an order
    Press 4 to UPDATE existing order
    Press 5 to DELETE existing order
    """
        self.status_list = ['Preparing', 'Waiting for courier', 'Out for delivery', 'Delivered']

    def update_status(self):
        
        while True:
            contents = self.show_contents()
            
            try:
                elem_num = int(input(f'\n Please enter ID of {self.name} to get status update or press 0 to return to the menu: \n'))
            
                if elem_num == 0:
                    break
                
                elif elem_num > 0:
                    if elem_num <= len(contents):

                        user_inp = int(input(f'Press 1 to confirm status update for {self.name} n. "{elem_num}"  \nPress 0 to return to the menu \n'))
                        wipe()
                    
                        if user_inp == 1:
                            elem_col = 'status'
                            if contents[elem_num-1]['status'] == 'Preparing':
                                new_val = 'Waiting for courier'
                            elif contents[elem_num-1]['status'] == 'Waiting for courier':
                                new_val = 'Out for delivery'
                            elif contents[elem_num-1]['status'] == 'Out for delivery':
                                new_val = 'Delivered'
                            elif contents[elem_num-1]['status'] == 'Delivered':
                                wipe()
                                print('This order has already been delivered.')
                                break
                            
                            execute_query(f'UPDATE {self.table_name} SET {elem_col} = "{new_val}" WHERE {self.props[0]} = {elem_num}')
                            
                            print(f'The {self.name} status has successfully been updated to "{new_val}"')
                            break                        
                        
                        elif user_inp == 0:
                            break
                        
                        else:
                            wipe()
                            print('Incorrect input. Please try again \n')
                    
                    else:
                        wipe()
                        print(f'Incorrect input. Please enter the ID of an existing {self.name} \n')
                
                else:
                    wipe()
                    print('Incorrect input. Please try again \n')
            except:
                wipe()
                print(f'Incorrect input. Please try again\n')