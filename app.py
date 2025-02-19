#!/usr/bin/env python
# coding: utf-8

# import statements
from fastapi import FastAPI, HTTPException
import json
import numpy as np
import pickle
from datetime import datetime

#initializing FastAPI app
app = FastAPI()

#loading airport_econdings.json and finalized_model.pkl
with open('airport_encodings.json', 'r') as f:
    airports = json.load(f)

with open('finalized_model.pkl', 'rb') as f:
    model = pickle.load(f)

def create_airport_encoding(airport, airports):
    temp = np.zeros(len(airports))
    if airport in airports:
        temp[airports[airport]] = 1
        return temp
    return None

# TODO:  write the back-end logic to provide a prediction given the inputs
# requires finalized_model.pkl to be loaded 
# the model must be passed a NumPy array consisting of the following:
# (polynomial order, encoded airport array, departure time as seconds since midnight, arrival time as seconds since midnight)
# the polynomial order is 1 unless you changed it during model training in Task 2
# YOUR CODE GOES HERE

# TODO:  write the API endpoints.  
# YOUR CODE GOES HERE

@app.get("/")
async def root():
    return {"message": "API is functional"}

@app.get("/predict/delays")
async def predict_delays(arrival_airport: str, departure_time: str, arrival_time: str):
    try:
        #encoding arrival airport
        arrival_encoding = create_airport_encoding(arrival_airport, airports)
        if arrival_encoding is None:
            raise HTTPException(status_code=400, detail="Invalid arrival airport")

        #converting times to seconds since midnight
        dep_seconds = int(datetime.strptime(departure_time, '%H:%M').hour * 3600 + 
                          datetime.strptime(departure_time, '%H:%M').minute * 60)
        arr_seconds = int(datetime.strptime(arrival_time, '%H:%M').hour * 3600 + 
                          datetime.strptime(arrival_time, '%H:%M').minute * 60)

        #preparing input for the model
        input_data = np.array([[1, *arrival_encoding, dep_seconds, arr_seconds]])
        prediction = model.predict(input_data)

        #converting prediction to a Python type
        #delay_minutes = max(0, float(prediction[0])) we can use this but removes negatives
        delay_minutes = float(prediction[0])

        return {"average_delay_minutes": delay_minutes}
        
    except HTTPException as e:
        #re-raise HTTPException for FastAPI to handle
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



