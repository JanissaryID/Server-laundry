from pydantic import BaseModel

class StoreBase(BaseModel):
    store_address: str

class StoreAdd(StoreBase):
    store_name: str

    class Config:
        orm_mode = True

class Store(StoreAdd):
    id: int

    class Config:
        orm_mode = True

class StoreUpdate(BaseModel):
    store_name: str
    store_address: str

    class Config:
        orm_mode = True