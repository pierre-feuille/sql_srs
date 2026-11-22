import streamlit as st

option = st.selectbox(
    "Quel moyen de contact préférez-vous ?",
    ("Email", "Tél portable", "Pigeon voyageur"),
    index=None,
    placeholder="Quel moyen de contact",
)

st.write("Mode de contact choisi : ", option)