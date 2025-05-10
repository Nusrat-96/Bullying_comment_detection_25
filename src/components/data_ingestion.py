# connect all the components and save the files 
import os 
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.exceptions import CustomException
from src.logger import logging
from src.components.data_cleaning import DataCleaning
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

'''
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
'''

@dataclass
class DataIngestionConfig:
    
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")
    raw_data_path = os.path.join("artifacts", "data.csv")

    Bengali_splling = os.path.join("artifacts","bangla_spelling_correction_dectionary.txt")
    positive_word = os.path.join("artifacts", "Bengali_positive_word.txt")
    negative_word = os.path.join("artifacts", "bengali_swear_word.txt")


class DataIngestion:
    def __init__(self):
        self.ingestion_confic = DataIngestionConfig()

    
    def initiate_data_ingestion(self):
        df = pd.read_csv("notebook/data/")


if __name__ == "__main__":
    obj = DataCleaning()
    obj.data_cleaning_process()
