import pandas as pd

csv_file_path = 'data/borrowers (1).csv'
df = pd.read_csv(csv_file_path)

df.replace('', pd.NA, inplace=True)


df.dropna(inplace=True)


df['phone'] = df['phone'].str.replace(r'\D', '', regex=True)


cleaned_csv_file_path = 'data/cleaned_borrowers.csv'
df.to_csv(cleaned_csv_file_path, index=False)
