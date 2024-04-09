# Library-Management-System-Backend-APIs-Task
Library Management System | Backend API Task

## Build the below APIs using FastAPI in python.
### Library Management System, specifically the backend layer of the application. Built the API Layer of this system, mainly CRUD Operation, Details of each API is given below.


## INtegration Requirements

First Step: Clone Poject from git.

$ git clone https://github.com/ranvijay12345/Library-Management-System-Backend-API-Task.git

Second Step: Need to install the following in your invirenment: 

$ pip install fastapi
$ pip install pymongo 
$ pip install "uvicorn[standard]" 
$ pip install MongoClint 

Third Step: To run the application, Use the below command

$  uvicorn index:app --reload 


## Below are the details about Project

POST API: {\students\}
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-APIs-Task/assets/54628721/5f5dd606-8c3c-4e41-96dc-7c691be6b8a5)

GET API: {\students\}
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-APIs-Task/assets/54628721/02930d4a-f2c8-45fc-b3b6-f1c95da7624b)

GET API: {\students\{id}}
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-APIs-Task/assets/54628721/74a5e869-9c32-4121-93c6-c2897ccb1f0d)

PATCH API: {\students\{id}}
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-APIs-Task/assets/54628721/c9185247-f482-4fbd-b1bd-89d000117b1b)

After Updation data:
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-APIs-Task/assets/54628721/97c51f13-cc51-4cf1-a01c-c4763e533756)

DELETE API: {\students\{id}}
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-APIs-Task/assets/54628721/b8db8af4-5d0f-4bcf-8b4e-52e49a296474)

After Deletion, details of this id is not present in database:
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-APIs-Task/assets/54628721/8e4ceee8-7789-4253-8b13-667be292f246)



MongoDB Compass Database Structure:
![image](https://github.com/ranvijay12345/Library-Management-System-Backend-APIs-Task/assets/54628721/554f97a1-5406-4744-9762-f5b84a2609d0)
