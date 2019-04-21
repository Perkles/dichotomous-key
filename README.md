## Dichotomous-key Algorithm 

Dichotomous classification schemes show the
relationship between different groups of plants or animals, thereby
distinguishing them by natural characters. Dichotomous keys, on the other hand, are produced solely for the purposes of identification, using features to distinguish different organisms and
are acknowledged to project artificial and contrived relationships [Griffing, 2011](https://bsapubs.onlinelibrary.wiley.com/doi/pdf/10.3732/ajb.1100188)

This script implements a Dichotomous key in python based on a key called:
[Arthropods - Key A: Arthropods with Six Legs, with Well Developed Wings](https://www.amnh.org/learn/biodiversity_counts/ident_help/Text_Keys/arthropod_keyA.htm) provided
by the [American Museum of Natural History website](https://www.amnh.org/)

The algorithm is projected to reed a CSV file (Comma separated value) where the key is written and execute the dichotomous key's steps.

In order to reproduce the algorithm in your computer, you'll need to download this repository and execute the `DichotomousKey.py`
To customize the key modify the `d_key.load()` function to receive a string with the name of your CSV without the '.txt' part.

The dichotomous key CSV file follows an organization and there are two different kinds of 'steps'

1 - `1,Two pairs of wings,3`

The number `1` is the level of the step on the general key, the `Two pairs of wings` refers to the 'instruction' part and the `3` is the level you'll follow if that step gets selected.

2- `8,Wings with many cross veins,0,NEUROPTERA`

This step is slightly different in the last two parts. This step indicates that you have found, in this case, an insect, and finished the key so there's nowhere to go.
The `0` part indicates the end of the key and is required. 
`NEUROPTERA` is the result of the identification.

The file `steps.txt` can be used to check different identifications and test if the dichotomous key works properly.