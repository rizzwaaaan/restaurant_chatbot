from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os
from models import db
from routes import routes

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Database Configuration using environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db.init_app(app)

# Register Routes
app.register_blueprint(routes)

# Run Flask App
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables are created

    print("🚀 Server running on http://127.0.0.1:5000")
    app.run(debug=True)
