import pandas as pd
import numpy as np
from tabulate import tabulate

def find_differences(df1: pd.DataFrame, df2: pd.DataFrame) -> None:
    """
    Find the differences between the columns of two DataFrames.

    Args:
        df1 (pandas.DataFrame): The first DataFrame.
        df2 (pandas.DataFrame): The second DataFrame.

    Returns:
        set: A set containing the column names that are present in one DataFrame but not in the other.
    """
    df1_columns = list(df1.columns)
    df2_columns = list(df2.columns)

    diff1 = set(df1_columns) - set(df2_columns)
    diff2 = set(df2_columns) - set(df1_columns)

    differences = diff1.union(diff2)

    print("Different values between the lists:", differences)
    
def get_columns_with_missing_values(df: pd.DataFrame, threshold: float = 0.3) -> list:
    """
    Get the columns with missing values in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame.
        threshold (float, optional): The threshold for missing values percentage. Defaults to 0.3.

    Returns:
        list: A list of column names with missing values.
    """
    missing_percentage = np.sum(pd.isnull(df)).sort_values(ascending=False) / len(df)
    columns_with_missing_values = [col for col, value in missing_percentage[missing_percentage > threshold].items()]

    print(tabulate([[col, value] for col, value in missing_percentage[missing_percentage > threshold].items()], headers=['Column', 'Missing Percentage'], tablefmt='psql'))

    return columns_with_missing_values