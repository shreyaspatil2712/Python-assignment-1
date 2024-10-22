import pandas as pd
import os

def analyze_salaries(input_file, output_file='salary_analysis.csv'):
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    try:
       
        data = pd.read_csv(input_file)

       
        if 'department' not in data.columns or 'salary' not in data.columns:
            print(f"Error: CSV file is missing 'department' or 'salary' columns.")
            return

      
        data['salary'] = pd.to_numeric(data['salary'], errors='coerce')  #invalid  to NaN

        
        data = data.dropna(subset=['department', 'salary'])

       
        salary_analysis = data.groupby('department')['salary'].agg(['sum', 'mean'])

        salary_analysis.to_csv(output_file)
        print(f"Salary analysis saved to '{output_file}'.")

    except pd.errors.EmptyDataError:
        print(f"Error: The file '{input_file}' is empty or contains no valid data.")
    except Exception as e:
        print(f"An error occurred: {e}")


input_file = 'employee_salaries.csv' 
analyze_salaries(input_file)
