import pickle
import pandas as pd
import numpy as np
from recommender import PodcastRecommender

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
pr = PodcastRecommender()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    title = str(request.form['title'])
    num_recs = int(request.form['num_recs'])

    recommendations = pr.get_recommendations(title, num_recs)
    return render_template('recommend.html', names=recommendations)



if __name__ == '__main__':
    # Load files.
    sim_mat = pd.read_pickle('similarity_matrix.pkl')
    with open('titles_list.pkl', 'rb') as f:
        titles_list = pickle.load(f)
    with open('category_dict.pkl', 'rb') as f:
        cat_dict = pickle.load(f)

    app.run(host='0.0.0.0', port=8080, debug=True)