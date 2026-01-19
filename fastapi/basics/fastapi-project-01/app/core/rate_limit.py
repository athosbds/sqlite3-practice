import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.errors.problem import problem_response

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, limit: int, window: int):
        super().__init__(app)
        self.limit = limit
        self.window = window
        self.requests = {}

    async def dispatch(self, request: Request, call_next):
        ip = request.client.host
        now = time.time()

        history = self.requests.get(ip, [])
        history = [t for t in history if now - t < self.window]

        if len(history) >= self.limit:
            return problem_response(
                429,
                "Too Many Requests",
                "Rate limit exceeded",
                "https://example.com/errors/rate-limit",
                str(request.url),
            )

        history.append(now)
        self.requests[ip] = history
        return await call_next(request)
