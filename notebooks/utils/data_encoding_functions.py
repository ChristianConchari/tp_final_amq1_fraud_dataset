import pandas as pd
from typing import List

def one_hot_encode_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Encodes the specified columns of a DataFrame using one-hot encoding.

    Parameters:
    - df (pd.DataFrame): The DataFrame to encode.
    - columns (List[str]): The list of column names to encode.

    Returns:
    - encoded_df (pd.DataFrame): The encoded DataFrame.
    """
    encoded_df = pd.get_dummies(df.copy(), columns=columns, drop_first=True, dtype=int)
    return encoded_df

def frequency_encoding(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Encodes a categorical column in a DataFrame using frequency encoding.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the categorical column.
        column_name (str): The name of the categorical column to be encoded.

    Returns:
        pd.DataFrame: The DataFrame with the encoded column.

    """
    frequency = df[column_name].value_counts().to_dict()
    df[column_name + '_freq'] = df[column_name].map(frequency)
    df.drop(columns=[column_name], inplace=True)
    
    return df