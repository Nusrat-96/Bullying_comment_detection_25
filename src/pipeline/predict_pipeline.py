import os 
import sys
import pandas as pd

from src.exceptions import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
         pass 
    

    def predict (self, features):
         try:
              cleaner_path = os.path.join("artifacts", "data_cleaner.pkl")
              preprocessor_path = os.path.join("artifacts", "processor.pkl")
              model_path = os.path.join("artifacts", "model.pkl")


              data_cleaning= load_object(file_path=cleaner_path)
              preprocessor = load_object(file_path=preprocessor_path)
              model = load_object(file_path=model_path)

              data_cleaned = data_cleaning.transform(features)
              data_scled = preprocessor.transform (data_cleaned)
              prediction = model.predict (data_scled)

              return prediction
              

         except Exception as e:
              raise CustomException(e, sys)


class CustomData:
    def __init__(self, 
                 comments: str, 
                 likes: int, 
                 Related_to_post:int):
         self.comments = comments
         self.likes = likes
         self.Related_to_post = Related_to_post
             

    def get_data_as_data_frame(self):
         try:
              custom_data_input_dict = {
                   "comments":[self.comments],
                   "likes":[self.likes],
                   "Related_to_post": [self.Related_to_post]
              }
              return pd.DataFrame(custom_data_input_dict)
         
         except Exception as e:
              raise CustomException(e, sys)