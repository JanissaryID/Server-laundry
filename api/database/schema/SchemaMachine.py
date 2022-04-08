import string
from typing import Optional
from pydantic import BaseModel

class MachineBase(BaseModel):
    machine_type: bool
    machine_status: bool
    machine_class: bool
    machine_store: int

class MachineAdd(MachineBase):
    machine_number: int

    class Config:
        orm_mode = True

class Machine(MachineAdd):
    id: int

    class Config:
        orm_mode = True

class UpdateMachine(BaseModel):
    machine_number: int
    machine_type: bool
    machine_status: bool
    machine_class: bool
    machine_store: int

    class Config:
        orm_mode = True

class UpdateStatusMachine(BaseModel):
    machine_status: bool

    class Config:
        orm_mode = True