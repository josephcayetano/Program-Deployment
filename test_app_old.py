#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is functional"}

def test_valid_prediction():
    response = client.get(
        "/predict/delays",
        params={
            "arrival_airport": "JFK",
            "departure_time": "13:00",
            "arrival_time": "17:30"
        }
    )
    assert response.status_code == 200
    assert "average_delay_minutes" in response.json()

