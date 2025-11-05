from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from src.database.db_connection import db
from src.models.Colegios import Colegio
from sqlalchemy import select
from models
login_userbp = Blueprint("login_user",__name__,static_folder="static",template_folder="templates")

@login_userbp.route("/login_user",methods=["POST","GET"])
def user_login():
    if request.method == "POST":
        
    return render_template("login_user.html",escudo = session["escudo"])