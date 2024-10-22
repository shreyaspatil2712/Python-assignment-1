import pandas as pd
import os

def analyze_inventory(file_path):
    try:
        data = pd.read_csv(file_path)
        required_columns = ['product_id', 'name', 'quantity']
        if not all(column in data.columns for column in required_columns):
            print(f"Error: The CSV file is missing one or more required columns: {required_columns}")
            return

        data['quantity'] = pd.to_numeric(data['quantity'], errors='coerce')  

        data = data.dropna(subset=['quantity'])

        low_stock_products = data[data['quantity'] < 10]

        if low_stock_products.empty:
            print("No products with low stock.")
        else:
            print("Products with low stock:")
            print(low_stock_products[['product_id', 'name', 'quantity']])

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty or malformed.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'product_inventory.csv'  
analyze_inventory(file_path)
