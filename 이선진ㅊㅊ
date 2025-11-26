# crime_kids_app.py
import streamlit as st
import matplotlib.pyplot as plt

st.title("👮‍♂️ 어린이 범죄 예방 퀴즈")

quizzes = [
    {
        "question": "길에서 낯선 사람이 말을 걸었어요. 어떻게 해야 할까요?",
        "options": ["따라간다", "모른 척 한다", "안전한 곳으로 이동하고 부모님께 알린다"],
        "answer": 2
    },
    {
        "question": "온라인에서 모르는 사람이 친구가 되자고 해요. 어떻게 해야 할까요?",
        "options": ["바로 친구 수락", "무시하고 부모님께 알린다", "비밀번호 공유"],
        "answer": 1
    },
    {
        "question": "학교에서 친구가 괴롭힘을 당하고 있어요. 어떻게 해야 할까요?",
        "options": ["함께 괴롭힌다", "선생님이나 어른에게 알린다", "사진 찍어서 소문낸다"],
        "answer": 1
    },
]

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

def check_answer(selected):
    q = quizzes[st.session_state.question_index]
    if selected == q['answer']:
        st.session_state.score += 1
        st.success("✅ 정답!")
    else:
        st.error(f"❌ 틀렸어요. 정답은 '{q['options'][q['answer']]}'입니다.")
    
    st.session_state.question_index += 1
    if st.session_state.question_index >= len(quizzes):
        show_result()

def show_result():
    st.write(f"🎉 퀴즈 종료! 점수: {st.session_state.score}/{len(quizzes)}")
    plt.figure(figsize=(6,4))
    plt.bar(["점수", "최대점수"], [st.session_state.score, len(quizzes)], color=["green","gray"])
    plt.ylim(0, len(quizzes))
    plt.title("범죄 예방 퀴즈 결과")
    plt.ylabel("점수")
    st.pyplot(plt)
    st.stop()

# 퀴즈 표시
if st.session_state.question_index < len(quizzes):
    q = quizzes[st.session_state.question_index]
    st.write(f"문제 {st.session_state.question_index+1}: {q['question']}")
    for i, option in enumerate(q['options']):
        if st.button(option, key=i):
            check_answer(i)
