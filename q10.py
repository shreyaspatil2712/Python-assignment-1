import re

def extract_phone_numbers(filename):
    phone_pattern = re.compile(r'\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}')
    
    try:
        with open(filename, 'r') as file:
            text = file.read()
        
        phone_numbers = phone_pattern.findall(text)

        if phone_numbers:
            print("Extracted Phone Numbers:")
            for phone in phone_numbers:
                print(phone)
        else:
            print("No valid phone numbers found.")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = 'client_data.txt'
extract_phone_numbers(filename)
