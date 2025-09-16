import pandas as pd

def extract_country_data(file_path):
    df = pd.read_excel(file_path, sheet_name=0)
    countries = df['Countries'].dropna().unique()

    for country in countries:
        country_df = df[df['Countries'] == country]
        with open(f'country-guides/{country.lower().replace(" ", "-")}.md', 'w', encoding='utf-8') as f:
            f.write(f"# {country} HR Guide\n\n")
            for col in country_df.columns:
                val = country_df[col].values[0]
                f.write(f"**{col}**: {val}\n\n")

extract_country_data('data/APAC_Country_Benefits.xlsx')
