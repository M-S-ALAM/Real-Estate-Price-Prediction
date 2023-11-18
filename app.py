import streamlit as st
from modular_code.Inference import Real_estate_inference

st.title('Real Estate Price Prediction')

col1, col2, col3 = st.columns(3)


with col1:
    property_type = st.number_input('Property Type in BHK', min_value=1.0, max_value=6.0, step=0.5,format="%.1f")
    township_name = st.selectbox('Township name', options=['Vanaha ', 'Godrej Hills retreat', 'ANP Universe', 'Urban Skyline','VTP Cierra', 'VTP Blue Water', 'OM Mangalam Chaitanya', 'Sukwani Aspire', 'Mantra 29 Gold', 'Mantra Monarch', 'Infinity', 'Mantra Insignia', '7Hills','Mantra Sky Tower', 'the work club', 'newton homes', 'lesiure Town', 'k ville', 'bluegrass residences', 'brookefield willows', 'tranquility annexe', 'mahalunge riviera ', 'simplicity', 'aureta ', 'unique legacy royale', 'Presidia ', 'Eternia 2.0', 'Bliss Solitaire', 'Impero', 'River Dale Residency', 'Neco Beaumont', 'Anutham' 'Sensorium ', 'kiarah terrazo', 'Dolphin Garima ', 'Oxy Beaumonde ', 'Sportsville ', 'Presidenta ', 'Bhaktamar Residency ', 'Parklane UrbanJoy ', 'khush vista', 'oxy eterno', 'Abitante Fiore', 'puraniks Sayama', 'Rhythm county ', 'Kalpataru Serenity', 'Satyam Shivam', 'Satyam Serenity', 'jade residences ', 'Satyam Shery', 'Atulya Kanhe', 'SUPREME ESTIA', 'TEJ ELEVIA', 'vtp solitaire '])
    mall_in = st.selectbox('Mall in township', options=['Yes', 'No'])
    gym_in = st.selectbox('Gym in township', options=['Yes', 'No'])

with col2:
    property_area = st.number_input('Property area in sq. Ft.', min_value=1000, max_value=10000)
    club_in = st.selectbox('Club house in property', options=['Yes', 'No'])
    park_jogging_track = st.selectbox('Park/Jogging track', options=['Yes', 'No'])
    city_name = st.selectbox('City', options=['Pune'])


with col3:
    property_locality = st.selectbox('Property locality', options=['Bavdhan', 'Mahalunge', 'Balewadi', 'Ravet', 'Baner', 'Kharadi','Koregaon Park', 'Keshav Nagar', 'KirkatWadi Sinhagad Road', 'Akurdi', 'pimpri pune', 'tathawade', 'hadapsar', 'kiwale', 'kayani nagar', 'pisoli', 'manjri ', 'mahalunge', 'handewadi', 'koregoan', 'Mundhwa', 'NIBM', 'BT Kawade RD', 'Undri ', 'Karvanagar ', 'magarpatta ', 'Hinjewadi ', 'ravet ', 'vimannagar', 'wadgaon sheri ', 'Susgaon ', 'mohammadwadi ', 'dhanori ','bavdhan budruk ', 'lonavala', 'baner', 'bavdhan', 'talegoan ', 'BANER'])
    school_university = st.selectbox('Is there is school/university near by', options=['Yes', 'No'])
    swimming_pool_in = st.selectbox('Swimming pool in property', options=['Yes', 'No'])
    state_name = st.selectbox('State', options=['Maharashtra/India'])


property_description = st.text_input('Property Descriptions')
value = {'Propert Type': property_type,'TownShip Name/ Society Name': township_name,'Mall in TownShip':mall_in,'Gym': gym_in, 'Property Area in Sq. Ft.': property_area, 'ClubHouse': club_in, 'Park / Jogging track': park_jogging_track, 'City': city_name, 'Sub-Area': property_locality, 'School / University in Township': school_university, 'Swimming Pool': swimming_pool_in,'State': state_name, 'Description':property_description}
st.write(value)
st.write(property_description)

submit_button = st.button(label='Prediction', type='primary')
if submit_button:
    real_state = Real_estate_inference(value)
    lower, upper = real_state.predict()
    text = 'The price of this property between {} lakhs and {} lakhs.'.format(lower, upper)
    st.write(text)