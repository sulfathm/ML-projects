# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 22:22:02 2023

@author: user pc
"""

from flask import Flask , request , render_template
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
def reg ():
    return render_template("reg.html")

@app.route("/upload3")
def check ():
    return render_template("check.html")

@app.route("/predict", methods=['POST'])
def predict():
    Country=(request.values['text1'])
    daily_oil_consumption=float(request.values['text2'])
    world_share=float(request.values['text3'])
    yearly_gallons_per_capita=float(request.values['text4'])
    price_per_liter_pkr=float(request.values['text5'])
    GDP_per_capita=float(request.values['text6'])
    price_per_gallon=float(request.values['text7'])
    gallons_gdp_per_capita_can_buy=float(request.values['text8'])
    Xtimes_yearly_gallons_per_capita_buy=float(request.values['text9'])
    df=pd.DataFrame({"a":[Country],
                     "b":[daily_oil_consumption],
                     "c":[world_share],
                     "d":[yearly_gallons_per_capita],
                     "e":[price_per_liter_pkr],
                     "f":[GDP_per_capita],
                     "g":[price_per_gallon],
                     "h":[gallons_gdp_per_capita_can_buy],
                     "i":[Xtimes_yearly_gallons_per_capita_buy]})
    print(df)
    y_prediction=model.predict(df)
    print(y_prediction)
    
    return render_template("result.html",prediction_text="Price per liter is {} .".format(y_prediction))
if __name__=='__main__':
  app.run()
    