# Open a new file named 'my_file.txt'
try:
    # Create and write to the file
    with open('my_file.txt', 'w') as file:
        file.write("My name is Victor. \n")
        file.write("I come from Kilifi, Mombasa. \n")
        file.write("I am an electric engineer. \n")
    
    print("File 'my_file.txt' created and data written successfully.")

    # Append additional lines of text to the file
    with open('my_file.txt', 'a') as file:
        file.write('Appending the fourth line. \n')
        file.write('I live in Japan. \n')

    print("2 lines appended to 'my_file.txt' successfully.")

    # Read and display the content of the file 
    with open('my_file.txt', 'r') as file:
        content = file.read()

    print("\nContent of 'my_file.txt':")
    print(content)

except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except PermissionError:
    print("Error: You do not have the necessary permissions to write to 'my_file.txt'.")
except Exception as e:
    # Catch any other exception that may occur
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile operations completed.")