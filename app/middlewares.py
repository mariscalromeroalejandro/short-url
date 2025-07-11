from starlette.status import HTTP_400_BAD_REQUEST
from app.schemas.UrlCreateRequest import UrlCreateRequest
from app.exceptions import InvalidUrlError, InvalidExpiryDateError
from datetime import datetime, timedelta, timezone





def validate_long_url(url: UrlCreateRequest) -> UrlCreateRequest:
    if not (url.long_url.startswith("http://") or url.long_url.startswith("https://")):
        raise InvalidUrlError("Invalid URL. Must start with http:// or https://")

def validate_expiry_date(url: UrlCreateRequest) -> str:
    if url.exp_date:
        now = datetime.now(timezone.utc)
        exp_date = url.exp_date
        if exp_date.tzinfo is None:
            exp_date = exp_date.replace(tzinfo=timezone.utc)
        max_expiry = now + timedelta(days=365)
        if exp_date < now:
            raise InvalidExpiryDateError("Expiry date must be in the future")
        if exp_date > max_expiry:
            raise InvalidExpiryDateError("Expiry date must be within 365 days from now")



def validate_create_request(url: UrlCreateRequest) -> UrlCreateRequest:
    validate_long_url(url)
    validate_expiry_date(url)
    return url