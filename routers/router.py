from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
async def root() -> JSONResponse:
    """
    Root endpoint
    """
    return JSONResponse(content={"message": "Hello World"})


@router.get("/hello/{name}")
async def say_hello(name: str) -> JSONResponse:
    """
    Say hello to someone
    """
    return JSONResponse(content={"message": f"Hello {name}"})
