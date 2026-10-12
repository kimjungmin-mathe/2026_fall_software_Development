import streamlit as st
import pandas as pd

data = st.file_uploader("upload file", type={"csv", "txt"})

if data is not None:
    df = pd.read_csv(data)
    df = df[::-1].reset_index(drop=True)
    df["time"] = df.index

    st.write(df)

    # 숫자형 열 자동 탐색
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    numeric_cols = [col for col in numeric_cols if col != "time"]

    if numeric_cols:
        st.line_chart(df, x="time", y=numeric_cols)
    else:
        st.warning("그래프로 표시할 숫자 데이터가 없습니다.")
