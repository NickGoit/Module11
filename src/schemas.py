from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class ContactModel(BaseModel):
    name: str = Field(max_length=25)


class ContactResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True

