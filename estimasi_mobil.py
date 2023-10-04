import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title("Estimasi Harga mobil bekas")

year = st.number_input("input tahun mobil")
mileage = st.number_input("input km mobil")
tax = st.number_input("input pajak mobil")
mpg = st.number_input("input konsumsi bbm mobil")
engineSize = st.number_input("input Engine size mobil")

predict = ""

if st.button("Estimasi harga"):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    st.write("Estimasi Harga Mobil Bekas dalam Ponds : ", predict)
    st.write("Estimasi Harga Mobil Bekas dalam IDR (juta) : ", predict*19000)
