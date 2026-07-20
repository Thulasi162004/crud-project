from bson import ObjectId
from app.database import user_collection
from app.models import user_serializer, users_serializer


def create_user(user):
    result = user_collection.insert_one(user)
    return str(result.inserted_id)


def get_all_users():
    users = user_collection.find()
    return users_serializer(users)


def get_user(user_id):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return user_serializer(user)
    return None


def update_user(user_id, user):
    user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user}
    )


def delete_user(user_id):
    user_collection.delete_one({"_id": ObjectId(user_id)})