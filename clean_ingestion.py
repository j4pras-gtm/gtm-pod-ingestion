# Create clean_ingestion.py (root)
import pandas as pd
df = pd.read_csv('raw_input.csv')  # or pd.read_excel('Final-Dataset.xls')
df['Phone'] = df['Phone'].str.replace(r'\d{3}-\d{3}-\d{4}', '***-***-****', regex=True)
df.to_csv('output_clean.csv', index=False)
print('✅ Cleaned!')
