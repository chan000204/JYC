import streamlit as st
import random


st.write("안녕하세요")

st.html('<h1>파이썬의 세계에 오신 것을 환영합니다.</h1>')


'# 파이썬의 *세계에* 오신 것을 환영합니다.'

# # 숫자 맞추기 게임

# st.title("숫자 맞추기 게임")
# secret = st.session_state.get('secret', random.randint(1, 100))

# if 'secret' not in st.session_state:
#     st.session_state.secret = secret

# guess = st.number_input("1부터 100 사이의 숫자를 입력하세요.", min_value=1, max_value=100, step=1)

# if st.button("확인"):
#     if guess < st.session_state.secret:
#         st.warning("너무 작아요.")
#     elif guess > st.session_state.secret:
#         st.warning("너무 커요!")
#     else:
#         st.success("정답입니다.")
#         st.balloons()
#         st.session_state.secret = random.randint(1,100)

# html_code = """
# <h2 style='color:blue;'>안녕하세요!</h2>
# <p>이것은 <b>streamlit</b>에사 HTML로 출력한 문장입니다.</P>
# """

# st.markdown(html_code, unsafe_allow_html=True)


# html_code = """
# <a href='https://www.naver.com' target='_blank'>
#     <button style='background-color:green; color:white; padding:10px; border:none; border-radius:5px;'>
#         네이버로 이동
#     </button>
# </a>
# """

# st.markdown(html_code, unsafe_allow_html=True)

# 실시간 주가 확인 앱

import yfinance as yf
import datetime

st.title("실시간 주가 확인기")

ticker = st.text_input("종목 티커를 입력하세요(예: AAPL, MSFT)", value="AAPL")
start_date = st.date_input("시작일", datetime.date(2023, 1, 1))
end_date = st.date_input("종료일", datetime.date.today())

if st.button("조회"):
    data = yf.download(ticker, start=start_date, end=end_date)
    st.line_chart(data['Close'])
    
