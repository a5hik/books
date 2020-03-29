from flask import Flask, request, jsonify
from service import BooksService


app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/books", methods=["POST"])
def create_book():
    return jsonify(BooksService().create(request.get_json()))


@app.route("/books", methods=["GET"])
def list_book():
    return jsonify(BooksService().list())


if __name__ == "__main__":
    app.run(debug=True, port=8888)
