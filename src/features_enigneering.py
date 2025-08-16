import pandas as pd
import logging 
from abc import ABC, abstractmethod 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class new_features_eng(ABC):
    @abstractmethod
    def perform_action(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Abstract method to perform feature engineering on the DataFrame """
        pass

class over_phase(new_features_eng):
    """This function basically divide the over in phases with (powerplay,middleover,deathover) """
    @staticmethod
    def assign_phase(over):
        if 1 <= over <= 6:
            return "Powerplay_over"
        elif 7 <= over <= 15:
            return "Middle_over"
        elif 16 <= over <= 20:
            return "Death_over"
        else:
            return "Unknown" 

    def perform_action(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            logging.info("Assigning over phases to 'phase' column")
            df['phase'] = df['over'].apply(self.assign_phase)
        except Exception as e:
            logging.error(f"Error in over_phase.perform_action: {e}")
        return df
        

class ball_clip(new_features_eng):
    def perform_action(self, df: pd.DataFrame) -> pd.DataFrame:
        """if balls in over greater then 6 then making new column and clipped them to 6 plus make new column which shows extra ball 1,2,3"""
        try:
            logging.info("Clipping balls and creating 'ball_clipped' and 'extra_ball' columns")
            df['ball_clipped']= df['ball'].apply(lambda x: min(x,6))
            df['extra_ball'] = df['ball'].apply(lambda x:x-6 if x>6 else 0)
        except Exception as e:
            logging.error(f"Error in ball_clip.perform_action: {e}")
        return df

class wlnt_clip(new_features_eng):
    def perform_action(self, df:pd.DataFrame) -> pd.DataFrame:
        """This function identifies wide, leg bye, no ball, and total runs that are outliers."""
        try:
            logging.info("Creating 'wide_leg_no_total_is_outlier' column for outlier detection")
            df["wide_leg_no_total_is_outlier"] = (
                    (df["wide_runs"] > 2) |
                    (df["legbye_runs"] > 2) |
                    (df["noball_runs"] > 1) |
                    (df["total_runs"] > 6)
                ).astype(int)
        except Exception as e:
            logging.error(f"Error in wlnt_clip.perform_action: {e}")
        return df

class rare_runs(new_features_eng):
    def perform_action(self, df: pd.DataFrame) -> pd.DataFrame:
        """ creating column which says if runs 3,5,7 then its 'rare_run' """
        try:
            logging.info("Creating 'batsman_rare_grouped' column for rare runs")
            df['batsman_rare_grouped']= df['batsman_runs'].apply(lambda x: 1 if x in [3,5,7] else 0)
        except Exception as e:
            logging.error(f"Error in rare_runs.perform_action: {e}")
        return df

class dropping(ABC):
    @abstractmethod
    def drop_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Abstract method to drop columns from the DataFrame """
        feature_to_drop=['is_super_over','bye_runs','penalty_runs','fielder']
        try:
            logging.info(f"Dropping columns: {feature_to_drop}")
            df= df.drop(columns=feature_to_drop)
        except Exception as e:
            logging.error(f"Error in dropping.drop_columns: {e}")
