# Backend - User CRUD API

This backend is a FastAPI application that provides CRUD operations for user data stored in MongoDB.

## Features

- Create a user
- Read all users
- Read a single user by ID
- Update a user
- Delete a user

## Stack

- Python
- FastAPI
- MongoDB
- PyMongo
- Python dotenv
- Pydantic

## Prerequisites

- Python 3.11+ installed
- MongoDB Atlas or local MongoDB instance
- `pip` package manager

## Setup

1. Open a terminal in the `backend` folder.
2. Create a virtual environment (recommended):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Create a `.env` file in the `backend` folder with these variables:

```dotenv
MONGODB_URL=<your_mongodb_connection_string>
DATABASE_NAME=<your_database_name>
```

Example:

```dotenv
MONGODB_URL=mongodb+srv://username:password@cluster0.example.mongodb.net/?retryWrites=true&w=majority
DATABASE_NAME=userdb
```

## Run the API

Start the development server:

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:

- `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

- `GET /` - Home endpoint
- `POST /users` - Create a new user
- `GET /users` - Get all users
- `GET /users/{user_id}` - Get a user by ID
- `PUT /users/{user_id}` - Update a user by ID
- `DELETE /users/{user_id}` - Delete a user by ID

## Data Model

Request body for `POST /users` and `PUT /users/{user_id}`:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 30
}
```

## Notes

- CORS is currently configured to allow any origin for development.
- Ensure the MongoDB connection string is valid and the database name exists or can be created by the app.
