from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from src.database.db_connection import db
from sqlalchemy import select
from src.models.Employees import Employee
login_userbp = Blueprint("login_user",__name__,static_folder="static",template_folder="templates")

@login_userbp.route("/login_user",methods=["POST","GET"])
def user_login():
    if request.method == "POST":
        ci = request.form["cedula"]
        result = db.session.execute(select(Employee).where(Employee.cedula == ci))
        emp_result = result.first()
        if emp_result is not None:
            print(emp_result[0].name)
    return render_template("login_user.html",escudo = session["escudo"])