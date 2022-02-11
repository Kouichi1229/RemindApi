from typing import List
from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app =FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#read
@app.get('/Remind/plant', response_model= List[schemas.Plant])
async def Get_PlantMsg(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    plantMsg = crud.getPlantMsg(db,skip=skip,limit=limit)
    return plantMsg

@app.get('/Remind/aler', response_model= List[schemas.Aler])
async  def Get_AlerMsg(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    alerMsg = crud.getAlerMsg(db,skip=skip,limit=limit)
    return alerMsg

#create
@app.post('/Remind/plant',response_model=schemas.Plant)
async  def PlantMsg(plantMsg: schemas.Plant, db: Session = Depends(get_db)):
    return crud.create_PlantMsg(db=db, plantMsg=plantMsg)


@app.post('/Remind/aler',response_model=schemas.Aler)
async  def AlerMsg(alerMsg: schemas.Aler , db: Session = Depends(get_db)):
    return crud.create_AlerMsg(db=db, alerMsg=alerMsg)
