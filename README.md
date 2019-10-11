# lil-peep-nlp

Predicting lyrics of Lil peep using the ULMFiT model. The songs were webscrape from an undisclosed lycris distribution page. 
The dataset is not supplied to avoid copyright issues. However the trained model can be download from a google drive:  

https://drive.google.com/file/d/1bkVQAcm8sllbf008usfzQ2AinfRB5Iuc/view?usp=sharing

The model.pth file should be saved in the model directory.

Lyrics can be predicted in the followint way:  
>$ python lil-peep.py "White wine"

Sample output:   
White wine , more wine , baby pour another cup   
  Ayo xxbos They do n't see me unless i pull up Lamborghini    
  Everybody wanna be me till i pull up and they meet me   
  Imma die slow sweetie , i ai n't never had a meaning   
  Just another fucking junkie , drain my blood but do n't be greedy   
  Leave some liquid for the centipedes , they eat away my memory   
  Feed me to my enemies   
  Lead me to death , i 'm Lil Kennedy   
  i ai n't got no remedy , bury me   
  Pocket full of ketamine , methamphetamine   
  Put me in a limousine , drive me to destiny    
  Pussy on the leather seats , music and ecstasy   
  She do n't think i 'm sexy , but i ca n't let that get to me   
  Fuck her till she red and then she keep coming next to me   
  Fuck her till she dead and she gon ' keep coming next to me   
  Fuck how dead do n't give   




`usage: lil-peep.py [-h] --words WORDS [--temperature TEMPERATURE]
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
jupyter@my-fastai-instance:~/projects/lil-peep-nlp$ `
