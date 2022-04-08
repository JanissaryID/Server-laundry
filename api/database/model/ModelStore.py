from sqlalchemy import Column, Integer, String
from database.db_handler import Base

class ModelStore(Base):

    __tablename__ = "store"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    store_name = Column(String, nullable=False, default="null")
    store_address = Column(String, nullable=False, default="null")