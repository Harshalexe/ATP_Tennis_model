from abc import ABC, abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class UnivariateAnalysis(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature: str):
        """
        Perform univariate analysis on the DataFrame.
        Returns a DataFrame with the results of the analysis.
        """
        pass

class numericalAnalysis(UnivariateAnalysis):
    def analyze(self, df: pd.DataFrame, feature: str):
        """
        Perform univariate analysis for numerical variables.
        Returns a DataFrame with the summary statistics.
        """
        print("Analyzing categorical variables...")
        plt.figure(figsize=(12, 8))
        sns.histplot(df[feature], kde=True, bins=30)
        plt.title(f'Univariate Analysis of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        plt.show()

class categoricalAnalysis(UnivariateAnalysis):
    def analyze(self, df: pd.DataFrame, feature: str):
        """
        Perform univariate analysis for categorical variables.
        Returns a DataFrame with the value counts.
        """
        print("Analyzing categorical variables...")
        plt.figure(figsize=(12, 8))
        sns.countplot(x=feature, data=df, palette='muted')
        plt.title(f'Univariate Analysis of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.show()

class UnivariateAnalysisMain:
    def __init__(self, strategy: UnivariateAnalysis):
        self._strategy = strategy

    def set_strategy(self, strategy: UnivariateAnalysis) -> None:
        """ Set the strategy for univariate analysis """
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature: str) -> None:
        """ Execute the univariate analysis using the current strategy """
        self._strategy.analyze(df, feature)