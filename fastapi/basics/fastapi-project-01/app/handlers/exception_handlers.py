from fastapi import Request
from fastapi.exceptions import RequestValidationError
from app.errors.problems import problem_response
from app.core.exceptions import BusinessRuleError

def business_rule_exception_handler(
    request: Request,
    exc: BusinessRuleError
):
    return problem_response(
        status=400,
        title="Business rule violation",
        detail=exc.detail,
        type_="https://example.com/problems/business-rule",
        instance=str(request.url),
    )


def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return problem_response(
        status=422,
        title="Validation error",
        detail=str(exc.errors()),
        type_="https://example.com/problems/validation-error",
        instance=str(request.url),
    )