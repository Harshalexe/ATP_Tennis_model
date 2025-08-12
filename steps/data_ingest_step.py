import pandas as pd
from src.ingest_data import DataIngestorMain

def data_ingest_step(file_path : str) -> pd.DataFrame:
    """ Step to ingest data from zip file"""
    extension = file_path.split('.')[-1]
    ingestor = DataIngestorMain.get_data_ingestor(extension)
    return ingestor.ingest_data(file_path)