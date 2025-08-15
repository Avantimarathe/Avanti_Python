def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File contents:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_file("sample.txt")