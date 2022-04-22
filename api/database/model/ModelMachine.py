from sqlalchemy import Boolean, Column, Integer
from database.db_handler import Base

class ModelMachine(Base):

    __tablename__ = "machine"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False, unique=True)
    machine_type = Column(Boolean, nullable=False, default=False)
    machine_number = Column(Integer, index=True, nullable=False)
    machine_status = Column(Boolean, nullable=False, default=False)
    machine_class = Column(Boolean, nullable=False, default=False)
    is_packet = Column(Boolean, nullable=False, default=False)
    machine_store = Column(Integer, index=True, nullable=False)