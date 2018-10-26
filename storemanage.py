from flask import jsonify, request
import datetime

goods = [{
    'quantity' : 2,
    'id': 1,
    'category': 'qw',
    'product_name': 'dom',
    'price': 23,
    'description':'it must be'
}]


class Products:

    @staticmethod
    def create_products():
        if not request.json and 'quantity' not in request.json:
            return 'Ensure that the quantity name exists and well spelt'
        elif type(request.json['quantity']) != int:
            return 'quantity must be a number'
        print('quantity passed')
        if not request.json and 'category' not in request.json:
            return 'Ensure that category name exists and well spelt'
        elif type(request.json['category']) == int:
            return 'category value must start with atleast a letter'
        print('category created')
        if not request.json and 'product_name' not in request.json:
            return 'Ensure that product_name exists and well spelt'
        elif type(request.json['product_name']) == int:
            return 'product_name value must be a word'
        if not request.json and 'price' not in request.json:
            return 'Ensure that the price exists and well spelt'
        elif type(request.json['price']) != int or float:
            return 'Price should be a number'
        if not request.json and 'description' not in request.json:
            return 'Ensure that description exists and well spelt'
        elif type(request.json['description']) == int or float:
            return 'description should start with a letter'

        product = {
            'id': len(goods) + 1,
            'quantity': request.json['quantity'],
            'category': request.json['category'],
            'product_name': request.json['product_name'],
            'price': request.json['price'],
            'description': request.json['description'],

        }
        goods.append(product)
        return jsonify({'product': product}), 201

    @staticmethod
    def get_products():
        if len(goods) == 0:
            return 'No, products created yet'
        else:
            return jsonify({'products': goods})

    @staticmethod
    def get_product(product_id):
        if len(goods) == 0:
            return 'No goods created, you need to create one'
        elif type(product_id) != int:
            return 'Product_id should be a number'
        else:
            for good in goods:
                if good['id'] == product_id:
                    return jsonify({'Your product is':good})


# sales = []
#
#
# class Sales:
#
#     @classmethod
#     def create_sales(cls):
#         dat = datetime.datetime.utcnow()
#         if not request.json and 'attendant_name' not in request.json:
#             return 'Ensure that the attendant name exists and well spelt'
#         elif type(request.json['attendant_name']) == int:
#             return 'attendant name should start with a letter'
#         print('name passed')
#         if not request.json and 'customer_name' not in request.json:
#             return 'Ensure that category name exists and well spelt'
#         elif type(request.json['customer_name']) == int:
#             return 'customer name must start with atleast a letter'
#         print('category created')
#         if not request.json and 'product_name' not in request.json:
#             return 'Ensure that product_name exists and well spelt'
#         elif type(request.json['product_name']) == int:
#             return 'product_name value must be a word'
#         if not request.json and 'unit_price' not in request.json:
#             return 'Ensure that the price exists and well spelt'
#         elif type(request.json['unit_price']) != float:
#             return 'Price should have a decimal point eg 0.00, 2.0'
#         if not request.json and 'quantity' not in request.json:
#             return 'Ensure the quantity exists and well spelt'
#         elif type(request.json['quantity']) != int:
#             return 'quantity should be a number'
#
#         sales_made = {
#             'id': len(sales) + 1,
#             'attendant_name': request.json['attendant_name'],
#             'customer_name': request.json['customer_name'],
#             'product_name': request.json['product_name'],
#             'quantity': request.json['quantity'],
#             'unit_price': request.json['unit_price'],
#             'total': request.json['unit_price'] * request.json['quantity'],
#             'date': dat
#
#         }
#         sales.append(sales_made)
#
#         return jsonify({'Created': sales_made})
#
#     @staticmethod
#     def get_sales():
#         if len(sales) == 0:
#             return 'No sales made, please create the sales'
#         else:
#             return jsonify({'goods': sales})
#
#     @staticmethod
#     def get_sale(sales_id):
#         if len(sales) == 0:
#             return 'No, sales_made yet'
#         elif type(sales_id) != int:
#             return 'Please make sure that the sales Id is a number'
#         else:
#             for sale in sales:
#                 if sale['id'] == sales_id:
#                     return jsonify({'Requested sales record': sale})
