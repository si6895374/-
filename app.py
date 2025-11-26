import streamlit as st
import random

st.title("🎯 숫자 맞추기 게임 (Streamlit Web Version)")
st.write("난이도를 선택하고 숫자를 맞춰보세요!")

# 난이도 설정
level = st.selectbox(
    "난이도를 선택하세요",
    ("Easy (1~50)", "Normal (1~100)", "Hard (1~200)")
)

if "answer" not in st.session_state:
    st.session_state.answer = None
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "max_try" not in st.session_state:
    st.session_state.max_try = 0
if "max_num" not in st.session_state:
    st.session_state.max_num = 0

# 난이도에 따라 값 설정
if st.button("게임 시작"):
    if "Easy" in level:
        st.session_state.max_num = 50
        st.session_state.max_try = 10
    elif "Normal" in level:
        st.session_state.max_num = 100
        st.session_state.max_try = 8
    else:
        st.session_state.max_num = 200
        st.session_state.max_try = 6

    st.session_state.answer = random.randint(1, st.session_state.max_num)
    st.session_state.attempts = 0

    st.success(f"게임 시작! 1~{st.session_state.max_num} 숫자 중 하나를 맞춰보세요!")

# 게임 진행
if st.session_state.answer:
    guess = st.number_input(
        "추측한 숫자를 입력하세요",
        min_value=1,
        max_value=st.session_state.max_num,
        step=1
    )
    
    if st.button("확인"):
        st.session_state.attempts += 1
        
        if guess < st.session_state.answer:
            st.warning("🔼 더 큰 숫자입니다!")
        elif guess > st.session_state.answer:
            st.warning("🔽 더 작은 숫자입니다!")
        else:
            st.success(f"🎉 정답! {st.session_state.attempts}번 만에 맞추셨습니다!")
            st.balloons()
            st.session_state.answer = None  # 게임 초기화
            
        # 힌트
        if st.session_state.answer is not None:
            diff = abs(st.session_state.answer - guess)
            if diff >= 20:
                st.info("💡 힌트: 정답과 꽤 차이가 커요!")
            elif diff >= 10:
                st.info("💡 힌트: 정답과 조금 차이가 나요!")
            else:
                st.info("💡 힌트: 거의 근접했어요!")

            # 남은 시도
            remaining = st.session_state.max_try - st.session_state.attempts
            st.write(f"⏳ 남은 시도: {remaining}번")

            if remaining <= 0:
                st.error(f"❌ 게임 오버! 정답은 {st.session_state.answer}였습니다.")
                st.session_state.answer = None
