import streamlit as st
import pandas as pd
import duckdb

st.write("Hello tout le monde")
data = {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}
df = pd.DataFrame(data)

# stockage du texte écrit dans une variable sql_query (requête)
sql_query = st.text_area(label="Entrez du texte ici ")

# stockage de ma requête sous format de requete SQL lisible par duckdb
result = duckdb.query(sql_query)
st.write(f" Requête demandée : {sql_query}")
# streamlit affiche le résultat de la requête
st.dataframe(result)

# Création de ma dataframe + affichage
# Afficher la frame
#st.write(df)
