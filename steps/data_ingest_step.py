import pandas as pd
from src.ingest_data import DataIngestorMain
from zenml import step

@step
def data_ingest_step(file_path : str) -> pd.DataFrame:
    """ Step to ingest data from zip file"""
    return pd.read_csv(file_path)