import os,sys
from datetime import datetime

# artifact > pipeline folder > timestamp > output

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()

# variables for fetching data
ROOT_DIR_KEY = os.getcwd()
DATA_DIR = "Data"
DATA_DIR_KEY = "finalTrain.csv"

# delivery_time_prediction/DATA_DIR/DATA_DIR_KEY

ARTIFACT_DIR_KEY = "Artifact"

# variables to store the ingested data into artifacts

# delivery_time_prediction/ARTIFACT_DIR_KEY/DATA_INGESTION_KEY
# delivery_time_prediction/ARTIFACT_DIR_KEY/DATA_INGESTION_KEY/DATA_INGESTION_RAW_DATA_DIR_KEY
# delivery_time_prediction/ARTIFACT_DIR_KEY/DATA_INGESTION_KEY/DATA_INGESTION_INGESTED_DATA_DIR_KEY

DATA_INGESTION_KEY = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested_dir"
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY = "train.csv"
TEST_DATA_DIR_KEY = "test.csv"

# Data Transformation related variables

DATA_TRANSFORMATION_ARTIFACT = "data_transformation"
DATA_PREPROCESSED_DIR = "processor"
DATA_TRANSFORMATION_PROCESSING_OBJ = "processor.pkl"
DATA_TRANSFORM_DIR = "transformation"
TRANSFORM_TRAIN_DIR_KEY = "train.csv"
TRANSFORM_TEST_DIR_KEY = "test.csv"

# artifact/data_transformation/processor >(processor.pkl) and transformation >(train.csv and test.csv)