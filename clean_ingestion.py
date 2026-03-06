import pandas as pd
import hashlib
import sys

# Find input file
input_files = ['raw_input.csv', 'CSV1.csv']
input_file = next((f for f in input_files if os.path.exists(f)), None)
if not input_file:
    print("No input CSV found")
    sys.exit(1)

print(f"Processing {input_file}")

# Read robustly
df = pd.read_csv(input_file, encoding='utf
