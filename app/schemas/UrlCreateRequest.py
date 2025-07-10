from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from datetime import datetime

class UrlCreateRequest(BaseModel):
    long_url: HttpUrl = Field(..., example="https://www.google.com")
    custom_alias: Optional[str] = Field(None, example="my-custom-alias")
    exp_date: Optional[datetime] = None
