'''movie_recomendation'''
import streamlit as st
from Multipage import MultiApp
from apps import info, recommender, similar_movie_type_model


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://cdn.wallpapersafari.com/29/57/QEj3Uo.jpg");
background-size: 200%;
background-position: centre;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(80,120,230,140);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("ARMI : Application to Recommend Movies & Information")


app = MultiApp()


app.add_app("Movie Information", info.app)
app.add_app("Movie Recommendation", recommender.app)
app.add_app("Recommendation using Recent Movie", similar_movie_type_model.app)
app.run()