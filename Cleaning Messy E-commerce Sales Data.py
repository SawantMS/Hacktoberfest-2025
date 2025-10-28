import pandas as pd
import numpy as np

# --- 1. Create Sample Messy Data ( CSV Load) ---
data = {
    'OrderID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1007], # Duplicate
    'Region': [' North ', 'South', 'East', 'north', 'West', 'South', 'North', 'North'], # Inconsistent casing/spaces
    'Sales': [150.50, '89.99', np.nan, 210.00, 'Error', 55.25, 150.50, 150.50], # Missing value and non-numeric
    'Quantity': [1, 2, 1, 3, 2, np.nan, 1, 1], # Missing value
    'Customer_ID': ['A101', 'B202', 'C303', 'D404', 'E505', 'B202', 'F606', 'F606'] # Duplicate customer ID
}
df = pd.DataFrame(data)

print("--- Initial Messy DataFrame ---")
print(df)
print("\nInitial Data Types:")
print(df.dtypes)
print("-" * 35)

# --- 2. Data Cleaning and Preprocessing ---

# A. Remove Duplicate Rows
# Keep the first occurrence of any fully duplicated row
df.drop_duplicates(inplace=True)
print("\nRemoved full duplicate rows.")

# B. Clean and Standardize Text Column ('Region')
# Remove leading/trailing whitespace, then convert to Title Case
df['Region'] = df['Region'].str.strip().str.title()
print("Cleaned 'Region' column (standardized text).")

# C. Handle Inconsistent Data and Convert Type ('Sales')
# Identify and replace non-numeric strings with NaN, then convert to float
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

# D. Handle Missing Values (Imputation and Dropping)
# Fill missing 'Quantity' values with the median (Imputation)
median_quantity = df['Quantity'].median()
df['Quantity'].fillna(median_quantity, inplace=True)

# Drop rows where 'Sales' is still NaN after conversion (due to 'Error' string)
df.dropna(subset=['Sales'], inplace=True)
print(f"Filled missing 'Quantity' with median ({median_quantity}).")
print("Dropped rows with bad 'Sales' data.")


print("\n--- Cleaned DataFrame ---")
print(df)

print("\nCleaned Data Types:")
print(df.dtypes)

sales_summary = df.groupby('Region')['Sales'].sum().reset_index()

print("\n--- Sales Summary (Analysis on Cleaned Data) ---")
print(sales_summary)
