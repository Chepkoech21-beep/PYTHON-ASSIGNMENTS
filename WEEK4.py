def simple_file_modifier():
    """Reads a file, converts text to uppercase, and saves to new file."""
    
    # Get input file name
    input_file = input("Enter input filename: ")
    
    try:
        # Read the file
        with open(input_file, 'r') as f:
            text = f.read()
        
        # Modify content (convert to uppercase)
        new_text = text.upper()
        
        # Get output file name
        output_file = input("Enter output filename: ")
        
        # Write to new file
        with open(output_file, 'w') as f:
            f.write(new_text)
            
        print(f"Success! Created {output_file}")
        
    except FileNotFoundError:
        print(f"Error: {input_file} not found")
    except:
        print("An error occurred")

