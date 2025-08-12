from zenml import pipeline, step, Model
from steps.data_ingest_step import data_ingest_step

@pipeline(
    model=Model(
        name="b2b_prediction"
    )
)
def dl_pipeline():
    """This is End-toEnd DL Pipeline"""
    raw_data = data_ingest_step(
        file_path= "data/zip/2008-2016 (detailed).zip"
    )
