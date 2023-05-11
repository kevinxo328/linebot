import os

import config
from fastapi import FastAPI
import uvicorn

from routers.line import line_app
from routers.router import router

app = FastAPI()

app.include_router(
    router=router,
    prefix="/api/v1",
)

app.include_router(router=line_app, prefix="/api/v1/line", tags=["line"])

if __name__ == "__main__":
    # Local WSGI: Uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=port,
        workers=4,
        log_level="info",
        access_log=True,
        use_colors=True,
        reload=True,
    )
