import pandas as pd
import logging 
from abc import ABC, abstractmethod 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class missingvaluehandler(ABC):
    @abstractmethod
    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Abstract method to handle missing values in a DataFrame """
        pass
