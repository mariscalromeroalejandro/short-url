from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions import DuplicatedAliasError, NotFoundUrl, InvalidUrlError, InvalidExpiryDateError

def add_exception_handlers(app):
    @app.exception_handler(DuplicatedAliasError)
    async def duplicated_alias_exception_handler(request: Request, exc: DuplicatedAliasError):
        return JSONResponse(status_code=409, content={"detail": "Alias already exists."})

    @app.exception_handler(NotFoundUrl)
    async def not_found_url_exception_handler(request: Request, exc: NotFoundUrl):
        return JSONResponse(status_code=404, content={"detail": "Short URL not found."})

    @app.exception_handler(InvalidUrlError)
    async def invalid_url_exception_handler(request: Request, exc: InvalidUrlError):
        return JSONResponse(status_code=400, content={"detail": "Invalid long URL provided."})

    @app.exception_handler(InvalidExpiryDateError)
    async def invalid_expiry_date_exception_handler(request: Request, exc: InvalidExpiryDateError):
        return JSONResponse(status_code=400, content={"detail": "Invalid expiry date provided."})


