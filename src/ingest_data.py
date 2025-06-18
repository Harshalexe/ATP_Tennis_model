import os
import pandas as pd
import zipfile
from abc import ABC, abstractmethod

class data_ingestor(ABC):
    @abstractmethod
    def ingest_data(self, file_path: str) -> pd.DataFrame:
        """" Abstract method to ingest data from a given file"""
        pass

class ZipDataIngestor(data_ingestor):
    def ingest_data(self,file_path: str) -> pd.DataFrame:
        """ Extacts and reads  a CSV file from a zip archive """
        if not file_path.endswith('.zip'):
            raise ValueError("File is not a zip file")
        
        with zipfile.ZipFile(file_path, "r") as z:
            z.extractall("../extracted_data")

        extracted_files= os.listdir("extracted_data")
        if not extracted_files:
            raise ValueError("No files found in the zip archive")
        csv_files = [f for f in extracted_files if f.endswith('.csv')]
        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV files found in the zip archive")
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files found in the zip archive, please specify which one to use")
        
        csv_file_data = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_data)

        return df
    

class DataIngestorMain:
    def get_data_ingestor(files_extension: str) -> data_ingestor:
        if files_extension == '.zip':
            return ZipDataIngestor()
        else:
            raise ValueError(f"Unsupported file extension: {files_extension}. Only .zip files are supported.")
        

if __name__ == "__main__":

    file_extension = ".zip" 
    ingestor = DataIngestorMain.get_data_ingestor(file_extension)
    file_path = "D:\\Code\\machine Learning & projects\\ATP_tennis_model\\data\\archive.zip"
    df=ingestor.ingest_data(file_path)
    print(df.head())

    