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


from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransfomrationConfig


from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:

    cleaned_data_path = os.path.join("artifacts", "clean_data.csv")
    
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")
    raw_data_path = os.path.join("artifacts", "data.csv")

    

class DataIngestion:
    def __init__(self):
        self.ingestion_confic = DataIngestionConfig()

    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            #create the folder aritfacts if not exist
            os.makedirs(os.path.dirname(self.ingestion_confic.train_data_path), exist_ok=True)
        
            corpus = pd.read_csv("artifacts/clean_data.csv")
            train_set, test_set = train_test_split(corpus, test_size=0.2, random_state= 15)

            train_set.to_csv(self.ingestion_confic.train_data_path, index = False, header=True)
            test_set.to_csv(self.ingestion_confic.test_data_path, index = False, header=True)

            logging.info("Inmgestion of the data iss completed")

            return (
                self.ingestion_confic.train_data_path,
                self.ingestion_confic.test_data_path
            )          





        except Exception as e:
            raise CustomException(e, sys)
        
        


if __name__ == "__main__":
    #call the from data_cleaning.py to clean the dataset and store in the artifacts folder
    obj = DataCleaning()
    df = obj.data_cleaning_process()
    print (df.head(5))


    obj_2 = DataIngestion()
    train_data, test_data = obj_2.initiate_data_ingestion()

    data_transformation=DataTransformation()
    X_train, Y_train, X_test, Y_test,_=data_transformation.initiate_data_transformation(train_data,test_data)
    print("*****")
    
    

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(X_train, Y_train, X_test, Y_test))
    

    


    
