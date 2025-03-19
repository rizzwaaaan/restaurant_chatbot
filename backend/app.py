from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins (for development)

# Database Configuration (SQLite Example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Menu Model
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to get all menu items
@app.route('/menu', methods=['GET'])
def get_menu():
    try:
        menu_items = Menu.query.all()
        return jsonify([{ "id": item.id, "name": item.name, "price": item.price } for item in menu_items])
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True, port=5050)
