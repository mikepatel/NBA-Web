"""
Michael Patel
September 2022

Project description:

File description:

"""
################################################################################
# Imports
from fastapi.testclient import TestClient

# from other modules in project
from run import app


################################################################################
# Test cases
def test_index():
    response = TestClient(app).get("/")
    assert response.status_code != 200


def test_databases():
    response = TestClient(app).get("/databases")
    assert response.status_code == 200
    assert type(response.json()) == list
