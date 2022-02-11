from sqlalchemy import Column,Integer, String,DateTime
#from sqlalchemy.orm import relationship

from .database import Base


class PlantMsg(Base):
    __tablename__ = "plantMsg"
    
    id = Column(Integer,primary_key=True, index=True,  nullable= False)
    update_time = Column(DateTime,  nullable= False)
    temMsg = Column(String)
    rainMsg = Column(String)

class AlerMsg(Base):
    __tablename__ = "alerMsg"

    id = Column(Integer,primary_key=True, index=True,  nullable= False)
    update_time = Column(DateTime, nullable= False)
    alercontent = Column(String)

    