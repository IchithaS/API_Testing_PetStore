import requests
import json
import pytest


@pytest.mark.store
# Positive Testcase for  Place an order
def test_place_order_positive(store_endpoint, headers):
    url = store_endpoint["store_place_order"]
    payload = {
            "id": 1,
            "petId": 1,
            "quantity": 2,
            "shipDate": "2024-07-13T07:04:44.213Z",
            "status": "placed",
            "complete": True
        }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 200
    print(f"\n{payload}\n{response} order placed successfully")
    assert response.json()["status"] == "placed"

@pytest.mark.store
# Negative Testcase for Place an order with InvalidID
def test_place_order_negative(store_endpoint, headers):
    url = store_endpoint["store_place_order"]
    payload = {
            "id": "123xyz",
            "petId": 1,
            "quantity": 2,
            "shipDate": "2024-07-13T07:04:44.213Z",
            "status": "placed",
            "complete": True
        }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 500
    print(f"\n{payload}\n{response} Invalid Store Data")

@pytest.mark.store
# Positive Testcase for geting order ByID
def test_get_OrderByID_positive(store_endpoint, headers):
    url = store_endpoint["store_get_OderById"].format(oder_id=1)
    response = requests.get(url)
    assert response.status_code == 200
    print(f"\n{response} successfull" )
    assert response.json()["id"] == 1

@pytest.mark.store
#Negative Testcase for Invalid OrderID
def test_get_Invalid_OrderID_negative(store_endpoint,headers):
    url= store_endpoint["store_get_OderById"].format(oder_id=33333)
    response = requests.get(url)
    assert response.status_code == 404
    print(f"\n{response} Order Not Found")

@pytest.mark.store
#Positive Testcase for Delete oder by ID
def test_delete_OrderID_Positive(store_endpoint,headers):
    url = store_endpoint["store_get_OderById"].format(oder_id=1)
    response = requests.get(url)
    assert response.status_code == 200
    print(f"\n{response} order deleted successfully")



