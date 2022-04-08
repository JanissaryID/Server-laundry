import string
from typing import Optional
from pydantic import BaseModel

class TransactionBase(BaseModel):
    transaction_type_menu:      str
    transaction_menu_machine:   str
    transaction_type_payment:   str
    transaction_class_machine:  str
    transaction_date:           str
    transaction_price:          str
    transaction_finish:         bool
    is_packet:                  bool
    step_one:                   bool
    transaction_store:          int

class TransactionAdd(TransactionBase):
    transaction_number_machine: int

    class Config:
        orm_mode = True

class Transaction(TransactionAdd):
    id: int

    class Config:
        orm_mode = True

class TransactionUpdate(BaseModel):
    transaction_number_machine: int
    transaction_type_menu:      str
    transaction_menu_machine:   str
    transaction_type_payment:   str
    transaction_class_machine:  str
    transaction_date:           str
    transaction_price:          str
    transaction_finish:         bool
    is_packet:                  bool
    step_one:                   bool
    transaction_store:          int

    class Config:
        orm_mode = True

class UpdateStatusTransaction(BaseModel):
    transaction_finish:         bool

    class Config:
        orm_mode = True