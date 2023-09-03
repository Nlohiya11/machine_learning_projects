import pandas as pd
import streamlit as st


def app():
    df = pd.read_csv('pictures.csv')
    mf = df.head(10000)
    mf['Stars'] = mf['Stars'].apply(lambda x: x.split(', '))
    mf['Stars'] = mf['Stars'].apply(lambda x: x[0:3])

    def details(column, list_name,dataset):
        information = dataset[column].unique()
        list_info = []
        for info in information:
            list_info += info.split(', ')
        for x in list_info:
            if x not in list_name:
                list_name.append(x)

    genre = []
    director = []
    details(column='Movie_director', list_name=director,dataset=mf)
    details(column='Genre', list_name=genre,dataset=df)
    Certified = df['Certified'].unique()
    title = df['Title'].values
    mt = []
    stars = []
    all_stars = df['Stars']
    for i in range(0, 10000):
        mt += all_stars[i]
    for x in mt:
        if x not in stars:
            stars.append(x)

    def intersection(list1, list2):
        list3 = [value for value in list1 if value in list2]
        return list3

    def selector(fun):
        if fun == 'Genre':
            data = st.selectbox("Select your Location", genre)
        if fun == 'Certified':
            data = st.selectbox("what age group it should be", Certified)
        if fun == 'Movie_director':
            data = st.selectbox("Select your choised Director", director)
        if fun == 'Stars':
            data = st.selectbox("Enter how many bathroom it required", stars)
        return data

    datase = st.radio('Chose either director or star', ['Stars', 'Movie_director'])

    def list_of_movies(selection, sort_by):
        nit = selection
        film = []
        print(nit, sort_by)
        for index, row in df.iterrows():
            if nit in row[sort_by]:
                film.append(row['Title'])
            else:
                r = nit
        return film
    print(datase)

    title = title[0:5]
    if st.button('Recommend'):
        for i in title:
            for index, row in df.iterrows():
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
