class DuplicatedAliasError(Exception):
    """Raised when the custom alias already exists in the system."""
    pass

class NotFoundUrl(Exception):
    """Raised when the short URL code does not exist."""
    pass

class InvalidUrlError(Exception):
    """Raised when the input URL is invalid or empty."""
    pass

class InvalidExpiryDateError(Exception):
    """Raised when the expiry date is in the past."""
    pass
