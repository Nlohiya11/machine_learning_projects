import streamlit as st
import pickle

def app():
    mf = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity_tfidf.pkl', 'rb'))

    movie_list = mf['Title'].values

    option = st.selectbox("Your Recent Movie", movie_list)

    def recommend(movie):
        index = mf[mf['Title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        movies = []
        for i in distances[1:6]:
            movies.append(mf.iloc[i[0]].Title)
        return movies

    if st.button('Recommend'):
        rec = recommend(option)
        for i in rec:
            for index, row in mf.iterrows():
                if row['Title'] == i:
                    col1, col2, col3, col4 = st.columns([0.2, 0.4, 0.15, 0.25])
                    with col1:
                        st.image(row['Image'])
                    with col2:
                        st.write(i)
                    with col3:
                        st.markdown(f'**:blue[{row["Year_of_Release"]}]**')
                    with col4:
                        st.markdown(f'**:star: :blue[{row["Rating"]}]**')

