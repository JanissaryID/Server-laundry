from sqlalchemy.orm import Session
import database.model.ModelTransaction as model
import database.schema.SchemaTransaction as schema

def get_transaction_by_finish_date(db: Session, finish: bool, date: str):
    transaction = db.query(model.ModelTransaction).filter(model.ModelTransaction.transaction_finish == finish,model.ModelTransaction.transaction_date == date).all()
    return transaction

def get_transaction_by_finish(db: Session, finish: bool):
    transaction = db.query(model.ModelTransaction).filter(model.ModelTransaction.transaction_finish == finish).all()
    return transaction

def get_transactions_by_transactions_date(db: Session, transacrions_date: str):
    return db.query(model.ModelTransaction).filter(model.ModelTransaction.transaction_date == transacrions_date).first()

def get_transaction_filter_three_parameter(db: Session, finish: bool, packet: bool, number: int):
    transaction = db.query(model.ModelTransaction).filter(model.ModelTransaction.transaction_finish == finish, model.ModelTransaction.is_packet == packet, model.ModelTransaction.transaction_number_machine == number).first()
    return transaction

def get_transactions_by_date(db: Session, date: str):
    return db.query(model.ModelTransaction).filter(model.ModelTransaction.transaction_date == date).all()

def get_transaction_by_id(db: Session, sl_id: int):
    return db.query(model.ModelTransaction).filter(model.ModelTransaction.id == sl_id).first()

def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.ModelTransaction).offset(skip).limit(limit).all()

def add_transaction_details_to_db(db: Session, transaction: schema.TransactionAdd):
    transaction_details = model.ModelTransaction(
        transaction_menu_machine = transaction.transaction_menu_machine,
        transaction_type_menu = transaction.transaction_type_menu,
        transaction_type_payment = transaction.transaction_type_payment,
        transaction_class_machine = transaction.transaction_class_machine,
        transaction_number_machine = transaction.transaction_number_machine,
        transaction_date = transaction.transaction_date,
        transaction_price = transaction.transaction_price,
        transaction_finish = transaction.transaction_finish,
        is_packet = transaction.is_packet,
        step_one = transaction.step_one,
        transaction_store = transaction.transaction_store
    )
    db.add(transaction_details)
    db.commit()
    db.refresh(transaction_details)
    return model.ModelTransaction(**transaction.dict())

def update_transaction_details(db: Session, sl_id: int, details: schema.TransactionUpdate):
    db.query(model.ModelTransaction).filter(model.ModelTransaction.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.ModelTransaction).filter(model.ModelTransaction.id == sl_id).first()

def update_status_transaction_details(db: Session, sl_id: int, details: schema.UpdateStatusTransaction):
    db.query(model.ModelTransaction).filter(model.ModelTransaction.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.ModelTransaction).filter(model.ModelTransaction.id == sl_id).first()

def update_stepOne_transaction_details(db: Session, sl_id: int, details: schema.UpdateStepOneTransaction):
    db.query(model.ModelTransaction).filter(model.ModelTransaction.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.ModelTransaction).filter(model.ModelTransaction.id == sl_id).first()

def delete_transaction_details_by_id(db: Session, sl_id: int):
    try:
        db.query(model.ModelTransaction).filter(model.ModelTransaction.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)