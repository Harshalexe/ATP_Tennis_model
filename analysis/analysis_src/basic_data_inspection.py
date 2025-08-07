import pandas as pd
from abc import ABC, abstractmethod

class DataInspector(ABC):
    @abstractmethod
    def inspect_data(self, df: pd.DataFrame) -> None:
        """ Abstract method to inspect the data 

        takes parameter df: pd.DataFrame
        and returns None
        
        """
        pass

class DatatypeInspector(DataInspector):
    def inspect_data(self, df: pd.DataFrame) -> None:
        """ Inspect the data types of the DataFrame 
        
        takes parameter df: pd.DataFrame
        and returns data types of the DataFrame
        """
        print("Data Types:")
        print(df.info())
        print(df.dtypes)

class summaryInspector(DataInspector):
    def inspect_data(self, df: pd.DataFrame) -> None:
        """ Inspect the summary statistics of the DataFrame

        takes parameter df: pd.DataFrame
        and returns summary statistics of the DataFrame
        """
        print("Summary Statistics: for numerical columns")
        print(df.describe())
        print("Summary Statistics: for categorical columns")
        print(df.describe(include='object'))

class DataInspectorStrategy:
    def __init__(self, strategy: DataInspector):
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspector) -> None:
        """ Set the strategy for data inspection """
        self._strategy = strategy

    def execute_inspection(self, df: pd.DataFrame) -> None:
        """ Execute the data inspection using the current strategy """
        self._strategy.inspect_data(df)


