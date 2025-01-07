import json
import pandas as pd

def load_customer_data(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

def extract_customer_phones(customers):
    phones = []
    for customer in customers:
        phones.append({
            'Customer ID': customer['customer_id'],
            'Phone Number': customer['phone']
        })
    return phones


def save_to_excel(customer_phones, output_file):
    df = pd.DataFrame(customer_phones)
    df.to_excel(output_file, index=False, engine='openpyxl')







customers = load_customer_data('customers.json')


customer_phones = extract_customer_phones(customers)


output_file = 'customer_phones.xlsx'
save_to_excel(customer_phones, output_file)

print(f"Customer phone numbers have been saved to {output_file}")
