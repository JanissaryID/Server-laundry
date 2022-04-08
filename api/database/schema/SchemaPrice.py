import string
from typing import Optional
from pydantic import BaseModel

# id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
# price_title = Column(String, nullable=False, default="null")
# price_type_menu = Column(Integer, index=True, nullable=False)
# price_class_machine = Column(Boolean, nullable=False, default=False)
# price = Column(String, nullable=False, default="null")
# price_store = Column(Integer, index=True, nullable=False)

class PriceBase(BaseModel):
    price_type_menu: str
    price_class_machine: bool
    price: str
    is_packet: bool
    price_time: int
    price_store: int

class PriceAdd(PriceBase):
    price_title: str

    class Config:
        orm_mode = True

class Price(PriceAdd):
    id: int

    class Config:
        orm_mode = True

class PriceUpdate(BaseModel):
    price_title: str
    price_type_menu: str
    price_class_machine: bool
    price: str
    is_packet: bool
    price_time: int
    price_store: int

    class Config:
        orm_mode = True