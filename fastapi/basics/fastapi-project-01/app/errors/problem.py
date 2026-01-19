from fastapi import Request
from fastapi.responses import JSONResponse

def problem_response(
    status: int,
    title: str,
    detail: str,
    type_: str,
    instance: str
):
    return JSONResponse(
        status_code=status,
        content={
            "type": type_,
            "title": title,
            "status": status,
            "detail": detail,
            "instance": instance,
        },
    )
