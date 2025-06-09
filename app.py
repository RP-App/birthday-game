import streamlit as st

birthday_sets = [
    [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31],
    [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31],
    [4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31],
    [8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31],
    [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
]

color_palette = ["#A2D2FF", "#FFAFCC", "#FFE066", "#CDB4DB", "#B5EAD7", "#FFDAC1", "#FAD2E1", "#BDE0FE"]

st.set_page_config(page_title="เกมทายวันเกิด", layout="centered")
st.title("🎂 เกมทายวันเกิด")

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []

step = st.session_state.step

if step < len(birthday_sets):
    st.subheader(f"ชุดที่ {step + 1} : วันเกิดของคุณอยู่ในนี้หรือไม่?")

    cols = st.columns(4)
    for idx, num in enumerate(birthday_sets[step]):
        with cols[idx % 4]:
            color = color_palette[idx % len(color_palette)]
            st.markdown(
                f"<div style='background-color:{color}; padding:10px; text-align:center; font-weight:bold; border-radius:6px;'>{num}</div>",
                unsafe_allow_html=True
            )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ ใช่"):
            st.session_state.answers.append(True)
            st.session_state.step += 1
            st.experimental_rerun()
    with col2:
        if st.button("❌ ไม่ใช่"):
            st.session_state.answers.append(False)
            st.session_state.step += 1
            st.experimental_rerun()
else:
    total = sum(2 ** i for i, val in enumerate(st.session_state.answers) if val)
    st.success(f"🎉 วันเกิดของคุณคือวันที่ **{total}**!")
    if st.button("🔁 เล่นใหม่"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.experimental_rerun()
