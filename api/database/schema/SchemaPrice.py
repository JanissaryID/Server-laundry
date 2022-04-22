from pydantic import BaseModel

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