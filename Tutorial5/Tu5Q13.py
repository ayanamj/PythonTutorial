import pandas as pd

def load_data(file):
    return pd.read_csv(file)

def process_employee_data(file):
    df = load_data(file)
    print("First 7 records:")
    print(df.head(7))
    print("\nEmployees in alphabetical order:")
    print(df.sort_values('name')['name'])
    print("\nEmployee with highest salary:")
    print(df.loc[df['salary'].idxmax(), 'name'])
    print("\nMale employees:")
    print(df[df['gender'] == 'Male']['name'])
    print("\nTeams employees belong to:")
    print(df['team'].unique())

employee_file = "employee.csv"
process_employee_data(employee_file)
