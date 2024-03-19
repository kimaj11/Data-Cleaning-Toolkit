
import pandas as pd
from sqlalchemy import create_engine

def load_data(source_type, path_or_connection_string):
    """
    Loads consumption data into a Pandas DataFrame from various sources.

    Parameters:
    - source_type: Type of the source ('csv', 'json', 'database')
    - path_or_connection_string: Path to the file or database connection string

    Returns:
    - A Pandas DataFrame containing the loaded data.
    """

    if source_type == 'csv':
        # Load data from a CSV file
        df = pd.read_csv(path_or_connection_string)
    elif source_type == 'json':
        # Load data from a JSON file
        df = pd.read_json(path_or_connection_string)
    elif source_type == 'database':
        # Load data from a database
        # Example for a SQLite database; adjust for other databases as necessary
        engine = create_engine(path_or_connection_string)
        # Replace 'table_name' with the actual table name
        df = pd.read_sql_table('table_name', engine)
    else:
        raise ValueError("Unsupported source type. Choose from 'csv', 'json', or 'database'.")

    return df

# Example usage:
# df_csv = load_data('csv', '/path/to/your/file.csv')
# df_json = load_data('json', '/path/to/your/file.json')
# df_db = load_data('database', 'sqlite:///path/to/your/database.db')


def explore_data(df):
    """
    Explores a given DataFrame, understanding its structure,
    and identifying potential issues or anomalies.

    Parameters:
    - df: Pandas DataFrame to explore.

    """
    print("First few rows of the dataset:")
    print(df.head())

    print("\nData types of each column:")
    print(df.dtypes)

    print("\nDataFrame summary:")
    df.info()

    print("\nDescriptive statistics for numerical features:")
    print(df.describe())

    print("\nDescriptive statistics for categorical features:")
    print(df.describe(include=['object', 'bool', 'category']))

    print("\nMissing values in each column:")
    print(df.isnull().sum())

    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        outlier_condition = ((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))
        if outlier_condition.any():
            print(f"\nPotential outliers detected in '{column}':")
            print(df[outlier_condition][column])

# Example usage:
# df_csv = load_data('csv', '/path/to/your/file.csv')
# explore_data(df_csv)

df = load_data('csv', '/Users/andrewkim/Downloads/Electric_Vehicle_Population_Data.csv')
explore_data(df)