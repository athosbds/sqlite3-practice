from typing import Dict
from app.models.product import Product

class ProductRepository:
    def __init__(self):
        self._db: Dict[int, Product] = {}
        self._id = 1

    def create(self, name: str, price: float) -> Product:
        product = Product(self._id, name, price)
        self._db[self._id] = product
        self._id += 1
        return product

    def list(self):
        return list(self._db.values())

    def get(self, product_id: int):
        return self._db.get(product_id)

    def update(self, product_id: int, name: str, price: float):
        if product_id not in self._db:
            return None
        product = Product(product_id, name, price)
        self._db[product_id] = product
        return product

    def delete(self, product_id: int):
        return self._db.pop(product_id, None)
