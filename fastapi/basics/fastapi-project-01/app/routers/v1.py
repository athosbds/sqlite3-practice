from fastapi import APIRouter, Request
from app.schemas.product import ProductCreate, ProductResponse
from app.repositories.product_repo import ProductRepository
from app.errors.problem import problem_response

router = APIRouter(prefix="/api/v1/products", tags=["products-v1"])
repo = ProductRepository()

@router.post("", response_model=ProductResponse)
def create_product(payload: ProductCreate):
    return repo.create(payload.name, payload.price)

@router.get("", response_model=list[ProductResponse])
def list_products():
    return repo.list()

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, request: Request):
    product = repo.get(product_id)
    if not product:
        return problem_response(
            404,
            "Resource not found",
            f"Product {product_id} does not exist",
            "https://example.com/errors/not-found",
            str(request.url),
        )
    return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, payload: ProductCreate, request: Request):
    product = repo.update(product_id, payload.name, payload.price)
    if not product:
        return problem_response(404, "Resource not found", "Product not found",
            "https://example.com/errors/not-found", str(request.url))
    return product

@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, request: Request):
    deleted = repo.delete(product_id)
    if not deleted:
        return problem_response(404, "Resource not found", "Product not found",
            "https://example.com/errors/not-found", str(request.url))
