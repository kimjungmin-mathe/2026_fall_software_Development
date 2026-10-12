import streamlit as st
import pandas as pd

data = st.file_uploader("upload file", type={"csv", "txt"})

if data is not None:
    df = pd.read_csv(data)
    df = df[::-1].reset_index(drop=True)
    df['time'] = df.index

    st.write(df)
    st.write("열 이름:", df.columns.tolist())
    st.write("데이터 타입:", df.dtypes)

    if "Close" in df.columns:
        df["Close"] = pd.to_numeric(
            df["Close"].astype(str).str.replace(",", ""),
            errors="coerce"
        )
        st.line_chart(df, x="time", y="Close")
    else:
        st.error("CSV 파일에 Close 열이 없습니다.")
