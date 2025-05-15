import streamlit as st

st.title("간단한 퀴즈!")

st.subheader("1. 바나나의 겉면 색깔은 무엇인가요?")
options = ["빨강", "노랑", "초록", "파랑", "보라"]
answer_q = st.radio("선택하세요:", options)
correct_q = "노랑"

st.subheader("2. 우리나라의 수도는 어디인가요?")
answer_subjective = st.text_input("정답을 입력하세요")
correct_subjective = "서울"

if st.button("제출하기"):
    if answer_q == correct_q:
        st.success("객관식: 정답입니다!")
    else:
        st.error("객관식: 오답입니다.")

    if answer_subjective == correct_subjective:
        st.success("주관식: 정답입니다!")
    else:
        st.error("주관식: 오답입니다.")
