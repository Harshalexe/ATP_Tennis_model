import pandas as pd
from src.handle_missing_value import missingvaluehandler
from zenml import step  

@step
def missing_step(df: pd.DataFrame) -> pd.DataFrame:
    """ Step to handle missing values in the DataFrame """
    handler = missingvaluehandler()
    return handler.handle_missing_values(df)