import os

def process_file_with_error_handling():
    """
    Reads a file, modifies its content, and writes the output to a new file.
    Includes robust error handling for common file issues.
    """
    input_filename = input("Enter the name of the file to read: ")
    output_filename = "output_" + input_filename

    try:
        # Step 1: Read the input file
        with open(input_filename, 'r') as file_in:
            lines = file_in.readlines()
        
        print(f"Successfully read from '{input_filename}'.")

        # Step 2: Modify the content
        modified_lines = []
        for line in lines:
            # Let's modify each line by making it uppercase and adding a prefix
            modified_line = f"MODIFIED: {line.strip().upper()}\n"
            modified_lines.append(modified_line)

        # Step 3: Write to a new output file
        with open(output_filename, 'w') as file_out:
            file_out.writelines(modified_lines)
        
        print(f"Successfully wrote modified content to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found. Please check the filename and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    process_file_with_error_handling()
