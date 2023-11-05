# WorldCall Connect

Dependencies: 
- python@3.11
- flask@2.3.2
- bcrypt
- pymysql

Framework used: Python with Flask
Database used: Mysql

Features: 
- Phone number Validation
- User Profile can be viewed
- Form validation (login, registration)

How to run this project?
1. Please ensure you have the dependencies mentioned above to run this project. 
2. Create a mysql database called ```users``` Make changes to the config file, if any.
3. Run this project using ```python3.10 main.py```
4. The application would be up and running on http://127.0.0.1:5000/

Routes for the app: 
1. http://127.0.0.1:5000/
2. http://127.0.0.1:5000/register
3. http://127.0.0.1:5000/login
4. http://127.0.0.1:5000/dashboard
5. http://127.0.0.1:5000/myprofile
