from typing import List
from sklearn.impute import SimpleImputer
import pandas as pd

class DataImputer:
    def __init__(self, strategy: str = 'mean'):
        """
        Initializes a DataInputation object.

        Parameters:
        - strategy (str): The strategy to be used for data imputation. Default is 'mean'.
        """
        self.strategy = strategy
        self.imputer = None

    def impute_train_set_values(self, df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        Imputes missing values in the specified columns of the input DataFrame using the specified strategy.

        Args:
            df (pd.DataFrame): The input DataFrame.
            columns (List[str]): The list of column names to impute.

        Returns:
            pd.DataFrame: The DataFrame with imputed values.
        """
        if self.imputer is None:
            self.imputer = SimpleImputer(strategy=self.strategy)

        print(f"Train missing values before imputation: \n\n{df[columns].isnull().sum()}\n")
        
        imputed_df = df.copy()
        self.imputer.fit(imputed_df[columns])

        imputed_df[columns] = self.imputer.transform(imputed_df[columns])
        print(f"Train missing values after imputation: \n\n{imputed_df[columns].isnull().sum()}\n")

        return imputed_df
    
    def impute_test_set_values(self, df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        Imputes missing values in the test set using the fitted imputer.

        Args:
            df (pd.DataFrame): The test set DataFrame.
            columns (List[str]): The list of columns to impute.

        Returns:
            pd.DataFrame: The test set DataFrame with imputed values.
        """
        if self.imputer is None:
            raise ValueError("Imputer has not been fitted. Please call impute_train_set_values first.")
        
        print(f"Test missing values before imputation: \n\n{df[columns].isnull().sum()}\n")

        imputed_df = df.copy()
        imputed_df[columns] = self.imputer.transform(imputed_df[columns])
        
        print(f"Test missing values after imputation: \n\n{imputed_df[columns].isnull().sum()}\n")

        return imputed_df