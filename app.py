from datetime import date
import streamlit as st
import requests
from PIL import Image


image = Image.open('taxi.jpg')

st.image(image, caption='Taxi Fare APP')

'''
# TaxiFareModel front
'''


date_and_time = st.text_input("show date and time")

pick_up_latitude = st.text_input("pick up latitude")
pick_up_longitude = st.text_input("pick up longitude")
drop_off_latitude = st.text_input("drop off latitude")
drop_off_longitude = st.text_input("drop off longitude")
passenger_count = st.text_input("passenger_count")



url = f"https://taxifare.lewagon.ai/predict?pickup_datetime={date_and_time}&pickup_longitude={pick_up_longitude}&pickup_latitude={pick_up_latitude}&dropoff_longitude={drop_off_longitude}&dropoff_latitude={drop_off_latitude}&passenger_count={passenger_count}"
response =  requests.get(url).json()

if date_and_time and pick_up_latitude and pick_up_longitude and drop_off_latitude and drop_off_longitude and passenger_count:
    st.write(response)
