from abc import ABC, abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class bivariate_analysis(ABC):
    @abstractmethod
    def analyze(self,df:pd.DataFrame, feature1:str, feature2:str):
        """
        Perform bivariate analysis on the DataFrame.
        Returns a DataFrame with the results of the analysis.
        """
        pass

class numericalvsnumerical(bivariate_analysis):
    """
        Perform bivariate analysis for 2 numerical variables.
        Returns a DataFrame with the scatter plot.
    """
    def analyze(self,df:pd.DataFrame, feature1: str, feature2: str):
        plt.figure(figsize=(12,8))
        sns.scatterplot(x=df[feature1], y=df[feature2])
        plt.title(f'Bivariate Analysis of {feature1} vs {feature2}')
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()

class catergoricalvsnumerical(bivariate_analysis):
    """
        Perform bivariate analysis for categorical vs numerical variables.
        Returns a DataFrame with the boxplot.
        """
    def analyze(self, df: pd.DataFrame, categorical_feature: str, numerical_feature: str):
        plt.figure(figsize=(12,8))
        sns.boxplot(x=df[categorical_feature], y=df[numerical_feature])
        plt.title(f'Bivariate Analysis of {categorical_feature} vs {numerical_feature}')
        plt.xlabel(categorical_feature)
        plt.ylabel(numerical_feature)
        plt.xticks(rotation=45)
        plt.show()

class categoricalvscategorical(bivariate_analysis):
    """
        Perform bivariate analysis for 2 categorical variables.
        Returns a DataFrame with the count plot.
    """
    def analyze(self, df: pd.DataFrame, categorical_feature1: str, categorical_feature2: str):
        plt.figure(figsize=(12,8))
        # sns.countplot(x=df[categorical_feature1], hue=df[categorical_feature2])
        plt.title(f'Bivariate Analysis of {categorical_feature1} vs {categorical_feature2}')
        plt.xlabel(categorical_feature1)
        plt.xticks(rotation=45)
        plt.ylabel('Count')
        plt.legend(title=categorical_feature2)
        top_n = 10
        top_categories = df[categorical_feature1].value_counts().nlargest(top_n).index

        sns.countplot(
            data=df[df[categorical_feature1].isin(top_categories)],
            x=df[categorical_feature1],
            order=top_categories
        )
        plt.xticks(rotation=45) 
        plt.show()

class bivariateAnalysisMain:
    def __init__(self, strategy: bivariate_analysis):
        self._strategy = strategy

    def set_strategy(self, strategy: bivariate_analysis) -> None:
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature1: str, feature2: str) -> None:
        self._strategy.analyze(df, feature1, feature2)