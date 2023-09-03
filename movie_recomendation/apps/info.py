import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import urllib.request


def app():
    df = pd.read_csv('pictures.csv')

    title = df['Title'].unique()
    movie = st.selectbox("Select your Movie", title, on_change=None)
    if st.button('Predict'):
        for index, row in df.iterrows():
            if row['Title'] == movie:
                urllib.request.urlretrieve(row['Image'], "movie.jpg")
                image = Image.open("movie.jpg")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(' ')
                with col2:
                    st.image(image, caption=row['Title'])
                with col3:
                    st.write(' ')
                st.write(f'**{row["Description"]}**')
                col1, col2 = st.columns([0.4, 0.6])
                with col1:
                    st.markdown(f':green[Year Of Release : ] **{row["Year_of_Release"]}** ')
                with col2:
                    st.markdown(f':green[Movie Genre :] **{row["Genre"]}**')
                col1, col2 = st.columns([0.4, 0.6])
                with col1:
                    st.markdown(f':green[Rating of movie is :] **:star: {row["Rating"]}**')
                with col2:
                    st.markdown(f':green[Meta Score : ] **:tomato: {row["Metascore"]}** ')
                col1, col2 = st.columns([0.2, 0.8])
                with col1:
                    st.markdown('**:green[Directed by :]**')
                with col2:
                    st.markdown(f'**{row["Movie_director"]}**')
                col1, col2 = st.columns([0.2, 0.8])
                with col1:
                    st.markdown('**:green[Cast of the movie :]**')
                with col2:
                    st.markdown(f'**{row["Stars"]}**')
                col1, col2 = st.columns([0.2, 0.8])
                with col1:
                    st.markdown('**:green[Certificates :]**')
                with col2:
                    st.markdown(f'**This movie is **:orange[{row["Certified"]}]** certified**')
            else:
                r = movie

