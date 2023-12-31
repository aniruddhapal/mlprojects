'''
'data_transformation.py'

Purpose:

This script is responsible for preprocessing and transforming the input data for machine learning.

Key Components:

1. DataTransformationConfig: A data class holding the file path for saving the preprocessor object.
2. DataTransformation: The main class responsible for data transformation. It defines a preprocessing pipeline and saves the preprocessor object.

Steps:

1. Define numerical and categorical columns.
2. Create a preprocessing pipeline for numerical and categorical columns separately.
3. Use a ColumnTransformer to combine the numerical and categorical pipelines.
4. Read training and testing datasets.
5. Obtain the preprocessing object.
6. Apply the preprocessing object to the datasets.
7. Save the preprocessing object.
8. Return the transformed training and testing arrays and the path to the saved preprocessor object.

Execution:
If imported as a module, the classes and functions are available for use in other scripts.
'''


import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self) -> None:
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):  

        '''This Function performing Preprocessing and Data Transformation'''

        try:
            numerical_columns = ['reading_score', 'writing_score']
            categorical_columns = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

            num_pipeline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler(with_mean=False))
                ]
            )
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )
            preprocessor=ColumnTransformer(
                [("num_pipelines",num_pipeline,numerical_columns),
                 ("cat_pipelines",cat_pipeline,categorical_columns)
                ]
            )
            
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

            try:
                train_df=pd.read_csv(train_path)
                test_df=pd.read_csv(test_path)

                logging.info("Read train and test data completed")
                logging.info("Obtaining preprocessing object")

                preprocessing_obj=self.get_data_transformer_object()

                target_column_name="math_score"
                numerical_columns=['writing_score','reading_score']

                input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
                target_feature_train_df=train_df[target_column_name]

                input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
                target_feature_test_df=test_df[target_column_name]

                logging.info("Applying preprocessing object on training dataframe and test dataframe")

                input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
                input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

                train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
                test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

                logging.info(f"Saved Preprocessing Object")

                save_object(
                    file_path=self.data_transformation_config.preprocessor_obj_file_path,
                            obj=preprocessing_obj
                            )
                
                return (
                    train_arr,
                    test_arr,
                    self.data_transformation_config.preprocessor_obj_file_path

                )

            except Exception as e:
                raise CustomException(e,sys)