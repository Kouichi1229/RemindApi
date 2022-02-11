import  streamlit as st
import requests
import json
import datetime

page = st.sidebar.selectbox('選擇頁面',['栽植期','預警報'])



if page == '栽植期':
    st.title("隔壁老洋-栽植期撰寫畫面")
    with  st.form(key='PlantMsg'):
        update_time = st.date_input(
        "更新日期",
        min_value=datetime.date.today())
        
        temMsg: str = st.text_area('溫度注意事項(若沒有可不填)',max_chars=150)
        rainMsg: str = st.text_area('雨量注意事項(若沒有可不填)',max_chars=150)

        data={
        'update_time':datetime.datetime(
            year=update_time.year,
            month=update_time.month,
            day=update_time.day,
            hour=0,
            minute=0).isoformat(),
        'temMsg': temMsg,
        'rainMsg': rainMsg
        }

        submit_btn=st.form_submit_button(label='送出')

    if submit_btn:
        st.write('## 送出資料')
        st.json(data)
        st.write('## 結果')
        url='http://127.0.0.1:8000/Remind/plant'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.json(res.json())
else:
    st.title("隔壁老洋-預警報撰寫畫面")
    with  st.form(key='AlerMsg'):
        update_time = st.date_input(
        "更新日期",
        min_value=datetime.date.today())
        alercontent: str = st.text_area('預警報',max_chars=400)

        data={
        'update_time':datetime.datetime(
            year=update_time.year,
            month=update_time.month,
            day=update_time.day,
            hour=0,
            minute=0).isoformat(),
        'alercontent': alercontent,
        }

        submit_btn=st.form_submit_button(label='送出')

    if submit_btn:
        st.write('## 送出資料')
        st.json(data)
        st.write('## 結果')
        url='http://127.0.0.1:8000/Remind/aler'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.json(res.json())
        
        
       