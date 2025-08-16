from zenml import pipeline, step, Model
from steps.data_ingest_step import data_ingest_step
from steps.handle_missing_step import missing_step

@pipeline(
    model=Model(
        name="b2b_prediction"
    )
)
def dl_pipeline():
    """This is End-toEnd DL Pipeline"""
    raw_data = data_ingest_step(
        file_path= "extracted_data/2008-2016-deliveries(detailed).csv"
    )
    handled_missing_data = missing_step(raw_data)
