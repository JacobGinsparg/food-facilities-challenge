from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient
from food_facilities_challenge.database import Database
from food_facilities_challenge.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(scope="session")
def db() -> Database:
    return Database(db_path="data/test_data.csv")


@pytest.mark.router_facilities
def test_get_facilities_by_applicant(client: TestClient):
    response = client.get(f"/facilities/search/applicant/The Geez Freeze")
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["Count"] == 1
    assert response_json["Facilities"][0]["Applicant"] == "The Geez Freeze"


@pytest.mark.router_facilities
def test_get_facilities_by_street(client: TestClient):
    response = client.get(f"/facilities/search/street/351 CALIFORNIA ST")
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["Count"] == 2
    assert {facility["locationid"] for facility in response_json["Facilities"]} == {1565593, 1606346}


@pytest.mark.router_facilities
def test_get_facilities_by_street_partial(client: TestClient):
    response = client.get(f"/facilities/search/street/SANSOME")
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["Count"] == 7
    assert {facility["locationid"] for facility in response_json["Facilities"]} == {
        1591820,
        934719,
        1591839,
        1585966,
        934518,
        934555,
        1337923,
    }


@pytest.mark.router_facilities
def test_get_nearby_facilities(client: TestClient):
    # Lat/Long for the MFA in Boston
    response = client.get("/facilities/search/location/42.339507857603564/-71.09410164701363")
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["Count"] == 5
    assert {facility["locationid"] for facility in response_json["Facilities"]} == {
        1591825,
        1589659,
        1585964,
        1575156,
        1585475,
    }
