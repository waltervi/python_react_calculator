import pytest
from app.db import get_db
import json

def test_exists_required(client, auth, app):
    response = client.post("/v1/auth/register", json={"username": "aaa101", "password": "aaa101"})
    assert response.status_code == 200
    
    auth.login("aaa101","aaa101")
    assert client.post("v1/operations/", json={"operation": "ADDITION", "operand1": 1, "operand2": 2}).status_code == 200
    
    response =  client.get("/v1/operations/findall")
    assert response.status_code == 200
    
    data = json.loads(response.data)
    print(data)
    
    assert data[0]["type"] == "ADDITION"
    assert data[0]["amount"] == 10
    assert data[0]["user_balance"] == 990
