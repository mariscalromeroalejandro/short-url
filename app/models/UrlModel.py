from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Url(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    short_code: str
    long_url: str
    exp_date: Optional[datetime] = None
    created_at: datetime
