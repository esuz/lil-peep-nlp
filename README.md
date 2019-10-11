# Lil Peep language model (ULMFiT)

Predicting lyrics of Lil peep using the ULMFiT model. The songs were webscraped from an undisclosed lycris distribution page. ULMFiT was fine-tuned on 2600 lyrical lines. The dataset is not supplied to avoid copyright issues. However the trained model can be download from a google drive:  
https://drive.google.com/file/d/1bkVQAcm8sllbf008usfzQ2AinfRB5Iuc/view?usp=sharing

The model.pth file should be saved in the model directory. 

### Example
Lyrics can be predicted in the following way:  
>$ python lil-peep.py "White wine"

### Sample output:   
white wine , eyes straight from the chosen  
  Memories haunt me , i know that they haunt you too   
 
  But it 's time i admit , my regrets     
  i did you dirty , did you dirty as fuck   
  Come and fuck with the kid   
  i ai n't tryna live , pray i die    
  i ai n't tryna live , pray i die    
  But i keep coming right up out of the mud   
  What you call a sin   
  i call a part of my day   
  Get the fuck out my way   
  Say she gon ' fuck but she gay   
 
  You got lucky today , you have nothing to say    
  Wo n't say shit to my face , ca n't say shit to my face   
  You got lucky today , you have nothing to say   
  Wo since n't say shit to my face , ca n't say shit to my face    
  You got lucky today , you have no to say    
  Wo n't say shit to my face , ca n't say shit to   


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


### Usage

usage: lil-peep.py [-h] --words WORDS [--temperature TEMPERATURE]  
                   [--num_words NUM_WORDS]    
                   
I would advise to play around with the temperature parameter. Try values in the range of 0.3 till 2.

### Requirements  
Anaconda Python 3.*  
pip install fastai
