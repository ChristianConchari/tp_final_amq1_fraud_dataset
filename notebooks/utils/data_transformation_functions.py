import pandas as pd
import datetime
import numpy as np

def transform_transaction_datetime(df: pd.DataFrame, startdate_str: str = '2017-12-01') -> pd.DataFrame:
    """
    Transforms the transaction datetime column in datetime format and adds columns for week day and hour.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the transaction data.
    - startdate_str (str): The start date for the transformation. Defaults to '2017-12-01'.

    Returns:
    - pd.DataFrame: The transformed DataFrame with additional columns for week day and hour.

    """
    transformed_df = df.copy()
    
    startdate = datetime.datetime.strptime(startdate_str, '%Y-%m-%d')
    
    transformed_df["TransactionDT_transformed"] = transformed_df['TransactionDT'].apply(lambda x: startdate + datetime.timedelta(seconds=x))
    transformed_df["Transaction_week_day"] = transformed_df["TransactionDT_transformed"].dt.dayofweek
    transformed_df["Transaction_hour"] = transformed_df["TransactionDT_transformed"].dt.hour
    
    transformed_df = transformed_df.drop(["TransactionDT", "TransactionDT_transformed"], axis=1)
    
    return transformed_df

def transform_transactionAmt(df: pd.DataFrame, isTest: bool = False) -> pd.DataFrame:
    """
    Transforms the 'TransactionAmt' column by taking the log of the values.

    Args:
        df (pd.DataFrame): The input DataFrame.
        isTest (bool, optional): Indicates whether the DataFrame is for testing data. Defaults to False.

    Returns:
        pd.DataFrame: The transformed DataFrame.
    """
    if not isTest:
        transformed_df = df[df['TransactionAmt'] < 10000].copy()
    else:
        transformed_df = df.copy()
    
    transformed_df['LogTransactionAmt'] = np.log(transformed_df['TransactionAmt'] + 1)
    transformed_df.drop('TransactionAmt', axis=1, inplace=True)
    
    return transformed_df

def replace_card(value: str) -> str:
    """
    Replaces the card value with 'debit' if it is 'debit or credit' or 'charge card'.

    Args:
        value (str): The card value to be replaced.

    Returns:
        str: The replaced card value.

    """
    if pd.isna(value):
        return value
    if value in ['debit or credit', 'charge card']:
        return 'debit'
    else:
        return value
    
def group_email_domains(df: pd.DataFrame, column_name: str, threshold: int = 1000) -> pd.DataFrame:
    """
    Groups email domains in a DataFrame column based on a mapping and a threshold.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        column_name (str): The name of the column containing the email domains.
        threshold (int, optional): The threshold for less frequent domains. Defaults to 1000.

    Returns:
        pd.DataFrame: The transformed DataFrame with grouped email domains.
    """
    transformed_df = df.copy()
    
    provider_mapping = {
        'Google Mail': ['gmail.com', 'gmail'],
        'Yahoo Mail': ['yahoo.com', 'ymail.com', 'yahoo.com.mx', 'yahoo.co.jp', 'yahoo.fr',
                       'yahoo.co.uk', 'yahoo.es', 'yahoo.de'],
        'Microsoft Mail': ['hotmail.com', 'outlook.com', 'msn.com', 'live.com', 'live.com.mx',
                           'outlook.es', 'hotmail.fr', 'hotmail.co.uk', 'live.fr', 'hotmail.es',
                           'hotmail.de'],
        'Apple Mail': ['icloud.com', 'me.com', 'mac.com']
    }

    for provider, domains in provider_mapping.items():
        transformed_df.loc[transformed_df[column_name].isin(domains), column_name] = provider

    domain_counts = transformed_df[column_name].value_counts()
    less_frequent_domains = domain_counts[domain_counts <= threshold].index
    transformed_df.loc[transformed_df[column_name].isin(less_frequent_domains), column_name] = 'Others'

    return transformed_df