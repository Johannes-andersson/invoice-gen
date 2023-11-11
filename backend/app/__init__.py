from app.routes import auth, invoice
from app.models import user, invoice
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)
