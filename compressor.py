import os

######################### String Collection #########################
setup = """import os

# fild a directory of a current file
def get_path():
    file_path = os.path.abspath(__file__)
    file_name = os.path.basename(__file__)
    current_path = file_path.replace(file_name, "")
    return current_path

def main():
    current_path = get_path()

    """

next = """
    """

#####################################################################

def get_path():
    file_path = os.path.abspath(__file__)
    file_name = os.path.basename(__file__)
    current_path = file_path.replace(file_name, "")
    return current_path

def main(): 
    # get current path
    current_path = get_path()
    all_files = os.listdir(current_path)
    py_files = {file for idx, file in enumerate(all_files) if file.endswith(".py") if not file == "compressor.py" and not file == "compressed.py"}

    # open a file in write mode
    new_file = open(f"{current_path}compressed.py", "w")
    new_file.write(setup)

    # open every python files in read mode
    # write code in new_file.py file
    for idx, py_file in enumerate(py_files):
        file = open(f"{current_path}{py_file}", "r")
        data = file.read()

        # open, write, close loop and insert data
        new_file.write("# file_"f"{idx}{next}")
        new_file.write("file_"f"{idx} = "'open(f"{current_path}'f"{py_file}"'", "w")'f"{next}")
        new_file.write("file_"f"{idx}.write("'"""'f"{data}"'""")'f"{next}")
        new_file.write("file_"f"{idx}.close()"f"{next}{next}")

        file.close()
 
    # write self-delete code
    # close a write mode file
    new_file.write(f"# delete current file{next}")
    new_file.write('file_path = os.path.abspath(__file__)'f"{next}")
    new_file.write('os.remove(f"{file_path}")'f"{next}")
    new_file.write("\nmain()")
    new_file.close()

if __name__ == "__main__":
    main()