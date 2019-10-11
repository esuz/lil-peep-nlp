# lil-peep-nlp

Predicting lyrics of Lil peep using the ULMFiT model. The songs were webscrape from an undisclosed lycris distribution page. 
The dataset is not supplied to avoid copyright issues. However the trained model can be download from a google drive:  

https://drive.google.com/file/d/1bkVQAcm8sllbf008usfzQ2AinfRB5Iuc/view?usp=sharing

The model.pth file should be saved in the model directory.

Lyrics can be predicted in the followint way:
$python lil-peep.py "White wine"


usage: lil-peep.py [-h] --words WORDS [--temperature TEMPERATURE]
                   [--num_words NUM_WORDS]

Enter some words.

optional arguments:
  -h, --help            show this help message and exit
  --words WORDS, -w WORDS
                        Enter a string.
  --temperature TEMPERATURE, -t TEMPERATURE
                        Temperature.
  --num_words NUM_WORDS, -n NUM_WORDS
                        Number of words to predict.
jupyter@my-fastai-instance:~/projects/lil-peep-nlp$ 
