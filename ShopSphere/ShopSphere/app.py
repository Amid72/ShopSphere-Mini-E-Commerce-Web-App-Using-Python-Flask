
from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "shopsphere_secret"

products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Headphones", "price": 2000},
    {"id": 3, "name": "Smart Watch", "price": 3500}
]

@app.route("/")
def home():
    return render_template("home.html", products=products)

@app.route("/add/<int:id>")
def add_to_cart(id):
    cart = session.get("cart", {})
    cart[str(id)] = cart.get(str(id), 0) + 1
    session["cart"] = cart
    return redirect(url_for("home"))

@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    cart_items = []
    total = 0

    for item_id, qty in cart.items():
        product = next(p for p in products if p["id"] == int(item_id))
        subtotal = product["price"] * qty
        total += subtotal
        cart_items.append({
            "product": product,
            "qty": qty,
            "subtotal": subtotal
        })

    return render_template("cart.html", cart_items=cart_items, total=total)

@app.route("/checkout")
def checkout():
    session.pop("cart", None)
    return "Order placed successfully!"

if __name__ == "__main__":
    app.run(debug=True)
