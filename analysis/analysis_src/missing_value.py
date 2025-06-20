import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class MissingValueAnalysis(ABC):

    def analyze(self, df: pd.DataFrame):
        """
        Perform missing value analysis on the DataFrame.
        Returns a DataFrame with the count of missing values per column.
        """
        self.identify_missing_values(df)
        self.visualize_missing_values(df)

    @abstractmethod
    def identify_missing_values(self, df:pd.DataFrame):
        pass

    @abstractmethod
    def visualize_missing_values(self, df:pd.DataFrame):
        pass


class SimpleMissingValueAnalysis(MissingValueAnalysis):
    def identify_missing_values(self, df: pd.DataFrame):
        """
        Identify missing values in the DataFrame.
        Returns a DataFrame with the count of missing values per column.
        """
        print("Identifying missing values...")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])

    def visualize_missing_values(self, df: pd.DataFrame):
        """
        Visualize missing values using a heatmap.
        """
        plt.figure(figsize=(12, 8))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
        plt.title('Missing Values Heatmap')
        plt.show()