# from ML_pipeline import load_model
import nltk
import re
import pandas as pd
import numpy as np


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

    def processing(self, data):
        numbers = re.compile(r"[-+]?(\d*\.\d+|\d+)")
        data['Property Type clean'] = data['Propert Type'].apply(
            lambda x: numbers.findall(x)[0] if len(numbers.findall(x)) > 0 else 0)
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
        numbers = re.compile(r"[-+]?(\d*\.\d+|\d+)")
        data['Price in lakhs clean'] = data['Price in lakhs'].apply(
            lambda x: np.float32(numbers.findall(str(x))[0]) if len(numbers.findall(str(x))) > 0 else np.nan)
        print(data.head())

    def predict(self):
        # self.model = load_model()
        self.test_data = pd.DataFrame(self.test, index=[0])
        self.processing(self.test_data)
        lower = 0
        upper = 100
        return lower, upper
