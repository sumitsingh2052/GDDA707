import pandas as pd

# Load healthcare associated infections data
hai_df = pd.read_csv('Healthcare_Associated_Infections-Hospital.csv')

# Load hospital general information data
hospital_info_df = pd.read_csv('Hospital_General_Information.csv')

# Standardizing column names
hai_df.columns = hai_df.columns.str.lower().str.replace(' ', '_')
hospital_info_df.columns = hospital_info_df.columns.str.lower().str.replace(' ', '_')

# Merge datasets on 'facility_id'
unified_df = pd.merge(hai_df, hospital_info_df, on='facility_id', how='inner')

# Display the first few rows of the unified dataset to verify the merge
print(unified_df.head())
