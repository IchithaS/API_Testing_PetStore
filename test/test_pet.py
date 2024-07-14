import requests
import json
import pytest

@pytest.mark.pet
# Positive Testcase for  adding a pet with valid data
def test_add_pet_positive(pet_endpoint, headers):
    url = pet_endpoint["add_new_pet"]
    payload = {
        "id": 1,
        "name": "Doggie",
        "status": "available"
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 200
    print(f"\n{payload}\n{response} Pet added successfully")
    assert response.json()["name"] == "Doggie"

@pytest.mark.pet
# Negative Testcase adding a pet with invalid data
def test_add_pet_negative(pet_endpoint, headers):
    url = pet_endpoint["add_new_pet"]
    payload = {
        "id": "123abc",
        "name": "Doggie",
        "status": "available"
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 500
    print(f"\n{payload}\n{response} Invalid Pet Data")

@pytest.mark.pet
# Positive Testcase for get the PetId by valid data
def test_get_PetId_positive(pet_endpoint, headers):
    url = pet_endpoint["get_pet_ByID"].format(pet_id=1)
    response = requests.get(url)
    assert response.status_code == 200
    print(f"\n{response} successfull" )
    assert response.json()["id"] == 1

@pytest.mark.pet
#Negative Testcase for Pet for InvalidID
def test_get_InvalidPetID_negative(pet_endpoint,headers):
    url= pet_endpoint["get_pet_ByID"].format(pet_id=22222)
    response = requests.get(url)
    assert response.status_code == 404
    print(f"\n{response} Pet Not Found")

@pytest.mark.pet
#Postive Testcase for Updating a pet Status
def test_update_Pet_Positive(pet_endpoint,headers):
    url = pet_endpoint["update_pet"]
    payload = {
        "id" : 1,
        "name" :"Doggie",
        "status": "sold"
    }
    response = requests.put(url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 200
    print(f"\n{payload}\n{response} Pet Updated successfully")
    assert response.json()["status"] == "sold"

@pytest.mark.pet
#Positive Testcase for Delete Pet by ID
def test_delete_PetID_Positive(pet_endpoint,headers):
    url = pet_endpoint["delete_pet"].format(pet_id=1)
    response = requests.get(url)
    assert response.status_code == 200
    print(f"\n{response} Pet deleted successfully")





