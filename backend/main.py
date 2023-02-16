import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
Json = "../brave-monitor-378007-e689e7e512c4.json"
Url = ["https://spreadsheets.google.com/feeds"]
Connect = SAC.from_json_keyfile_name(Json, Url)
GoogleSheets = gspread.authorize(Connect)
Sheet = GoogleSheets.open_by_key("1m1tKd59BYHmYMJOY4e7W5lFShxvtzzpi-Y1sfrrzw3U")
Sheets = Sheet.sheet1
# dataTitle = ["date", "time", "events", "place"]
datas = ["03/12", "16:00", "lunch", "taoyuan"]
# 先塞一筆假資料
# Sheets.append_row(dataTitle)
Sheets.append_row(datas)
# print("寫入成功")
# print(Sheets.get_all_values())
# ----- fast api -----
app = FastAPI()
@app.get("/")
def getAllData():
    return Sheets.get_all_values() #get_all_records() 會出錯
# class Info(BaseModel):
#     id: int
#     data: list
# @app.post("/addNewEvents")
# def getInformation(info: Info):
#     Sheets.append_row(info.data)
#     return {"status": "SUCCESS", "data": info}