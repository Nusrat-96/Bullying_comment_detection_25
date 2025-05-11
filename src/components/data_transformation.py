#this file will transform the cleaned comment to array value

import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

from src.exceptions import CustomException
from src.logger import logging
import os

from src.utils import save_object
from sklearn.preprocessing import FunctionTransformer


class DataTransfomrationConfig:
    processor_file_path = os.path.join("artifacts", "processor.pkl")



class DataTransformation:
    def __init__(self):
        self.data_trans_config = DataTransfomrationConfig()

    
    def get_data_transform_obj(self):

        try:
            categorical_feature= ["spell_correct_without_emo"]
            numerical_feature = ['likes',
                                 'Related_to_post',
                                 'punc_number',
                                 'emoji_number',
                                 'abusive_word_number',
                                 'positive_word_number']
            

            ''''
            # Fixed numerical pipeline
            numerical_pipeline = Pipeline([
                ('selector', FunctionTransformer(lambda x: x[numerical_feature], validate=False)),
                ('imputer', SimpleImputer(strategy="median")),
                ('scaler', StandardScaler())
            ])

            # Fixed categorical pipeline
            categorical_pipeline = Pipeline([
                ('selector', FunctionTransformer(lambda x: x[categorical_feature].squeeze(), validate=False)),
                ('tfidf', TfidfVectorizer(ngram_range=(1,1)))
            ])

            
            
            '''
            preprocessor = ColumnTransformer([('vectorizer', TfidfVectorizer(ngram_range=(1,1)), "spell_correct_without_emo",)],
                                             remainder="passthrough")
            

            logging.info("Get the Preprocessor Object")
            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
        


    def initiate_data_transformation(self, train_path, test_path):
        try:

            columns_name = ['spell_correct_without_emo','likes','Related_to_post',
            'punc_number','emoji_number',
            'abusive_word_number', 'positive_word_number','label']

            train_df = pd.read_csv(train_path, usecols = columns_name )
            test_df = pd.read_csv (test_path, usecols = columns_name )


            target_column = "label"

            input_feature_train_df = train_df.drop(columns=[target_column], axis=1)
            target_feature_train_df = train_df[target_column]


            input_feature_test_df = test_df.drop(columns=[target_column], axis=1)
            target_feature_test_df = test_df[target_column]



            preprocessing_obj= self.get_data_transform_obj()
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            #concatenates transformed
            '''
            # Safe concatenation with sparse matrix support
            def safe_concatenate(features, targets):
                # Convert sparse to dense if needed
                if hasattr(features, 'toarray'):
                    features = features.toarray()
                # Ensure targets are 2D
                targets = np.array(targets).reshape(-1, 1)
                return np.hstack([features, targets])

            
            train_arr = safe_concatenate(input_feature_train_arr, target_feature_train_df)
            test_arr = safe_concatenate(input_feature_test_arr, target_feature_test_df)
            '''

            

            save_object(
                file_path=self.data_trans_config.processor_file_path,
                obj = preprocessing_obj
            )


            return (
                input_feature_train_arr,
                target_feature_train_df,
                input_feature_test_arr,
                target_feature_test_df,
                self.data_trans_config.processor_file_path
            )
        


        except Exception as e:
            raise CustomException(e,sys)

