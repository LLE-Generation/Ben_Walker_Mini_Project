import File_Functions 

products_list = [] #function that imports products file into list and strips whitespace
File_Functions.read_csv_file("products.csv", products_list)
product_dict = {"Product": "None",
"Price": "0"}

courier_list = [] #function that imports couriers file into list and strips whitespace
File_Functions.read_csv_file("couriers.csv", courier_list)
courier_dict = {"Name": "None",
"Phone Number": "00000000000"}

order_list = []
File_Functions.read_csv_file("Orders.csv", order_list)
order_dict = {"Customer Name": "None",
"Customer Address": "None",
"Customer Phone Number": "0000000",
"Courier": "None",
"Order Status": "Processing"}

Order_status = ["Processing", "Preparing", "Shipping", "Delivered"]
    
while True: # While loop that will display the main menu
    try:
        main_menu = int(input("\nMain Menu\n3 - Order_Menu\n2 - Courier_Menu\n1 - Products_Menu\no - Exit\n<<< ")) #Main menu
        if main_menu == 0: # closes the system if user enters the value 0
            File_Functions.write_csv_file("products.csv", products_list) # function that writes list to file then closes file
            File_Functions.write_csv_file("couriers.csv", courier_list) # function that writes list to file then closes file
            File_Functions.write_csv_file("Orders.csv", order_list)
            break # breaks loop and ends program
        elif main_menu == 1: # moves on to the options menu if user enters the value 1
            while True: # while loop that displays the options menu
                try: #Products menu
                    products_menu = int(input(("\nProducts_Menu\n----------------\n4 - Delete_Product\n3 - Edit_Product\n2 - Add_Product\n1 - Show_Products\n0 - Main_Menu\n<<< ")))
                    
                    if products_menu == 0: # returns to main menu if user enters the value 0
                        break

                    elif products_menu == 1: # displays the users list if the user enters the value 1
                        File_Functions.print_list(products_list)

                    elif products_menu == 2: # while loop that allows user to add product
                        while True:    
                            try:
                                product = input("Please enter product name: ").title()
                                if product == "":
                                    print("Invalid product name")
                                    break

                                price = float(input("Please enter the products price: "))
                                if type(price) is not float:
                                    print("Invalid input!")
                                    break
                                float_price = "{:.2f}".format(price)
                                product_dict = {"Product": product,
                                "Price": float_price}

                                products_list.append(product_dict)
                                break
                            except Exception as e:
                                break

                    elif products_menu == 3: # while loop that allows user to edit list via index
                        while True:    
                            try:
                                product = input("Please enter product name: ").title()
                                if product == "":
                                    print("Invalid product name")
                                    break

                                price = float(input("Please enter the products price: "))
                                if type(price) is not float:
                                    print("Invalid input!")
                                    break
                                float_price = "{:.2f}".format(price)
                                product_dict = {"Product": product,
                                "Price": float_price}

                                File_Functions.edit_list(products_list, product_dict)
                                break
                            except Exception:
                                print("An error occurred!!")
                                break

                    elif products_menu == 4: # while loop that allows user to delete product
                        File_Functions.del_list_element(products_list)
                    else:
                        print("\nInvalid input!")
                
                except ValueError as e:
                    print("Please enter a valid number!")

        elif main_menu == 2: # moves on to the Courier menu if user enters the value 2
            while True: # while loop that displays the courier menu
                try:
                    courier_menu = int(input(("\nCourier_Menu\n-----------------\n4 - Delete_Courier\n3 - Edit_Courier\n2 - Add_Courier\n1 - Show_Couriers\n0 - Main_Menu\n<<< ")))
                    if courier_menu == 0: # returns to main menu if user enters the value 0
                        break
                    
                    elif courier_menu == 1: # displays the courier list 
                        File_Functions.print_list(courier_list)
                    
                    elif courier_menu == 2: # add to courier list
                        while True:   
                            try:
                                courier_name = input("Please enter courier name: ").title()
                                if courier_name == "":
                                    print("Invalid name")
                                    break
                                phone_number = input(int("Please enter the couriers phone number: "))
                                if len(phone_number) is not 11:
                                    print("Invalid phone number")
                                    break
                                courier_dict = {"Name": courier_name,
                                "Phone Number": phone_number}

                                courier_list.append(courier_dict)
                            except Exception as e:
                                break
                            break
                    
                    elif courier_menu == 3: # while loop that allows user to edit list via index 
                        courier_name = input("Please enter courier name: ").title()
                        phone_number = input("Please enter the couriers phone number: ")

                        courier_dict = {"Name": courier_name,
                        "Phone Number": phone_number}

                        File_Functions.edit_list(courier_list, courier_dict)
                    
                    elif courier_menu == 4: # while loop that allows user to delete courier
                        File_Functions.del_list_element(courier_list)
                    else:
                        print("\nInvalid input!")
                
                except ValueError as e:
                    print("Please enter a valid number!")

        elif main_menu == 3:
            while True:
                try:
                    order_menu = int(input("\nOrder_menu\n----------------------\n5 - Delete_Order\n4 - Update_Order\n3 - Update_Order_Status\n2 - Add_User_Details\n1 - Print_Orders\n0 - Main_Menu\n<<< "))
                    if order_menu == 0:
                        break
                    elif order_menu == 1:
                        File_Functions.print_list(order_list)
                    elif order_menu == 2:
                        Customer_name = input("Please enter your name: ").title()
                        order_dict["Customer Name"] = Customer_name

                        Customer_address = input("Please enter your Address: ").title()
                        order_dict["Customer Address"] = Customer_address

                        Customer_phone_number = int(input("Please enter your phone number: "))
                        order_dict["Customer Phone Number"] = Customer_phone_number

                        print(list(enumerate(courier_list)))
                        courier_index = int(input("Please select a courier via index: "))
                        order_dict["Courier"] = courier_list[courier_index]

                        order_dict["Order Status"] = ["Preparing"]
                        order_list.append(order_dict)
                    elif order_menu == 3:
                        print(list(enumerate(order_list)))
                        order_list_index = int(input("Please select order via index: "))
                        print(list(enumerate(Order_status)))
                        Order_status_index = int(input("Please update order status via index: "))
                        order_list[order_list_index]["Order Status"] = Order_status[Order_status_index]

                    elif order_menu == 4:
                        print(list(enumerate(order_list)))
                        order_list_index = int(input("Please select order via index: "))

                        Customer_name = input("Please enter your name: ").title()
                        if Customer_name == "":
                            print("Invalid input!!")
                            break
                        else:
                            order_list[order_list_index]["Customer Name"] = Customer_name

                        Customer_address = input("Please enter your Address: ").title()
                        if Customer_address == "":
                            print("Invalid input!!")
                            break
                        else:
                            order_list[order_list_index]["Customer Address"] = Customer_address

                        Customer_phone_number = int(input("Please enter your phone number: "))
                        if Customer_phone_number == "":
                            print("Invalid input!!")
                            break
                        else:
                            order_list[order_list_index]["Customer Phone Number"] = Customer_phone_number

                        print(list(enumerate(courier_list)))
                        courier_index = int(input("Please select a courier via index: "))
                        order_list[order_list_index]["Courier"] = courier_list[courier_index]

                        order_list[order_list_index]["Order Status"] = ["Preparing"]

                    elif order_menu == 5:
                        File_Functions.del_list_element(order_list)

                except IndexError as e:
                    print("Invalid index!!")
                except ValueError as e:
                    print("Please enter a valid number!")
        else:
            print("\nInvalid input!")
    
    except ValueError as e:
        print("Please enter a valid number!")
    
    except Exception as e:
        print(f"An error has occurred!!!\n{e}")
        break

print("System Exit!!!")