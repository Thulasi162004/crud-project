from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import User
from app.crud import (
    create_user,
    get_all_users,
    get_user,
    update_user,
    delete_user,
)

app = FastAPI(
    title="User CRUD API",
    version="1.0.0",
    description="FastAPI CRUD Application using MongoDB",
)

# -----------------------------
# CORS Configuration
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Development only
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Home
# -----------------------------
@app.get("/")
def home():
    return {"message": "Welcome to User CRUD API"}

# -----------------------------
# Create User
# -----------------------------
@app.post("/users")
def add_user(user: User):
    try:
        user_id = create_user(user.model_dump())
        return {
            "message": "User created successfully",
            "id": user_id,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------------
# Get All Users
# -----------------------------
@app.get("/users")
def fetch_users():
    try:
        return get_all_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------------
# Get User By ID
# -----------------------------
@app.get("/users/{user_id}")
def fetch_user(user_id: str):
    try:
        user = get_user(user_id)

        if user:
            return user

        raise HTTPException(status_code=404, detail="User not found")

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------------
# Update User
# -----------------------------
@app.put("/users/{user_id}")
def edit_user(user_id: str, user: User):
    try:
        update_user(user_id, user.model_dump())

        return {
            "message": "User updated successfully"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------------
# Delete User
# -----------------------------
@app.delete("/users/{user_id}")
def remove_user(user_id: str):
    try:
        delete_user(user_id)

        return {
            "message": "User deleted successfully"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))