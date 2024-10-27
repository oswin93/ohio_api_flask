import sqlite3
from data_loading import calculate_annual_data

def load_data_to_sqlite(dataframe, db_name='well_production.db', table_name='annual_production'):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        API_WELL_NUMBER INTEGER PRIMARY KEY,
        oil INTEGER,
        gas INTEGER,
        brine INTEGER
    );
    """
    cursor.execute(create_table_query)

    dataframe.to_sql(table_name, conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()


annual_data = calculate_annual_data()
load_data_to_sqlite(annual_data)