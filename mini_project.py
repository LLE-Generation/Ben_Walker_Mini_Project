from logging import exception
import File_Functions


while True: # While loop that will display the main menu
    try:
        main_menu = int(input("\nMain Menu\n4 - Customer Menu\n3 - Order_Menu\n2 - Courier_Menu\n1 - Products_Menu\no - Exit\n<<< ")) #Main menu
        if main_menu == 0: # closes the system if user enters the value 0
            products = File_Functions.get_dict_data("select * from products")
            File_Functions.write_csv_file("Products.csv", products)
            couriers = File_Functions.get_dict_data("select * from couriers")
            File_Functions.write_csv_file("Couriers.csv", couriers)
            customers = File_Functions.get_dict_data("select * from customers")
            File_Functions.write_csv_file("Customers.csv", customers)
            orders = File_Functions.get_dict_data("select * from orders")
            File_Functions.write_csv_file("Orders.csv", orders)
            break # breaks loop and ends program
        elif main_menu == 1: # moves on to the options menu if user enters the value 1
            while True: # while loop that displays the options menu
                try: #Products menu
                    products_menu = int(input(("\nProducts_Menu\n----------------\n4 - Delete_Product\n3 - Edit_Product\n2 - Add_Product\n1 - Show_Products\n0 - Main_Menu\n<<< ")))
                    
                    if products_menu == 0: # returns to main menu if user enters the value 0
                        break

                    elif products_menu == 1: # displays the users list if the user enters the value 1
                        File_Functions.print_products()

                    elif products_menu == 2: # while loop that allows user to add product
                        while True:    
                            try:
                                product = input("\n\n\nPlease enter product name: ").title()
                                if product == "":
                                    print("Invalid product name")
                                    break                                    
                                price = float(input("\n\n\nPlease enter the products price: "))
                                if type(price) is not float:
                                    print("Invalid input!")
                                    break
                                else:
                                    float_price = "{:.2f}".format(price)
                                File_Functions.add_product(product, price)
                                break
                            except Exception as e:
                                print(f"An error occured \n{e}")
                                break

                    elif products_menu == 3: # while loop that allows user to edit list via index
                        while True:
                            try:
                                id = int(input("\n\n\nID:<<< "))
                                if not id:
                                    print("Product ID required!!!")
                                    break
                                product = input("\n\n\nPlease enter product name: ").title()
                                price = float(input("\n\n\nPlease enter the products price: "))
                                float_price = "{:.2f}".format(price)
                                File_Functions.edit_product(id, product, float_price)
                                break
                            except ValueError:
                                print("An error ocurred!!!")
                                break
                        
                    elif products_menu == 4: # while loop that allows user to delete product
                        while True:
                            try:
                                File_Functions.print_products()
                                id = int(input("\n\n\nPlease enter product ID to delete: "))
                                if not id:
                                    print("\n\n\nProduct ID required!!!")
                                    break
                                File_Functions.delete_product(id)
                                break
                            except exception as e:
                                print("An error occured!!")
                                break
                except exception:
                    break

        elif main_menu == 2: # moves on to the Courier menu if user enters the value 2
            while True: # while loop that displays the courier menu
                try:
                    courier_menu = int(input(("\n\n\n\nCourier_Menu\n-----------------\n4 - Delete_Courier\n3 - Edit_Courier\n2 - Add_Courier\n1 - Show_Couriers\n0 - Main_Menu\n<<< ")))
                    if courier_menu == 0: # returns to main menu if user enters the value 0
                        break
                    
                    elif courier_menu == 1: # displays the courier list 
                        File_Functions.print_couriers()
                    
                    elif courier_menu == 2: # add to courier list
                        while True:   
                            try:
                                first_name = input("\n\n\nCourier first name: ").title()
                                if not first_name:
                                    print("First name required!!!")
                                    break
                                last_name = input("\n\n\nCourier last name: ").title()
                                if not last_name:
                                    print("First name required!!!")
                                    break
                                try:
                                    phone_number = input("\n\n\nCourier phone number: ")
                                    if not int(phone_number):
                                        print("Invalid phone number")
                                        break
                                    if len(phone_number) not in range(8, 12):                         
                                        print("Invalid phone number!!!")
                                        break
                                except ValueError:
                                    print("Invalid phone number!!!")
                                    break
                                else:    
                                    File_Functions.add_courier(first_name, last_name, phone_number)
                                    break
                            except ValueError:
                                print("Invalid input!!")
                                break
                    
                    elif courier_menu == 3: # while loop that allows user to edit list via index 
                        while True:    
                            try:
                                id = int(input("\n\n\nID:<<< "))
                                if not id:
                                    print("Courier ID required!!!")
                                    break
                                first_name = input("\n\n\nCourier first name: ").title()
                                last_name = input("\n\n\nCourier last name: ").title()
                                try:
                                    phone_number = input("\n\n\nCourier phone number")
                                    if len(phone_number) not in range(8, 14):
                                        phone_number = ""
                                    if not int(phone_number):
                                        phone_number = ""
                                except ValueError:
                                    phone_number = ""
                                File_Functions.edit_courier(id, first_name, last_name, phone_number)
                                break
                            except IndexError:
                                print("Invalid index!!!")
                                break
                            except ValueError:
                                print("Invalid input")
                                break
                            except Exception as e:
                                print(f"An error occured!!! {e}")
                                break
                    
                    elif courier_menu == 4: # while loop that allows user to delete courier
                        try:
                            File_Functions.print_couriers()
                            id = int(input("\n\n\nPlease enter courier ID to delete: "))
                            File_Functions.delete_courier(id)
                        except ValueError:
                            pass
                        except TypeError:
                            pass
                        
                
                except ValueError as e:
                    print("Please enter a valid number!")

        elif main_menu == 3:
            while True:
                try:
                    order_menu = int(input("\n\n\n\nOrder_menu\n----------------------\n5 - Delete_Order\n4 - Update_Order\n3 - Update_Order_Status\n2 - Add_User_Details\n1 - Print_Orders\n0 - Main_Menu\n<<< "))
                    if order_menu == 0:
                        break
                    elif order_menu == 1:
                        File_Functions.print_orders()
                        
                    elif order_menu == 2:
                        while True:
                            try:
                                File_Functions.print_customers()
                                customer_id = int(input("\n\n\nCustomer_id<<<"))
                                if not customer_id:
                                    print("\n\n\nCustomer ID required!!!")
                                    break
                                File_Functions.print_couriers()
                                courier_id = int(input("\n\n\nCourier id"))
                                if not customer_id:
                                    print("Customer ID required!!!")
                                    break
                                File_Functions.print_products()
                                product_list = list(map(int, input("\n\n\nProduct ID <<<").split(",")))
                                if not product_list:
                                    print("Product ID required!!!")
                                    break

                                File_Functions.add_orders(customer_id, courier_id, product_list)
                                break
                            except ValueError:
                                print("Incorrect input!!!")
                                break
                            except IndexError as e:
                                print(f"Invalid index!!! {e}")
                                break
                    elif order_menu == 3:
                        while True:
                            File_Functions.print_orders()
                            order_id = int(input("Order id <<< "))
                            File_Functions.execute_query("\n\n\nUpdate orders set order_status = %s where order_id = %s", ("Preparing", order_id))
                            break
                    elif order_menu == 4:
                        while True:
                            try:
                                File_Functions.print_orders()
                                order_id = int(input("\n\n\nOrder id<<<"))
                                if not order_id:
                                    print("\n\n\nOrder id required!!!")
                                    break
                                File_Functions.print_customers()
                                customer_id = int(input("\n\n\nCustomer_id<<<"))

                                File_Functions.print_couriers()
                                courier_id = int(input("\n\n\nCourier id"))

                                File_Functions.print_products()
                                product_id = int(input("\n\n\nProduct id<<"))


                                File_Functions.edit_orders(order_id, customer_id, courier_id, product_id)
                                break
                            except ValueError:
                                print("Invalid input!!!")
                                break

                    elif order_menu == 5:
                        order_id = int(input("\n\n\nOrder id<<< "))
                        File_Functions.delete_order(order_id)

                except IndexError as e:
                    print(f"Invalid index!! {e}")
                except ValueError as e:
                    print("Please enter a valid number!")
        
        elif main_menu == 4:
            while True:
                try:
                    customer_menu = int(input(("\\n\n\nnCustomer_Menu\n-----------------\n4 - Delete User\n3 - Edit User\n2 - Create user\n1 - Show_Customers\n0 - Main_Menu\n<<< ")))
                    if customer_menu == 0:
                        break
                    elif customer_menu == 1:
                        File_Functions.print_customers()
                    elif customer_menu == 2:
                        while True:
                            try:
                                first_name = input("\n\n\nEnter your first name: ").title()
                                if not first_name:
                                    print("First name required!!!")
                                    break
                                last_name = input("\n\n\nEnter your last name: ").title()
                                if not last_name:
                                    print("Last name required!!!")
                                    break
                                phone_number = input("\n\n\nEnter your phone number: ")
                                if len(phone_number) not in range(8,12):
                                    print("Invalid phone number!!!")
                                    break
                                if not int(phone_number):
                                    print("Invalid phone number!!!")
                                    break
                                street_town = input("\n\n\nEnter your street and town names: ").title()
                                if not street_town:
                                    print ("Street name and town required!!!")
                                    break
                                postcode = input("\n\n\nEnter your postcode: ").upper()
                                if not postcode:
                                    print("Postcode required!!!")
                                    break
                                File_Functions.add_customer(first_name, last_name, phone_number, street_town, postcode)
                                break
                            except ValueError:
                                print("Invalid input!!!")
                                break
                    elif customer_menu == 3:
                        while True:
                            try:
                                File_Functions.print_customers()
                                customer_id = int(input("\n\n\nEnter your customer ID: "))
                                if not customer_id:
                                    print("Customer ID required!!!")
                                    break
                                first_name = input("\n\n\nEnter your first name: ").title()
                                last_name = input("\n\n\nEnter your last name: ").title()
                                try:
                                    phone_number = input("\n\n\nEnter your phone number: ")
                                    if len(phone_number) not in range(8,12):
                                        phone_number = ""
                                    if not int(phone_number):
                                        phone_number = ""
                                except ValueError:
                                    phone_number = ""       
                                street_town = input("\n\n\nEnter your street and town names: ").title()
                                postcode = input("\n\n\nEnter your postcode: ").upper()
                                File_Functions.edit_customer(customer_id, first_name, last_name, phone_number, street_town, postcode)
                                break
                            except ValueError:
                                print("Invalid input!!!")
                                break
                    elif customer_menu == 4:
                        File_Functions.print_customers()
                        while True:
                            try:
                                customer_id = int(input("\n\n\nEnter your customer ID: "))
                                if not customer_id:
                                    print("Customer ID required!!!")
                                    break
                                File_Functions.delete_customer(customer_id)
                                break
                            except ValueError:
                                print("Invalid input!!!")
                                break
                except exception as e:
                    print(f"An error ocurred!! {e}")
                    break

        else:
            print("\nInvalid input!")
    
    except ValueError as e:
        print("Please enter a valid number!")
    
    except Exception as e:
        print(f"An error has occurred!!!\n{e}")
        break

print("System Exit!!!")

