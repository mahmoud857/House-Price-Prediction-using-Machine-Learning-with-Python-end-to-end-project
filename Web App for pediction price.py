#Importing Libraries

import numpy as np 
import pickle 
import streamlit

#Loading the Model
load_model=pickle.load(open("F:\ماشين ليرنج\مشاريع ماشين ليرنج end to end\Project 3 House Price Prediction using Machine Learning with Python  Machine Learning Project\Model for predicting house price","rb"))

#Function for prediction

def price_prediction(input_data):
    #change the input data to a numpy array
    input_data_asarray=np.asarray(input_data)
    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_asarray.reshape(1,-1)

    #predict the price of the house
    prediction=load_model.predict(input_data_reshaped)

    
    return prediction





def main():
    #title of the web app
    streamlit.title("House Price Prediction Web App")

    #input data from the user
    CRIM = float(streamlit.text_input("CRIM", value="0.0"))
    ZN = float(streamlit.text_input("ZN", value="0.0"))
    INDUS = float(streamlit.text_input("INDUS", value="0.0"))
    CHAS = int(streamlit.text_input("CHAS", value="0"))
    NOX = float(streamlit.text_input("NOX", value="0.0"))
    RM = float(streamlit.text_input("RM", value="0.0"))
    AGE = float(streamlit.text_input("AGE", value="0.0"))
    DIS = float(streamlit.text_input("DIS", value="0.0"))
    RAD = int(streamlit.text_input("RAD", value="0"))
    TAX = float(streamlit.text_input("TAX", value="0.0"))
    PTRATIO = float(streamlit.text_input("PTRATIO", value="0.0"))
    B = float(streamlit.text_input("B", value="0.0"))
    LSTAT = float(streamlit.text_input("LSTAT", value="0.0"))

    prices=""

    #creating a button for prediction
    if streamlit.button("House pricing prediction web app"):
        prices=price_prediction([CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT])
    streamlit.success(prices)


if __name__=="__main__":
    main()
    