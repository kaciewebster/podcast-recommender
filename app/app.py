import pickle
import pandas as pd
import numpy as np
from recommender import PodcastRecommender

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
feature_df = pickle.load(open('features.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl','rb'))
pr = PodcastRecommender()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    key_words = str(request.form['key_words'])
    num_recs = int(request.form['num_recs'])

    recommendations = pr.get_recommendations([key_words], num_recs)
    return render_template('recommend.html', names=recommendations)



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080, debug=True)