
# Program to read a text file and print its contents
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print("File Contents:")
            print(contents)
    except FileNotFoundError:
        print("The file does not exist.")

# Example usage
read_file('example.txt')
