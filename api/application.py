from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import database.crud.CrudMachine as CrudMachine
import database.model.ModelMachine as ModelMachine
import database.schema.SchemaMachine as SchemaMachine

import database.crud.CrudStore as CrudStore
import database.model.ModelStore as ModelStore
import database.schema.SchemaStore as SchemaStore

import database.crud.CrudPrice as CrudPrice
import database.model.ModelPrice as ModelPrice
import database.schema.SchemaPrice as SchemaPrice

import database.crud.CrudTransaction as CrudTransaction
import database.model.ModelTransaction as ModelTransaction
import database.schema.SchemaTransaction as SchemaTransaction

import database.crud.CrudQris as CrudQris
import database.model.ModelQris as ModelQris
import database.schema.SchemaQris as SchemaQris

from database.db_handler import SessionLocal, engine

ModelMachine.Base.metadata.create_all(bind=engine)
ModelStore.Base.metadata.create_all(bind=engine)
ModelPrice.Base.metadata.create_all(bind=engine)
ModelTransaction.Base.metadata.create_all(bind=engine)
ModelQris.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Laundry Api",
    description="You can perform CRUD operation by using this API",
    version="2.0.0"
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/fetch-machine', response_model=List[SchemaMachine.Machine])
def retrieve_all_machine_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    machine = CrudMachine.get_machine(db=db, skip=skip, limit=limit)
    return machine

@app.get('/filter-machine', response_model=List[SchemaMachine.Machine])
def retrieve_filter_machine_details(classes: bool, type: bool, db: Session = Depends(get_db)):
    machine = CrudMachine.get_machine_by_class_type(db=db, clases=classes, type=type)
    if not machine:
        raise HTTPException(status_code=404, detail=f"No record found to show")

    try:
        showfilter = CrudMachine.get_machine_by_class_type(db=db, clases=classes, type=type)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to get Transaction: {e}")
    return showfilter

@app.post('/add-machine', response_model=SchemaMachine.MachineAdd)
def add_new_machine(machine: SchemaMachine.MachineAdd, db: Session = Depends(get_db)):
    return CrudMachine.add_machine_details_to_db(db=db, machine=machine)

@app.delete('/delete-machine')
def delete_machine_by_id(id: int, db: Session = Depends(get_db)):
    details = CrudMachine.get_machine_by_id(db=db, sl_id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        CrudMachine.delete_machine_details_by_id(db=db, sl_id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}

@app.put('/update-status-machine', response_model=SchemaMachine.Machine)
def update_status_machine_details(id: int, update_param: SchemaMachine.UpdateStatusMachine, db: Session = Depends(get_db)):
    details = CrudMachine.get_machine_by_id(db=db, sl_id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return CrudMachine.update_status_machine_details(db=db, details=update_param, sl_id=id)

@app.put('/update-machine', response_model=SchemaMachine.Machine)
def update_machine_details(id: int, update_param: SchemaMachine.UpdateMachine, db: Session = Depends(get_db)):
    details = CrudMachine.get_machine_by_id(db=db, sl_id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return CrudMachine.update_machine_details(db=db, details=update_param, sl_id=id)


################################    STORE    ################################

@app.get('/fetch-store', response_model=List[SchemaStore.Store])
def retrieve_all_store_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    store = CrudStore.get_store(db=db, skip=skip, limit=limit)
    return store

@app.post('/add-store', response_model=SchemaStore.StoreAdd)
def add_new_store(store: SchemaStore.StoreAdd, db: Session = Depends(get_db)):
    return CrudStore.add_store_details_to_db(db=db, store=store)

@app.delete('/delete-store')
def delete_store_by_id(id: int, db: Session = Depends(get_db)):
    details = CrudStore.get_store_by_id(db=db, sl_id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        CrudStore.delete_store_details_by_id(db=db, sl_id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}

@app.put('/update-store', response_model=SchemaStore.Store)
def update_store_details(id: int, update_param: SchemaStore.StoreUpdate, db: Session = Depends(get_db)):
    details = CrudStore.get_store_by_id(db=db, sl_id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return CrudStore.update_store_details(db=db, details=update_param, sl_id=id)


################################    PRICE    ################################

@app.get('/fetch-price', response_model=List[SchemaPrice.Price])
def retrieve_all_price_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    price = CrudPrice.get_price(db=db, skip=skip, limit=limit)
    return price

@app.post('/add-price', response_model=SchemaPrice.PriceAdd)
def add_new_price(price: SchemaPrice.PriceAdd, db: Session = Depends(get_db)):
    return CrudPrice.add_price_details_to_db(db=db, price=price)

@app.delete('/delete-price')
def delete_price_by_id(id: int, db: Session = Depends(get_db)):
    details = CrudPrice.get_price_by_id(db=db, sl_id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        CrudPrice.delete_price_details_by_id(db=db, sl_id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}

@app.put('/update-price', response_model=SchemaPrice.Price)
def update_price_details(id: int, update_param: SchemaPrice.PriceUpdate, db: Session = Depends(get_db)):
    details = CrudPrice.get_price_by_id(db=db, sl_id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return CrudPrice.update_price_details(db=db, details=update_param, sl_id=id)

################################    TRANSACTION    ################################

@app.get('/fetch-transactions', response_model=List[SchemaTransaction.Transaction])
def retrieve_all_transactions_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transaction = CrudTransaction.get_transactions(db=db, skip=skip, limit=limit)
    return transaction

@app.get('/fetch-transactions-filter-finish-date', response_model=List[SchemaTransaction.Transaction])
def get_transaction_by_finish_date(finish: bool ,date: str, db: Session = Depends(get_db)):
    details = CrudTransaction.get_transaction_by_finish_date(db=db, date=date, finish=finish)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to show")

    try:
        showfilter = CrudTransaction.get_transaction_by_finish_date(db=db, date=date, finish=finish)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to get Transaction: {e}")
    return showfilter

@app.get('/fetch-transactions-filter-finish', response_model=List[SchemaTransaction.Transaction])
def get_transaction_by_finish(finish: bool, db: Session = Depends(get_db)):
    details = CrudTransaction.get_transaction_by_finish(db=db, finish=finish)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to show")

    try:
        showfilter = CrudTransaction.get_transaction_by_finish(db=db, finish=finish)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to get Transaction: {e}")
    return showfilter

@app.get('/fetch-transactions-filter-machine', response_model=List[SchemaTransaction.Transaction])
def get_transaction_filter_machine(finish: bool, packet: bool, number: int, db: Session = Depends(get_db)):
    details = CrudTransaction.get_transaction_filter_three_parameter(db=db, packet=packet, finish=finish, number=number)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to show")

    try:
        showfilter = CrudTransaction.get_transaction_filter_three_parameter(db=db, packet=packet, finish=finish, number=number)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to get Transaction: {e}")
    return showfilter

@app.get('/fetch-transactions-filter-date', response_model=List[SchemaTransaction.Transaction])
def get_transaction_by_date(date: str, db: Session = Depends(get_db)):
    details = CrudTransaction.get_transactions_by_date(db=db, date=date)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to show")

    try:
        showfilter = CrudTransaction.get_transactions_by_date(db=db, date=date)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to get Transaction: {e}")
    return showfilter

@app.post('/add-transaction', response_model=SchemaTransaction.TransactionAdd)
def add_new_transaction(transaction: SchemaTransaction.TransactionAdd, db: Session = Depends(get_db)):
    return CrudTransaction.add_transaction_details_to_db(db=db, transaction=transaction)

@app.delete('/delete-transaction')
def delete_transaction_by_id(id: int, db: Session = Depends(get_db)):
    details = CrudTransaction.get_transaction_by_id(db=db, sl_id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        CrudTransaction.delete_transaction_details_by_id(db=db, sl_id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}

@app.put('/update-transaction', response_model=SchemaTransaction.UpdateStepOneTransaction)
def update_transaction_details(id: int, update_param: SchemaTransaction.UpdateStepOneTransaction, db: Session = Depends(get_db)):
    details = CrudTransaction.get_transaction_by_id(db=db, sl_id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return CrudTransaction.update_stepOne_transaction_details(db=db, details=update_param, sl_id=id)

@app.put('/update-status-transaction', response_model=SchemaTransaction.Transaction)
def update_status_transaction_details(id: int, update_param: SchemaTransaction.UpdateStatusTransaction, db: Session = Depends(get_db)):
    details = CrudTransaction.get_transaction_by_id(db=db, sl_id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return CrudTransaction.update_status_transaction_details(db=db, details=update_param, sl_id=id)


################################    QRIS    ################################

@app.get('/fetch-qris', response_model=List[SchemaQris.Qris])
def retrieve_all_qris_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    qris = CrudQris.get_qris(db=db, skip=skip, limit=limit)
    return qris

@app.post('/add-qris', response_model=SchemaQris.QrisAdd)
def add_new_qris(qris: SchemaQris.QrisAdd, db: Session = Depends(get_db)):
    return CrudQris.add_qris_details_to_db(db=db, qris=qris)

@app.delete('/delete-qris')
def delete_qris_by_id(id: int, db: Session = Depends(get_db)):
    details = CrudQris.get_qris_by_id(db=db, sl_id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        CrudQris.delete_qris_details_by_id(db=db, sl_id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}

@app.put('/update-qris', response_model=SchemaQris.Qris)
def update_qris_details(id: int, update_param: SchemaQris.QrisUpdate, db: Session = Depends(get_db)):
    details = CrudQris.get_qris_by_id(db=db, sl_id=id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return CrudQris.update_qris_details(db=db, details=update_param, sl_id=id)