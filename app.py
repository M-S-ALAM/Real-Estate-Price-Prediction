import streamlit as st

st.title('Real Estate Price Prediction')

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


property_description = st.text_input('Property Descriptions')
value = {'Property type': property_type,'Town ship name': township_name,'Mall in Township':mall_in,'Gym in Property': gym_in, 'Property Area': property_area,'Club in Township': club_in, 'Park/Jogging Track': park_jogging_track, 'City name': city_name, 'Property Locality': property_locality, 'School//University': school_university, 'Swimming pool near by': swimming_pool_in,'State name': state_name}
st.write(value)
st.write(property_description)

submit_button = st.button(label='Prediction', type='primary')