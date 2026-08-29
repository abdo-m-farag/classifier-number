import streamlit as st
from PIL import Image 
from inference import predict

st.title("classfier")

uploaded_file=st.file_uploader("upload",type=['png','jpg','peg'])
if uploaded_file is not None:
    img=Image.open(uploaded_file)
    st.image(img,caption="upload image ",width=200)
    prediction =predict(img)

    st.success(f"predcit : {prediction}")