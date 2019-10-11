from fastai.text import *
import argparse

parser = argparse.ArgumentParser(description="Enter some words.")
parser.add_argument('--words', '-w', type=str, required=True, help="Enter a string.")
parser.add_argument('--temperature', '-t', type=float, help="Temperature.", default=1.)
parser.add_argument('--num_words', '-n', type=int, help="Number of words to predict.", default=200)


args = parser.parse_args()

start_lyrics = args.words
temp = args.temperature

path = Path("./")
data_lm = load_data(path, 'data_lm.pkl')

learner =  language_model_learner(
        data_lm,
        AWD_LSTM,
        drop_mult=0.5,
        metrics=error_rate)

import os
learner.load(os.getcwd() +  "/model/" + "lil-peep-lyrics-model", with_opt=False)
lyrics = learner.predict(start_lyrics, n_words=200, temperature=temp)

print(lyrics)

