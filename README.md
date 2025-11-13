# Task Manager API

A backend API built with **FastAPI** that provides secure user authentication and task management.

## Features
- User Signup and Login with JWT-based authentication
- Password hashing and verification (Passlib)
- SQLAlchemy ORM integration (SQLite database)
- Modular architecture: models, schemas, auth, jwt_handler, database
- Environment variable management using `.env`
- Interactive API docs powered by FastAPI’s Swagger UI
- In-progress: Protected routes for user-specific task access

## Tech Stack
**Backend:** Python, FastAPI, SQLAlchemy, JWT, Passlib  
**Database:** SQLite (local dev)  
**Docs & Testing:** Swagger UI 
 

## Endpoints
| Method 	| Endpoint 		| Description 					|
|---------------|-----------------------|-----------------------------------------------|
| POST 		| `/signup` 		| Create a new user 				|
| POST 		| `/login` 		| Login and get JWT access token 		|
| GET  		| `/tasks/protected` 	| Access user-protected tasks (JWT required)	|

## Installation

git clone https://github.com/NikitaBhatia10/task-manager-api.git
cd task-manager-api
pip install -r requirements.txt
uvicorn main:app --reload


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
GET	               /tasks/protected	                      Example of secured endpoint	          ✅


Future Improvements:

Link tasks to logged-in user (multi-user support)
Add pagination and filtering
Add role-based access (Admin / User)
Deploy using Docker and Render


