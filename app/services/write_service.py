# app/services/write_service.py

import base62
from app.core.redis_counter import redis_counter
from datetime import datetime
from sqlmodel import Session, select
from app.db import engine
from app.models.UrlModel import Url
from app.schemas.UrlCreateRequest import UrlCreateRequest
from app.exceptions import DuplicatedAliasError
from typing import Optional
import os


BASE_URL = os.getenv('BASE_URL')


def get_url_by_short_code(session: Session, short_code: str) -> Optional[Url]:
    statement = select(Url).where(Url.short_code == short_code)
    return session.exec(statement).first()


def generate_short_url(data: UrlCreateRequest) -> str:
    with Session(engine) as session:
        # Check if alias exists
        if data.custom_alias:
            existing = get_url_by_short_code(session, data.custom_alias)
            if existing:
                raise DuplicatedAliasError("Alias already exists")
            code = data.custom_alias
        else:
            unique_id = redis_counter.incr("url_counter")
            code = base62.encode(unique_id)

        url = Url(
            short_code=code,
            long_url=data.long_url,
            exp_date=data.exp_date,
            created_at=datetime.now()
        )
        session.add(url)
        session.commit()

    return f"{BASE_URL}{code}"
