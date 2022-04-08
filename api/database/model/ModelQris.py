from sqlalchemy import Column, Integer, String
from database.db_handler import Base

class ModelQris(Base):

    __tablename__ = "qris"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    qris_name = Column(String, nullable=False, default="null")
    qris_value = Column(String, nullable=False, default="null")