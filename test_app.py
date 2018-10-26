
import json
from manager import app

import pytest

@pytest.fixture()
def client():
    test_child = app.test_client()
    return test_child


class TestCases:
    def test_create_products(self, client):
        response = client.post('/api/v1/products/', content_type="application/json", data=json.dumps({
            "quantity": 8,
            "id": 1,
            "category":"qw",
            "product_name":"dom",
            "price": 23,
            "description":"it must be"
        }))
        assert response.status_code == 200
        assert response.quantity == 8
    def test_get_products(self, client):
        response = client.get('/api/v1/products/')
        assert response.status_code == 200

    def test_get_product(self, client):
        response = client.get('/api/v1/products/1')
        assert response.status_code == 200

    def test_get_sales(self, client):
        response = client.get('/api/v1/sales/')
        assert response.status_code == 200

    def test_get_sale(self, client):
        response = client.get('api/v1/sales/w')
        assert response.status_code == 404

    def test_create_sales(self, client):
        response = client.post('/api/v1/sales/', content_type="application/json", data=json.dumps({
            'id': 2,
            'attendant_name': 'stanley',
            'customer_name': 'Dominic',
            'product_name': 'suga',
            'quantity': 3,
            'unit_price':3000,
            'total': 9000}))
        assert response.status_code == 200


if __name__ == '__main__':
    pytest.run()


