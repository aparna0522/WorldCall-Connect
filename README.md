# WorldCall Connect

# Project Description:
A simple login, and registration portal(microservice), created using flask framework for Python, supporting the system using MySQL database. Lets user to see their profile. 

# Dependencies: 
- python@3.11
- flask@2.3.2
- bcrypt
- pymysql

# Features: 
- Phone number Validation
- User Profile can be viewed
- Form validation (login, registration)

# How to run this project?
1. Please ensure you have the dependencies mentioned above to run this project. 
2. Create a mysql database called ```users``` Make changes to the config file, if any.
3. Next create a table users inside this database with the following command:
   ```create table users(name varchar(20), email varchar(20) primary key, phone_num varchar(30), password varchar(20), confirm_password varchar(20));```
5. Run this project using ```python3.10 main.py```
6. The application would be up and running on http://127.0.0.1:5000/

# Project Demo
https://github.com/aparna0522/WorldCall-Connect/assets/36110304/c6b3d2b2-e4cc-4e01-a3a1-43ef24766d00

# Routes for the app: 
1. http://127.0.0.1:5000/
2. http://127.0.0.1:5000/register
3. http://127.0.0.1:5000/login
4. http://127.0.0.1:5000/dashboard
5. http://127.0.0.1:5000/myprofile
