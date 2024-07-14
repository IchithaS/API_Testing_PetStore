import pytest
import requests

# Base URL - PetStrore Swagger
@pytest.fixture(scope="session")
def base_url():
    return "https://petstore.swagger.io/v2"

# Headers
@pytest.fixture(scope="session")
def headers():
    return {"Content-Type": "application/json"}

# Pet API Endpoints
@pytest.fixture(scope="session")
def pet_endpoint(base_url):
    return {
        "add_new_pet": f"{base_url}/pet",
        "get_pet_ByID": f"{base_url}/pet/{{pet_id}}",
        "update_pet": f"{base_url}/pet",
        "delete_pet": f"{base_url}/pet/{{pet_id}}"
    }

#Store API Endpoints
@pytest.fixture(scope="session")
def store_endpoint(base_url):
    return {
        "store_place_order": f"{base_url}/store/order",
        "store_get_OderById": f"{base_url}/store/order/{{oder_id}}",
        "Sore_detele_order": f"{base_url}/store/order/{{oder_id}}",
    }

#User API Endpoints
@pytest.fixture(scope="session")
def user_endpoint(base_url):
    return {
        "create_new_user": f"{base_url}/user",
        "get_username": f"{base_url}/user/{{username}}",
        "update_user": f"{base_url}/user/{{username}}",
        "delete_user": f"{base_url}/user/{{username}}"
    }