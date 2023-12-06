import streamlit as st
import os
from PIL import Image

st.title('Dog Breed Classifier')

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('static/images',uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1    
    except:
        return 0
      
      
uploaded_file = st.file_uploader("Upload Image")

# text over upload button "Upload Image"

if uploaded_file is not None:
  if save_uploaded_file(uploaded_file):
    st.write("File saved Successfully")
    display_image = Image.open(uploaded_file)
    st.image(display_image)
