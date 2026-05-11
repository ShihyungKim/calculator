import streamlit as st
import math

st.set_page_config(page_title="Advanced Calculator", page_icon="🧮")

# 계산기 그림
calculator_svg = """
<div style="text-align:center;">
<svg width="180" height="180" viewBox="0 0 200 200">
  <rect x="45" y="20" width="110" height="160" rx="18" fill="#4B5563"/>
  <rect x="60" y="38" width="80" height="35" rx="6" fill="#E5E7EB"/>
  <text x="100" y="62" text-anchor="middle" font-size="20" fill="#111827">123</text>

  <circle cx="70" cy="95" r="10" fill="#F9FAFB"/>
  <circle cx="100" cy="95" r="10" fill="#F9FAFB"/>
  <circle cx="130" cy="95" r="10" fill="#F9FAFB"/>

  <circle cx="70" cy="125" r="10" fill="#F9FAFB"/>
  <circle cx="100" cy="125" r="10" fill="#F9FAFB"/>
  <circle cx="130" cy="125" r="10" fill="#F59E0B"/>

  <circle cx="70" cy="155" r="10" fill="#F9FAFB"/>
  <circle cx="100" cy="155" r="10" fill="#F9FAFB"/>
  <circle cx="130" cy="155" r="10" fill="#10B981"/>
</svg>
</div>
"""

st.markdown(calculator_svg, unsafe_allow_html=True)

st.title("🧮 Advanced Calculator")

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

num1 = st.number_input("첫 번째 숫자", value=0.0)

if operation == "로그 (log)":
    base = st.number_input("밑 (base)", value=10.0)
else:
    num2 = st.number_input("두 번째 숫자", value=0.0)

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
            if num2 == 0:
                st.error("0으로 나눌 수 없습니다.")
                st.stop()
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
