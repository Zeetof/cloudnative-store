from flask import Flask, jsonify

app = Flask(__name__)

# Dummy product data
products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Headphones", "price": 200},
    {"id": 3, "name": "Keyboard", "price": 100}
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
