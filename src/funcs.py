import csv
import os

## GENERAL FUNCTIONS
def wipe():
    """Clears command window"""
    os.system('cls')
    
def print_list(inp_list):
    """Takes a list of strings as input and prints the contents of the list with an index next to them (starting from '1')."""
    i = 1
    for elem in inp_list:
        print(f'{i}. {elem}')
        i += 1
    print('\n')

def print_main_menu():
    """Prints main menu for the app."""
    menu = """PLEASE SELECT ONE OF THE FOLLOWING OPTIONS:
    Press 1 to see PRODUCT OPTIONS
    Press 2 to see COURIER OPTIONS
    Press 3 to see ORDER OPTIONS
    Press 0 to EXIT app """
    print(menu)
    return()

def get_prods(prod_list):
    """Takes a list of strings as input and allows the user to select elements from the list.
    Returns a string with all the selected elements separated by commas."""
    while True:
        print_list(prod_list)
        try: 
            prod_index = int(input('Please enter the index of a product or press 0 to return to the menu: \n'))
            wipe()
            
            if prod_index == 0:
                order_prods = False
                return(order_prods)
            
            elif prod_index > 0:
                prod = prod_list[prod_index - 1]
                order_prods = [prod]
                
                while True:
                    print_list(prod_list)
                    prod_index = int(input('Please enter the index of another product or press 0 to finish: \n'))
                    wipe()
            
                    if prod_index == 0: # turn order_prods list into string and return it
                        order_prods_string = ''
                        
                        cont = 0
                        
                        for i in order_prods:
                            if cont == 0:
                                order_prods_string += i
                                
                            else:
                                order_prods_string += f', {i}'
                            
                            cont += 1
                            
                        order_prods = order_prods_string
                        
                        return(order_prods)
                    
                    elif prod_index > 0:
                        new_prod = prod_list[prod_index - 1]
                        order_prods.append(new_prod)
                    
                    else:
                        wipe()
                        print('Incorrect input. Please enter the index number of an existing product \n')
            else:
                wipe()
                print('Incorrect input. Please enter the index number of an existing product \n')
                
        except:
            wipe()
            print('Incorrect input. Please enter the index number of an existing product \n')

def get_courier(cour_list):
    while True:
        print_list(cour_list)
    
        try: 
            cour_index = int(input('Please enter the index of a courier or press 0 to return to the menu: \n'))
            wipe()
            
            if cour_index == 0:
                order_courier = False
                return(order_courier)
            
            elif cour_index > 0:
                order_courier = cour_list[cour_index - 1]
                return(order_courier)
                
            else:
                wipe()
                print('Incorrect input. Please enter the index number of an existing courier \n')
        
        except:
            wipe()
            print('Incorrect input. Please enter the index number of an existing courier \n')

def select_key(props):
    """Takes a list of strings as input. 
    Returns the element of the list selected by the user"""
    while True:
        print_list(props)
        try:
            user_inp = int(input('\n Please enter index of field to be updated or press 0 to return to the menu: \n'))
            
            if user_inp == 0:
                break
            
            elif user_inp > 0:
                key = props[user_inp-1]
                print(f'Press 1 to UPDATE "{key}"\nPress 0 to cancel \n')
                user_inp2 = int(input())
                wipe()
            
                if user_inp2 == 1:
                    return(key)
                
                elif user_inp2 == 0:
                    break
                
                else:
                    wipe()
                    print('Incorrect input. Please try again.')
            else:
                wipe()
                print('Incorrect input. Please try again.')
        except:
            print('Incorrect input. Please try again.')
