'''
'data_ingestion.py'

Purpose:

This script is responsible for ingesting raw data, performing train-test split, and saving the datasets into separate files.

Key Components:

1. DataIngestionConfig: A data class that holds default file paths for the training, testing, and raw data.
2. DataIngestion: The main class responsible for data ingestion. It reads a CSV file (notebook/data/stud.csv), performs train-test split, and saves the datasets.

Steps:

1. Read the raw dataset ('notebook/data/stud.csv') into a Pandas DataFrame (df).
2. Create directories for the output files if they don't exist.
3. Save the raw dataset to a CSV file (self.ingestion_config.raw_data_path).
4. Perform train-test split on the DataFrame.
5. Save the training and testing datasets into separate CSV files.
6. Return the paths of the training and testing datasets.

Execution:
If the script is run directly (__name__ == "__main__"), an instance of DataIngestion is created, and the initiate_data_ingestion method is called to perform data ingestion.'''

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method or component')
        try:
            df=pd.read_csv('notebook/data/stud.csv')
            logging.info('read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train Test Split Initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        

        except Exception as e:
            raise CustomException(e,sys)

if __name__== "__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
    
   
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
