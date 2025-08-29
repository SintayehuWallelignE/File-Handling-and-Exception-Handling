import os

def process_and_write_file(filename):
    """
    Reads a file, modifies its content, and writes the modified content
    to a new file. Handles potential file-related errors.

    Args:
        filename (str): The name of the file to be processed.
    """
    try:
        # Step 1: Read the content from the specified file
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Successfully read from '{filename}'.")
            
        # Step 2: Modify the content (e.g., convert to uppercase and add a header)
        modified_content = f"--- Modified Content ---\n\n{content.upper()}\n\n--- End of File ---"

        # Step 3: Create a new filename for the output
        base, extension = os.path.splitext(filename)
        output_filename = f"{base}_modified{extension}"
        
        # Step 4: Write the modified content to the new file
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"Successfully wrote the modified content to '{output_filename}'.")
        print("Check your directory to find the new file.")

    except FileNotFoundError:
        # Handles the case where the user-provided file does not exist
        print(f"Error: The file '{filename}' was not found.")
        print("Please make sure the file exists in the same directory.")
    except IOError as e:
        # Handles other potential I/O errors (e.g., permission issues)
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        # Catches any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user to enter a filename
    user_filename = input("Enter the filename to process (e.g., input.txt): ")
    
    # Call the function to perform the file operations
    process_and_write_file(user_filename)