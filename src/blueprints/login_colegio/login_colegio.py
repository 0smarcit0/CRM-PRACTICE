from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from src.database.db_connection import db
from src.models.Colegios import Colegio
from sqlalchemy import select
login_colebp = Blueprint("login_colegio",__name__,static_folder="static",template_folder="templates")

@login_colebp.route("/login_colegio",methods=["POST","GET"],)
def login_colegio():
    state =""
    if request.method == "POST":
       requested = True
       colegio = Colegio(colegio=request.form["colegio"],password=request.form["password"])
       result = db.session.execute(select(Colegio).where(Colegio.colegio == colegio.colegio).where(Colegio.password == colegio.password))
       colegio_enc=result.first()
       if colegio_enc is not None:
           session['escudo'] = colegio_enc[0].escudo
           print(colegio_enc[0].escudo)
           return redirect(url_for('login_user.user_login'))

    
    return render_template("login_colegio.html",found = state)