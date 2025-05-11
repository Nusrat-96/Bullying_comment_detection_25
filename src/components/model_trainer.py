import os
import sys
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.metrics import classification_report, accuracy_score

from src.logger import logging
from src.exceptions import CustomException
from src.utils import save_object, load_object, evaluate_models


from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    model_train_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:

    def __init__(self):
        self.model_train_config = ModelTrainerConfig()

    def initiate_model_trainer(self, X_train, Y_train, X_test, Y_test):
        
        try:
            
            models = {
                "Random_Forest": RandomForestClassifier(),
                "SVM": SVC(),
                "KNN":KNeighborsClassifier(),
                "Adaboost": AdaBoostClassifier(),
                "NaiveBayes": MultinomialNB()
            }

            
            params = {
                "Random_Forest": {
                    "n_estimators": [170],
                    "random_state": [3]  # Standard practice to use a single fixed random state
                },
                "SVM": {
                    "kernel": ["linear", "rbf"],  # Corrected spelling and added options
                    "C": [0.1, 1, 10],          # More reasonable C values
                    "gamma": ['scale', 'auto']   # Important for rbf kernel
                },
                "KNN": {"n_neighbors":[3]},
                "Adaboost":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "NaiveBayes": {"alpha":[0.5,1.0]}
            }
            
            
            model_report:dict=evaluate_models(X_train=X_train, Y_train=Y_train,
                                               X_test=X_test, Y_test = Y_test,
                                                models=models,param=params)
                
            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            

            if best_model_score<0.4:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_train_config.model_train_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_square = accuracy_score(Y_test, predicted)
            return r2_square, best_model_name, model_report
            

            '''
            model = RandomForestClassifier(n_estimators=170, random_state=3)
            model.fit(X_train, Y_train)
            predict = model.predict(X_test)
            print(accuracy_score(Y_test,predict))
            '''

            
        except Exception as e:
            raise CustomException(e,sys)