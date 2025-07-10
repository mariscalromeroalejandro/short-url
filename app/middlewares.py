from starlette.status import HTTP_400_BAD_REQUEST
from app.schemas.UrlCreateRequest import UrlCreateRequest
from app.exceptions import InvalidUrlError


def validate_long_url(url: UrlCreateRequest) -> UrlCreateRequest:
    if not (url.long_url.startswith("http://") or url.long_url.startswith("https://")):
        raise InvalidUrlError("Invalid URL. Must start with http:// or https://")
    return url
