"""
Inference of Real Estate Price Prediction.
===================================================================
This module to predict the price of real state in lakhs based on
size, Locality, company name and many other things.
"""
import re
import os
import nltk
import pickle
import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from ML_pipeline.textprocess import process_text

#nltk.download('stopwords', halt_on_error=False)


class Real_estate_inference:
    def __init__(self, test):
        self.test_data = None
        self.model = None
        self.test = test

    def avg_property_area(self, x):
        numbers = re.compile(r"[-+]?(\d*\.\d+|\d+)")
        x = numbers.findall(x)
        if len(x) == 1:
            return np.float32(x[0])
        elif len(x) == 2:
            return (np.float32(x[0]) + np.float32(x[1])) / 2
        else:
            return -99

    def generate_sentiment_scores(self, data):
        sid = SentimentIntensityAnalyzer()
        neg = []
        pos = []
        neu = []
        comp = []
        for sentence in data['Description clean'].values:
            sentence_sentiment_score = sid.polarity_scores(sentence)
            comp.append(sentence_sentiment_score['compound'])
            neg.append(sentence_sentiment_score['neg'])
            pos.append(sentence_sentiment_score['pos'])
            neu.append(sentence_sentiment_score['neu'])
        return comp, neg, pos, neu

    def add_features(self, data):
        # Load Area price
        print(os.getcwd())
        fileName = '/home/shobot/Desktop/Project/Real Estate Price Prediction/model/sub_area_price_map.pkl'
        with open(fileName, 'rb') as file:
            sub_area_price = pickle.load(file)
        data['Price by sub-area'] = data['Sub-Area clean'].map(sub_area_price)
        fileName = '/home/shobot/Desktop/Project/Real Estate Price Prediction/model/company_price_map.pkl'
        with open(fileName, 'rb') as file:
            company_area_price = pickle.load(file)
        data['Price by company'] = data['Company Name clean'].map(company_area_price)
        fileName = '/home/shobot/Desktop/Project/Real Estate Price Prediction/model/township_society_price_map.pkl'
        with open(fileName, 'rb') as file:
            society_area_price = pickle.load(file)
        data['Price by township_society'] = data['TownShip Name/ Society Name clean'].map(society_area_price)
        amenities_col = ['Property Type clean', 'ClubHouse Clean', 'School / University in Township Clean',
                         'Hospital in TownShip Clean', 'Mall in TownShip Clean', 'Park / Jogging track Clean',
                         'Swimming Pool Clean']
        temp = data[amenities_col].values
        Amenities_score = temp.sum()
        fileName = '/home/shobot/Desktop/Project/Real Estate Price Prediction/model/amenities_score_price_map.pkl'
        with open(fileName, 'rb') as file:
            amenities_price = pickle.load(file)
        data['Price by Amenities score'] = amenities_price[Amenities_score]
        data['Description clean'] = data['Description'].apply(lambda x: x.lower().strip())
        data['compound'], data['negative'], data['positive'], data['neutral'] = self.generate_sentiment_scores(data)
        data['Description clean'] = data['Description clean'].astype(str).apply(process_text)
        fileName = '/home/shobot/Desktop/Project/Real Estate Price Prediction/model/count_vectorizer.pkl'
        # with open(fileName, 'wb') as f:
        cv_object = pickle.load(fileName)
        X = cv_object.transform(data['Description clean'])

        print(data)

    def processing(self, data):
        numbers = re.compile(r"[-+]?(\d*\.\d+|\d+)")
        data['Property Type clean'] = data['Propert Type'].apply(
            lambda x: float(numbers.findall(x)[0]) if len(numbers.findall(x)) > 0 else 0)
        data['Sub-Area clean'] = data['Sub-Area'].apply(lambda x: x.lower().strip())
        data['Company Name clean'] = data['Company Name'].apply(lambda x: x.lower().strip())
        data['TownShip Name/ Society Name clean'] = data['TownShip Name/ Society Name'].apply(
            lambda x: x.lower().strip())
        data['Description clean'] = data['Description'].apply(lambda x: x.lower().strip())
        data['ClubHouse Clean'] = data['ClubHouse'].apply(lambda x: x.lower().strip()).map(
            {'yes': 1, 'no': 0})
        data['School / University in Township Clean'] = data['School / University in Township '].apply(
            lambda x: x.lower().strip()).map({'yes': 1, 'no': 0})
        data['Hospital in TownShip Clean'] = data['Hospital in TownShip'].apply(
            lambda x: x.lower().strip()).map({'yes': 1, 'no': 0})
        data['Mall in TownShip Clean'] = data['Mall in TownShip'].apply(lambda x: x.lower().strip()).map(
            {'yes': 1, 'no': 0})
        data['Park / Jogging track Clean'] = data['Park / Jogging track'].apply(
            lambda x: x.lower().strip()).map({'yes': 1, 'no': 0})
        data['Swimming Pool Clean'] = data['Swimming Pool'].apply(lambda x: x.lower().strip()).map(
            {'yes': 1, 'no': 0})
        data['Gym Clean'] = data['Gym'].apply(lambda x: x.lower().strip()).map({'yes': 1, 'no': 0})
        data['Property Area in Sq. Ft. clean'] = data['Property Area in Sq. Ft.'].apply(
            lambda x: self.avg_property_area(str(x)))
        return data

    def predict(self):
        # self.model = load_model()
        self.test_data = pd.DataFrame(self.test, index=[0])
        data = self.processing(self.test_data)
        self.add_features(data)
        lower = 0
        upper = 100
        return lower, upper


def main():
    property_type = '3 Bhk'
    hospital_in = 'Yes'
    township_name = 'Godrej Hills retreat'
    mall_in = "Yes"
    gym_in = "Yes"
    city_name = "Pune"
    school_university = "yes"
    park_jogging_track = "Yes"
    club_in = "Yes"
    property_area = 2000
    swimming_pool_in = "Yes"
    company_name = "ANP CORP"
    property_locality = "Mahalunge"
    property_description = 'Shapoorji Paloonji comunity located in the suburbs of Bavadhan locality is situated in a pleasant environment around. This 1BHK property comes with a swimming pool and parking facilty in the community. It also comes with temples and Churches near by for devotional purposes'
    value = {'Propert Type': property_type, 'Hospital in TownShip': hospital_in,
             'TownShip Name/ Society Name': township_name, 'Mall in TownShip': mall_in, 'Gym': gym_in,
             'Property Area in Sq. Ft.': property_area, 'ClubHouse': club_in,
             'Park / Jogging track': park_jogging_track, 'City': city_name, 'Sub-Area': property_locality,
             'School / University in Township ': school_university, 'Swimming Pool': swimming_pool_in,
             'Company Name': company_name, 'Description': property_description}
    real_estate_price = Real_estate_inference(value)
    lower, upper = real_estate_price.predict()
    text = 'The price of this property between {} lakhs and {} lakhs.'.format(lower, upper)
    print(text)


if __name__ == '__main__':
    main()
