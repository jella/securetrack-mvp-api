from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return {"message": "API SecureTrack ativa"}

if __name__ == '__main__':
    app.run(debug=True)
