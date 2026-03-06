import pandas as pd
import hashlib
import glob

# Find input file (CSV1 or raw_input.csv)
input_file = glob.glob("*CSV1.csv") or glob.glob("raw_input.csv") or "raw_input.csv"
print(f"Using input:
    print("Columns found:", df.columns.tolist())
    
# 2) Keep only the relevant columns (only if exist)
keep_cols = [
    "Phone",
    "SenderName",
    "Message",
    "LinkedInPostURL",
    "Person",
    "LinkedInProfileURL",
    "PostCount",
]
df = df[[c for c in keep_cols if c in df.columns]]

# 3) Anonymize PII (safe for public repo)
df["Phone_hash"] = df["Phone"].astype(str).apply(
    lambda x: hashlib.sha256(x.encode()).hexdigest()[:12]
)
df["Sender_hash"] = df["SenderName"].astype(str).apply(
    lambda x: hashlib.sha256(x.encode()).hexdigest()[:12]
)

# 4) Drop raw PII columns before saving
df_clean = df[
    [
        "Phone_hash",
        "Sender_hash",
        "Message",
        "LinkedInPostURL",
        "Person",
        "LinkedInProfileURL",
        "PostCount",
    ]
]

# 5) Write anonymized output for Firecrawl/content brain ingestion
df_clean.to_csv("output_clean.csv", index=False)
