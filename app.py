from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from create import create_api
from delete import delete_api
from update import update_api
from getAudio import get_api
from modell import db, init_app
import urllib.parse

app = Flask(__name__)

# Connection string parameters
params = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=RLE1340;"   
    "DATABASE=Audio_File;"  
    "Trusted_Connection=yes;"
)

# Encode the connection string using urllib.parse.quote_plus
app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(params)}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


init_app(app)

# Register blueprints
app.register_blueprint(create_api, url_prefix='/api')
app.register_blueprint(delete_api, url_prefix='/api')
app.register_blueprint(update_api, url_prefix='/api')
app.register_blueprint(get_api, url_prefix='/api')

# Default route
@app.route('/')
def index():
    return "Welcome to the Flask App"

if __name__ == "__main__":
    app.run(debug=True)
