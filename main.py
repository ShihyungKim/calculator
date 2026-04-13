import streamlit as st
import math

st.set_page_config(page_title="Advanced Calculator", page_icon="🧮")

st.title("🧮 Advanced Calculator")

# 연산 선택
operation = st.selectbox(
    "연산을 선택하세요",
    (
        "덧셈 (+)",
        "뺄셈 (-)",
        "곱셈 (*)",
        "나눗셈 (/)",
        "모듈러 (%)",
        "지수 (x^y)",
        "로그 (log)"
    )
)

# 입력값
num1 = st.number_input("첫 번째 숫자", value=0.0)

# 로그일 때는 입력 다르게 처리
if operation == "로그 (log)":
    base = st.number_input("밑 (base)", value=10.0)
else:
    num2 = st.number_input("두 번째 숫자", value=0.0)

# 계산 버튼
if st.button("계산하기"):

    try:
        if operation == "덧셈 (+)":
            result = num1 + num2

        elif operation == "뺄셈 (-)":
            result = num1 - num2

        elif operation == "곱셈 (*)":
            result = num1 * num2

        elif operation == "나눗셈 (/)":
            if num2 == 0:
                st.error("0으로 나눌 수 없습니다.")
                st.stop()
            result = num1 / num2

        elif operation == "모듈러 (%)":
            result = num1 % num2

        elif operation == "지수 (x^y)":
            result = num1 ** num2

        elif operation == "로그 (log)":
            if num1 <= 0 or base <= 0 or base == 1:
                st.error("올바른 로그 입력값이 아닙니다.")
                st.stop()
            result = math.log(num1, base)

        st.success(f"결과: {result}")

    except Exception as e:
        st.error(f"오류 발생: {e}")
