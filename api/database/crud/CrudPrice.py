from sqlalchemy.orm import Session
import database.model.ModelPrice as model
import database.schema.SchemaPrice as schema

def get_price_by_title(db: Session, title: str):
    return db.query(model.ModelPrice).filter(model.ModelPrice.price_title == title).first()

def get_price_by_id(db: Session, sl_id: int):
    return db.query(model.ModelPrice).filter(model.ModelPrice.id == sl_id).first()

def get_price(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.ModelPrice).offset(skip).limit(limit).all()

def add_price_details_to_db(db: Session, price: schema.PriceAdd):
    price_details = model.ModelPrice(
        price_title=price.price_title,
        price_type_menu=price.price_type_menu,
        price_class_machine=price.price_class_machine,
        price_time=price.price_time,
        price=price.price,
        is_packet=price.is_packet,
        price_store=price.price_store
    )
    db.add(price_details)
    db.commit()
    db.refresh(price_details)
    return model.ModelPrice(**price.dict())

def update_price_details(db: Session, sl_id: int, details: schema.PriceUpdate):
    db.query(model.ModelPrice).filter(model.ModelPrice.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.ModelPrice).filter(model.ModelPrice.id == sl_id).first()

def delete_price_details_by_id(db: Session, sl_id: int):
    try:
        db.query(model.ModelPrice).filter(model.ModelPrice.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)