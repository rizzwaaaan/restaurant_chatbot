import openai
import os
from dotenv import load_dotenv
from flask import Blueprint, request, jsonify
from models import db, Menu, Customer, Reservation, Order, Payment

load_dotenv()

routes = Blueprint("routes", __name__)

# ✅ Chatbot API (NLP)
openai.api_key = os.getenv("OPENAI_API_KEY")

@routes.route("/chatbot", methods=["POST"])
def chatbot_response():
    user_query = request.json.get("query", "")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful restaurant assistant."},
            {"role": "user", "content": user_query}
        ]
    )
    
    return jsonify({"response": response["choices"][0]["message"]["content"]})

# ✅ Fetch Menu Items
@routes.route('/menu', methods=['GET'])
def get_menu():
    menu_type = request.args.get("type")
    category = request.args.get("category")
    
    query = Menu.query
    if menu_type:
        query = query.filter(Menu.type == menu_type)
    if category:
        query = query.filter(Menu.category == category)
    
    menu_items = [{"name": item.name, "price": item.price, "image": item.image_url} for item in query.all()]
    
    return jsonify(menu_items)

# ✅ Create Reservation
@routes.route('/reserve', methods=['POST'])
def make_reservation():
    data = request.json
    new_reservation = Reservation(
        customer_id=data["customer_id"],
        table_number=data["table_number"],
        date=data["date"]
    )
    db.session.add(new_reservation)
    db.session.commit()
    
    return jsonify({"message": "Reservation Successful!", "reservation_id": new_reservation.id})

# ✅ Place Order
@routes.route('/order', methods=['POST'])
def place_order():
    data = request.json
    new_order = Order(
        customer_id=data.get("customer_id"),
        menu_item_id=data["menu_item_id"],
        quantity=data["quantity"]
    )
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify({"message": "Order Placed!", "order_id": new_order.id})

# ✅ Process Payment
@routes.route('/payment', methods=['POST'])
def process_payment():
    data = request.json
    new_payment = Payment(
        order_id=data["order_id"],
        amount=data["amount"],
        payment_method=data["payment_method"]
    )
    db.session.add(new_payment)
    db.session.commit()
    
    return jsonify({"message": "Payment Successful!", "payment_id": new_payment.id})