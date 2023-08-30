from src.constants import *
from src.logger import logging
from src.exception import CustomException
import os, sys
import pandas as pd
import numpy as np
from src.config.configuration import *
from src.utils import load_model
from sklearn.pipeline import Pipeline
import pickle


PREDICTION_FOLDER = "batch_prediction"
PREDICTION_CSV = "prediction_csv"
PREDICTION_FILE = "output.csv"
FEATURE_ENGG_FOLDER = "feature_eng"

ROOT_DIR = os.getcwd()

BATCH_PREDICTION = os.path.join(ROOT_DIR,PREDICTION_FOLDER,PREDICTION_CSV)
FEATURE_ENG = os.path.join(ROOT_DIR,PREDICTION_FOLDER,FEATURE_ENGG_FOLDER)

class BatchPrediction:

    def __init__(self,input_file_path,
                 model_file_path,
                 transformer_file_path,
                 feature_engineering_file_path) -> None:
        self.input_file_path = input_file_path
        self.model_file_path = model_file_path
        self.transformer_file_path = transformer_file_path
        self.feature_engineering_file_path = feature_engineering_file_path


    def start_batch_prediction(self):
        try:
            # Load the feature engineering pipeline path
            with open(self.feature_engineering_file_path,'rb') as f:
                feature_pipeline = pickle.load(f)

            # Load the data transformation pipeline path

            with open(self.transformer_file_path,'rb') as f:
                processor = pickle.load(f)

            model = load_model(file_path=self.model_file_path)

            # Create feature engineering pipeline

            feature_engg_pipeline = Pipeline([
                ('feature_engineering',feature_pipeline)
            ])

            df = pd.read_csv(self.input_file_path)

            df.to_csv('zomato_delivery_time_prediction.csv')

            # Applying feature engineering pipeline steps

            df = feature_engg_pipeline.transform(df)

            df.to_csv('feature_engineering.csv')

            FEATURE_ENGINEERING_PATH = FEATURE_ENG
            os.makedirs(FEATURE_ENGINEERING_PATH,exist_ok=True)

            file_path = os.path.join(FEATURE_ENGINEERING_PATH,'batch_feature_eng.csv')
            df.to_csv(file_path,index=False)

            df = df.drop('Time_taken (min)',axis=1)
            df.to_csv('Time taken dropped.csv')

            transformed_data = processor.transform(df)

            file_path = os.path.join(FEATURE_ENGINEERING_PATH,'processor.csv')
            transformed_data.to_csv(file_path,index=False)

            predictions = model.predict(transformed_data)

            df_prediction = pd.DataFrame(predictions,columns=['prediction'])

            BATCH_PREDICTION_PATH = BATCH_PREDICTION

            os.makedirs(BATCH_PREDICTION_PATH,exist_ok=True)

            csv_path = os.path.join(BATCH_PREDICTION_PATH,'output.csv')

            df_prediction.to_csv(csv_path,index=False)
            logging.info('Batch Prediction done')

        except Exception as e:
            raise CustomException(e,sys)