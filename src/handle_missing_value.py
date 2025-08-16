import pandas as pd
import logging 
from abc import ABC, abstractmethod 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class missingvaluehandler(ABC):
    @abstractmethod
    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Abstract method to handle missing values in a DataFrame """
        try:
            logging.info("Filling missing values in 'player_dismissed' with 'Not Out'")
            df['player_dismissed'] = df['player_dismissed'].fillna('Not Out')
        except Exception as e:
            logging.error(f"Error filling 'player_dismissed': {e}")

        try:
            logging.info("Filling missing values in 'dismissal_kind' with 'None'")
            df['dismissal_kind'] = df['dismissal_kind'].fillna('None')
        except Exception as e:
            logging.error(f"Error filling 'dismissal_kind': {e}")

        rare_kinds =  ["Caught and Bowled", "retired hurt", "Stumped", "hit wicket", "obstructing the field"]
        try:
            logging.info("Grouping rare dismissal kinds into 'others'")
            df['dismissal_kind_grouped'] = df['dismissal_kind'].apply(lambda x: "others" if x in rare_kinds else x)
        except Exception as e:
            logging.error(f"Error grouping rare dismissal kinds: {e}")

        logging.info("Missing value handling completed")
        return df