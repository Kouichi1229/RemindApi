from . import models, schemas
from sqlalchemy.orm import Session

def getPlantMsg(db:Session, skip:int=0,limit:int =100):
    return db.query(models.PlantMsg).offset(skip).limit(limit).all()

def getAlerMsg(db:Session, skip:int=0,limit:int =100):
    return db.query(models.AlerMsg).offset(skip).limit(limit).all()

def create_PlantMsg(db:Session,plantMsg: schemas.Plant):
    db_plantMsg = models.PlantMsg(update_time = plantMsg.update_time,
                                  temMsg = plantMsg.temMsg,
                                  rainMsg = plantMsg.rainMsg)
    db.add(db_plantMsg)
    db.commit()
    db.refresh(db_plantMsg)

    return db_plantMsg


def create_AlerMsg(db:Session,alerMsg: schemas.Aler):
    db_alerMsg = models.AlerMsg(update_time = alerMsg.update_time,
                                  alercontent = alerMsg.alercontent)
    db.add(db_alerMsg)
    db.commit()
    db.refresh(db_alerMsg)
    
    return db_alerMsg