from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from app.schemas.UrlCreateRequest import UrlCreateRequest
from app.services.write_service import generate_short_url
from app.services.read_service import get_original_url
from app.middlewares import validate_create_request

api_router = APIRouter()
public_router = APIRouter()

@api_router.post("/urls")
def create_url(url: UrlCreateRequest = Depends(validate_create_request)):
    short_url = generate_short_url(url)
    return {"short_url": short_url}

@public_router.get("/{short_code}")
async def redirect_to_long_url(short_code: str):
    original_url = await get_original_url(short_code)
    return RedirectResponse(original_url, status_code=302)
