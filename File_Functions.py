import csv

def read_csv_file(file_name, list_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list_name.append(row)



def write_csv_file(file_name, list_name):
    fieldnames = list_name[0].keys()
    with open(file_name, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        writer.writerows(list_name)


def print_list(list_name):
    print("\n")
    for lines in range(len(list_name)):
         print(list_name[lines])


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

def add_to_dict(dict_name, list_name):
    while True:
        try:
            fieldnames = list_name[0].keys()
            name = str(input("Press Enter to exit\n<<< ")).title()
            if name == "":
                break
            price = int(input("<<< "))
            if price == "":
                break
            dict_name = {"Name":name, "Price": price}
            list_name.append(dict_name)
            break
        except Exception as e:
            print(f"An error occured!! {e}")
            break

    

def edit_list(list_name, dict_name):
    while True:
        try:
            index = int(input("Index:<<< "))
            list_name[index] = dict_name
            break
        except IndexError as e:
            print("Product price does not exist!!!")
            break
        except ValueError as e:
            print("Invalid input!!!")
            break


def del_list_element(list_name):
    while True:
        try:
            print(list(enumerate(list_name)))
            del_input = int(input("Please enter index to remove: "))
            del list_name[del_input]
            break
        except IndexError as i:
            print("Invalid index price!!!")
            break
        except ValueError as e:
            print("Please enter a valid input!!!")
            break

# def print_list(list_name):
#     print("\n")
#     for lines in range(len(list_name)):
#          print(list_name[lines])

