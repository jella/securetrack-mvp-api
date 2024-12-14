from flask import Flask
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run('127.0.0.1','3001',debug=True)