import pickle
import random
import pandas as pd
import numpy as np

class PodcastRecommender():
    
    def __init__(self):
        self.sim_mat = None
        self.titles_list = None
        self.podcast_recs = None
        
    def get_recommendations(self, sim_mat, titles_list, title, num_recs=3):
        '''
        Returns the top num_recs recommendations for the specified title given the similarity matrix of podcasts, a list of the titles, specified title, and the number of recommendations.
        Input:
            sim_mat: pandas dataframe
            titles_list: list
            title: string
            num_recs: integer
        Output:
            list
        '''
        self.sim_mat = sim_mat
        self.titles_list = titles_list
        
        idx_titles = {key:val for key, val in zip(range(0, self.sim_mat.shape[0]), self.titles_list)}
        key_list = list(idx_titles.keys())
        val_list = list(idx_titles.values())
        
        if title in titles_list:
            position = val_list.index(title)
            recs_idx = self.sim_mat.iloc[position].values.argsort()[-(num_recs+1):-1][::-1]
        
            self.podcast_recs = []
            for idx in recs_idx:
                self.podcast_recs.append(titles_list[idx])
            return self.podcast_recs
        else:
            return "Sorry, we couldn't find your podcast."
    
    
    
if __name__=='__main__':
    # Load files.
    sim_mat = pd.read_pickle('../data/similarity_matrix.pkl')
    with open('../data/titles_list.pkl', 'rb') as f:
        titles_list = pickle.load(f)
    # To test.
    sample = random.sample(titles_list, 1)
    sample = sample[0]
    print('Sample:' + sample)
    
    x = PodcastRecommender()
    recommendations = x.get_recommendations(sim_mat, titles_list, sample)
    print(recommendations)
        
    