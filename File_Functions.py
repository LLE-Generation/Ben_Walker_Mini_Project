def read_file(file_name, list_name):
    try: #reads a file to a list
        with open(file_name, 'r') as my_file:
            for line in my_file.readlines():
                list_name.append(line.rstrip())
    except Exception as e:
        print(f"An error has occurred!!! {e}")


def write_file(file_name, list_name):
    try: #writes list to a file 
        with open(file_name, "w") as my_file:
            for product in list_name:
                my_file.writelines(product + "\n")
    except Exception as e:
        print(f"An error occurred!!! {e}")
    