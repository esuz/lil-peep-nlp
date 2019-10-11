from fastai import *
from fastai.text import *
from create_dataset import create_dataset


lyrics = create_dataset("./lyrics")

data_lm = (TextList.
    from_csv(Path("."), "./lyrics-dataset.txt", cols="lyrics").
    split_by_rand_pct().label_for_lm().databunch())

learn = language_model_learner(data_lm, AWD_LSTM, drop_mult=0.3)

learn.fit_one_cycle(4, 1e-2, moms=(0.8,0.7))


TEXT = "You like attention, I find it"
N_WORDS = 40
N_SENTENCES = 2

print("\n".join(learn.predict(TEXT, N_WORDS, temperature=0.75) for _ in range(N_SENTENCES)))