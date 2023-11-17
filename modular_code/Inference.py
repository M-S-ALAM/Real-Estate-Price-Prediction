# from ML_pipeline import load_model
import nltk


class Real_estate_inference:
    def __init__(self, data):
        self.model = None
        self.data = data

    def predict(self):
        # self.model = load_model()
        pass


def main():
    nltk.download('stopwords')


if __name__ == '__main__':
    main()
