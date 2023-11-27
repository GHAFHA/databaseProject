import pandas as pd

csv_file_path = 'data/books (1).csv'
df = pd.read_csv(csv_file_path, delimiter='\t')


df.replace('', pd.NA, inplace=True)


df.dropna(inplace=True)


df['Publisher'] = df['Publisher'].str.replace('&amp;', '&', regex=False)


df['Pages'] = df['Pages'].replace(0, pd.NA)
df['Pages'] = df['Pages'].astype('Int64')

cleaned_csv_file_path = 'data/cleaned_books.csv'
df.to_csv(cleaned_csv_file_path, index=False, sep='\t')
