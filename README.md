# Library-Management-System-Backend-APIs-Task
Library Management System | Backend API Task

## Build the below APIs using FastAPI in python.
### Library Management System, specifically the backend layer of the application. Built the API Layer of this system, mainly CRUD Operation, Details of each API is given below.


### INtegration Requirements

First Step: Clone Poject from git.

    $ git clone https://github.com/ranvijay12345/Library-Management-System-Backend-API-Task.git

Second Step: Need to install the following in your invirenment: 

    $ pip install fastapi

    $ pip install pymongo

    $ pip install "uvicorn[standard]"

    $ pip install MongoClint
  


### Running the project

    $ uvicorn index:app --reload

### Project URL link : https://library-management-system-backend-api-zkxk.onrender.com/students


#### Below are the details about Project

POST API: {\students\}
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-API-Task/assets/54628721/d263cf8e-f0a5-4251-bac4-3d0ee7ae7bed)


GET API: {\students\}
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-API-Task/assets/54628721/4d7a4c3c-fc64-4784-829c-0a95446d6346)


GET API: {\students\{id}}
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-API-Task/assets/54628721/dd1554d2-6d8a-410f-b396-935e6dbfb7d5)


PATCH API: {\students\{id}}
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-API-Task/assets/54628721/583147f5-c4f0-41e1-97c6-98ba7ad9f593)


After Updation data:
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-API-Task/assets/54628721/5c2f4adc-aff9-45d2-8d78-b9625d20b042)


DELETE API: {\students\{id}}
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-API-Task/assets/54628721/910d56cd-9325-46c0-94e2-b7777f72e1f6)


After Deletion, details of this id is not present in database:
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-API-Task/assets/54628721/b11f86f4-7b3f-47f3-b5df-37fd75e10eed)


MongoDB Compass Database Structure:
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-API-Task/assets/54628721/f4dcb9f7-6452-4a1a-ad08-e17f28e19c16)

