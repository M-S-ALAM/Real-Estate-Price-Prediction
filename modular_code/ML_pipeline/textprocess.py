import re
import nltk
from nltk.corpus import stopwords
from collections import Counter


def process_text(data):
    REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;!]')
    BAD_SYMBOLS_RE = re.compile("[^0-9a-z #+_]")
    STOPWORDS_nlp = set(stopwords.words('english'))
    # Custom Stoplist
    stoplist = ["i", "project", "living", "home", 'apartment', "pune", "me", "my", "myself", "we", "our", "ours",
                "ourselves", "you", "you're", "you've", "you'll", "you'd", "your",
                "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "she's", "her", "hers",
                "herself", "it",
                "it's", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who",
                "whom", "this", "that", "that'll",
                "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
                "having", "do", "does", "did",
                "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at",
                "by", "for", "with", "about",
                "against", "between", "into", "through", "during", "before", "after", "above", "below", "to",
                "from", "up", "down", "in", "out",
                "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where",
                "why", "all", "any",
                "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own",
                "same", "so", "than", "too",
                "very", "s", "t", "can", "will", "just", "don", "don't", "should", "should've", "now", "d", "ll",
                "m", "o", "re", "ve", "y", "ain",
                "aren", "couldn", "didn", "doesn", "hadn", "hasn",
                "haven", "isn", "ma", "mightn", "mustn", "needn", "shan", "shan't",
                "shouldn", "wasn", "weren", "won", "rt", "rt", "qt", "for",
                "the", "with", "in", "of", "and", "its", "it", "this", "i", "have", "has", "would", "could", "you",
                "a", "an",
                "be", "am", "can", "edushopper", "will", "to", "on", "is", "by", "ive", "im", "your", "we", "are",
                "at", "as", "any", "ebay", "thank", "hello", "know",
                "need", "want", "look", "hi", "sorry", "http", "https", "body", "dear", "hello", "hi", "thanks",
                "sir", "tomorrow", "sent", "send", "see", "there", "welcome", "what", "well", "us"]

    STOPWORDS_nlp.update(stoplist)

    def pos_counter(x, pos):
        """
        Returns the count for the given parts of speech tag

        NN - Noun
        VB - Verb
        JJ - Adjective
        RB - Adverb
        """
        tokens = nltk.word_tokenize(x.lower())
        tokens = [word for word in tokens if word not in STOPWORDS_nlp]
        text = nltk.Text(tokens)
        tags = nltk.pos_tag(text)
        counts = Counter(tag for word, tag in tags)
        return counts[pos]

    # Function to preprocess the text
    def text_prepare(text):
        """
            text: a string

            return: modified initial string
        """
        text = text.replace("\d+", " ")  # removing digits
        text = re.sub(r"(?:\@|https?\://)\S+", "", text)  # removing mentions and urls
        text = text.lower()  # lowercase text
        text = re.sub('[0-9]+', '', text)
        text = REPLACE_BY_SPACE_RE.sub(" ", text)  # replace REPLACE_BY_SPACE_RE symbols by space in text
        text = BAD_SYMBOLS_RE.sub(" ", text)  # delete symbols which are in BAD_SYMBOLS_RE from text
        text = ' '.join([word for word in text.split() if word not in STOPWORDS_nlp])  # delete stopwors from text
        text = text.strip()
        return text

    data["Description clean"] = data["Description clean"].astype(str).apply(text_prepare)
    data['Noun_Counts'] = data['Description clean'].apply(lambda x: pos_counter(x, 'NN'))
    data['Verb_Counts'] = data['Description clean'].apply(lambda x: (pos_counter(x, 'VB') + pos_counter(x, 'RB')))
    data['Adjective_Counts'] = data['Description clean'].apply(lambda x: pos_counter(x, 'JJ'))
    return data
