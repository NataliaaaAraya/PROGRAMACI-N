import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("UNI_CORR_500_01.txt", skiprows=4, sep="\t", names=["ID", "frames", "X", "Y", "Z"])

st.write(""" 
         # mi primera app locura 
         ### aaaaaa """)

div = st.slider("numero de bins: ", 0, 130, 25)

st.write("Bins=", div)

fig, ax = plt.subplots(figsize=(10, 3))
ax.hist(df["Y"], bins=div, color= "lightcoral")
ax.set_xlabel("Posición en metros")
ax.set_ylabel("Frecuencia")
ax.set_title("Histograma posiciónes enel eje X")
st.pyplot(fig)