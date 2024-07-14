# ** Developed and implementing an API testing framework using Python and Pytest for or PetStore Swagger API  **

**## About the Project** -- Overview

- This project presents a comprehensive API testing framework designed to automate API testing of the Petstore Swagger API, ensuring its quality and reliability. It focuses on testing the Pet, Store and User models.

**Setup and About the project**:

1. Install Required Libraries

   
     pip install 

     pytest : A framework for writing and running tests.
     requests : library for HTTP requests.
     pytest-html : generating HTML reports for pytest results.
     allure-pytest : generating Allure reports for pytest results.

2.  requirements.txt : This file lists the dependencies needed for the project

    pip install -r requirements.txt


3. List of the key features:
  - Test cases covering GET, POST, PUT, DELETE HTTP requests for Pet, Store and User models

4. Technologies Used
  - IDE: Pycharm
  - Coding language: python
  - Test automation framework: pytest
  - API testing library: requests for handling HTTP requests.
  - API testing tool: Postman

  5. Framework Structure
  
          PetStore_APIAutomation/
          ├── AllureReport_API
          ├── Report_Screenshots
          ├── test/
          │   ├──conftest.py
          │   ├── test_pets.py
          │   ├── test_store.py
          │   ├── test_User.py
          ├── main.py
          ├── README.md
          ├── report.html
          ├── requirements.txt
          ├── Test Result_Failed_Pet(example)-.html
          ├── Test Result_Pets -.html
          ├── Test Result_stores -.html
          ├── Test Result_user -.html

6 Project Structure
- Source code:
  - All project Source code are located within the 'Petstore_APIAutomation/test' folder.
  - Other Files: like README.md, Reqirement.txt, AllureReport_API, Test Results of HTML



7. validation of API responses:

   Successful status code verification: All response status codes matched expectations based on the Swagger document, for successful HTTP requests.

   Response body: Response body data consistently matched with the API's Swagger document.


8.  'conftest.py'  : is used to define fixtures and common setup tasks.

  
      --base_url() : Base URL for the API.
      --headers: headers used in requests.
      --pet_endpoints : pet API endpoints using the base URL.
      --store_endpoints : store API endpoints using the base URL.
      --user_endpoints : user API endpoints using the base URL.

9.  Test cases for Automation 

   - Pet Endpoint


        -Positive :-Creating a new pet
                   -Fetch Pet By PetID
                   -Updating a pet Status
                   -Delete Pet by ID
        -Negative :- Creating a pet with invalid data
                    -Fetch Pet By invalid PetID


- Store Endpoint


        -Positive :-Place an Order
                   -Fetch order ByID
                   -Delete oder by ID
                   
        -Negative :- Place an order with InvalidID
                    -Fetch by using Invalid OrderID

- User Endpoint


        -Positive :-Creating a new user
                   -Fetch user by username
                   -updating a user data
                  -Deleting a user by username
                   
        -Negative :- Fetch user by Invalid Username
                    -updating a user with Invalid data





 10. HTML Report

         Pets - file:///C:/Users/This%20Pc/PycharmProjects/APIAutomation/PetStrore_APIAutomation/Test%20Results_Pets%20-%20.html
         
         Store - file:///C:/Users/This%20Pc/PycharmProjects/APIAutomation/PetStrore_APIAutomation/Test%20Results_Store%20-%20.html
    
         Users - file:///C:/Users/This%20Pc/PycharmProjects/APIAutomation/PetStrore_APIAutomation/Test%20Results_User%20-%20.html

 11. Running the Tests
             Allure report

             pytest --alluredir=AllureReport_API
             allure serve .\AllureReport_API\
            
             Allure Report:
             http://192.168.220.251:56664/index.html#

 pytest-html
             
             py.test -v -s
             pytest --html=report.html

report.html

http://localhost:63342/PetStrore_APIAutomation/report.html?_ijt=nfl8rvsspmg1s0uihcckaepkg2&_ij_reload=RELOAD_ON_SAVE&sort=result

http://192.168.220.251:51839/index.html#





*Developed and implementing an API testing framework using Python and Pytest for or PetStore Swagger API 
-BY Ichitha S Bangera*