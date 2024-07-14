import requests
import json
import pytest

@pytest.mark.user
# Positive Testcase for  Creating a new user
def test_create_user_positive(user_endpoint, headers):
    url = user_endpoint["create_new_user"]
    payload = {
        "id": 1,
        "username": "user123",
        "firstName": "John",
        "lastName": "nick",
        "email": "john@gmail.com",
        "password": "John123",
        "phone": "1234567890",
        "userStatus": 1
}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 200
    print(f"\n{payload}\n{response} User added successfully")

@pytest.mark.user
# Positive Testcase for getting a user by username
def test_get_username_positive(user_endpoint):
    url = user_endpoint["get_username"].format(username="user123")
    response = requests.get(url)
    assert response.status_code == 200
    print(f"\n{response} successfull")
    assert response.json()["username"] == "user123"

@pytest.mark.user
# Negative Testcase for checking a user by Invalid Username
def test_get_username_negative(user_endpoint):
    url = user_endpoint["get_username"].format(username="User_10001")
    response = requests.get(url)
    assert response.status_code == 404
    print(f"\n{response} user Not Found")

@pytest.mark.user
# Positive Testcase for  updating a user data - firstName
def test_update_user_positive(user_endpoint, headers):
    url = user_endpoint["update_user"].format(username="user123")
    payload = {
        "id": 1,
        "username": "user123",
        "firstName": "Mac",
        "lastName": "nick",
        "email": "john@gmail.com",
        "password": "John123",
        "phone": "1234567890",
        "userStatus": 1
    }
    response = requests.put(url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 200
    print(f"\n{payload}\n{response} user Updated successfully")

@pytest.mark.user
# Negative Testcase for  updating a user Invalid data
def test_update_user_negative(user_endpoint, headers):
    url = user_endpoint["update_user"].format(username="user123")
    payload = {
        "id": "xyz1001",
        "username": "user123",
        "firstName": "Mac",
        "lastName": "nick",
        "email": "john@gmail.com",
        "password": "John123",
        "phone": "1234567890",
        "userStatus": 1
    }
    response = requests.put(url, data=json.dumps(payload), headers=headers)
    assert response.status_code == 500
    print(f"\n{payload}\n{response} Invalid User Data")

@pytest.mark.user
# Positive Testcase deleting a user by username
def test_delete_user_positive(user_endpoint):
    url = user_endpoint["delete_user"].format(username="user123")
    response = requests.delete(url)
    assert response.status_code == 200
    print(f"\n{response} User deleted successfully")
