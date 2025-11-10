Task Manager API

A secure and modern Task Management REST API built using FastAPI, SQLAlchemy, and JWT authentication.
It supports user registration, login, and protected task management routes.

Features:

User signup and login
Secure JWT authentication
Create, Read, Update, Delete (CRUD) tasks
Each user can access only their own tasks
SQLite database (can easily switch to PostgreSQL/MySQL)
Automatic API documentation with Swagger UI

Tech Stack:

Backend Framework  - 	  FastAPI
Database ORM       - 	  SQLAlchemy
Authentication     - 	  JWT (via python-jose)
Password Hashing   - 	  Passlib Bcrypt
Server             - 	  Uvicorn


 Installation & Setup:
 
1. Clone the repository
git clone https://github.com/<your-username>/task-manager-api.git
cd task-manager-api

2️. Create a virtual environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️. Install dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt yet, you can create one:

pip freeze > requirements.txt

4️. Run the app
uvicorn main:app --reload


Open in browser:
http://127.0.0.1:8000/docs
 (Swagger UI)

Authentication Flow

Register a new user

POST /signup


Example body:

{
  "username": "john",
  "password": "mypassword"
}


Login and get JWT token

POST /login


Response:

{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}


Authorize in Swagger UI

Click Authorize

Paste:

Bearer <your_token_here>


Click Authorize → Close

Access protected routes

Example:

GET /tasks/protected


Response:

{
  "message": "Hello john, here are your protected tasks!"
}


Project Structure:

task_manager_api/
│
├── main.py             # FastAPI app & routes
├── models.py           # SQLAlchemy models (User, Task)
├── schemas.py          # Pydantic schemas
├── database.py         # DB connection
├── auth.py             # Password hashing & auth helpers
├── jwt_handler.py      # JWT token creation/verification

API Endpoints Overview: 
Method	          Endpoint	                              Description	                        Auth Required
POST               /signup	                              Register a new user	                  ❌
POST	             /login	                                Login and get JWT token	              ❌
GET	               /tasks	                                Get all tasks                        	✅
POST	             /tasks	                                Create a new task	                    ✅
PUT	               /tasks/{id}	                          Update a task	                        ✅
DELETE	           /tasks/{id}	                          Delete a task	                        ✅
GET	               /tasks/protected	                      Example of secured endpoint	          ✅


Future Improvements:

Link tasks to logged-in user (multi-user support)
Add pagination and filtering
Add role-based access (Admin / User)
Deploy using Docker and Render


