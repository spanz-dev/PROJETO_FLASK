from app.repositories.user_repository import (
    get_all, get_by_id, create, update, delete
)

def list_users():
    return get_all()

def get_user(id):
    return get_by_id(id)

def add_user(name):
    if name:
        create(name)

def edit_user(id, name):
    if name:
        update(id, name)

def remove_user(id):
    delete(id)