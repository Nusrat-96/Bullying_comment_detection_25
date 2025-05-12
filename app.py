from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

#app.debug = True

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            comments=request.form.get('comments'),
            likes=request.form.get('likes'),
            Related_to_post=request.form.get('Related_to_post')
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline=PredictPipeline()

        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        print(results)
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0", debug = True)        # if we don't give debug=True then it would not work



#to relseast the server command is -> sudo kill -9 $(sudo lsof -t -i :5000) 