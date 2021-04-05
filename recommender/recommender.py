import pandas as pd
import pickle
import numpy as np

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import unicodedata
import string
from langid.langid import LanguageIdentifier, model

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class PodcastRecommender():

    def __init__(self):
        self.feature_df = None
        self.tfidf = None

    def remove_accents(self, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        return only_ascii.decode()

    def clean_text(self, docs):
        # Make all words in documents lowercase.
        low_docs = [doc.lower() for doc in docs]
        # Remove all accents from documents.
        acc_docs = [self.remove_accents(doc) for doc in low_docs]
        # Tokenize each document.
        tokens = [word_tokenize(doc) for doc in acc_docs]
        # Remove stopwords and punctuation.
        stopwords_ = set(stopwords.words('english'))
        punctuation_ = set(string.punctuation)
        tokens = [[word for word in token if word not in stopwords_ and word not in punctuation_] for token in tokens]
        # Apply Lemmatizer Stemmer.
        lemmatizer = WordNetLemmatizer()
        lemmatize_tokens = [list(map(lemmatizer.lemmatize, token)) for token in tokens]
        # Join tokens in each document.
        token_docs = [' '.join(tokens) for tokens in lemmatize_tokens]
        return token_docs

    def get_recommendations(self, key_words, num_recs=3):
        '''
        Return recommendations based on cosine similarity of key words in the text descriptions
        Input:
            key_words: list of a string
            num_recs: integer
        Output:
            list of lists
        '''
        self.feature_df = feature_df
        self.tfidf = tfidf

        cleaned_test = self.clean_text(key_words)
        test_matrix = tfidf.transform(cleaned_test)
        test_matrix = test_matrix.toarray()
        feature_names = tfidf.get_feature_names()
        test_df = pd.DataFrame(test_matrix, index=['test'], columns=feature_names)

        test_similarities = cosine_similarity(feature_df, test_df).T[0]
        idxs = test_similarities.argsort()[-(num_recs):]

        return list(zip(list(reversed(list(feature_df.iloc[idxs].index))), list(reversed(list(test_similarities[idxs])))))


if __name__=='__main__':
    # Load files
    feature_df = pickle.load(open('../data/features.pkl', 'rb'))
    tfidf = pickle.load(open('../data/vectorizer.pkl','rb'))

    # Test
    test = PodcastRecommender()
    recommendations = test.get_recommendations(['sports, basketball, nba, talk show'])
    print(recommendations)

