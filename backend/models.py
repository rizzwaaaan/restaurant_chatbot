from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # 'veg' or 'non-veg'
    category = db.Column(db.String(50), nullable=False)  # 'appetizer', 'main course', 'dessert'
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.Text, nullable=False)  # Using Text for long URLs

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    preferences = db.Column(db.JSON, nullable=True)  # Use JSONB for efficient querying

class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    table_number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default='pending', nullable=False)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=True)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)
    status = db.Column(db.String(50), default='pending', nullable=False)
    order_time = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)  # 'cash', 'card', 'UPI'
    status = db.Column(db.String(50), default='pending', nullable=False)
    payment_time = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
