#1. Write a Python program to list only directories, files and all directories, files in a specified path
import os
def list_contents(path):
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return

    all_items = os.listdir(path)
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("\nOnly Directories:")
    print(directories)

    print("\nOnly Files:")
    print(files)

    print("\nAll Directories and Files:")
    print(all_items)

specified_path = input("Enter the directory path: ")
list_contents(specified_path)

#2. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os
def check_path_access(path):
    print(f"Checking access for: {path}\n")

    if os.path.exists(path):
        print("✔ Path exists")
    else:
        print("✖ Path does not exist")
        return

    if os.access(path, os.R_OK):
        print("✔ Readable")
    else:
        print("✖ Not readable")

    if os.access(path, os.W_OK):
        print("✔ Writable")
    else:
        print("✖ Not writable")

    if os.access(path, os.X_OK):
        print("✔ Executable")
    else:
        print("✖ Not executable")

specified_path = input("Enter the path to check: ")
check_path_access(specified_path)

#3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path
import os
def check_path(path):
    if os.path.exists(path):
        print(f"✔ The path '{path}' exists.")
        directory = os.path.dirname(path)
        filename = os.path.basename(path)

        print(f"Directory portion: {directory}")
        print(f"Filename portion: {filename}")
    else:
        print(f"✖ The path '{path}' does not exist.")

specified_path = input("Enter the path to check: ")
check_path(specified_path)

#4. Write a Python program to count the number of lines in a text file
def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)
        print(f"Number of lines in '{file_path}': {line_count}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = input("Enter the file path: ")
count_lines(file_path)

#5. Write a Python program to write a list to a file.
def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print(f"List successfully written to '{file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
file_path = input("Enter the file path to save the list: ")
write_list_to_file(file_path, data)

#6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string
def generate_text_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"This is {filename}\n")
        print(f"Created {filename}")

generate_text_files()

#7. Write a Python program to copy the contents of a file to another file
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as src:
            content = src.read()
        with open(destination_file, 'w', encoding='utf-8') as dest:
            dest.write(content)
        print(f"Contents copied from '{source_file}' to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

source = input("Enter the source file path: ")
destination = input("Enter the destination file path: ")
copy_file(source, destination)

#8. Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os
def delete_file(file_path):
    if not os.path.exists(file_path):
        print(f"✖ The file '{file_path}' does not exist.")
        return

    if not os.access(file_path, os.W_OK):
        print(f"✖ No write permission to delete '{file_path}'.")
        return

    try:
        os.remove(file_path)
        print(f"✔ File '{file_path}' deleted successfully.")
    except Exception as e:
        print(f"✖ An error occurred while deleting the file: {e}")


file_path = input("Enter the file path to delete: ")
delete_file(file_path)



