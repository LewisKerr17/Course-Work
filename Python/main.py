try:
    # Open the file in append mode ('a')
    with open('example.txt', 'a') as file:
        # Data to be appended to the file
        data_to_append = "New log entry: User logged in.\n"
        
        # Write data to the file
        file.write(data_to_append)
        
        print("Data successfully appended to 'logfile.txt'.")
except IOError as e:
    # Handle errors related to file I/O operations
    print(f"I/O error occurred: {e}")
except Exception as e:
    # Handle any other exceptions
    print(f"An unexpected error occurred: {e}")
finally:
    # This block will execute no matter what
    print("File append operation completed.")