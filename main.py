import requests
import streamlit as st

st.set_page_config(
    page_icon=':shark',
    page_title='BrewMatch'
)



st.header('Welcome To BrewMatch - Find All Cafes By City Name')
city_name = st.text_input('Enter the city name: ')

submit = st.button(label='Fetch Cafes')

if city_name:
    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries?by_city={city_name}')
    if response.status_code == 200:
        data = response.json()
        if submit:
            for index,cafe in enumerate(data, start=1):
                st.write(f'Cafe {index}: ')
                st.write(f"     Name: {cafe['name']}")
                st.write(f"     Cafe Address:{cafe['address_1']}")
                st.write(f"     Cafe Type: {cafe['brewery_type']}")
                st.write(f"     Website URL Of The Cafe: {cafe['website_url']}")
                st.write(f"     Phone Number: {cafe['phone']}")
                st.write(f"     Postal Code: {cafe['postal_code']}")
                st.write(f"     State: {cafe['street']}")
        else:
            st.error('Please Press the Fetch Cafes Button')
    else:
        st.error('Please Enter A Valid City Name Or Sorry, We are unable to find any city with the name into our database🙏')

