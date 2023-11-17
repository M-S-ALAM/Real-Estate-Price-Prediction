import streamlit as st

st.title('Real Estate Price Prediction of PUNE')

col1, col2, col3 = st.columns(3)


with col1:
    property_type = st.number_input('Property Type in BHK', min_value=1, max_value=6)
    township_name = st.selectbox('Township name', options=['A','B'])
    mall_in = st.selectbox('Mall in township', options=['Yes', 'No'])
    gym_in = st.selectbox('Gym in township', options=['Yes', 'No'])

with col2:
    property_area = st.number_input('Property area in sq. Ft.', min_value=1000, max_value=10000)
    club_in = st.selectbox('Club house in property', options=['Yes', 'No'])
    park_jogging_track = st.selectbox('Park/Jogging track', options=['Yes', 'No'])
    city_name = st.selectbox('City', options=['Pune'])


with col3:
    property_locality = st.selectbox('Property locality', options=['A', 'B'])
    school_university = st.selectbox('Is there is school/university near by', options=['Yes', 'No'])
    swimming_pool_in = st.selectbox('Swimming pool in property', options=['Yes', 'No'])
    state_name = st.selectbox('State', options=['Maharashtra/India'])


property_description = st.text_input('Property descriptions')
value = [property_type,township_name,mall_in,gym_in, property_area,club_in, park_jogging_track, city_name, property_locality, school_university, swimming_pool_in, state_name]
st.write(value)
st.write(property_description)

submit_button = st.button(label='Predict', type='primary')