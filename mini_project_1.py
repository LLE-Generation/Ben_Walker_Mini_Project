import File_Functions

products_list = [] #function that imports products file into list and strips whitespace
File_Functions.read_file("products.txt", products_list)
    
courier_list = [] #function that imports couriers file into list and strips whitespace
File_Functions.read_file("couriers.txt", courier_list)
    
while True: # While loop that will display the main menu
    try:
        main_menu = int(input("Main Menu\n2 - Courier_Menu\n1 - Products_Menu\no - Exit\n<<< ")) #Main menu
        if main_menu == 0: # closes the system if user enters the value 0
            File_Functions.write_file("products.txt", products_list) # function that writes list to file then closes file
            File_Functions.write_file("couriers.txt", courier_list) # function that writes list to file then closes file
            break # breaks loop and ends program
        elif main_menu == 1: # moves on to the options menu if user enters the value 1
            while True: # while loop that displays the options menu
                try: #Products menu
                    products_menu = int(input(("Products_Menu\n----------------\n4 - Delete_Product\n3 - Edit_Product\n2 - Add_Product\n1 - Show_Products\n0 - Main_Menu\n<<< ")))
                    if products_menu == 0: # returns to main menu if user enters the value 0
                        break

                    elif products_menu == 1: # displays the users list if the user enters the value 1
                        print(list(enumerate(products_list)))

                    elif products_menu == 2: # while loop that allows user to add product
                        while True:
                            item = input("exit - Exit\n<<< ").title()
                            if item == "Exit": # if user enters the string 'exit' returns to the options menu
                                break
                            else:
                                products_list.append(item) #appends product list
                                print(list(enumerate(products_list)))

                    elif products_menu == 3: # while loop that allows user to edit list via index 
                        while True:
                            try:
                                print(list(enumerate(products_list)))
                                index = int(input("Index:<<< "))
                                item = input("Edit:<<< ").title()
                                products_list[index] = item
                                break
                            except IndexError as e:
                                print("Product number does not exist!!!")
                                break
                            except ValueError as e:
                                print("Invalid input!!!")
                                break
                    elif products_menu == 4: # while loop that allows user to delete product
                        while True:
                            try:
                                print(list(enumerate(products_list)))
                                del_input = input("exit - Exit\n<<< ").title()
                                if del_input == "Exit": # removes elements of list if userinput is the same
                                    break
                                else:
                                    products_list.remove(del_input)
                            except ValueError as e:
                                print("Please enter a valid input!!!")
                    else:
                        print("\nInvalid input!")
                except ValueError as e:
                    print("Please enter a valid number!")

        elif main_menu == 2: # moves on to the Courier menu if user enters the value 2
            while True: # while loop that displays the courier menu
                try:
                    courier_menu = int(input(("Courier_Menu\n-----------------\n4 - Delete_Courier\n3 - Edit_Courier\n2 - Add_Courier\n1 - Show_Couriers\n0 - Main_Menu\n<<< ")))
                    if courier_menu == 0: # returns to main menu if user enters the value 0
                        break
                    elif courier_menu == 1: # displays the courier list 
                        print(list(enumerate(courier_list)))
                    elif courier_menu == 2: # add to courier list
                        while True:
                            item = input("exit - Exit\n<<< ").title()
                            if item == "Exit": # if user enters the string 'exit' returns to the options menu
                                break
                            else:
                                courier_list.append(item)
                                print(list(enumerate(courier_list)))
                    elif courier_menu == 3: # while loop that allows user to edit list via index 
                        while True:
                            try:
                                print(list(enumerate(courier_list)))
                                item = input("Edit:<<< ").title()
                                if item == "Exit": # if user enters the string 'exit' returns to the options menu
                                    break
                                index = int(input("Index:<<< "))
                                courier_list[index] = item
                            except IndexError as e:
                                print("Product number does not exist!!!")
                            except ValueError as e:
                                print("Invalid input!!!")
                    elif courier_menu == 4: # while loop that allows user to delete courier
                        while True:
                            try:
                                print(list(enumerate(courier_list)))
                                del_input = input("exit - Exit\n<<< ").title()
                                if del_input == "Exit": # removes elements of list if userinput is the same
                                    break
                                else:
                                    courier_list.remove(del_input)
                            except ValueError as e:
                                print("Please enter a valid input!!!")
                    else:
                        print("\nInvalid input!")
                except ValueError as e:
                    print("Please enter a valid number!")
        else:
            print("\nInvalid input!")
    except ValueError as e:
        print("Please enter a valid number!")
    except Exception as e:
        print("An error has occurred!!!")
        break
print("System Exit!!!")