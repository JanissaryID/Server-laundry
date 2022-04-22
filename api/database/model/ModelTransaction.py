from sqlalchemy import Boolean, Column, Integer, String
from database.db_handler import Base

class ModelTransaction(Base):

    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    transaction_menu_machine = Column(String, nullable=False, default="null")
    transaction_type_menu = Column(String, nullable=False, default="null")
    transaction_type_payment = Column(String, nullable=False, default="null")
    transaction_class_machine = Column(String, nullable=False, default="null")
    transaction_id_machine = Column(Integer, index=True, nullable=False)
    transaction_number_machine = Column(Integer, index=True, nullable=False)
    transaction_date = Column(String, nullable=False, default="1-1-2000")
    transaction_price = Column(String, nullable=False, default="null")
    transaction_finish = Column(Boolean, nullable=False, default=False)
    is_packet = Column(Boolean, nullable=False, default=False)
    step_one = Column(Boolean, nullable=False, default=False)
    transaction_store = Column(Integer, index=True, nullable=False)