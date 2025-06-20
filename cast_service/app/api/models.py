﻿#~/python-microservices/cast-service/app/api/models.py

from pydantic import BaseModel # type: ignore
from typing import List, Optional

class CastIn(BaseModel):
    name: str
    nationality: Optional[str] = None


class CastOut(CastIn):
    id: int


class CastUpdate(CastIn):
    name: Optional[str] = None