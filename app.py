from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from src.database.db_connection import db
from src.blueprints.login_colegio import login_colegio
from src.blueprints.login_user import login_user
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+mysqlconnector://{config("MYSQL_USER")}:{config("MYSQL_PASSWORD")}@{config("MYSQL_HOST")}:{config("MYSQL_PORT")}/{config("MYSQL_DB")}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = config("SECRET_KEY")
app.register_blueprint(login_user.login_userbp)
app.register_blueprint(login_colegio.login_colebp)





if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)