import pickle
import pandas as pd
import numpy as np
from recommender import PodcastRecommender

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommendations():
    user_input = request.json
    title, num_recs = user_input['title'], user_input['num_recs']
    rec_list = _recommendations(sim_mat, titles_list, title, num_recs)
    if rec_list:
        rec_dict = {letter:rec for letter, rec in zip(['a', 'b', 'c'], rec_list)}
        return jsonify(rec_dict)
    else:
        return jsonify({})

def _recommendations(sim_mat, titles_list, title, num_recs):
    # title = str(request.form['title'])
    # num_recs = int(request.form['num_recs'])
    user_input = request.json
    title, num_recs = user_input['title'], user_input['num_recs']

    if title in titles_list:
        pr = PodcastRecommender()
        recommendations = pr.get_recommendations(sim_mat, titles_list, title, num_recs)
        return recommendations
    else:
        return []



if __name__ == '__main__':
    sim_mat = pd.read_pickle('similarity_matrix.pkl')

    with open('titles_list.pkl', 'rb') as f:
        titles_list = pickle.load(f)

    app.run(host='0.0.0.0', port=8080, debug=True)