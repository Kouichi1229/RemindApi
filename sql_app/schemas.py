from datetime import datetime
from typing import Optional
from pydantic import BaseModel,Field

class PlantCreat(BaseModel):
    update_time : datetime
    temMsg: Optional[str] = None
    rainMsg: Optional[str] = None
    # temMsg : str = Field(max_length=500) 
    # rainMsg : str = Field(max_length=500) 

    class config:
        orm_mode =True

class Plant(PlantCreat):
    plant_id : int

    class config:
        orm_mode =True


class AlerCreat(BaseModel):
    update_time : datetime
    alercontent : str =Field(max_length=500) 

    class config:
        orm_mode =True


class Aler(AlerCreat):
    aler_id : int

    class config:
        orm_mode =True

# plant_db : List[PlantMsg] =[
#     PlantMsg(
#         update_time='2022-01-26T13:00:00+00:00',
#         temMsg='在生長期間溫度 較去年同期小幅度上升1~2°C，但整個生長期間的每月溫度均溫還在洋蔥耐熱範圍(15~26°C)。',
#         rainMsg='在生長期間雨量，整個生長期間的每月平均降雨量在洋蔥雨量接受範圍(10mm以下)，雨量正常，期間內適宜栽種洋蔥。')
# ]

# AlerMsg_db : List[AlerMsg] =[
#     AlerMsg(
#         update_time='2022-01-26T13:00:00+00:00',
#         alercontent ='颱風圓規昨晚(10日)在鵝鑾鼻東南方海面，暴風圈正擴大，中央氣象局昨晚發布海上颱風警報，雖不會登陸台灣，外圍環流將影響台灣9縣市有豪雨發生，恆春半島預估會下100至200毫米的雨量，目前正值洋蔥株苗栽種時間，利用巧固架育苗的農民可以盡快搬往集貨場。苗齡已達40~45天以上之苗圃採後苗株整理成束，以報紙包覆直立放置塑膠籃中以5℃冰存，等待適合的天候再行種植，避免苗株受損。',
#         )
# ]