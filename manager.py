from flask import Flask
from storemanage import Products, Sales

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


@app.route('/api/v1/products/<int:product_id>', methods=['Get'])
def get_product(product_id):
    return Products.get_product(product_id)


@app.route('/api/v1/sales/', methods=['Get'])
def get_sales():
    return Sales.get_sales()

@app.route('/api/v1/sales/<int:sales_id>', methods=['GET'])
def get_sale(sales_id):
    return Sales.get_sale(sales_id)


@app.route('/api/v1/sales/', methods=['POST'])
def create_sales():
    return Sales.create_sales()


if __name__ == '__main__':
    app.run(debug=True)