from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.routers import v1
from app.core.exceptions import BusinessRuleError

from app.handlers.exception_handlers import (
    business_rule_exception_handler,
    validation_exception_handler,
)

app = FastAPI(title="FastAPI Basics Study")

app.add_exception_handler(
    BusinessRuleError,
    business_rule_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.include_router(v1.router)