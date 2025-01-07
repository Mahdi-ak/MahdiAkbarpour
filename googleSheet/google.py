import pandas as pd
import os

def load_data():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory, 'googlesheet.csv')  
    
    if not os.path.exists(file_path):
        file_path = os.path.join(current_directory, 'googlesheet.xlsx')
    
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        print("Unsupported file format.")
        return None

def find_by_national_code(df, code):
    
    df.columns = df.columns.str.strip()  
    
    df['National code'] = df['National code'].astype(str)  
    result = df[df['National code'] == str(code)]  
    if not result.empty:
        return result
    return None


df = load_data()

if df is not None:
    code = input("Enter national code: ")
    info = find_by_national_code(df, code)
    
    if info is not None:
        print(info)
    else:
        print("No information found.")
