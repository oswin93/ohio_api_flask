import pandas as pd

def calculate_annual_data():
    # Loading  the data into a DataFrame
    file_path = 'well_production_data.xls'
    df = pd.read_excel(file_path)
    df = df.rename(columns={'API WELL  NUMBER': 'API_WELL_NUMBER'}) #renaming api well number

    df = df[['API_WELL_NUMBER', 'OIL', 'GAS', 'BRINE']]
    annual_data = df.groupby('API_WELL_NUMBER').sum().reset_index()
    return annual_data






