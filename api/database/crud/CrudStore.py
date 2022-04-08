from sqlalchemy.orm import Session
import database.model.ModelStore as model
import database.schema.SchemaStore as schema

def get_store_by_name(db: Session, name: str):
    return db.query(model.ModelStore).filter(model.ModelStore.store_name == name).first()

def get_store_by_id(db: Session, sl_id: int):
    return db.query(model.ModelStore).filter(model.ModelStore.id == sl_id).first()

def get_store(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.ModelStore).offset(skip).limit(limit).all()

def add_store_details_to_db(db: Session, store: schema.StoreAdd):
    store_details = model.ModelStore(
        store_name=store.store_name,
        store_address=store.store_address
    )
    db.add(store_details)
    db.commit()
    db.refresh(store_details)
    return model.ModelStore(**store.dict())

def update_store_details(db: Session, sl_id: int, details: schema.StoreUpdate):
    db.query(model.ModelStore).filter(model.ModelStore.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.ModelStore).filter(model.ModelStore.id == sl_id).first()

def delete_store_details_by_id(db: Session, sl_id: int):
    try:
        db.query(model.ModelStore).filter(model.ModelStore.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)