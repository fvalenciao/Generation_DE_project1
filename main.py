#%%
from funcs import wipe, print_main_menu
from classes import OrderQueries, ProductQueries, CourierQueries

# # LOAD PRODUCTS AND   COURIERS
prods_file = r'data\products.csv'
cours_file = r'data\couriers.csv'
order_file = r'data\orders.csv'

products = ProductQueries('products')
couriers = CourierQueries('couriers')
orders = OrderQueries('orders')

prod_list = products.list_prop('prod_name')
cour_list = couriers.list_prop('cour_name')

while True:
    wipe()
    print_main_menu()
    user_inp = input()
    
    if user_inp == '0':
        break
    
    ## PRODUCT OPTIONS
    elif user_inp == '1':
        wipe()
        while True:
            
            print(products.menu)
            user_inp2 = int(input())
            
            if user_inp2 == 0:
                wipe()
                print('Returning to main menu')
                break
            
            elif user_inp2 == 1:
                wipe()
                products.show_contents()
                
            elif user_inp2 == 2:
                wipe()
                products.add_elem(prod_list,cour_list)
                prod_list = products.list_prop('prod_name')
            
            elif user_inp2 == 3:
                wipe()
                products.update_elem(prod_list,cour_list)
                prod_list = products.list_prop('prod_name')
            
            elif user_inp2 == 4:
                wipe()
                products.delete_elem()
                prod_list = products.list_prop('prod_name')
    
    ## COURIER OPTIONS
    elif user_inp == '2':
        wipe()
        while True:
            
            print(couriers.menu)
            user_inp2 = int(input())
            
            if user_inp2 == 0:
                wipe()
                print('Returning to main menu')
                break
            
            elif user_inp2 == 1:
                wipe()
                couriers.show_contents()
                
            elif user_inp2 == 2:
                wipe()
                couriers.add_elem(prod_list,cour_list)
                cour_list = couriers.list_prop('cour_name')
            
            elif user_inp2 == 3:
                wipe()
                couriers.update_elem(prod_list,cour_list)
                cour_list = couriers.list_prop('cour_name')
            
            elif user_inp2 == 4:
                wipe()
                couriers.delete_elem()
                cour_list = couriers.list_prop('cour_name')

    ## ORDER OPTIONS            
    elif user_inp == '3':
        wipe()
        while True:
            
            print(orders.menu)
            user_inp2 = int(input())
            
            if user_inp2 == 0:
                wipe()
                print('Returning to main menu')
                break
            
            elif user_inp2 == 1:
                wipe()
                orders.show_contents()
                
            elif user_inp2 == 2:
                wipe()
                orders.add_elem(prod_list, cour_list)
            
            elif user_inp2 == 3:
                wipe()
                orders.update_status()
                
            elif user_inp2 == 4:
                wipe()
                orders.update_elem(prod_list, cour_list)
            
            elif user_inp2 == 5:
                wipe()
                orders.delete_elem()

wipe()
print('Exporting changes to CSV files...')
products.save_csv(prods_file)
couriers.save_csv(cours_file)
orders.save_csv(order_file)
print('All changes have been successfully saved.')
print('Closing app. Thank you.')