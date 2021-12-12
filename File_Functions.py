def read_file(file_name, list_name):
    try: #reads a file to a list
        with open(file_name, 'r') as my_file:
            for line in my_file.readlines():
                list_name.append(line.rstrip())
    except FileNotFoundError as f:
        print("File not found!")
    except Exception as e:
        print(f"An error has occurred!!! {e}")


def write_file(file_name, list_name):
    try: #writes list to a file 
        with open(file_name, "w") as my_file:
            for product in list_name:
                my_file.writelines(product + "\n")
    except FileNotFoundError as f:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred!!! {e}")


def print_list(list_name):
    for lines in range(len(list_name)):
         print("\n" + list_name[lines])


def add_item(list_name):
    while True:
        try:
            item = input(str("Press Enter to exit\n<<< ").title())
            if item == "":
                break
            list_name.append(item) #appends list
            print(list_name)
        except ValueError as e:
            print("Invalid input!!!")
        except Exception as e:
            print("An error occured!!!")
        break
    

def edit_list(list_name):
    while True:
        try:
            print(list(enumerate(list_name)))
            index = int(input("Index:<<< "))
            item = input("Edit:<<< ").title()
            list_name[index] = item
            break
        except IndexError as e:
            print("Product number does not exist!!!")
            break
        except ValueError as e:
            print("Invalid input!!!")
            break


def del_list_element(list_name):
    while True:
        try:
            print(list(enumerate(list_name)))
            del_input = int(input("Please enter index number to remove: "))
            del list_name[del_input]
            break
        except IndexError as i:
            print("Invalid index number!!!")
            break
        except ValueError as e:
            print("Please enter a valid input!!!")
            break