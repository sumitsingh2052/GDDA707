import pandas as pd

# Load healthcare associated infections data
hai_df = pd.read_csv('Healthcare_Associated_Infections-Hospital.csv')

# Load hospital general information data
hospital_info_df = pd.read_csv('Hospital_General_Information.csv')

# Handling missing values in healthcare associated infections data
hai_df = hai_df.drop(columns=['Footnote'])  # Dropping column with numerous missing values

# Handling missing values in hospital general information data
columns_to_drop = [
    'Meets criteria for promoting interoperability of EHRs',
    'Meets criteria for birthing friendly designation',
    'Hospital overall rating footnote',
    'MORT Group Footnote',
    'Safety Group Footnote',
    'READM Group Footnote',
    'Pt Exp Group Footnote',
    'TE Group Footnote'
]
hospital_info_df = hospital_info_df.drop(columns=columns_to_drop)
hospital_info_df = hospital_info_df.ffill()  # Forward filling missing values

# Standardizing column names
hai_df.columns = hai_df.columns.str.lower().str.replace(' ', '_')
hospital_info_df.columns = hospital_info_df.columns.str.lower().str.replace(' ', '_')

# Convert relevant columns to numeric in healthcare associated infections data
hai_df['score'] = pd.to_numeric(hai_df['score'], errors='coerce')
hai_df['compared_to_national'] = pd.to_numeric(hai_df['compared_to_national'], errors='coerce')

# Calculating infection rates
hai_df['infection_rate'] = hai_df['score'] / hai_df['compared_to_national']

# Output the first few rows of each DataFrame to verify
print(hai_df.head())
print(hospital_info_df.head())
