from flask import Blueprint, request, redirect, url_for, render_template
from app.services.user_service import (
    list_users, add_user, remove_user, get_user, edit_user
)

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def index():
    return render_template("index.html", users=list_users())

@user_bp.route("/add", methods=["POST"])
def add():
    add_user(request.form.get("name"))
    return redirect(url_for("user.index"))

@user_bp.route("/delete/<int:id>")
def delete(id):
    remove_user(id)
    return redirect(url_for("user.index"))

@user_bp.route("/edit/<int:id>")
def edit_page(id):
    user = get_user(id)
    return render_template("edit.html", user=user)

@user_bp.route("/update/<int:id>", methods=["POST"])
def update(id):
    edit_user(id, request.form.get("name"))
    return redirect(url_for("user.index"))