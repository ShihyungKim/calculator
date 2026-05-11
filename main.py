import streamlit as st
import math

st.set_page_config(page_title="Button Calculator", page_icon="🧮")

st.title("🧮 진짜 계산기처럼 누르는 계산기")

# 화면에 표시될 식 저장
if "expression" not in st.session_state:
    st.session_state.expression = ""

def press(value):
    st.session_state.expression += str(value)

def clear():
    st.session_state.expression = ""

def calculate():
    try:
        expr = st.session_state.expression

        expr = expr.replace("×", "*")
        expr = expr.replace("÷", "/")
        expr = expr.replace("^", "**")

        result = eval(expr)
        st.session_state.expression = str(result)

    except ZeroDivisionError:
        st.session_state.expression = "0으로 나눌 수 없습니다"

    except:
        st.session_state.expression = "오류"

# 계산기 화면
st.text_input(
    "계산식",
    value=st.session_state.expression,
    disabled=True
)

# 버튼 배치
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7"):
        press("7")
    if st.button("4"):
        press("4")
    if st.button("1"):
        press("1")
    if st.button("0"):
        press("0")

with col2:
    if st.button("8"):
        press("8")
    if st.button("5"):
        press("5")
    if st.button("2"):
        press("2")
    if st.button("."):
        press(".")

with col3:
    if st.button("9"):
        press("9")
    if st.button("6"):
        press("6")
    if st.button("3"):
        press("3")
    if st.button("="):
        calculate()

with col4:
    if st.button("÷"):
        press("÷")
    if st.button("×"):
        press("×")
    if st.button("-"):
        press("-")
    if st.button("+"):
        press("+")

st.write("")

col5, col6, col7, col8 = st.columns(4)

with col5:
    if st.button("C"):
        clear()

with col6:
    if st.button("^"):
        press("^")

with col7:
    if st.button("("):
        press("(")

with col8:
    if st.button(")"):
        press(")")
