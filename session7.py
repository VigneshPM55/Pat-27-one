#1. File with content of current time stamp
def create_text_file_with_timestamp():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{timestamp}.txt"
    file_content = timestamp
    with open(file_name, 'w') as file:
        file.write(file_content)

    print(f"File '{file_name}' created with content '{file_content}'")
    
create_text_file_with_timestamp()

#2. Read the contents
def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Eg
read_text_file("example.txt")  
# In the place of "example.txt" give the name of your text file

#END OF TASK SESSION7