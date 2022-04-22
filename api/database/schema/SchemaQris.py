from pydantic import BaseModel

class QrisBase(BaseModel):
    qris_value: str

class QrisAdd(QrisBase):
    qris_name: str

    class Config:
        orm_mode = True

class Qris(QrisAdd):
    id: int

    class Config:
        orm_mode = True

class QrisUpdate(BaseModel):
    qris_name: str
    qris_value: str

    class Config:
        orm_mode = True