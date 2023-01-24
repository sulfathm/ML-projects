# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 23:44:11 2023

@author: user pc
"""

from flask import Flask, render_template , request
import pandas as pd
import numpy as np
import pickle


app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))
@app.route("/")
def home():
  return render_template("index.html")

@app.route("/upload1")
def login ():
  return render_template("login.html")

@app.route("/upload2")
def reg():
  return render_template("register.html")

@app.route("/upload3")
def check():
  return render_template("check.html")


@app.route("/predict", methods=['POST'])
def predict():
    servingsize=(request.values['text1'])
    
    calories=(request.values['text2'])
    
    totalfat=(request.values['text3'])
    
    saturatedfat=(request.values['text4'])
    
    transfat=(request.values['text5'])

    cholesterol=(request.values['text6'])
    sugar=(request.values['text7'])
    
    totalcarbohydrate=(request.values['text8'])
    protein=(request.values['text9'])
    sodium=(request.values['text10'])
    
    dieteryfibre=(request.values['text11'])
    calcium=(request.values['text12'])
    vitaminD=(request.values['text13'])
    iron=(request.values['text14'])
    
    df=pd.DataFrame({"servingsize":[servingsize],
                     "calories":[calories],
                     "totalfat":[totalfat],
                     "saturatedfat":[saturatedfat],
                     "transfat":[transfat],
                     "cholesterol":[cholesterol],
                     "sugar":[sugar],
                     "totalcarbohydrate":[totalcarbohydrate],
                     "protein":[protein],
                     "sodium":[sodium],
                     "dieteryfibre":[dieteryfibre],
                     "calcium":[calcium],
                     "vitaminD":[vitaminD],
                     "iron":[iron]})
    print(df)
    y_predict=model.predict(df)
    print(y_predict)
    
    if y_predict>=0 and y_predict <=0.9:
      prediction=("1 % low fat milk")
    elif y_predict>=1 and y_predict<=1.9:
      prediction=("Almond milk")
    elif y_predict>=2 and y_predict<=2.9:
      prediction=("Cashew Milk	")
    elif y_predict>=3 and y_predict<=3.9:
      prediction=("Coconut Milk	")
    elif y_predict>=4 and y_predict<=4.9:
      prediction=("Oat Milk")
    elif y_predict >=5 and y_predict<=5.9:
      prediction=("soy milk")
    else:
      prediction=("whole milk")
    
    return render_template("result.html",prediction_text="your milk type is {} .".format(prediction))
if __name__=='__main__':
  app.run()

