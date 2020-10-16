import numpy as np
import pickle
import pandas as pd
import streamlit as st


pickle_in = open("random_forest_regression_model.pkl","rb")
model = pickle.load(pickle_in)

#def car_selling_price(Present_Price,Kms_Driven,Owner,Fuel_Type,Transmission):
 #   prediction = model.predict([[Present_Price,Kms_Driven,Owner,Fuel_Type,Transmission]])
 #   print(prediction)
  #  return prediction



def run():
    st.sidebar.info("This app is created using pycaret and streamlit")
    st.title("Car_Seelling Price")


    Present_Price = st.number_input("Present_Price(in lakhs)")
    Kms_Driven = st.number_input("Kms_Driven")
    Owner = st.selectbox("Owner",[0,1,3])
    st.text("Fuel Type")
    if st.checkbox("Petrol"):
        Fuel_Type_Diesel = 0
    elif st.checkbox("Diesel"):
        Fuel_Type_Diesel = 1
    st.text("Transmission")
    if st.checkbox("Manual"):
        Transmission_Manual = 1
    elif st.checkbox("Auto"):
        Transmission_Manual = 1
    st.text("Seller_type")
    if st.checkbox("Individual"):
        Seller_Type_Individual = 0
    elif st.checkbox("Dealer"):
        Seller_Type_Individual = 1

    no_year = st.selectbox("no_year", [ 6,  7,  3,  9,  2,  5,  4, 11, 10,  8, 17, 12, 14, 15, 16, 13])


    result = ""




    if st.button("Predict"):
        result = model.predict([[Present_Price,Kms_Driven,Owner,Fuel_Type_Diesel,Transmission_Manual,Seller_Type_Individual,no_year]])
    st.success("You can sell car at {} lakhs".format(result))






if __name__=="__main__":
    run()