from abc import ABC, abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class multivariate_analysis(ABC):
        
    def analyze(self, df: pd.DataFrame):
        self.generate_heatmap(df)
        self.generate_pairplot(df)

    def generate_heatmap(self, df: pd.DataFrame):
        """
        Generate a heatmap of the correlation matrix.
        """
        pass

    def generate_pairplot(self, df: pd.DataFrame):
        """
        Generate a pairplot of the DataFrame.
        """
        pass

class multivariate_analysis_core(multivariate_analysis):

    def generate_heatmap(self, df: pd.DataFrame):
        plt.figure(figsize=(12, 10))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', square=True)
        plt.title('Heatmap of Feature Correlations')
        plt.show()

    def generate_pairplot(self, df: pd.DataFrame):
        plt.figure(figsize=(12, 10))
        sns.pairplot(df)
        plt.title('Pairplot of Features', y=1.02)
        plt.show()
