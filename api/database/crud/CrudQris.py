from sqlalchemy.orm import Session
import database.model.ModelQris as model
import database.schema.SchemaQris as schema

def get_qris_by_name(db: Session, name: str):
    return db.query(model.ModelQris).filter(model.ModelQris.qris_name == name).first()

def get_qris_by_id(db: Session, sl_id: int):
    return db.query(model.ModelQris).filter(model.ModelQris.id == sl_id).first()

def get_qris(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.ModelQris).offset(skip).limit(limit).all()

def add_qris_details_to_db(db: Session, qris: schema.QrisAdd):
    qris_details = model.ModelQris(
        qris_name=qris.qris_name,
        qris_value=qris.qris_value
    )
    db.add(qris_details)
    db.commit()
    db.refresh(qris_details)
    return model.ModelQris(**qris.dict())

def update_qris_details(db: Session, sl_id: int, details: schema.QrisUpdate):
    db.query(model.ModelQris).filter(model.ModelQris.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.ModelQris).filter(model.ModelQris.id == sl_id).first()

def delete_qris_details_by_id(db: Session, sl_id: int):
    try:
        db.query(model.ModelQris).filter(model.ModelQris.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)