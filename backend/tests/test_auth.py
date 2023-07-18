import pytest
from flask import g
from flask import session

from app.db import get_db

def test_auth_full_flow(client, app):

    # test that successful registration redirects to the login page
   # headers = {'Content-Type': 'application/json'}
    response = client.post("/v1/auth/register", json={"username": "aaa100", "password": "aaa100"})
    assert response.status_code == 200

    # test that the user was inserted into the database
    with app.app_context():
        assert (get_db().execute("SELECT * FROM user WHERE username = 'aaa100'").fetchone() is not None)

    # test the user can login now
    response = client.post("/v1/auth/login", json={"username": "aaa100", "password": "aaa100"})
    assert response.status_code == 200
    