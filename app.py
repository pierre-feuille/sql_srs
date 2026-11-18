import streamlit as st
import pandas as pd
import duckdb

st.write("Hello tout le monde")
data = {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat","Dog","Owl"])

# stockage du texte écrit dans une variable sql_query (requête)
with tab1:
    sql_query = st.text_area(label="Entrez du texte ici ")
    # stockage de ma requête sous format de requete SQL lisible par duckdb
    result = duckdb.query(sql_query)
    st.write(f" Requête demandée : {sql_query}")
    # streamlit affiche le résultat de la requête
    st.dataframe(result)

with tab2:
    st.header("Un chien !")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("Un hibou !")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
# Création de ma dataframe + affichage
# Afficher la frame
#st.write(df)
