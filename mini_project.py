import File_Functions 

products_list = [] #function that imports products file into list and strips whitespace
File_Functions.read_csv_file("products.csv", products_list)
product_dict = {"Product ID": int(products_list[-1]["Product ID"]),
                "Product": "None",
                "Price": "0"}

courier_list = [] #function that imports couriers file into list and strips whitespace
File_Functions.read_csv_file("couriers.csv", courier_list)
courier_dict = {"Courier ID": courier_list[-1]["Courier ID"],
                "Name": "None",
                "Phone Number": "00000000000"}

order_list = []
File_Functions.read_csv_file("Orders.csv", order_list)
order_dict = {"Customer Name": "None",
              "Customer Address": "None",
              "Customer Phone Number": 00000000000,
              "Courier": "None",
              "Order Status": "Processing",
              "Products": 0}

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
                        for dict in products_list:
                            id = dict["Product ID"]
                            name = dict["Product"]
                            price = dict["Price"] 
                            print("ID: {}: {}: £{} ".format(id, name, price))

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
                                else:
                                    float_price = "{:.2f}".format(price)

                                product_dict["Product ID"] +=1
                                product_dict["Product"] = product
                                product_dict["Price"] = float_price 
                                products_list.append(product_dict)

                                break
                            except Exception as e:
                                print(f"An error occured \n{e}")
                                break

                    elif products_menu == 3: # while loop that allows user to edit list via index
                        while True:    
                            try:
                                print(list(enumerate(products_list)))
                                index = int(input("Index:<<< "))
                                product = input("Please enter product name: ").title()
                                if product == "":
                                    pass
                                else: 
                                    products_list[index]["Product"] = product

                                price = float(input("Please enter the products price: "))
                                float_price = "{:.2f}".format(price)
                                if type(price) is not float:
                                    pass
                                else:
                                    products_list[index]["Price"] = float_price
                                break
                            except IndexError:
                                print("Invalid index!!!")
                                break
                            except ValueError:
                                break
                            except Exception as e:
                                print("An error occured!!! {e}")
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
                        for dict in courier_list:
                            id = dict["Courier ID"]
                            name = dict["Name"]
                            phone_number = dict["Phone Number"] 
                            print("ID: {}: {}: {} ".format(id, name, phone_number))
                    
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
                                print("{e}")
                                break
                            break
                    
                    elif courier_menu == 3: # while loop that allows user to edit list via index 
                        while True:    
                            try:
                                print(list(enumerate(courier_list)))
                                index = int(input("Index:<<< "))
                                courier_name = input("Please enter courier name: ").title()
                                if courier_name == "":
                                    pass
                                else: 
                                    courier_list[index]["Name"] = courier_name

                                phone_number = int(input("Please enter the couriers phone number: "))
                                if len(phone_number) is not 11:
                                    pass
                                else:
                                    courier_list[index]["Phone Number"] = phone_number
                                break
                            except IndexError:
                                print("Invalid index!!!")
                                break
                            except ValueError:
                                break
                            except Exception:
                                print("An error occured!!!")
                                break
                    
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
                        for dict in order_list:
                            name = dict["Customer Name"]
                            address = dict["Customer Address"] 
                            phone_number = dict["Customer Phone Number"]
                            Courier = dict["Courier"]
                            status = dict["Order Status"]
                            products = dict["Products"]
                            print("{}: {}: {}: {}: {}: {} ".format(name, address, phone_number, Courier, status, products))
                    elif order_menu == 2:
                        while True:
                            try:
                                Customer_name = input("Please enter your name: ").title()
                                if Customer_name == "":
                                    print("Invalid name!!")
                                    break
                                order_dict["Customer Name"] = Customer_name
                                Customer_address = input("Please enter your Address: ")
                                if Customer_address == "":
                                    print("Invalid address")
                                    break
                                order_dict["Customer Address"] = Customer_address

                                Customer_phone_number = int(input("Please enter your phone number: "))
                                if len(str(Customer_phone_number)) != 10:
                                    print("Invalid Phone number!!!")
                                    break
                                order_dict["Customer Phone Number"] = Customer_phone_number

                                print(list(enumerate(products_list)))
                                items_list = list(map(int, input().split(",")))
                                indexed_list = []
                                for num in items_list:
                                    try:
                                        if products_list[num]:
                                            indexed_list.append(num)
                                            order_dict["Products"] = indexed_list
                                        else:
                                            pass
                                    except IndexError:
                                        pass
                                    except Exception:
                                        print("An error occured!!!")
                                        break

                                print(list(enumerate(courier_list)))
                                courier_index = int(input("Please select a courier via index: "))
                                order_dict["Courier"] = courier_list[courier_index]

                                order_dict["Order Status"] = ["Preparing"]
                                order_list.append(order_dict)
                                break
                            except ValueError:
                                print("Incorrect input!!!")
                                break
                            except IndexError:
                                print("Invalid index!!!")
                                break
                    elif order_menu == 3:
                        while True:
                            try:
                                print(list(enumerate(order_list)))
                                order_list_index = int(input("Please select order via index: "))
                                print(list(enumerate(Order_status)))
                                Order_status_index = int(input("Please update order status via index: "))
                                order_list[order_list_index]["Order Status"] = Order_status[Order_status_index]
                                break
                            except IndexError:
                                print("Invalid index!!")
                                break

                    elif order_menu == 4:
                        while True:
                            try:
                                print(list(enumerate(order_list)))
                                order_list_index = int(input("Please select order via index: "))

                                Customer_name = input("Please enter your name: ").title()
                                if Customer_name == "":
                                    pass
                                else:
                                    order_list[order_list_index]["Customer Name"] = Customer_name

                                Customer_address = input("Please enter your Address: ")
                                if not Customer_address:
                                    pass
                                else:
                                    order_list[order_list_index]["Customer Address"] = Customer_address
                                while True:
                                    try:
                                        Customer_phone_number = int(input("Please enter your phone number: "))
                                        order_list[order_list_index]["Customer Phone Number"] = Customer_phone_number
                                    except ValueError:
                                        break

                                print(list(enumerate(products_list)))
                                try:
                                    items_list = list(map(int, input().split(",")))
                                    indexed_list = []
                                    for num in items_list:
                                        if products_list[num]:
                                            indexed_list.append(num)
                                            order_dict["Products"] = indexed_list
                                    else:
                                        pass
                                except IndexError:
                                    pass
                                except Exception:
                                    pass

                                print(list(enumerate(courier_list)))
                                while True:
                                    try:
                                        courier_index = int(input("Please select a courier via index: "))
                                        order_list[order_list_index]["Courier"] = courier_list[courier_index]                                      
                                        break
                                    except Exception:
                                        break
                                order_list[order_list_index]["Order Status"] = ["Preparing"]
                                break
                            except Exception as e:
                                print(f"An error occurred!! {e}")
                                break
                           

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