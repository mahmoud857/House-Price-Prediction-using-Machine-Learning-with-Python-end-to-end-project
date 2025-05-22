#first import the libraries 

import pickle
import numpy as np 

#load the model from disk
load_model=pickle.load(open("F:\ماشين ليرنج\مشاريع ماشين ليرنج end to end\Project 3 House Price Prediction using Machine Learning with Python  Machine Learning Project\Model for predicting house price","rb"))

input_data=(0.62739,0.00,8.140,0,0.5380,5.8340,56.50,4.4986,4,307.0,21.00,395.62,8.47)
#change the input data to a numpy array
input_data_asarray=np.asarray(input_data)
#reshape the array as we are predicting for one instance
input_data_reshaped=input_data_asarray.reshape(1,-1)

#predict the price of the house
prediction=load_model.predict(input_data_reshaped)

print("the prediction of the house price is:",prediction)