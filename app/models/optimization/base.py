from abc import ABC
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.models.enums.status import Status


class OptimizationBase(ABC, BaseModel):
    optimization_id: Optional[UUID] = None
    status: Optional[Status] = None
