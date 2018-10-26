from flask import Flask
from storemanage import Products

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to the Store Manager App'


@app.route('/api/v1/products/', methods=['POST'])
def create_products():
    return Products.create_products()


@app.route('/api/v1/products/', methods=['GET'])
def get_products():
    return Products.get_products()


