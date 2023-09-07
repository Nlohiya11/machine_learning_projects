import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import streamlit as st

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpapers.com/images/hd/iconic-amazon-logo-l83gjulwv6pcklbl.jpg");
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

datainput = st.text_area("Enter the message")
if st.button('Predict'):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    name = []
    price = []
    rating = []
    image = []
    stars = []
    arrival = []
    last_buy = []
    for number in range(0, 8):
        webpage = ""
        string = requests.get(f'https://www.amazon.in/s?k={datainput}&page={number}&ref=sr_pg_1', headers=headers).text
        webpage = string + webpage
        soup = BeautifulSoup(webpage, 'html.parser')
        page = soup.find('div', class_='a-section a-spacing-small a-spacing-top-small').text.strip().split(' ')[0].split('-')
        total_item = int(page[1]) - int(page[0])
        total_item = int(total_item)
        if total_item > 20:
            products_2 = soup.find_all('div', class_='s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-v11f16tn6b5f9e2nrycg91ik6p8 s-latency-cf-section s-card-border')
            for info in products_2:
                try:
                    i = info.find('div', class_='a-row a-size-base a-color-base').text.strip()
                    price.append(i.split('₹')[1])
                except:
                    price.append(np.nan)
                try:
                    i = info.find('span', class_='a-size-base s-underline-text').text.strip()
                    rating.append(i)
                except:
                    rating.append(np.nan)
                try:
                    image.append(info.find('img', class_='s-image').get('src'))
                except:
                    image.append(np.nan)
                try:
                    stars.append(info.find('span', class_='a-icon-alt').text.strip().split(' ')[0])
                except:
                    stars.append(np.nan)
                try:
                    i = info.find('span', class_='a-color-base a-text-bold').text.strip()
                    arrival.append(i)
                except:
                    arrival.append('No Date specified')
                try:
                    i = info.find('span', class_='a-size-base-plus a-color-base a-text-normal').text.strip()
                    name.append(i)
                except:
                    name.append(np.nan)
                try:
                    i = info.find('span', class_='a-size-base a-color-secondary').text.strip()
                    last_buy.append(i)
                except:
                    last_buy.append(np.nan)
                len(last_buy)
            dictionary = {'Product': name, 'Stars': stars, 'Rating': rating, 'Image': image, 'Price': price, 'Delievery_time': arrival, 'Previous_buyers': last_buy}

        else:
            products_1 = soup.find_all('div', class_ = 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')
            for info in products_1:
                try:
                    i = info.find('span', class_='a-price-whole').text.strip()
                    price.append(i)
                except:
                    price.append('kalu')
                try:
                    i = info.find('span', class_='a-size-base s-underline-text').text.strip()
                    rating.append(i)
                except:
                    rating.append(np.nan)
                try:
                    image.append(info.find('img', class_='s-image').get('src'))
                except:
                    image.append(np.nan)
                try:
                    stars.append(info.find('span', class_='a-icon-alt').text.strip().split(' ')[0])
                except:
                    stars.append(np.nan)
                try:
                    i = info.find('span', class_='a-color-base a-text-bold').text.strip()
                    arrival.append(i)
                except:
                    arrival.append('No Date specified')
                try:
                    i = info.find('span', class_='a-size-medium a-color-base a-text-normal').text.strip()
                    name.append(i)
                except:
                    name.append('Kalu')
            dictionary = {'Product': name, 'Stars': stars, 'Rating': rating, 'Image': image, 'Price': price, 'Delievery_time': arrival}
    df = pd.DataFrame(dictionary)
    st.write(df.head(5))