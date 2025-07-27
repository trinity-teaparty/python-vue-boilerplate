# proxy/vue_proxy_middleware.py

import httpx
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response, PlainTextResponse

VUE_DEV_SERVER = "http://localhost:3000"

class VueProxyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, upstream: str):
        super().__init__(app)
        self.upstream = upstream.rstrip('/')

    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/api") or request.url.path.startswith("/docs"):
            return await call_next(request)

        vue_url = f"{self.upstream}{request.url.path}"
        if request.url.query:
            vue_url += f"?{request.url.query}"

        try:
            async with httpx.AsyncClient() as client:
                proxied_response = await client.request(
                    method=request.method,
                    url=vue_url,
                    headers=request.headers.raw,
                    content=await request.body()
                )
        except httpx.RequestError as e:
            return Response(content=f"Vue dev server proxy failed: {e}", status_code=502)

        return Response(
            content=proxied_response.content,
            status_code=proxied_response.status_code,
            headers=dict(proxied_response.headers),
        )