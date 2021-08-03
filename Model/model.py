#Importing Packages
import numpy as np
import pandas as pd
import pickle
import re
import nltk
import string
import warnings
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
import json

#Function to predict from saved model
def model_pred(json_file):

    #Initialize the variables
    df1 = json_file 
    tweet=[]

    #Arrange data
    for i in range(len(df1)):
      tweet.append(df1[i])
    df=pd.DataFrame(tweet, columns=["text"])

    #Data Cleaning
    df['cleantext'] = df['text'].str.replace("@", "") 
    df['cleantext']=df['cleantext'].str.replace(r"http\S+", "")
    df['cleantext']=df['cleantext'].str.replace("[^a-zA-Z]", " ")

    #Extract models from saved models
    vect=CountVectorizer(decode_error="replace", vocabulary=pickle.load(open("feature.pkl", "rb"))) #Change the feature vector
    test=vect.transform(df['cleantext'])
    model=pickle.load(open("finalized_model.sav", "rb")) #Change the model name

    #Pass the data to the model
    res=model.predict(test)
    total=0
    hpcount=0
    for i in res:
        total+=1
        if i==4:
            hpcount+=1
    hpper=float(hpcount)/total

    #Return the results
    return hpper