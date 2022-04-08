from sqlalchemy import Boolean, Column, Integer, String
from database.db_handler import Base

class ModelPrice(Base):

    __tablename__ = "price"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    price_title = Column(String, nullable=False, default="null")
    price_type_menu = Column(String, nullable=False, default="null")
    price_class_machine = Column(Boolean, nullable=False, default=False)
    price_time = Column(Integer, index=True, nullable=False)
    is_packet = Column(Boolean, nullable=False, default=False)
    price = Column(String, nullable=False, default="null")
    price_store = Column(Integer, index=True, nullable=False)