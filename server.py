from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__) # intance of Flask


# http://127.0.0.1:5000/
@app.route("/", methods=["GET"])
def index():
    return "Welcome To Flask Framework"


# http://127.0.0.1:5000/cohort-62
@app.route("/cohort-62", methods=["GET"])
def cohort62():
    students_list = ["John", "Micheal", "Carlos", "Jonathan", "Robert", "Ashton", "Kirt"]
    return students_list


# http://127.0.0.1:5000/cohort-100
@app.route("/cohort-100", methods=["GET"])
def cohort100():
    students_list = ["Ashton", "John", "Carlos", "Johnathon"]
    return students_list


# http://127.0.0.1:5000/contact
@app.route("/contact", methods=["GET"])
def contact():
    information = {"email": "lmiranda@sdgku.edu", "phone": "619-123-4567"}
    return information


# http://127.0.0.1:5000/course-information
@app.route("/course-information", methods=["GET"])
def course_information():
    course_information = {
        "title": "Introduction Web API with Flask",
        "duration": "4 sessions", 
        "level": "beginner"
    }
    return course_information


# ---- Minichallenge ----
# Create a /user endpoint
# Return a dictionary with: name, role, is_active, and favorite_technologies
# Test it by visiting http://127.0.0.1:5000/user
@app.route("/user", methods=["GET"])
def get_user():
    user_information = {
        "name": "Ashton", 
        "role": "Software Developer", 
        "is_active": True,
        "favorite_technologies": ["Vue.js", "FastAPI", "Flask", "Curtis"]
    }
    return user_information, HTTPStatus.OK


# Path parameter
# Is a dynamic part of the URL used to identify a specific item or resource within an API.
@app.route("/greet/<string:name>")
def greet(name):
    return {"message": f"Hello {name}"}


# ----------- PRODUCTS ------------

products = [
  {
    "_id": 1,
    "title": "Freebird Scooter",
    "price": 249.99,
    "category": "Electronic",
    "image": "https://picsum.photos/seed/1/300/300"
  },
  {
    "_id": 2,
    "title": "Smart Watch",
    "price": 199.99,
    "category": "accessories",
    "image": "https://picsum.photos/seed/2/300/300"
  },
  {
    "_id": 3,
    "title": "Bluetooth Speaker",
    "price": 79.99,
    "category": "Electronics",
    "image": "https://picsum.photos/seed/3/300/300"
  }
]

# GET /api/products endpoint that return a list of products
@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify({
        "success": True,
        "message": "Products retrieved successfully",
        "data": products
    }), HTTPStatus.OK


# GET /api/products/2
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    for product in products:
        print(product)
        if product["_id"] == product_id:
            return jsonify({
                "success": True,
                "message": "Product retrieved successfully",
                "data": product
            }), HTTPStatus.OK

    return "Not found"


# POST /api/products
@app.route("/api/products", methods=["POST"])
def create_product():
    print(request.get_json())
    new_product = request.get_json()
    products.append(new_product)
    return jsonify({
        "success": True,
        "message": "Product successfully created",
        "data": new_product    
    }), HTTPStatus.CREATED


# ----------- COUPONS ------------
coupons = [
  {"_id": 1, "code": "WELCOME10", "discount": 10},
  {"_id": 2, "code": "SPOOKY25", "discount": 25},
  {"_id": 3, "code": "VIP50", "discount": 50}
]


# GET /api/coupons endpoint that returns a list of coupons.
@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return {"coupons": coupons}


# GET /api/coupons/count returns the number of coupons in the system.
@app.route("/api/coupons/count", methods=["GET"])
def get_coupons_count():
    return {"get-coupons-count": len(coupons)}


# POST /api/coupons
# GET /api/coupons/<int:id> 

if __name__ == "__main__":
    app.run(debug=True)
# When this file is run directly: __name__ == "__main__"
# When this file is imported as a module:

# Path parameter
# A path parameter is a dynamic segment of the URL to pinpoint a specific item or resource.
# http://127.0.0.1:5000/greet/leo
@app.route("/greet/<string:name>", methods=["GET"])
def greet(name):
  return f"hello {name}", HTTPStatus.OK


# GET - get a coupon by id
@app.route("/api/coupons/<int:id>", methods=["GET"])
def get_coupon_by_id(id):
  for coupon in coupons:
    if coupon["_id"] == id:
      return jsonify(coupon), HTTPStatus.OK
  return jsonify({"message": "Coupon not found"}), HTTPStatus.NOT_FOUND

# UPDATE - 


# DELETE - delete a coupon
@app.route("/api/coupons/<int:id>", methods=["DELETE"])
def delete_coupon(id):
  for index, coupon in enumerate(coupons):
    if coupon["_id"] == id:
      coupons.pop(index)
      return HTTPStatus.NO_CONTENT # 204
  return jsonify({"message": "Coupon not found"})


if __name__ == "__main__":
  app.run(debug=True)