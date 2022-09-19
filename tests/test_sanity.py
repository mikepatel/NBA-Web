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
# Setup
client = TestClient(app)


################################################################################
# Test cases
def test_index():
    response = client.get("/")
    assert response.status_code != 200


def test_databases():
    response = client.get("/databases")
    assert response.status_code == 200
    assert type(response.json()) == list
