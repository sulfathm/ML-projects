# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 23:50:29 2023

@author: user pc
"""

from flask import Flask , request , render_template
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)
model=pickle.load(open("energymodel.pkl","rb"))
@app.route("/")

def home():
    return render_template("index.html")
@app.route("/upload1")
def home1 ():
    return render_template("index2.html")

# @app.route("/upload2")
# def home2 ():
#     return render_template("register.html")

@app.route("/upload3")
def check ():
    return render_template("check.html")

@app.route("/upload4")
def reg ():
    return render_template("reg.html")

@app.route("/predict", methods=['POST'])
def predict():
    Thermal_Generation_Actual=float(request.values['text1'])
    Thermal_Generation_Estimated=float(request.values['text2'])
    Nuclear_Generation_Actual=float(request.values['text3'])
    Nuclear_Generation_Estimated=float(request.values['text4'])
    Hydro_Generation_Actual=float(request.values['text5'])
    Hydro_Generation_Estimated=float(request.values['text6'])
    df=pd.DataFrame({"Thermal_Generation_Actual":[Thermal_Generation_Actual],
                 "Thermal_Generation_Estimated":[Thermal_Generation_Estimated],
                 "Nuclear_Generation_Actual":[Nuclear_Generation_Actual],
                 "Nuclear_Generation_Estimated":[Nuclear_Generation_Estimated],
                 "Hydro_Generation_Actual":[Hydro_Generation_Actual],
                 "Hydro_Generation_Estimated":[Hydro_Generation_Estimated]})
    print(df)
    y_prediction=model.predict(df)
    print(y_prediction)
    
    
    return render_template("result.html",prediction_text="The total actual production is {} .".format(y_prediction))
if __name__=='__main__':
  app.run()
    