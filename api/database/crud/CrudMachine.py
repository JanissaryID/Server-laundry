from sqlalchemy.orm import Session
import database.model.ModelMachine as model
import database.schema.SchemaMachine as schema

def get_machine_by_class_type(db: Session, clases: bool, type: bool):
    machine_type = db.query(model.ModelMachine).filter(model.ModelMachine.machine_type == type,model.ModelMachine.machine_class == clases).all()
    return machine_type

def get_machine_by_number(db: Session, number: int):
    return db.query(model.ModelMachine).filter(model.ModelMachine.machine_number == number).first()

def get_machine_by_id(db: Session, sl_id: int):
    return db.query(model.ModelMachine).filter(model.ModelMachine.id == sl_id).first()

def get_machine(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.ModelMachine).offset(skip).limit(limit).all()

def add_machine_details_to_db(db: Session, machine: schema.MachineAdd):
    machine_details = model.ModelMachine(
        machine_type=machine.machine_type,
        machine_number=machine.machine_number,
        machine_status=machine.machine_status,
        machine_class=machine.machine_class,
        is_packet=machine.is_packet,
        machine_store=machine.machine_store
    )
    db.add(machine_details)
    db.commit()
    db.refresh(machine_details)
    return model.ModelMachine(**machine.dict())

def update_machine_details(db: Session, sl_id: int, details: schema.UpdateMachine):
    db.query(model.ModelMachine).filter(model.ModelMachine.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.ModelMachine).filter(model.ModelMachine.id == sl_id).first()

def update_status_machine_details(db: Session, sl_id: int, details: schema.UpdateStatusMachine):
    db.query(model.ModelMachine).filter(model.ModelMachine.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.ModelMachine).filter(model.ModelMachine.id == sl_id).first()

def delete_machine_details_by_id(db: Session, sl_id: int):
    try:
        db.query(model.ModelMachine).filter(model.ModelMachine.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)