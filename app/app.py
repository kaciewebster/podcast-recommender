import pickle
import pandas as pd
import numpy as np
from recommender import PodcastRecommender

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_page():
    return '''<h1>Content Based Podcast Recommender</h1>
                <p>This app will recommend similar podcasts based on a podcast you provide.
                <br>Recommendations are based on a combination of the description, category, and language of each podcast.
                <br><br>Let's get started!</p>
                <p>Because you listened to ...</p>
                <form action="/recommend" method='POST' >
                <input type="string" name="title" />
                <input type="submit" />
                </form>
                '''

@app.route('/recommend', methods=['POST'])
def recommend():
    title = str(request.form['title'])
    num_recs = 3
    
    if title in titles_list:
        pr = PodcastRecommender()
        recommendations = pr.get_recommendations(sim_mat, titles_list, title, num_recs)
        return "We would recommend {}.".format(recommendations)
    else:
        return "We're sorry, but we couldn't find your podcast!"

    



if __name__ == '__main__':
    sim_mat = pd.read_pickle('similarity_matrix.pkl')
    
    with open('titles_list.pkl', 'rb') as f:
        titles_list = pickle.load(f)

    app.run(host='0.0.0.0', port=8080, debug=True)